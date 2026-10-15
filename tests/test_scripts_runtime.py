"""Runtime behavior tests: error paths and result generation.

These exercise the no-SDK prebuilt failure modes and the .NET-only result
output without requiring k6, .NET or network access.
"""

import glob
import json
import os
import re
import shutil
import subprocess
import tempfile
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SUMMARY = {
    "vus": 50,
    "duration": "120s",
    "metrics": {
        "http_reqs": {"values": {"rate": 1000, "count": 120000}},
        "http_req_duration": {"values": {"avg": 5.0, "p(95)": 10.0}},
        "http_req_failed": {"values": {"passes": 0}},
        "success_rate": {"values": {"fails": 0}},
    },
}


def make_run(artifacts_dir, gateway, display_name, run_index=1, mode="constant"):
    make_tech_run(
        artifacts_dir,
        gateway,
        display_name,
        subgraph_tech=".net",
        subgraphs="subgraphs-net",
        run_index=run_index,
        mode=mode,
    )


def make_tech_run(
    artifacts_dir, gateway, display_name, subgraph_tech, subgraphs, run_index=1, mode="constant"
):
    run_dir = os.path.join(
        artifacts_dir, f"results-{gateway}-{mode}", f"2024010{run_index}_000000"
    )
    os.makedirs(run_dir, exist_ok=True)
    with open(os.path.join(run_dir, "metadata.json"), "w") as fh:
        json.dump(
            {
                "gateway": gateway,
                "gateway_path": "composite-schema/gateways/fusion",
                "category": "composite-schema",
                "mode": mode,
                "timestamp": f"2024010{run_index}_000000",
                "run": run_index,
                "total_runs": 1,
                "display_name": display_name,
                "version": "16.6.0",
                "subgraphs": subgraphs,
                "subgraph_tech": subgraph_tech,
                "machine_hostname": "test-host",
                "machine_os": "Linux",
                "machine_cpu": "Test CPU",
                "machine_cores": "16 logical",
                "machine_ram": "32 GB",
            },
            fh,
        )
    with open(os.path.join(run_dir, "k6_summary.json"), "w") as fh:
        json.dump(SUMMARY, fh)
    with open(os.path.join(run_dir, "k6_summary.txt"), "w") as fh:
        fh.write("k6 summary\n")


def expected_entry(name):
    return {
        "name": name,
        "base_name": name,
        "subgraph_tech": ".net",
        "display_name": f"{name} (HotChocolate subgraphs)",
    }


class StartScriptErrorPathTests(unittest.TestCase):
    """start.sh must fail fast with a clear message when the bundled runtime
    or the apphost build output is missing (the no-SDK benchmark machines hit
    exactly these paths on a broken artifact)."""

    FAMILIES = ("apollo-federation", "composite-schema")

    def run_copy(self, family):
        workdir = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, workdir, True)
        copied = os.path.join(workdir, "start.sh")
        shutil.copy(
            os.path.join(REPO_ROOT, family, "subgraphs-net", "start.sh"), copied
        )
        return workdir, copied

    def test_missing_bundled_runtime_fails(self):
        for family in self.FAMILIES:
            with self.subTest(family=family):
                workdir, copied = self.run_copy(family)
                if family == "apollo-federation":
                    # Needs a discoverable project so the failure is about the
                    # runtime, not about missing projects.
                    proj = os.path.join(workdir, "eShop.Fake")
                    os.makedirs(proj)
                    open(os.path.join(proj, "eShop.Fake.csproj"), "w").close()
                proc = subprocess.run(
                    ["bash", copied],
                    capture_output=True,
                    text=True,
                    timeout=60,
                )
                self.assertNotEqual(proc.returncode, 0)
                self.assertIn(
                    "no bundled .NET runtime", proc.stderr + proc.stdout
                )

    def test_missing_build_output_fails(self):
        for family in self.FAMILIES:
            with self.subTest(family=family):
                workdir, copied = self.run_copy(family)
                # Stub a bundled runtime so the check under test is apphost
                # resolution.
                os.makedirs(
                    os.path.join(workdir, ".dotnet", "shared", "Microsoft.NETCore.App")
                )
                if family == "apollo-federation":
                    proj = os.path.join(workdir, "eShop.Fake")
                    os.makedirs(proj)
                    open(os.path.join(proj, "eShop.Fake.csproj"), "w").close()
                else:
                    os.makedirs(os.path.join(workdir, "eShop.Accounts"))
                proc = subprocess.run(
                    ["bash", copied],
                    capture_output=True,
                    text=True,
                    timeout=60,
                )
                self.assertNotEqual(proc.returncode, 0)
                self.assertIn("no build output", proc.stderr + proc.stdout)


