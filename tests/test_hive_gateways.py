"""Hive release pins and launch contracts; opt-in installed-runtime smoke tests."""

import json
import os
from pathlib import Path
import re
import shutil
import socket
import subprocess
import tempfile
import time
import unittest
from urllib.error import URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
GATEWAYS = ROOT / "apollo-federation" / "gateways"
NODE_GATEWAYS = ("hive-gateway", "hive-gateway-router-runtime")


class HiveGatewayTests(unittest.TestCase):
    def test_exact_pins_match_lockfiles(self):
        for name in NODE_GATEWAYS:
            with self.subTest(gateway=name):
                directory = GATEWAYS / name
                package = json.loads((directory / "package.json").read_text())
                lock = json.loads((directory / "package-lock.json").read_text())
                self.assertEqual(package["dependencies"]["@graphql-hive/gateway"], "2.15.3")
                self.assertEqual(package["dependencies"]["graphql"], "16.13.2")
                self.assertEqual(lock["packages"][""]["dependencies"], package["dependencies"])
                for dependency, version in package["dependencies"].items():
                    self.assertEqual(lock["packages"][f"node_modules/{dependency}"]["version"], version)
                if name == "hive-gateway-router-runtime":
                    self.assertEqual(package["dependencies"]["@graphql-hive/router-runtime"], "1.6.6")

    def test_router_installer_uses_release_script_and_records_version(self):
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            curl = directory / "curl"
            curl.write_text("#!/bin/sh\nprintf '%s\\n' \"$*\" > curl_args\nprintf 'test \"$1\" = v0.3.6\\n'\n")
            curl.chmod(0o755)
            environment = dict(os.environ, PATH=f"{directory}:{os.environ['PATH']}")
            result = subprocess.run(["bash", str(GATEWAYS / "hive-router" / "install.sh")],
                                    cwd=directory, env=environment, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual((directory / "version.txt").read_text(), "v0.3.6\n")
            self.assertIn("-fsSL https://raw.githubusercontent.com/graphql-hive/router/hive-router/v0.3.6/install.sh",
                          (directory / "curl_args").read_text())

    def test_router_installer_does_not_record_failed_download(self):
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            curl = directory / "curl"
            curl.write_text("#!/bin/sh\nexit 22\n")
            curl.chmod(0o755)
            result = subprocess.run(["bash", str(GATEWAYS / "hive-router" / "install.sh")],
                                    cwd=directory, env=dict(os.environ, PATH=f"{directory}:{os.environ['PATH']}"),
                                    capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertFalse((directory / "version.txt").exists())

    def test_router_start_sets_supported_environment(self):
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            router = directory / "hive_router"
            router.write_text('#!/bin/sh\nprintf "%s\\n" "$LOG_LEVEL" "$PORT" "$SUPERGRAPH_FILE_PATH" "$HIVE__SUPERGRAPH__PATH"\n')
            router.chmod(0o755)
            result = subprocess.run(["bash", str(GATEWAYS / "hive-router" / "start.sh")],
                                    cwd=directory, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual((directory / "gateway_log.txt").read_text(), "info\n5220\n./supergraph.graphql\n\n")


@unittest.skipUnless(os.environ.get("HIVE_GATEWAY_SMOKE") == "1",
                     "set HIVE_GATEWAY_SMOKE=1 after installing Hive and starting Federation subgraphs; "
                     "HIVE_SMOKE_SUBGRAPH_BASE_PORT defaults to 5221")
class HiveGatewaySmokeTests(unittest.TestCase):
    def request(self, port, query):
        request = Request(f"http://127.0.0.1:{port}/graphql",
                          data=json.dumps({"query": query}).encode(),
                          headers={"Content-Type": "application/json", "Authorization": "Bearer hive-smoke"})
        with urlopen(request, timeout=30) as response:
            self.assertEqual(response.status, 200)
            return json.load(response)

    def test_installed_gateways_execute_benchmark_operation(self):
        source = (ROOT / "k6" / "k6.js").read_text()
        query = re.search(r"query: `([^`]+)`", source).group(1)
        for name in (*NODE_GATEWAYS, "hive-router"):
            with (
                self.subTest(gateway=name),
                tempfile.TemporaryFile(mode="w+") as log,
                tempfile.TemporaryDirectory() as temporary,
            ):
                directory = GATEWAYS / name
                supergraph = Path(temporary) / "supergraph.graphql"
                schema = (directory / "supergraph.graphql").read_text()
                base_port = int(os.environ.get("HIVE_SMOKE_SUBGRAPH_BASE_PORT", "5221"))
                for offset in range(4):
                    schema = schema.replace(f"localhost:{5221 + offset}/", f"localhost:{base_port + offset}/")
                supergraph.write_text(schema)
                with socket.socket() as listener:
                    listener.bind(("127.0.0.1", 0))
                    port = listener.getsockname()[1]
                if name == "hive-router":
                    command = [str(directory / "hive_router")]
                    environment = {"LOG_LEVEL": "info", "PORT": str(port),
                                   "SUPERGRAPH_FILE_PATH": str(supergraph)}
                else:
                    command = [shutil.which("node"), "node_modules/@graphql-hive/gateway/dist/bin.js",
                               "supergraph", str(supergraph), "--port", str(port)]
                    if name == "hive-gateway":
                        command.append("--jit")
                    environment = dict(os.environ, NODE_ENV="production")
                process = subprocess.Popen(command, cwd=directory, env=environment,
                                           stdout=log, stderr=subprocess.STDOUT)
                try:
                    deadline = time.monotonic() + 45
                    while True:
                        try:
                            self.assertEqual(self.request(port, "{ __typename }")["data"]["__typename"], "Query")
                            break
                        except (URLError, TimeoutError):
                            if process.poll() is not None or time.monotonic() > deadline:
                                log.seek(0)
                                self.fail(f"{name} did not become ready:\n{log.read()}")
                            time.sleep(0.2)
                    first = self.request(port, query)
                    self.assertFalse(first.get("errors"), first.get("errors"))
                    self.assertTrue(first["data"]["users"])
                    self.assertTrue(first["data"]["topProducts"])
                    self.assertIsNotNone(first["data"]["topProducts"][0]["shippingEstimate"])
                    self.assertEqual(first, self.request(port, query))
                finally:
                    process.terminate()
                    try:
                        process.wait(timeout=10)
                    except subprocess.TimeoutExpired:
                        process.kill()
                        process.wait(timeout=5)


if __name__ == "__main__":
    unittest.main()
