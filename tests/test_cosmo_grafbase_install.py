"""Offline installer checks for the pinned Cosmo and Grafbase release assets."""

import io
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tarfile
import tempfile
import unittest

REPO_ROOT = Path(__file__).resolve().parents[1]
GATEWAYS = REPO_ROOT / "apollo-federation" / "gateways"


class CosmoGrafbaseInstallTests(unittest.TestCase):
    def run_installer(self, gateway, platform):
        workdir = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, workdir, True)
        bindir = workdir / "bin"
        bindir.mkdir()
        shutil.copy(GATEWAYS / gateway / "install.sh", workdir / "install.sh")
        uname = bindir / "uname"
        uname.write_text(f"#!/bin/sh\nprintf '%s\\n' '{platform}'\n")
        uname.chmod(0o755)
        archive = workdir / "router.tar.gz"
        with tarfile.open(archive, "w:gz") as output:
            binary = b"#!/bin/sh\nexit 0\n"
            entry = tarfile.TarInfo("router")
            entry.size = len(binary)
            entry.mode = 0o755
            output.addfile(entry, io.BytesIO(binary))
        curl = bindir / "curl"
        curl.write_text(
            f"#!{sys.executable}\n"
            "import os, pathlib, shutil, sys\n"
            "args = sys.argv[1:]\n"
            "url = next(arg for arg in args if arg.startswith('https://'))\n"
            "pathlib.Path('download-url.txt').write_text(url)\n"
            "flag = '-o' if '-o' in args else '--output'\n"
            "output = args[args.index(flag) + 1]\n"
            "if url.endswith('.tar.gz'):\n"
            "    shutil.copy('router.tar.gz', output)\n"
            "else:\n"
            "    pathlib.Path(output).write_text('#!/bin/sh\\nexit 0\\n')\n"
        )
        curl.chmod(0o755)
        env = dict(os.environ, PATH=str(bindir) + os.pathsep + os.environ["PATH"])
        proc = subprocess.run(
            ["sh" if gateway == "cosmo" else "bash", "install.sh"],
            cwd=workdir,
            env=env,
            capture_output=True,
            text=True,
            timeout=30,
        )
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        return workdir

    def test_cosmo_pinned_asset_and_architecture(self):
        platforms = {
            "Darwin x86_64": "darwin-amd64",
            "Darwin arm64": "darwin-arm64",
            "Linux x86_64": "linux-amd64",
            "Linux arm64": "linux-arm64",
            "Linux aarch64": "linux-arm64",
        }
        for platform, target in platforms.items():
            with self.subTest(platform=platform):
                workdir = self.run_installer("cosmo", platform)
                self.assertEqual((workdir / "version.txt").read_text(), "0.361.0\n")
                self.assertEqual(
                    (workdir / "download-url.txt").read_text(),
                    "https://github.com/wundergraph/cosmo/releases/download/"
                    f"router@0.361.0/router-router@0.361.0-{target}.tar.gz",
                )
                self.assertTrue(os.access(workdir / "cosmo", os.X_OK))

    def test_grafbase_remains_on_latest_published_gateway(self):
        platforms = {
            "Darwin arm64": "aarch64-apple-darwin",
            "Linux x86_64": "x86_64-unknown-linux-musl",
            "Linux arm64": "aarch64-unknown-linux-musl",
            "Linux aarch64": "aarch64-unknown-linux-musl",
        }
        for platform, target in platforms.items():
            with self.subTest(platform=platform):
                workdir = self.run_installer("grafbase", platform)
                self.assertEqual((workdir / "version.txt").read_text(), "0.53.5\n")
                self.assertEqual(
                    (workdir / "download-url.txt").read_text(),
                    "https://github.com/grafbase/grafbase/releases/download/"
                    f"gateway-0.53.5/grafbase-gateway-{target}",
                )
                self.assertTrue(os.access(workdir / "grafbase-gateway", os.X_OK))


if __name__ == "__main__":
    unittest.main()
