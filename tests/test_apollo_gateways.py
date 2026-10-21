"""Apollo install, configuration, and workflow regression coverage without downloads."""

import json
import os
import re
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

REPO_ROOT = Path(__file__).resolve().parents[1]
GATEWAYS = REPO_ROOT / "apollo-federation" / "gateways"
ROUTER_VERSIONS = {
    "apollo-router": "v2.18.0",
    "apollo-router-v3": "v3.0.0-preview.0",
}


class ApolloGatewayTests(unittest.TestCase):
    def test_gateway_and_lockfile_pin_same_stable_version(self):
        directory = GATEWAYS / "apollo-gateway"
        package = json.loads((directory / "package.json").read_text())
        lock = json.loads((directory / "package-lock.json").read_text())
        self.assertEqual(package["dependencies"]["@apollo/gateway"], "2.14.4")
        self.assertEqual(lock["packages"][""]["dependencies"], package["dependencies"])
        for name in ("gateway", "composition", "federation-internals", "query-graphs", "query-planner"):
            with self.subTest(package=name):
                entry = lock["packages"][f"node_modules/@apollo/{name}"]
                self.assertEqual(entry["version"], "2.14.4")
                self.assertTrue(entry["integrity"])
        for dependency, version in package["dependencies"].items():
            with self.subTest(dependency=dependency):
                self.assertRegex(version, r"^\d+\.\d+\.\d+(?:-[\w.-]+)?$")
                self.assertEqual(lock["packages"][f"node_modules/{dependency}"]["version"], version)

    def test_router_installers_download_exact_pins_and_write_own_metadata(self):
        for name, version in ROUTER_VERSIONS.items():
            with self.subTest(gateway=name), tempfile.TemporaryDirectory() as temporary:
                directory = Path(temporary)
                bin_directory = directory / "bin"
                bin_directory.mkdir()
                # Capture the requested download and supply a local installer instead.
                curl = bin_directory / "curl"
                curl.write_text(
                    '#!/bin/sh\nprintf "%s\\n" "$@" > curl-args.txt\n'
                    'printf \'#!/bin/sh\\nprintf installed > router\\n\'\n'
                )
                curl.chmod(0o755)
                environment = dict(os.environ, PATH=f"{bin_directory}:{os.environ['PATH']}")
                result = subprocess.run(
                    ["bash", str(GATEWAYS / name / "install.sh")],
                    cwd=directory, env=environment, capture_output=True, text=True, timeout=10,
                )
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual((directory / "version.txt").read_text(), version + "\n")
                self.assertIn(
                    f"https://router.apollo.dev/download/nix/{version}",
                    (directory / "curl-args.txt").read_text().splitlines(),
                )
                self.assertEqual((directory / "router").read_text(), "installed")

    def test_router_startup_uses_local_artifacts_and_isolates_environment(self):
        for name in ROUTER_VERSIONS:
            with self.subTest(gateway=name), tempfile.TemporaryDirectory() as temporary:
                directory = Path(temporary)
                router = directory / "router"
                router.write_text(
                    '#!/bin/sh\nprintf "%s\\n" "$@" > router-args.txt\n'
                    'printf "%s\\n" "$APOLLO_TELEMETRY_DISABLED" "${APOLLO_KEY-unset}" > router-env.txt\n'
                )
                router.chmod(0o755)
                shutil.copy(GATEWAYS / name / "start.sh", directory / "start.sh")
                result = subprocess.run(
                    ["bash", "start.sh"], cwd=directory,
                    env=dict(os.environ, APOLLO_KEY="must-not-reach-router"),
                    capture_output=True, text=True, timeout=10,
                )
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(
                    (directory / "router-args.txt").read_text().splitlines(),
                    ["--supergraph", "./supergraph.graphql", "--config", "config.yaml"],
                )
                self.assertEqual((directory / "router-env.txt").read_text(), "true\nunset\n")
                self.assertTrue((directory / "gateway_log.txt").exists())

    def test_preview_preserves_schema_endpoints_and_settings(self):
        stable = GATEWAYS / "apollo-router"
        preview = GATEWAYS / "apollo-router-v3"
        for filename in ("supergraph.graphql", "settings.json", "start.sh"):
            with self.subTest(filename=filename):
                self.assertEqual((preview / filename).read_bytes(), (stable / filename).read_bytes())
        stable_config = (stable / "config.yaml").read_text()
        preview_config = (preview / "config.yaml").read_text()
        # Router 3 changes this default. Keep Router 2's cancellation semantics.
        self.assertIn("    early_cancel: false\n", preview_config)
        preview_config = "\n".join(
            line for line in preview_config.splitlines()
            if "early_cancel:" not in line and not line.lstrip().startswith("#")
        ) + "\n"
        self.assertEqual(preview_config, stable_config)
        self.assertIn("deduplicate_query: true", stable_config)
        self.assertIn(
            "        request:\n            operations:\n                - propagate:\n                    named: Authorization",
            stable_config,
        )
        self.assertEqual((preview / ".gitignore").read_text().strip(), "router")

    def test_workflow_exposes_preview_and_preserves_distinct_artifacts_in_all_modes(self):
        workflow = (REPO_ROOT / ".github" / "workflows" / "benchmark.yml").read_text()
        options = workflow.split("      gateway:", 1)[1].split("      fusion_version:", 1)[0]
        self.assertIn("          - apollo-router\n", options)
        self.assertIn("          - apollo-router-v3\n", options)
        jobs = (
            ("benchmark-constant", "constant", "gateways_constant"),
            ("benchmark-burst", "burst", "gateways_burst"),
            ("benchmark-constant-latency", "constant-latency", "gateways"),
        )
        for job, mode, matrix in jobs:
            with self.subTest(mode=mode):
                section = re.split(r"\n  [a-z]", workflow.split(f"\n  {job}:\n", 1)[1], maxsplit=1)[0]
                self.assertIn(f"outputs.{matrix})", section)
                self.assertIn("name: ${{ matrix.gateway.gateway_artifact }}", section)
                self.assertIn("chmod +x apollo-federation/gateways/apollo-router-v3/router", section)
                self.assertIn("BENCH_GATEWAY_NAME: ${{ matrix.gateway.base_name || '' }}", section)
                self.assertIn(f"name: results-${{{{ matrix.gateway.name }}}}-{mode}", section)
                self.assertIn("path: ${{ matrix.gateway.path }}/results/", section)


if __name__ == "__main__":
    unittest.main()
