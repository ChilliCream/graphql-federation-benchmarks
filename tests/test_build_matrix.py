"""Regression tests for k6/build-matrix.py.

All benchmarks run against the HotChocolate subgraphs only: every matrix entry must
reference subgraphs-net, and gateway names carry no tech suffix.
"""

import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MATRIX_SCRIPT = os.path.join(REPO_ROOT, "k6", "build-matrix.py")


def load_matrix_module():
    spec = importlib.util.spec_from_file_location("build_matrix", MATRIX_SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


MATRIX = load_matrix_module()


class BuildMatrixTests(unittest.TestCase):
    def test_all_entries_dotnet_only(self):
        matrices = MATRIX.build_matrices(
            "all", preview_check=lambda: (False, "16.6.0", None)
        )
        self.assertTrue(matrices["gateways"], "expected a non-empty gateway matrix")
        for entry in matrices["gateways"]:
            with self.subTest(gateway=entry["name"]):
                self.assertEqual(entry["subgraphs"], "subgraphs-net")
                self.assertEqual(entry["subgraph_tech"], ".net")
                self.assertFalse(entry["name"].endswith("-rust"))
                self.assertFalse(entry["name"].endswith("-net"))
                self.assertEqual(entry["name"], entry["base_name"])

    def test_display_name_leads_with_hotchocolate(self):
        matrices = MATRIX.build_matrices(
            "all", preview_check=lambda: (False, "16.6.0", None)
        )
        self.assertTrue(matrices["gateways"], "expected a non-empty gateway matrix")
        for entry in matrices["gateways"]:
            with self.subTest(gateway=entry["name"]):
                self.assertEqual(
                    entry["display_name"],
                    f"{entry['name']} (HotChocolate subgraphs)",
                )

    def test_no_gateways_net_output(self):
        matrices = MATRIX.build_matrices(
            "all", preview_check=lambda: (False, "16.6.0", None)
        )
        self.assertNotIn("gateways_net", matrices)

    def test_subgraph_builds_cover_both_families(self):
        matrices = MATRIX.build_matrices(
            "all", preview_check=lambda: (False, "16.6.0", None)
        )
        by_path = {b["path"]: b["artifact"] for b in matrices["subgraph_builds"]}
        self.assertEqual(
            by_path,
            {
                "apollo-federation/subgraphs-net": "prebuilt-apollo-federation-subgraphs",
                "composite-schema/subgraphs-net": "prebuilt-composite-schema-subgraphs",
            },
        )

    def test_net11_selection(self):
        matrices = MATRIX.build_matrices(
            "fusion-nightly-net11",
            preview_check=lambda: (False, "16.6.0", None),
        )
        self.assertEqual(len(matrices["gateways"]), 1)
        entry = matrices["gateways"][0]
        self.assertEqual(entry["name"], "fusion-nightly-net11")
        self.assertEqual(entry["dotnet"], "11")
        self.assertEqual(entry["channel"], "preview")
        self.assertEqual(entry["path"], "composite-schema/gateways/fusion")
        self.assertEqual(entry["subgraphs"], "subgraphs-net")
        self.assertEqual(entry["subgraph_tech"], ".net")
        self.assertEqual(
            entry["gateway_artifact"], "prebuilt-gateway-fusion-nightly-net11"
        )

    def test_stable_and_preview_variants_preserved(self):
        matrices = MATRIX.build_matrices(
            "all", preview_check=lambda: (True, "16.6.0", "16.7.0-p.1")
        )
        by_name = {e["name"]: e for e in matrices["gateways"]}
        self.assertEqual(by_name["fusion"]["channel"], "stable")
        self.assertEqual(by_name["fusion"]["dotnet"], "10")
        self.assertEqual(by_name["fusion-nightly"]["channel"], "preview")
        self.assertEqual(by_name["fusion-nightly"]["dotnet"], "10")
        self.assertEqual(by_name["fusion-nightly-net11"]["dotnet"], "11")
        self.assertEqual(by_name["fusion-nightly-fed"]["channel"], "preview")

    def test_nightly_skipped_when_preview_not_ahead(self):
        matrices = MATRIX.build_matrices(
            "all", preview_check=lambda: (False, "16.6.0", "16.6.0")
        )
        names = {e["name"] for e in matrices["gateways"]}
        self.assertFalse(names & {"fusion-nightly", "fusion-nightly-net11", "fusion-nightly-fed"})
        # Stable and non-nightly gateways still run.
        self.assertIn("fusion", names)
        self.assertIn("cosmo", names)

    def test_explicit_nightly_selection_always_honored(self):
        for nightly in ("fusion-nightly", "fusion-nightly-net11", "fusion-nightly-fed"):
            with self.subTest(gateway=nightly):
                matrices = MATRIX.build_matrices(
                    nightly, preview_check=lambda: (False, "16.6.0", None)
                )
                self.assertEqual(
                    [e["name"] for e in matrices["gateways"]], [nightly]
                )

    def test_feddi_burst_exclusion_preserved(self):
        matrices = MATRIX.build_matrices(
            "all", preview_check=lambda: (False, "16.6.0", None)
        )
        burst_names = {e["base_name"] for e in matrices["gateways_burst"]}
        self.assertNotIn("feddi", burst_names)
        not_run_names = {e["base_name"] for e in matrices["not_run_burst"]}
        self.assertIn("feddi", not_run_names)
        constant_names = {e["base_name"] for e in matrices["gateways_constant"]}
        self.assertIn("feddi", constant_names)

    def test_single_gateway_selection(self):
        matrices = MATRIX.build_matrices(
            "cosmo", preview_check=lambda: (False, "16.6.0", None)
        )
        self.assertEqual([e["name"] for e in matrices["gateways"]], ["cosmo"])
        self.assertEqual(
            matrices["subgraph_builds"],
            [
                {
                    "path": "apollo-federation/subgraphs-net",
                    "artifact": "prebuilt-apollo-federation-subgraphs",
                }
            ],
        )

    def test_unknown_gateway_fails(self):
        with self.assertRaises(SystemExit):
            MATRIX.build_matrices(
                "does-not-exist", preview_check=lambda: (False, "16.6.0", None)
            )

    def test_legacy_tech_suffix_selection_rejected(self):
        # The old "-rust"/"-net" suffixed selections no longer exist.
        for legacy in ("fusion-rust", "fusion-net", "cosmo-rust"):
            with self.subTest(selection=legacy):
                with self.assertRaises(SystemExit):
                    MATRIX.build_matrices(
                        legacy, preview_check=lambda: (False, "16.6.0", None)
                    )

    def test_empty_version_keeps_entries_unchanged(self):
        # Empty FUSION_VERSION must keep the matrix byte-identical: no
        # "version" key anywhere and today's display names.
        for version in ("", None):
            with self.subTest(version=version):
                matrices = MATRIX.build_matrices(
                    "all",
                    preview_check=lambda: (True, "16.6.0", "16.7.0-p.1"),
                    fusion_version=version,
                )
                for entry in matrices["gateways"]:
                    self.assertNotIn("version", entry)
                    self.assertEqual(
                        entry["display_name"],
                        f"{entry['name']} (HotChocolate subgraphs)",
                    )
                for build in matrices["gateway_builds"]:
                    self.assertNotIn("version", build)

    def test_explicit_version_flows_into_fusion_entries_only(self):
        matrices = MATRIX.build_matrices(
            "all",
            preview_check=lambda: (False, "16.6.0", None),
            fusion_version="16.6.8",
        )
        by_name = {e["name"]: e for e in matrices["gateways"]}
        for nightly in (
            "fusion",
            "fusion-nightly",
            "fusion-nightly-net11",
            "fusion-nightly-fed",
        ):
            with self.subTest(gateway=nightly):
                self.assertEqual(by_name[nightly]["version"], "16.6.8")
                self.assertEqual(
                    by_name[nightly]["display_name"],
                    f"{nightly} 16.6.8 (HotChocolate subgraphs)",
                )
        # Non-fusion gateways ignore the pin.
        self.assertNotIn("version", by_name["cosmo"])
        self.assertEqual(
            by_name["cosmo"]["display_name"], "cosmo (HotChocolate subgraphs)"
        )
        # Gateway builds carry the pin for fusion artifacts only.
        builds = {b["artifact"]: b for b in matrices["gateway_builds"]}
        self.assertEqual(
            builds["prebuilt-gateway-fusion-nightly"]["version"], "16.6.8"
        )
        self.assertNotIn("version", builds["prebuilt-gateway-cosmo"])

    def test_explicit_version_bypasses_nightly_skip(self):
        # Preview not ahead, yet the nightly variants are kept when pinned.
        matrices = MATRIX.build_matrices(
            "all",
            preview_check=lambda: (False, "16.6.0", "16.6.0"),
            fusion_version="16.7.0-p.27",
        )
        names = {e["name"] for e in matrices["gateways"]}
        self.assertTrue(
            {"fusion-nightly", "fusion-nightly-net11", "fusion-nightly-fed"}
            <= names
        )

    def test_explicit_version_ignored_for_single_nonfusion_selection(self):
        matrices = MATRIX.build_matrices(
            "cosmo",
            preview_check=lambda: (False, "16.6.0", None),
            fusion_version="16.6.8",
        )
        self.assertEqual([e["name"] for e in matrices["gateways"]], ["cosmo"])
        self.assertNotIn("version", matrices["gateways"][0])

    def test_invalid_version_rejected(self):
        for bad in (
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
        ):
            with self.subTest(version=bad):
                with self.assertRaises(SystemExit):
                    MATRIX.build_matrices(
                        "all",
                        preview_check=lambda: (False, "16.6.0", None),
                        fusion_version=bad,
                    )

    def test_prerelease_version_accepted(self):
        matrices = MATRIX.build_matrices(
            "fusion-nightly",
            preview_check=lambda: (False, "16.6.0", None),
            fusion_version="16.7.0-p.27",
        )
        self.assertEqual(matrices["gateways"][0]["version"], "16.7.0-p.27")

    def test_main_reads_fusion_version_env(self):
        env = dict(os.environ)
        env["SELECTED_GATEWAY"] = "all"
        env["FUSION_VERSION"] = "16.6.8"
        with tempfile.TemporaryDirectory() as tmp:
            output_path = os.path.join(tmp, "github_output")
            env["GITHUB_OUTPUT"] = output_path
            proc = subprocess.run(
                [sys.executable, MATRIX_SCRIPT],
                env=env,
                capture_output=True,
                text=True,
                timeout=120,
            )
            self.assertEqual(proc.returncode, 0, proc.stderr)
            outputs = {}
            with open(output_path) as fh:
                for line in fh:
                    key, _, value = line.strip().partition("=")
                    outputs[key] = value
            gateways = json.loads(outputs["gateways"])
            by_name = {g["name"]: g for g in gateways}
            self.assertEqual(by_name["fusion"]["version"], "16.6.8")
            self.assertNotIn("version", by_name["cosmo"])
            builds = {
                b["artifact"]: b for b in json.loads(outputs["gateway_builds"])
            }
            self.assertEqual(
                builds["prebuilt-gateway-fusion"]["version"], "16.6.8"
            )

    def test_main_rejects_invalid_fusion_version_env(self):
        env = dict(os.environ)
        env["SELECTED_GATEWAY"] = "all"
        env["FUSION_VERSION"] = "not-a-version"
        proc = subprocess.run(
            [sys.executable, MATRIX_SCRIPT],
            env=env,
            capture_output=True,
            text=True,
            timeout=120,
        )
        self.assertNotEqual(proc.returncode, 0)
        self.assertIn("invalid FUSION_VERSION", proc.stderr)

    def test_main_writes_workflow_outputs(self):
        env = dict(os.environ)
        env["SELECTED_GATEWAY"] = "cosmo"
        with tempfile.TemporaryDirectory() as tmp:
            output_path = os.path.join(tmp, "github_output")
            env["GITHUB_OUTPUT"] = output_path
            proc = subprocess.run(
                [sys.executable, MATRIX_SCRIPT],
                env=env,
                capture_output=True,
                text=True,
                timeout=120,
            )
            self.assertEqual(proc.returncode, 0, proc.stderr)
            outputs = {}
            with open(output_path) as fh:
                for line in fh:
                    key, _, value = line.strip().partition("=")
                    outputs[key] = value
            self.assertNotIn("gateways_net", outputs)
            gateways = json.loads(outputs["gateways"])
            self.assertEqual([g["name"] for g in gateways], ["cosmo"])
            self.assertEqual(gateways[0]["subgraphs"], "subgraphs-net")


if __name__ == "__main__":
    unittest.main()
