"""Regression tests for k6/migrate-gateway-variants.py.

Covers the historical Fusion rename (fusion -> fusion-net-10,
fusion-nightly -> fusion-nightly-net-10,
fusion-nightly-net11 -> fusion-nightly-net-11,
fusion-nightly-fed -> fusion-nightly-fed-net-10) and the Feddi rename
(feddi -> feddi-gateway, commit a9becec), including property verification,
collision/data-loss avoidance, and markdown idempotency.
"""

import copy
import importlib.util
import json
import os
import tempfile
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MIGRATE_SCRIPT = os.path.join(REPO_ROOT, "k6", "migrate-gateway-variants.py")
MATRIX_SCRIPT = os.path.join(REPO_ROOT, "k6", "build-matrix.py")


def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


MIGRATE = load_module(MIGRATE_SCRIPT, "migrate_gateway_variants")
MATRIX = load_module(MATRIX_SCRIPT, "build_matrix")


def fusion_variant(old_id, version, composition, runtime_version, features=()):
    return {
        "id": old_id,
        "version": version,
        "composition": composition,
        "platform": {
            "language": {"name": "C#"},
            "runtime": {"name": ".NET", "version": runtime_version},
            **({"features": list(features)} if features else {}),
        },
        **({"label": "Fusion Nightly"} if "nightly" in old_id else {}),
    }


RUNTIME_ASYNC = [{
    "id": "runtime-async",
    "description": "C# async methods compiled to runtime-async (.NET 11 opt-in).",
}]


def feddi_variant(old=True):
    vid = "feddi" if old else "feddi-gateway"
    return {
        "id": vid,
        "version": "e91d605ed222",
        "preview": True,
        "composition": "composite-schema",
        "platform": {
            "language": {"name": "Java"},
            "runtime": {"name": "JVM", "version": "25.0.4"},
        },
    }


def results_doc(variants, gateway_id="fusion", scenario_gateway=None):
    return {
        "gateways": [{
            "id": gateway_id,
            "name": gateway_id,
            "variants": copy.deepcopy(variants),
        }],
        "scenarios": [{
            "id": "constant",
            "results": [{
                "gateway": scenario_gateway or gateway_id,
                "variants": [
                    {"variant": v["id"], "status": "complete"}
                    for v in variants
                ],
            }],
        }],
    }


def write_doc(directory, doc):
    path = os.path.join(directory, "results.json")
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(doc, fh, indent=2)
        fh.write("\n")
    return path