class BenchmarkValidationTests(unittest.TestCase):
    def test_rust_override_rejected(self):
        proc = subprocess.run(
            [
                "bash",
                os.path.join(REPO_ROOT, "k6", "benchmark.sh"),
                "composite-schema/gateways/fusion",
                "subgraphs-rust",
                "constant",
            ],
            capture_output=True,
            text=True,
            timeout=60,
            cwd=REPO_ROOT,
        )
        self.assertNotEqual(proc.returncode, 0)
        self.assertIn(
            "only 'subgraphs-net' is supported", proc.stdout + proc.stderr
        )


class GenerateResultsTests(unittest.TestCase):
    def run_generator(self, expected, with_runs=None, not_run=(), mode="constant"):
        workdir = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, workdir, True)
        artifacts = os.path.join(workdir, "artifacts")
        os.makedirs(artifacts)
        for gateway in with_runs if with_runs is not None else expected:
            make_run(artifacts, gateway, f"{gateway} (HotChocolate subgraphs)", mode=mode)
        outdir = os.path.join(workdir, "out")
        env = dict(os.environ)
        env["EXPECTED_GATEWAYS_JSON"] = json.dumps([expected_entry(g) for g in expected])
        env["NOT_RUN_GATEWAYS_JSON"] = json.dumps([expected_entry(g) for g in not_run])
        env["RESULT_MODES"] = mode
        proc = subprocess.run(
            ["python3", os.path.join(REPO_ROOT, "k6", "generate-results.py"), artifacts, outdir],
            env=env,
            capture_output=True,
            text=True,
            timeout=120,
            cwd=REPO_ROOT,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr)
        filename = f"RESULTS_{mode.upper().replace('-', '_')}.md"
        with open(os.path.join(outdir, filename)) as fh:
            return fh.read()

    def test_dotnet_only_table(self):
        md = self.run_generator(["fusion", "cosmo"])
        self.assertIn("### HotChocolate Subgraphs", md)
        self.assertNotIn("Rust Subgraphs", md)
        self.assertIn("4 HotChocolate subgraphs", md)
        self.assertIn("| fusion |", md)
        self.assertIn("| cosmo |", md)

    def test_apollo_router_generations_have_separate_rows(self):
        gateways = ["apollo-router", "apollo-router-v3"]
        for mode in ("constant", "constant-latency", "burst"):
            with self.subTest(mode=mode):
                md = self.run_generator(gateways, mode=mode)
                for gateway in gateways:
                    rows = [line for line in md.splitlines() if line.startswith(f"| {gateway} |")]
                    self.assertEqual(len(rows), 1)
                    self.assertNotIn("benchmark run failed", rows[0])
                self.assertIn("apollo-router (HotChocolate subgraphs)", md)
                self.assertIn("apollo-router-v3 (HotChocolate subgraphs)", md)

    def test_missing_apollo_preview_does_not_reuse_stable_result(self):
        md = self.run_generator(
            ["apollo-router", "apollo-router-v3"], with_runs=["apollo-router"]
        )
        stable = next(line for line in md.splitlines() if line.startswith("| apollo-router |"))
        preview = next(line for line in md.splitlines() if line.startswith("| apollo-router-v3 |"))
        self.assertNotIn("benchmark run failed", stable)
        self.assertIn("benchmark run failed", preview)

    def test_missing_gateway_marked_failed(self):
        md = self.run_generator(["fusion", "grafbase"], with_runs=["fusion"])
        self.assertIn("| grafbase |", md)
        self.assertIn("benchmark run failed", md)

    def test_excluded_gateway_marked_not_run(self):
        md = self.run_generator(["fusion", "feddi"], with_runs=["fusion"], not_run=("feddi",))
        feddi_rows = [line for line in md.splitlines() if line.startswith("| feddi |")]
        self.assertEqual(len(feddi_rows), 1)
        self.assertIn("not run", feddi_rows[0])
        self.assertNotIn("benchmark run failed", feddi_rows[0])

    def test_historical_rust_not_described_as_dotnet(self):
        # Reproduces the reported contradiction: a historical Rust artifact
        # must render its Rust rows without the document claiming every
        # benchmark used HotChocolate subgraphs.
        workdir = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, workdir, True)
        artifacts = os.path.join(workdir, "artifacts")
        os.makedirs(artifacts)
        make_run(artifacts, "fusion", "fusion (HotChocolate subgraphs)")
        make_tech_run(
            artifacts,
            "cosmo",
            "cosmo (Rust subgraphs)",
            subgraph_tech="rust",
            subgraphs="subgraphs-rust",
        )
        outdir = os.path.join(workdir, "out")
        env = dict(os.environ)
        env["EXPECTED_GATEWAYS_JSON"] = json.dumps(
            [expected_entry("fusion"), expected_entry("cosmo")]
        )
        env["RESULT_MODES"] = "constant"
        proc = subprocess.run(
            ["python3", os.path.join(REPO_ROOT, "k6", "generate-results.py"), artifacts, outdir],
            env=env,
            capture_output=True,
            text=True,
            timeout=120,
            cwd=REPO_ROOT,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr)
        with open(os.path.join(outdir, "RESULTS_CONSTANT.md")) as fh:
            md = fh.read()
        # Historical Rust measurements are preserved, not relabeled.
        self.assertIn("### Rust Subgraphs", md)
        self.assertIn("### HotChocolate Subgraphs", md)
        # The setup claim must be qualified and flag the historical rows.
        self.assertNotIn(
            "Each benchmark runs a GraphQL gateway with 4 HotChocolate subgraphs", md
        )
        self.assertIn("Current benchmarks run a GraphQL gateway with 4 HotChocolate subgraphs", md)
        self.assertIn("Historical note", md)


    def test_old_dotnet_display_name_still_parses(self):
        # Backward compatibility: artifacts recorded before the HotChocolate
        # relabel carry display_name "(.NET subgraphs)" with tech ".net" and
        # must still group under the HotChocolate heading.
        workdir = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, workdir, True)
        artifacts = os.path.join(workdir, "artifacts")
        os.makedirs(artifacts)
        make_tech_run(
            artifacts,
            "fusion",
            "fusion (.NET subgraphs)",
            subgraph_tech=".net",
            subgraphs="subgraphs-net",
        )
        outdir = os.path.join(workdir, "out")
        env = dict(os.environ)
        env["EXPECTED_GATEWAYS_JSON"] = json.dumps([expected_entry("fusion")])
        env["RESULT_MODES"] = "constant"
        proc = subprocess.run(
            ["python3", os.path.join(REPO_ROOT, "k6", "generate-results.py"), artifacts, outdir],
            env=env,
            capture_output=True,
            text=True,
            timeout=120,
            cwd=REPO_ROOT,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr)
        with open(os.path.join(outdir, "RESULTS_CONSTANT.md")) as fh:
            md = fh.read()
        self.assertIn("### HotChocolate Subgraphs", md)
        self.assertIn("| fusion |", md)

    def test_new_hotchocolate_display_name_parses_without_tech(self):
        # The new "(HotChocolate subgraphs)" label must resolve to the .net
        # group even when subgraph_tech is missing from the metadata.
        workdir = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, workdir, True)
        artifacts = os.path.join(workdir, "artifacts")
        os.makedirs(artifacts)
        make_tech_run(
            artifacts,
            "cosmo",
            "cosmo (HotChocolate subgraphs)",
            subgraph_tech="",
            subgraphs="",
        )
        outdir = os.path.join(workdir, "out")
        env = dict(os.environ)
        env["EXPECTED_GATEWAYS_JSON"] = json.dumps([expected_entry("cosmo")])
        env["RESULT_MODES"] = "constant"
        proc = subprocess.run(
            ["python3", os.path.join(REPO_ROOT, "k6", "generate-results.py"), artifacts, outdir],
            env=env,
            capture_output=True,
            text=True,
            timeout=120,
            cwd=REPO_ROOT,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr)
        with open(os.path.join(outdir, "RESULTS_CONSTANT.md")) as fh:
            md = fh.read()
        self.assertIn("### HotChocolate Subgraphs", md)
        self.assertIn("| cosmo |", md)


