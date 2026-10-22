"""Regression tests for k6/build-matrix.py.

All benchmarks run against the HotChocolate subgraphs only: every matrix entry must
reference subgraphs-net, and gateway names carry no tech suffix.
"""

import glob
import importlib.util
import json
import os
import re
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
            "fusion-nightly-net-11",
            preview_check=lambda: (False, "16.6.0", None),
        )
        self.assertEqual(len(matrices["gateways"]), 1)
        entry = matrices["gateways"][0]
        self.assertEqual(entry["name"], "fusion-nightly-net-11")
        self.assertEqual(entry["dotnet"], "11")
        self.assertEqual(entry["channel"], "preview")
        self.assertEqual(entry["aot"], "0")
        self.assertEqual(entry["path"], "composite-schema/gateways/fusion")
        self.assertEqual(entry["subgraphs"], "subgraphs-net")
        self.assertEqual(entry["subgraph_tech"], ".net")
        self.assertEqual(
            entry["gateway_artifact"], "prebuilt-gateway-fusion-nightly-net-11"
        )

    def test_aot_selection(self):
        matrices = MATRIX.build_matrices(
            "fusion-aot-11",
            preview_check=lambda: (False, "16.6.0", None),
        )
        self.assertEqual(len(matrices["gateways"]), 1)
        entry = matrices["gateways"][0]
        self.assertEqual(entry["name"], "fusion-aot-11")
        self.assertEqual(entry["dotnet"], "11")
        self.assertEqual(entry["channel"], "stable")
        self.assertEqual(entry["aot"], "1")
        self.assertEqual(entry["path"], "composite-schema/gateways/fusion")
        self.assertEqual(
            entry["gateway_artifact"], "prebuilt-gateway-fusion-aot-11"
        )

    def test_stable_and_preview_variants_preserved(self):
        matrices = MATRIX.build_matrices(
            "all", preview_check=lambda: (True, "16.6.0", "16.7.0-p.1")
        )
        by_name = {e["name"]: e for e in matrices["gateways"]}
        self.assertEqual(by_name["fusion-net-10"]["channel"], "stable")
        self.assertEqual(by_name["fusion-net-10"]["dotnet"], "10")
        self.assertEqual(by_name["fusion-net-10"]["aot"], "0")
        self.assertEqual(by_name["fusion-net-11"]["channel"], "stable")
        self.assertEqual(by_name["fusion-net-11"]["dotnet"], "11")
        self.assertEqual(by_name["fusion-aot-11"]["aot"], "1")
        self.assertEqual(by_name["fusion-fed-net-10"]["channel"], "stable")
        self.assertEqual(
            by_name["fusion-fed-net-10"]["path"],
            "apollo-federation/gateways/fusion-fed",
        )
        self.assertEqual(by_name["fusion-nightly-net-10"]["channel"], "preview")
        self.assertEqual(by_name["fusion-nightly-net-10"]["dotnet"], "10")
        self.assertEqual(by_name["fusion-nightly-net-11"]["dotnet"], "11")
        self.assertEqual(by_name["fusion-nightly-aot-11"]["aot"], "1")
        self.assertEqual(by_name["fusion-nightly-fed-net-10"]["channel"], "preview")
        self.assertEqual(
            by_name["fusion-nightly-fed-net-10"]["path"],
            "apollo-federation/gateways/fusion-fed",
        )
        self.assertEqual(by_name["fusion-nightly-fed-net-11"]["dotnet"], "11")
        self.assertEqual(by_name["fusion-nightly-fed-aot-11"]["aot"], "1")

    def test_nightly_skipped_when_preview_not_ahead(self):
        matrices = MATRIX.build_matrices(
            "all", preview_check=lambda: (False, "16.6.0", "16.6.0")
        )
        names = {e["name"] for e in matrices["gateways"]}
        self.assertFalse(names & {
            "fusion-nightly-net-10",
            "fusion-nightly-net-11",
            "fusion-nightly-aot-11",
            "fusion-nightly-fed-net-10",
            "fusion-nightly-fed-net-11",
            "fusion-nightly-fed-aot-11",
        })
        # Stable and non-nightly gateways still run.
        self.assertIn("fusion-net-10", names)
        self.assertIn("fusion-fed-net-10", names)
        self.assertIn("cosmo", names)

    def test_explicit_nightly_selection_always_honored(self):
        for nightly in (
            "fusion-nightly-net-10",
            "fusion-nightly-net-11",
            "fusion-nightly-aot-11",
            "fusion-nightly-fed-net-10",
            "fusion-nightly-fed-net-11",
            "fusion-nightly-fed-aot-11",
        ):
            with self.subTest(gateway=nightly):
                matrices = MATRIX.build_matrices(
                    nightly, preview_check=lambda: (False, "16.6.0", None)
                )
                self.assertEqual(
                    [e["name"] for e in matrices["gateways"]], [nightly]
                )

    def test_feddi_runs_in_every_mode(self):
        matrices = MATRIX.build_matrices(
            "all", preview_check=lambda: (False, "16.6.0", None)
        )
        burst_names = {e["base_name"] for e in matrices["gateways_burst"]}
        self.assertIn("feddi-gateway", burst_names)
        not_run_names = {e["base_name"] for e in matrices["not_run_burst"]}
        self.assertNotIn("feddi-gateway", not_run_names)
        constant_names = {e["base_name"] for e in matrices["gateways_constant"]}
        self.assertIn("feddi-gateway", constant_names)

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

    def test_caliban_selection(self):
        matrices = MATRIX.build_matrices(
            "caliban", preview_check=lambda: (False, "16.6.0", None)
        )
        self.assertEqual([e["name"] for e in matrices["gateways"]], ["caliban"])
        entry = matrices["gateways"][0]
        self.assertEqual(entry["path"], "apollo-federation/gateways/caliban")
        self.assertEqual(entry["gateway_artifact"], "prebuilt-gateway-caliban")
        self.assertEqual(entry["subgraphs"], "subgraphs-net")
        self.assertEqual(entry["subgraph_tech"], ".net")
        self.assertEqual(
            entry["display_name"], "caliban (HotChocolate subgraphs)"
        )
        self.assertEqual(
            matrices["subgraph_builds"],
            [
                {
                    "path": "apollo-federation/subgraphs-net",
                    "artifact": "prebuilt-apollo-federation-subgraphs",
                }
            ],
        )

    def test_apollo_routers_have_independent_builds_and_identities_in_all_modes(self):
        for preview_ahead in (False, True):
            with self.subTest(fusion_preview_ahead=preview_ahead):
                matrices = MATRIX.build_matrices(
                    "all", preview_check=lambda: (preview_ahead, "16.6.0", "16.7.0-p.1")
                )
                for key in ("gateways", "gateways_constant", "gateways_burst"):
                    by_name = {entry["name"]: entry for entry in matrices[key]}
                    for name, channel in (("apollo-router", "stable"), ("apollo-router-v3", "preview")):
                        entry = by_name[name]
                        self.assertEqual(entry["base_name"], name)
                        self.assertEqual(entry["path"], f"apollo-federation/gateways/{name}")
                        self.assertEqual(entry["gateway_artifact"], f"prebuilt-gateway-{name}")
                        self.assertEqual(entry["channel"], channel)
                        self.assertEqual(entry["display_name"], f"{name} (HotChocolate subgraphs)")
                builds = {entry["artifact"]: entry for entry in matrices["gateway_builds"]}
                for name in ("apollo-router", "apollo-router-v3"):
                    self.assertEqual(
                        builds[f"prebuilt-gateway-{name}"]["path"],
                        f"apollo-federation/gateways/{name}",
                    )
                for key in ("not_run_constant", "not_run_burst"):
                    self.assertFalse({e["name"] for e in matrices[key]} & {"apollo-router", "apollo-router-v3"})

    def test_select_apollo_router_v3_without_querying_fusion_channel(self):
        def unexpected_preview_check():
            self.fail("Apollo Router preview must not depend on the Fusion channel")

        matrices = MATRIX.build_matrices(
            "apollo-router-v3", preview_check=unexpected_preview_check, fusion_version="16.6.8"
        )
        for key in ("gateways", "gateways_constant", "gateways_burst"):
            self.assertEqual([entry["name"] for entry in matrices[key]], ["apollo-router-v3"])
            self.assertNotIn("version", matrices[key][0])
        self.assertEqual(
            matrices["gateway_builds"],
            [{
                "path": "apollo-federation/gateways/apollo-router-v3",
                "artifact": "prebuilt-gateway-apollo-router-v3",
                "channel": "preview",
                "dotnet": "10",
                "aot": "0",
            }],
        )
        self.assertEqual(
            matrices["subgraph_builds"],
            [{
                "path": "apollo-federation/subgraphs-net",
                "artifact": "prebuilt-apollo-federation-subgraphs",
            }],
        )

    def test_select_apollo_router_keeps_stable_identity(self):
        matrices = MATRIX.build_matrices("apollo-router")
        self.assertEqual([entry["name"] for entry in matrices["gateways"]], ["apollo-router"])
        self.assertEqual(matrices["gateways"][0]["channel"], "stable")
        self.assertEqual(matrices["gateway_builds"][0]["artifact"], "prebuilt-gateway-apollo-router")

    def test_unknown_gateway_fails(self):
        with self.assertRaises(SystemExit):
            MATRIX.build_matrices(
                "does-not-exist", preview_check=lambda: (False, "16.6.0", None)
            )

    def test_legacy_tech_suffix_selection_rejected(self):
        # The old "-rust"/"-net" suffixed selections no longer exist, nor do
        # the pre-rename Fusion ids.
        for legacy in (
            "fusion-rust",
            "fusion-net",
            "cosmo-rust",
            "fusion",
            "fusion-nightly",
            "fusion-nightly-net11",
            "fusion-nightly-fed",
        ):
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
            "fusion-net-10",
            "fusion-net-11",
            "fusion-aot-11",
            "fusion-fed-net-10",
            "fusion-fed-net-11",
            "fusion-fed-aot-11",
            "fusion-nightly-net-10",
            "fusion-nightly-net-11",
            "fusion-nightly-aot-11",
            "fusion-nightly-fed-net-10",
            "fusion-nightly-fed-net-11",
            "fusion-nightly-fed-aot-11",
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
            builds["prebuilt-gateway-fusion-nightly-net-10"]["version"], "16.6.8"
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
            {
                "fusion-nightly-net-10",
                "fusion-nightly-net-11",
                "fusion-nightly-aot-11",
                "fusion-nightly-fed-net-10",
                "fusion-nightly-fed-net-11",
                "fusion-nightly-fed-aot-11",
            }
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
            "fusion-nightly-net-10",
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
            self.assertEqual(by_name["fusion-net-10"]["version"], "16.6.8")
            self.assertNotIn("version", by_name["cosmo"])
            builds = {
                b["artifact"]: b for b in json.loads(outputs["gateway_builds"])
            }
            self.assertEqual(
                builds["prebuilt-gateway-fusion-net-10"]["version"], "16.6.8"
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
            gateways = json.loads(outputs["gateways"])
            self.assertEqual([g["name"] for g in gateways], ["cosmo"])
            self.assertEqual(gateways[0]["subgraphs"], "subgraphs-net")


class ResolveHotchocolateChannelsTests(unittest.TestCase):
    """Direct SemVer tests for resolve_hotchocolate_channels.

    The nightly gating tests above mock preview_check; these exercise the real
    resolver against version feeds so numeric ordering bugs (string
    comparison of 16.10 vs 16.9, or of p.10 vs p.9) cannot slip through.
    """

    INSTALL_SCRIPTS = (
        os.path.join(
            REPO_ROOT, "composite-schema", "gateways", "fusion", "install.sh"
        ),
        os.path.join(
            REPO_ROOT, "apollo-federation", "gateways", "fusion-fed",
            "install.sh",
        ),
    )
    RESOLVER_START = (
        "# --- Resolve latest HotChocolate version for channel: begin ---"
    )
    RESOLVER_END = "# --- Resolve latest HotChocolate version for channel: end ---"

    def test_same_core_preview_is_not_ahead(self):
        # A prerelease on the shipped core line is older than the stable
        # release itself (SemVer: 16.6.8-p.27 < 16.6.8), so nightly must stay
        # off even though a "newer-looking" preview tag exists.
        ahead, stable, preview = MATRIX.resolve_hotchocolate_channels([
            "16.6.7", "16.6.8", "16.6.8-p.27",
        ])
        self.assertFalse(ahead)
        self.assertEqual(stable, "16.6.8")
        self.assertEqual(preview, "16.6.8-p.27")

    def test_higher_patch_preview_is_ahead(self):
        ahead, stable, preview = MATRIX.resolve_hotchocolate_channels([
            "16.6.8", "16.6.9-p.1",
        ])
        self.assertTrue(ahead)
        self.assertEqual(stable, "16.6.8")
        self.assertEqual(preview, "16.6.9-p.1")

    def test_minor_version_compares_numerically(self):
        # 16.10 > 16.9 numerically; a string comparison would rank "16.10.x"
        # below "16.9.x" and pick the wrong latest on both channels.
        ahead, stable, preview = MATRIX.resolve_hotchocolate_channels([
            "16.9.3", "16.10.0", "16.9.4-p.2", "16.10.1-p.5",
        ])
        self.assertEqual(stable, "16.10.0")
        self.assertEqual(preview, "16.10.1-p.5")
        self.assertTrue(ahead)

    def test_prerelease_number_compares_numerically(self):
        # p.10 > p.9 numerically; a string comparison would pick p.9.
        ahead, stable, preview = MATRIX.resolve_hotchocolate_channels([
            "16.6.8", "16.7.0-p.9", "16.7.0-p.10",
        ])
        self.assertEqual(stable, "16.6.8")
        self.assertEqual(preview, "16.7.0-p.10")
        self.assertTrue(ahead)

    def test_feed_order_does_not_matter(self):
        versions = ["16.6.8", "16.7.0-p.9", "16.7.0-p.10", "16.6.9",
                    "16.10.0-p.1"]
        expected = (True, "16.6.9", "16.10.0-p.1")
        self.assertEqual(
            MATRIX.resolve_hotchocolate_channels(versions), expected)
        orders = [
            list(reversed(versions)),
            versions[2:] + versions[:2],
            sorted(versions),
            sorted(versions, reverse=True),
        ]
        for order in orders:
            with self.subTest(order=order):
                self.assertEqual(
                    MATRIX.resolve_hotchocolate_channels(order), expected)

    def extract_installer_resolver(self, script):
        with open(script, encoding="utf-8") as fh:
            content = fh.read()
        start = content.index(self.RESOLVER_START) + len(self.RESOLVER_START)
        end = content.index(self.RESOLVER_END)
        return content[start:end]

    def run_installer_resolver(self, script, channel, versions):
        proc = subprocess.run(
            [sys.executable, "-c", self.extract_installer_resolver(script)],
            input=json.dumps({"versions": versions}),
            capture_output=True,
            text=True,
            timeout=60,
            env={**os.environ, "CHANNEL": channel},
        )
        self.assertEqual(proc.returncode, 0, proc.stderr)
        return proc.stdout.strip()

    def test_installer_and_matrix_resolvers_agree(self):
        # Both fusion install.sh scripts embed their own channel resolver for
        # the build-time version pick; it must select the same latest stable
        # and latest preview as the matrix resolver, on a feed that stresses
        # numeric ordering (16.10, p.10).
        versions = [
            "16.6.7", "16.6.8", "16.6.8-p.27", "16.6.9-p.1",
            "16.7.0-p.9", "16.7.0-p.10", "16.9.3", "16.10.0",
            "16.10.1-p.5",
        ]
        _, stable, preview = MATRIX.resolve_hotchocolate_channels(versions)
        self.assertEqual((stable, preview), ("16.10.0", "16.10.1-p.5"))
        for script in self.INSTALL_SCRIPTS:
            with self.subTest(script=script):
                self.assertEqual(
                    self.run_installer_resolver(script, "stable", versions),
                    stable,
                )
                self.assertEqual(
                    self.run_installer_resolver(script, "preview", versions),
                    preview,
                )


class ConfigTests(unittest.TestCase):

    def read(self, *parts):
        with open(os.path.join(REPO_ROOT, *parts), encoding="utf-8") as fh:
            return fh.read()

    def test_config_file_is_canonical_json_without_versions(self):
        raw = self.read("k6", "benchmark-config.json")
        self.assertEqual(raw, json.dumps(json.loads(raw), indent=2, ensure_ascii=False) + "\n")
        self.assertEqual(list(MATRIX.CONFIG), ["subgraphs", "gateways"])
        self.assertNotIn('"version"', raw)
        allowed_variant_keys = {"id", "label", "preview", "path", "language", "runtime", "channel", "dotnet",
                                "aot", "platformFeatures", "gatewayFeatures"}
        for product in MATRIX.GATEWAYS:
            self.assertEqual(set(product), {"id", "name", "vendor", "repositoryUrl", "variants"})
            for variant in product["variants"]:
                self.assertLessEqual(set(variant), allowed_variant_keys, variant["id"])
        self.assertEqual(
            {v["id"]: v["label"] for v in MATRIX.VARIANTS if "label" in v},
            {
                "fusion-nightly-net-10": "Fusion Nightly",
                "fusion-nightly-net-11": "Fusion Nightly",
                "fusion-nightly-aot-11": "Fusion Nightly",
                "fusion-nightly-fed-net-10": "Fusion Nightly",
                "fusion-nightly-fed-net-11": "Fusion Nightly",
                "fusion-nightly-fed-aot-11": "Fusion Nightly",
            },
        )
        self.assertEqual(
            {v["id"]: v["preview"] for v in MATRIX.VARIANTS if "preview" in v},
            {"feddi-gateway": True},
        )

    def test_variant_ids_unique_and_paths_exist(self):
        ids = [v["id"] for v in MATRIX.VARIANTS]
        self.assertEqual(len(ids), len(set(ids)))
        for variant in MATRIX.VARIANTS:
            with self.subTest(variant=variant["id"]):
                self.assertTrue(os.path.isfile(os.path.join(REPO_ROOT, variant["path"], "install.sh")))
                self.assertIn(variant["path"].split("/", 1)[0], MATRIX.SUBGRAPH_ARTIFACT_BY_CATEGORY)

    def test_matrix_is_derived_from_variants(self):
        matrices = MATRIX.build_matrices("all", preview_check=lambda: (True, "16.6.0", "16.7.0-p.1"))
        self.assertEqual([e["name"] for e in matrices["gateways"]], [v["id"] for v in MATRIX.VARIANTS])
        self.assertEqual(MATRIX.FUSION_BASE_NAMES,
                         ("fusion-net-10", "fusion-net-11", "fusion-aot-11",
                          "fusion-fed-net-10", "fusion-fed-net-11", "fusion-fed-aot-11",
                          "fusion-nightly-net-10", "fusion-nightly-net-11", "fusion-nightly-aot-11",
                          "fusion-nightly-fed-net-10", "fusion-nightly-fed-net-11",
                          "fusion-nightly-fed-aot-11"))
        self.assertEqual(MATRIX.NIGHTLY_BASE_NAMES,
                         ("fusion-nightly-net-10", "fusion-nightly-net-11", "fusion-nightly-aot-11",
                          "fusion-nightly-fed-net-10", "fusion-nightly-fed-net-11",
                          "fusion-nightly-fed-aot-11"))
        self.assertEqual(MATRIX.FUSION_VARIANT_MIGRATION,
                         {"fusion": "fusion-net-10",
                          "fusion-nightly": "fusion-nightly-net-10",
                          "fusion-nightly-net11": "fusion-nightly-net-11",
                          "fusion-nightly-fed": "fusion-nightly-fed-net-10"})
        for old, new in MATRIX.FUSION_VARIANT_MIGRATION.items():
            self.assertEqual(MATRIX.migrate_fusion_variant(old), new)
            self.assertEqual(MATRIX.migrate_fusion_variant(new), new)

    def test_workflow_dispatch_gateway_options_match_variants(self):
        # Choice options can't be computed in GitHub Actions.
        workflow = self.read(".github", "workflows", "benchmark.yml")
        block = workflow.split("      gateway:\n", 1)[1].split("      fusion_version:", 1)[0]
        options = re.findall(r"^          - (\S+)$", block, re.M)
        self.assertEqual(options, ["all"] + [v["id"] for v in MATRIX.VARIANTS])

    def test_runtime_async_feature_matches_dotnet_11_build(self):
        # install.sh enables runtime-async exactly for the .NET 11 target.
        declared = {
            v["id"] for v in MATRIX.VARIANTS
            if "runtime-async" in [f["id"] for f in v.get("platformFeatures", [])]
        }
        self.assertEqual(declared, {v["id"] for v in MATRIX.VARIANTS if v.get("dotnet") == "11"})
        self.assertEqual(declared, {
            "fusion-net-11", "fusion-aot-11",
            "fusion-fed-net-11", "fusion-fed-aot-11",
            "fusion-nightly-net-11", "fusion-nightly-aot-11",
            "fusion-nightly-fed-net-11", "fusion-nightly-fed-aot-11",
        })
        self.assertEqual(
            {v["id"] for v in MATRIX.VARIANTS if v.get("aot")},
            {"fusion-aot-11", "fusion-fed-aot-11",
             "fusion-nightly-aot-11", "fusion-nightly-fed-aot-11"},
        )
        for path in {MATRIX.VARIANTS_BY_ID[v]["path"] for v in MATRIX.FUSION_BASE_NAMES}:
            with self.subTest(script=path):
                script = self.read(path, "install.sh")
                block = script.split('    if [[ "$DOTNET_TARGET" == "11" ]]; then\n', 1)[1].split("    fi\n", 1)[0]
                self.assertIn("<TargetFramework>net11.0</TargetFramework>", block)
                self.assertIn("runtime-async=on", block)
                code = "\n".join(l for l in script.splitlines() if not l.lstrip().startswith("#"))
                self.assertEqual(code.count("runtime-async=on"), 1)
                csproj = self.read(path, "eShop.Gateway", "eShop.Gateway.csproj")
                self.assertNotIn("runtime-async=on", csproj)

    def test_subgraph_delay_not_hardcoded(self):
        for family in MATRIX.SUBGRAPH_ARTIFACT_BY_CATEGORY:
            for program in glob.glob(os.path.join(REPO_ROOT, family, "subgraphs-net", "eShop.*", "Program.cs")):
                with self.subTest(program=os.path.relpath(program, REPO_ROOT)):
                    with open(program, encoding="utf-8") as fh:
                        content = fh.read()
                    self.assertNotRegex(content, r"Task\.Delay\(\d")
                    self.assertIn('"BENCHMARK_SUBGRAPH_DELAY_MS"', content)

    def test_catalog_groups_variants_by_product(self):
        catalog = {p["id"]: p for p in MATRIX.report_gateway_catalog()}
        self.assertEqual([p["id"] for p in MATRIX.GATEWAYS], list(catalog))
        variants = {v["id"]: v for p in catalog.values() for v in p["variants"]}
        self.assertEqual(list(variants), [v["id"] for v in MATRIX.VARIANTS])
        self.assertEqual(variants["fusion-nightly-fed-net-10"]["composition"], "apollo-federation")
        self.assertEqual(variants["fusion-fed-net-10"]["composition"], "apollo-federation")
        self.assertEqual(variants["feddi-gateway"]["composition"], "composite-schema")
        self.assertTrue(variants["feddi-gateway"]["preview"])
        self.assertEqual(variants["fusion-nightly-net-10"]["label"], "Fusion Nightly")
        self.assertEqual(variants["fusion-nightly-net-11"]["label"], "Fusion Nightly")
        self.assertEqual(variants["fusion-nightly-aot-11"]["label"], "Fusion Nightly")
        self.assertEqual(variants["fusion-nightly-fed-net-10"]["label"], "Fusion Nightly")
        self.assertEqual(variants["fusion-nightly-fed-net-11"]["label"], "Fusion Nightly")
        self.assertEqual(variants["fusion-nightly-fed-aot-11"]["label"], "Fusion Nightly")
        self.assertNotIn("label", variants["fusion-net-10"])
        self.assertEqual(
            [f["id"] for f in variants["hive-gateway-router-runtime"]["features"]],
            ["router-runtime"],
        )
        self.assertNotIn("runtime", variants["hive-router"]["platform"])
        self.assertEqual(variants["fusion-net-10"]["platform"]["runtime"], {"name": ".NET"})


if __name__ == "__main__":
    unittest.main()