class MigrationMappingTests(unittest.TestCase):
    def test_canonical_mappings_match_build_matrix(self):
        self.assertEqual(MIGRATE.load_migrations(), {
            **MATRIX.FUSION_VARIANT_MIGRATION,
            **MATRIX.FEDDI_VARIANT_MIGRATION,
        })
        self.assertEqual(MATRIX.FUSION_VARIANT_MIGRATION, {
            "fusion": "fusion-net-10",
            "fusion-nightly": "fusion-nightly-net-10",
            "fusion-nightly-net11": "fusion-nightly-net-11",
            "fusion-nightly-fed": "fusion-nightly-fed-net-10",
        })
        self.assertEqual(MATRIX.FEDDI_VARIANT_MIGRATION, {"feddi": "feddi-gateway"})

    def test_fusion_targets_do_not_collide_with_canonical_ids(self):
        canonical = set(MATRIX.FUSION_BASE_NAMES) | {"feddi-gateway"}
        for old, new in MIGRATE.load_migrations().items():
            self.assertIn(new, canonical, new)
            self.assertNotIn(old, canonical, old)

    def test_fusion_variants_migrate_with_properties_preserved(self):
        variants = [
            fusion_variant("fusion", "16.6.9", "composite-schema", "10.0.13"),
            fusion_variant("fusion-nightly", "16.7.0-p.31", "composite-schema", "10.0.13"),
            fusion_variant("fusion-nightly-net11", "16.7.0-p.31", "composite-schema",
                           "11.0.0-rc.2.26504.105", RUNTIME_ASYNC),
            fusion_variant("fusion-nightly-fed", "16.7.0-p.31", "apollo-federation", "10.0.13"),
        ]
        with tempfile.TemporaryDirectory() as tmp:
            path = write_doc(tmp, results_doc(variants))
            changed, ambiguous = MIGRATE.migrate_results_json(
                path, MIGRATE.load_migrations())
            self.assertEqual(ambiguous, [])
            # 4 catalog + 4 scenario variants; the fusion product id is unchanged.
            self.assertEqual(changed, 8)
            with open(path, encoding="utf-8") as fh:
                doc = json.load(fh)
            self.assertEqual(doc["gateways"][0]["id"], "fusion")
            self.assertEqual(
                [v["id"] for v in doc["gateways"][0]["variants"]],
                ["fusion-net-10", "fusion-nightly-net-10",
                 "fusion-nightly-net-11", "fusion-nightly-fed-net-10"],
            )
            # Measured values and provenance survive the rename.
            by_id = {v["id"]: v for v in doc["gateways"][0]["variants"]}
            self.assertEqual(by_id["fusion-net-10"]["version"], "16.6.9")
            self.assertEqual(by_id["fusion-net-10"]["composition"], "composite-schema")
            self.assertEqual(
                by_id["fusion-nightly-net-11"]["platform"]["runtime"]["version"],
                "11.0.0-rc.2.26504.105",
            )
            self.assertEqual(
                doc["scenarios"][0]["results"][0]["gateway"], "fusion")
            self.assertEqual(
                [v["variant"] for v in doc["scenarios"][0]["results"][0]["variants"]],
                ["fusion-net-10", "fusion-nightly-net-10",
                 "fusion-nightly-net-11", "fusion-nightly-fed-net-10"],
            )

    def test_feddi_product_variant_and_scenario_ids_migrate(self):
        doc = {
            "gateways": [{
                "id": "feddi",
                "name": "feddi",
                "vendor": "feddi",
                "variants": [feddi_variant(old=True)],
            }],
            "scenarios": [{
                "id": "constant",
                "results": [{
                    "gateway": "feddi",
                    "variants": [{"variant": "feddi", "status": "complete",
                                  "throughput": {"medianRps": 20}}],
                }],
            }],
        }
        with tempfile.TemporaryDirectory() as tmp:
            path = write_doc(tmp, doc)
            changed, ambiguous = MIGRATE.migrate_results_json(
                path, MIGRATE.load_migrations())
            self.assertEqual(ambiguous, [])
            with open(path, encoding="utf-8") as fh:
                migrated = json.load(fh)
            self.assertEqual(migrated["gateways"][0]["id"], "feddi-gateway")
            self.assertEqual(migrated["gateways"][0]["name"], "feddi-gateway")
            self.assertEqual(migrated["gateways"][0]["vendor"], "feddi")
            self.assertEqual(
                migrated["gateways"][0]["variants"][0]["id"], "feddi-gateway")
            self.assertEqual(
                migrated["scenarios"][0]["results"][0]["gateway"], "feddi-gateway")
            variant = migrated["scenarios"][0]["results"][0]["variants"][0]
            self.assertEqual(variant["variant"], "feddi-gateway")
            self.assertEqual(variant["throughput"]["medianRps"], 20)

    def test_property_mismatch_is_left_untouched(self):
        # A fusion-nightly-fed tag on a composite-schema variant contradicts
        # the recorded composition: do not rename, report it.
        variants = [fusion_variant(
            "fusion-nightly-fed", "16.7.0-p.31", "composite-schema", "10.0.13")]
        with tempfile.TemporaryDirectory() as tmp:
            path = write_doc(tmp, results_doc(variants))
            changed, ambiguous = MIGRATE.migrate_results_json(
                path, MIGRATE.load_migrations())
            self.assertEqual(changed, 0)
            self.assertEqual(len(ambiguous), 1)
            self.assertIn("composition", ambiguous[0])
            with open(path, encoding="utf-8") as fh:
                doc = json.load(fh)
            self.assertEqual(doc["gateways"][0]["variants"][0]["id"],
                             "fusion-nightly-fed")
            self.assertEqual(
                doc["scenarios"][0]["results"][0]["variants"][0]["variant"],
                "fusion-nightly-fed",
            )

    def test_mismatch_rejects_whole_document_atomically(self):
        # One unverified entry blocks every rename in the document: verified
        # catalog entries keep their old ids, scenario references (fusion and
        # feddi alike) are untouched, and the file on disk is byte-identical
        # — no partial write with renamed references pointing elsewhere.
        good = fusion_variant("fusion", "16.6.9", "composite-schema", "10.0.13")
        bad = fusion_variant(
            "fusion-nightly-fed", "16.7.0-p.31", "composite-schema", "10.0.13")
        doc = {
            "gateways": [
                {
                    "id": "fusion",
                    "name": "fusion",
                    "variants": copy.deepcopy([good, bad]),
                },
                {
                    "id": "feddi",
                    "name": "feddi",
                    "vendor": "feddi",
                    "variants": [feddi_variant(old=True)],
                },
            ],
            "scenarios": [{
                "id": "constant",
                "results": [
                    {
                        "gateway": "fusion",
                        "variants": [
                            {"variant": "fusion", "status": "complete"},
                            {"variant": "fusion-nightly-fed", "status": "complete"},
                        ],
                    },
                    {
                        "gateway": "feddi",
                        "variants": [{"variant": "feddi", "status": "complete"}],
                    },
                ],
            }],
        }
        with tempfile.TemporaryDirectory() as tmp:
            path = write_doc(tmp, doc)
            with open(path, "rb") as fh:
                before = fh.read()
            changed, ambiguous = MIGRATE.migrate_results_json(
                path, MIGRATE.load_migrations())
            self.assertEqual(changed, 0)
            self.assertEqual(len(ambiguous), 1)
            self.assertIn("composition", ambiguous[0])
            with open(path, "rb") as fh:
                self.assertEqual(fh.read(), before)
            with open(path, encoding="utf-8") as fh:
                migrated = json.load(fh)
            fusion_gateway = next(
                g for g in migrated["gateways"] if g["id"] == "fusion")
            self.assertEqual(
                [v["id"] for v in fusion_gateway["variants"]],
                ["fusion", "fusion-nightly-fed"],
            )
            feddi_gateway = next(
                g for g in migrated["gateways"] if g["id"] == "feddi")
            self.assertEqual(feddi_gateway["name"], "feddi")
            self.assertEqual(feddi_gateway["variants"][0]["id"], "feddi")
            by_gateway = {
                r["gateway"]: [v["variant"] for v in r["variants"]]
                for r in migrated["scenarios"][0]["results"]
            }
            self.assertEqual(
                by_gateway,
                {
                    "fusion": ["fusion", "fusion-nightly-fed"],
                    "feddi": ["feddi"],
                },
            )

    def test_collision_avoids_data_loss(self):
        # A document containing both the old and the new tag must not merge
        # the two series.
        variants = [
            fusion_variant("fusion", "16.6.9", "composite-schema", "10.0.13"),
            fusion_variant("fusion-net-10", "16.6.9", "composite-schema", "10.0.13"),
        ]
        with tempfile.TemporaryDirectory() as tmp:
            path = write_doc(tmp, results_doc(variants))
            changed, ambiguous = MIGRATE.migrate_results_json(
                path, MIGRATE.load_migrations())
            self.assertEqual(changed, 0)
            self.assertEqual(len(ambiguous), 1)
            self.assertIn("collision", ambiguous[0])
            with open(path, encoding="utf-8") as fh:
                doc = json.load(fh)
            self.assertEqual(
                [v["id"] for v in doc["gateways"][0]["variants"]],
                ["fusion", "fusion-net-10"],
            )