class SubgraphBuildPinTests(unittest.TestCase):
    """subgraphs-net/build.sh verifies a pinned HotChocolate release instead of
    resolving the latest stable from NuGet and rewriting tracked csproj files."""

    FAMILIES = ("apollo-federation", "composite-schema")
    PINNED_VERSION = "16.6.8"

    def read_build(self, family):
        with open(
            os.path.join(REPO_ROOT, family, "subgraphs-net", "build.sh"),
            encoding="utf-8",
        ) as fh:
            return fh.read()

    def extract_pin_block(self, family):
        content = self.read_build(family)
        start = content.index("# --- Verify pinned HotChocolate version ---")
        end = content.index("# --- Install the .NET SDK")
        return content[start:end]

    def test_pinned_version_declared(self):
        for family in self.FAMILIES:
            with self.subTest(family=family):
                self.assertIn(
                    f'PINNED_HOTCHOCOLATE_VERSION="{self.PINNED_VERSION}"',
                    self.read_build(family),
                )

    def test_no_nuget_version_fetch_or_csproj_rewrite(self):
        for family in self.FAMILIES:
            with self.subTest(family=family):
                content = self.read_build(family)
                self.assertNotIn("api.nuget.org", content)
                self.assertNotIn("LATEST_STABLE", content)
                self.assertNotIn("sed -i", content)
                # The pin check fails fast instead of mutating tracked files.
                self.assertIn("not pinned to", content)
                self.assertIn("exit 1", content)
                # Pin validation must use an XML parser, not regex, so
                # single-quoted attributes parse and comments are ignored.
                self.assertIn("xml.etree.ElementTree", content)
                self.assertNotIn("attr_re", content)

    def test_all_hotchocolate_refs_pinned(self):
        for family in self.FAMILIES:
            with self.subTest(family=family):
                csprojs = sorted(
                    glob.glob(
                        os.path.join(
                            REPO_ROOT, family, "subgraphs-net", "eShop.*", "*.csproj"
                        )
                    )
                )
                self.assertEqual(len(csprojs), 4, f"expected 4 csprojs in {family}")
                for csproj in csprojs:
                    with open(csproj, encoding="utf-8") as fh:
                        content = fh.read()
                    refs = re.findall(
                        r'Include="HotChocolate[^"]*" Version="([^"]*)"', content
                    )
                    self.assertTrue(refs, f"no HotChocolate refs in {csproj}")
                    for version in refs:
                        self.assertEqual(
                            version,
                            self.PINNED_VERSION,
                            f"{csproj} pins {version}, want {self.PINNED_VERSION}",
                        )

    def run_pin_block(self, family, csproj_version):
        workdir = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, workdir, True)
        projdir = os.path.join(workdir, "eShop.Fake")
        os.makedirs(projdir)
        csproj = os.path.join(projdir, "eShop.Fake.csproj")
        with open(csproj, "w", encoding="utf-8") as fh:
            fh.write(
                '<Project Sdk="Microsoft.NET.Sdk.Web">\n'
                '  <ItemGroup>\n'
                f'    <PackageReference Include="HotChocolate.AspNetCore" Version="{csproj_version}" />\n'
                "  </ItemGroup>\n</Project>\n"
            )
        wrapper = os.path.join(workdir, "pin-check.sh")
        with open(wrapper, "w", encoding="utf-8") as fh:
            fh.write("set -u\n")
            fh.write(f'SCRIPT_DIR="{workdir}"\n')
            fh.write(f'CSPROJ_FILES=("{csproj}")\n')
            fh.write(self.extract_pin_block(family))
        return subprocess.run(
            ["bash", wrapper],
            capture_output=True,
            text=True,
            timeout=60,
        )

    def test_pin_checked_before_sdk_download(self):
        for family in self.FAMILIES:
            with self.subTest(family=family):
                content = self.read_build(family)
                verify_at = content.index("# --- Verify pinned HotChocolate version ---")
                cleanup_at = content.index('rm -rf "$BUNDLED_DOTNET_DIR"')
                download_at = content.index("dotnet-install.sh")
                self.assertLess(
                    verify_at,
                    cleanup_at,
                    f"{family}/build.sh must verify the pin before SDK cleanup",
                )
                self.assertLess(
                    verify_at,
                    download_at,
                    f"{family}/build.sh must verify the pin before SDK download",
                )

    def run_whole_build_script(self, family, csproj_xml):
        """Run the real build.sh with a stubbed curl.

        The stub records any invocation and exits 23 (offline curl), so a
        pin mismatch must surface as a pin error without touching curl.
        """
        workdir = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, workdir, True)
        shutil.copy(
            os.path.join(REPO_ROOT, family, "subgraphs-net", "build.sh"),
            os.path.join(workdir, "build.sh"),
        )
        projdir = os.path.join(workdir, "eShop.Fake")
        os.makedirs(projdir)
        with open(
            os.path.join(projdir, "eShop.Fake.csproj"), "w", encoding="utf-8"
        ) as fh:
            fh.write(csproj_xml)
        bindir = os.path.join(workdir, "bin")
        os.makedirs(bindir)
        marker = os.path.join(workdir, "curl-invoked")
        with open(os.path.join(bindir, "curl"), "w", encoding="utf-8") as fh:
            fh.write(f'#!/usr/bin/env bash\ntouch "{marker}"\nexit 23\n')
        os.chmod(os.path.join(bindir, "curl"), 0o755)
        env = dict(os.environ)
        env["PATH"] = bindir + os.pathsep + env.get("PATH", "")
        proc = subprocess.run(
            ["bash", os.path.join(workdir, "build.sh")],
            capture_output=True,
            text=True,
            timeout=60,
            cwd=workdir,
            env=env,
        )
        return proc, os.path.exists(marker)

    PINNED_CSPROJ = (
        '<Project Sdk="Microsoft.NET.Sdk.Web">\n'
        '  <ItemGroup>\n'
        '    <PackageReference Include="HotChocolate.AspNetCore" Version="16.6.8" />\n'
        "  </ItemGroup>\n</Project>\n"
    )
    MISMATCHED_VARIANTS = {
        "ordered": (
            '<Project Sdk="Microsoft.NET.Sdk.Web">\n'
            '  <ItemGroup>\n'
            '    <PackageReference Include="HotChocolate.AspNetCore" Version="16.5.0-p.1" />\n'
            "  </ItemGroup>\n</Project>\n"
        ),
        "reordered": (
            '<Project Sdk="Microsoft.NET.Sdk.Web">\n'
            '  <ItemGroup>\n'
            '    <PackageReference Version="16.5.0-p.1" Include="HotChocolate.AspNetCore" />\n'
            "  </ItemGroup>\n</Project>\n"
        ),
        "separated": (
            '<Project Sdk="Microsoft.NET.Sdk.Web">\n'
            '  <ItemGroup>\n'
            '    <PackageReference Include="HotChocolate.AspNetCore" PrivateAssets="all" Version="16.5.0-p.1" />\n'
            "  </ItemGroup>\n</Project>\n"
        ),
        "multiline": (
            '<Project Sdk="Microsoft.NET.Sdk.Web">\n'
            '  <ItemGroup>\n'
            '    <PackageReference\n'
            '      Version="16.5.0-p.1"\n'
            '      Include="HotChocolate.AspNetCore" />\n'
            "  </ItemGroup>\n</Project>\n"
        ),
        "single_quoted": (
            '<Project Sdk="Microsoft.NET.Sdk.Web">\n'
            '  <ItemGroup>\n'
            "    <PackageReference Include='HotChocolate.AspNetCore' Version='16.5.0-p.1' />\n"
            "  </ItemGroup>\n</Project>\n"
        ),
    }
    COMMENTED_MISMATCH_CSPROJ = (
        '<Project Sdk="Microsoft.NET.Sdk.Web">\n'
        '  <ItemGroup>\n'
        '    <!-- <PackageReference Include="HotChocolate.AspNetCore" Version="16.5.0-p.1" /> -->\n'
        '    <PackageReference Include="HotChocolate.AspNetCore" Version="16.6.8" />\n'
        "  </ItemGroup>\n</Project>\n"
    )

    def test_whole_script_fails_fast_on_pin_mismatch(self):
        for family in self.FAMILIES:
            for variant, xml in self.MISMATCHED_VARIANTS.items():
                with self.subTest(family=family, variant=variant):
                    proc, curl_invoked = self.run_whole_build_script(family, xml)
                    self.assertNotEqual(proc.returncode, 0)
                    self.assertIn(
                        "not pinned to", proc.stdout + proc.stderr
                    )
                    self.assertFalse(
                        curl_invoked,
                        f"{family}/build.sh attempted the SDK download "
                        f"before reporting the pin mismatch ({variant})",
                    )

    def test_whole_script_ignores_commented_reference(self):
        # A commented-out mismatched reference alongside an active pinned
        # reference must pass the pin check (and therefore reach the
        # stubbed SDK download).
        for family in self.FAMILIES:
            with self.subTest(family=family):
                proc, curl_invoked = self.run_whole_build_script(
                    family, self.COMMENTED_MISMATCH_CSPROJ
                )
                self.assertTrue(
                    curl_invoked,
                    f"{family}/build.sh treated a commented-out "
                    "PackageReference as active",
                )

    def test_whole_script_passes_pin_check_before_sdk_install(self):
        # The pinned tree must get past pin verification (it then proceeds
        # to the stubbed SDK download and fails there, proving the pin
        # check ran first and accepted the pinned version).
        for family in self.FAMILIES:
            with self.subTest(family=family):
                proc, curl_invoked = self.run_whole_build_script(
                    family, self.PINNED_CSPROJ
                )
                self.assertIn(
                    "Verifying HotChocolate package references are pinned",
                    proc.stdout + proc.stderr,
                )
                self.assertTrue(
                    curl_invoked,
                    f"{family}/build.sh should reach the SDK download "
                    "once the pin check passes",
                )

    def test_pin_block_accepts_pinned_version(self):
        for family in self.FAMILIES:
            with self.subTest(family=family):
                proc = self.run_pin_block(family, self.PINNED_VERSION)
                self.assertEqual(proc.returncode, 0, proc.stderr + proc.stdout)

    def test_pin_block_rejects_mismatch(self):
        for family in self.FAMILIES:
            with self.subTest(family=family):
                proc = self.run_pin_block(family, "16.5.0-p.1")
                self.assertNotEqual(proc.returncode, 0)
                self.assertIn("not pinned to", proc.stdout + proc.stderr)


class FusionVersionOverrideTests(unittest.TestCase):
    """Both fusion install.sh scripts validate BENCH_GATEWAY_VERSION before any
    download and install exactly that HotChocolate version instead of resolving
    the latest for the channel."""

    INSTALL_SCRIPTS = (
        os.path.join(
            REPO_ROOT, "composite-schema", "gateways", "fusion", "install.sh"
        ),
        os.path.join(
            REPO_ROOT,
            "apollo-federation",
            "gateways",
            "fusion-nightly-fed",
            "install.sh",
        ),
    )
    BLOCK_START = (
        "# --- Validate explicit HotChocolate version override: begin ---"
    )
    BLOCK_END = "# --- Validate explicit HotChocolate version override: end ---"

    GOOD_VERSIONS = ("16.6.8", "16.7.0-p.27", "16.10.0-preview.1")
    BAD_VERSIONS = (
        "abc",
        "16.6",
        "16",
        "v16.6.8",
        "16.6.8;",
        "16.6.8..1",
        "16.6.8-",
        "16.6.8-.",
        "16.6.8-p.",
        "16.6.8-p..27",
        "16.6.8-.27",
        "latest",
        "16.6.x",
        "16.6.8 foo",
    )

    def extract_validation_block(self, path):
        with open(path, encoding="utf-8") as fh:
            content = fh.read()
        start = content.index(self.BLOCK_START)
        end = content.index(self.BLOCK_END)
        return content[start:end]

    def run_validation_block(self, path, version):
        block = self.extract_validation_block(path)
        workdir = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, workdir, True)
        wrapper = os.path.join(workdir, "version-check.sh")
        with open(wrapper, "w", encoding="utf-8") as fh:
            fh.write("set -u\n")
            fh.write('CHANNEL="preview"\n')
            fh.write(block + "\n")
        env = dict(os.environ)
        if version is not None:
            env["BENCH_GATEWAY_VERSION"] = version
        else:
            env.pop("BENCH_GATEWAY_VERSION", None)
        return subprocess.run(
            ["bash", wrapper],
            capture_output=True,
            text=True,
            timeout=60,
            env=env,
        )

    def test_validation_block_accepts_versions(self):
        for script in self.INSTALL_SCRIPTS:
            for version in self.GOOD_VERSIONS:
                with self.subTest(script=script, version=version):
                    proc = self.run_validation_block(script, version)
                    self.assertEqual(
                        proc.returncode, 0, proc.stderr + proc.stdout
                    )
                    self.assertIn("pinned", proc.stdout + proc.stderr)

    def test_validation_block_accepts_empty(self):
        for script in self.INSTALL_SCRIPTS:
            for version in ("", None):
                with self.subTest(script=script, version=version):
                    proc = self.run_validation_block(script, version)
                    self.assertEqual(
                        proc.returncode, 0, proc.stderr + proc.stdout
                    )

    def test_validation_block_rejects_garbage(self):
        for script in self.INSTALL_SCRIPTS:
            for version in self.BAD_VERSIONS:
                with self.subTest(script=script, version=version):
                    proc = self.run_validation_block(script, version)
                    self.assertNotEqual(proc.returncode, 0)
                    self.assertIn(
                        "invalid BENCH_GATEWAY_VERSION",
                        proc.stdout + proc.stderr,
                    )

    def run_whole_install_script(self, script, version):
        """Run the real install.sh with a stubbed curl.

        The stub records any invocation and exits 23 (offline curl), so an
        invalid pin must surface as a pin error before any download, while a
        valid pin must sail through validation and reach the SDK download.
        """
        workdir = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, workdir, True)
        shutil.copy(script, os.path.join(workdir, "install.sh"))
        bindir = os.path.join(workdir, "bin")
        os.makedirs(bindir)
        marker = os.path.join(workdir, "curl-invoked")
        with open(os.path.join(bindir, "curl"), "w", encoding="utf-8") as fh:
            fh.write(f'#!/usr/bin/env bash\ntouch "{marker}"\nexit 23\n')
        os.chmod(os.path.join(bindir, "curl"), 0o755)
        env = dict(os.environ)
        env["PATH"] = bindir + os.pathsep + env.get("PATH", "")
        env["BENCH_GATEWAY_VERSION"] = version
        env["BENCH_GATEWAY_CHANNEL"] = "preview"
        env["BENCH_GATEWAY_DOTNET"] = "10"
        proc = subprocess.run(
            ["bash", os.path.join(workdir, "install.sh")],
            capture_output=True,
            text=True,
            timeout=60,
            cwd=workdir,
            env=env,
        )
        return proc, os.path.exists(marker)

    def test_whole_script_fails_fast_on_invalid_version(self):
        for script in self.INSTALL_SCRIPTS:
            with self.subTest(script=script):
                proc, curl_invoked = self.run_whole_install_script(
                    script, "not-a-version"
                )
                self.assertNotEqual(proc.returncode, 0)
                self.assertIn(
                    "invalid BENCH_GATEWAY_VERSION",
                    proc.stdout + proc.stderr,
                )
                self.assertFalse(
                    curl_invoked,
                    f"{script} attempted a download before reporting the "
                    "invalid version",
                )

    def test_whole_script_passes_validation_before_sdk_download(self):
        # A valid pin must get past validation (it then proceeds to the
        # stubbed SDK download and fails there, proving validation ran first
        # and accepted the pin).
        for script in self.INSTALL_SCRIPTS:
            with self.subTest(script=script):
                proc, curl_invoked = self.run_whole_install_script(
                    script, "16.6.8"
                )
                self.assertNotEqual(proc.returncode, 0)
                self.assertNotIn(
                    "invalid BENCH_GATEWAY_VERSION",
                    proc.stdout + proc.stderr,
                )
                self.assertTrue(
                    curl_invoked,
                    f"{script} should reach the SDK download once the pin "
                    "check passes",
                )


if __name__ == "__main__":
    unittest.main()