class MarkdownMigrationTests(unittest.TestCase):
    def write_md(self, directory, text):
        path = os.path.join(directory, "RESULTS_CONSTANT.md")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(text)
        return path

    def test_markdown_migrates_once_and_is_idempotent(self):
        migration = MIGRATE.load_migrations()
        body = (
            "| fusion-nightly | 1 |\n"
            "| fusion-nightly-net11 | 2 |\n"
            "| fusion-nightly-fed | 3 |\n"
            "| fusion | 4 |\n"
            "| feddi | 5 |\n"
            "| feddi-gateway | 6 |\n"
            "Summary for: fusion-nightly (HotChocolate subgraphs)\n"
        )
        with tempfile.TemporaryDirectory() as tmp:
            path = self.write_md(tmp, body)
            self.assertEqual(MIGRATE.migrate_markdown(path, migration), 1)
            with open(path, encoding="utf-8") as fh:
                migrated = fh.read()
            self.assertIn("| fusion-nightly-net-10 |", migrated)
            self.assertIn("| fusion-nightly-net-11 |", migrated)
            self.assertIn("| fusion-nightly-fed-net-10 |", migrated)
            self.assertIn("| fusion-net-10 |", migrated)
            self.assertIn("| feddi-gateway |", migrated)
            self.assertNotIn("| fusion |", migrated.replace("| fusion-net-10 |", ""))
            # Already-migrated tags are untouched on re-run.
            self.assertEqual(MIGRATE.migrate_markdown(path, migration), 0)
            with open(path, encoding="utf-8") as fh:
                self.assertEqual(fh.read(), migrated)

    def test_markdown_keeps_paths_urls_and_vendor_prose(self):
        migration = MIGRATE.load_migrations()
        body = (
            "composite-schema/gateways/fusion\n"
            "apollo-federation/gateways/fusion-fed\n"
            "https://github.com/feddi-dev/feddi-gateway\n"
            "by [feddi](https://feddi.dev)\n"
        )
        with tempfile.TemporaryDirectory() as tmp:
            path = self.write_md(tmp, body)
            self.assertEqual(MIGRATE.migrate_markdown(path, migration), 0)


if __name__ == "__main__":
    unittest.main()
