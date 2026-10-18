"""Tests for k6/build-history.py."""

import copy
import importlib.util
import json
import os
import shutil
import subprocess
import tempfile
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT = os.path.join(REPO_ROOT, "k6", "build-history.py")


def load_builder():
    spec = importlib.util.spec_from_file_location("build_history", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


BUILDER = load_builder()

CATALOG = [
    ("apollo-router", [("apollo-router", "2.18.0", "Rust"), ("apollo-router-v3", "3.0.0-preview.0", "Rust")]),
    ("caliban", [("caliban", "3.2.0", "Scala")]),
    ("fusion", [
        ("fusion", "16.6.8", "C#"),
        ("fusion-nightly", "16.7.0-p.27", "C#"),
        ("fusion-nightly-net11", "16.7.0-p.27", "C#"),
        ("fusion-nightly-fed", "16.7.0-p.27", "C#"),
    ]),
    ("feddi-gateway", [("feddi-gateway", "e91d605ed222", "Go")]),
]

CPU_ALLOCATION = {
    "system": {"threadIds": [0, 8], "physicalCores": 1, "hardwareThreads": 2},
    "k6": {"threadIds": [1, 9], "physicalCores": 1, "hardwareThreads": 2},
    "gateway": {
        "threadIds": [2, 3, 10, 11], "physicalCores": 2, "hardwareThreads": 4,
    },
    "subgraphs": {
        "threadIds": [4, 5, 6, 7, 12, 13, 14, 15],
        "physicalCores": 4,
        "hardwareThreads": 8,
    },
}


def variant_result(variant_id):
    return {
        "variant": variant_id,
        "status": "complete",
        "throughput": {"medianRps": 1000, "bestRps": 1010, "worstRps": 990, "cvPercent": 0.5,
                       "runsRps": [1010, 1000, 990]},
        "latencyMs": {"avg": 10.0, "med": 9.5, "p90": 15.0, "p95": 18.0, "p99_9": 40.0, "max": 80.0},
        "requests": {"total": 120000, "successful": 120000, "failed": 0},
        "memory": {"peakRssKiB": 204800},
        "cpu": {"avgUtilizationPercent": 87.5, "maxUtilizationPercent": 100.0},
    }


def results_doc():
    scenarios = []
    for scenario_id in ("constant", "constant-latency", "burst"):
        results = [
            {"gateway": gateway_id, "variants": [variant_result(v[0]) for v in variants]}
            for gateway_id, variants in CATALOG
            # burst omits feddi-gateway, like the real runs.
            if not (scenario_id == "burst" and gateway_id == "feddi-gateway")
        ]
        scenarios.append({
            "id": scenario_id,
            "name": scenario_id.title(),
            "status": "complete",
            "config": {"durationSeconds": 120, "virtualUsers": 50,
                       "subgraphDelayMs": 4 if scenario_id == "constant-latency" else 0,
                       "warmupRuns": 1, "measuredRuns": 9,
                       "cpuAllocation": copy.deepcopy(CPU_ALLOCATION)},
            "results": results,
        })
    return {
        "run": {"number": 1, "startedAt": "2026-10-15T21:04:03Z", "completedAt": "2026-10-16T10:24:10Z",
                "sourceCommit": "c" * 40, "event": "schedule"},
        "hardware": {
            "host": "bench-001",
            "cpuModel": "AMD Ryzen 7 5700G",
            "physicalCores": 8,
            "hardwareThreads": 16,
            "threadsPerCore": 2,
            "coreThreads": [[core, core + 8] for core in range(8)],
            "memoryGb": 122,
            "os": "Linux",
        },
        "subgraphs": {
            "framework": {"name": "Hot Chocolate", "version": "16.6.8"},
            "platform": {"language": {"name": "C#"}, "runtime": {"name": ".NET", "version": "10.0.13"}},
        },
        "gateways": [
            {"id": gateway_id, "name": gateway_id, "variants": [
                {"id": vid, "version": version, "composition": "apollo-federation",
                 "platform": {"language": {"name": language}},
                 **({"label": "Fusion Nightly"} if vid in (
                     "fusion-nightly", "fusion-nightly-net11", "fusion-nightly-fed"
                 ) else {}),
                 **({"preview": True} if vid == "feddi-gateway" else {})}
                for vid, version, language in variants
            ]}
            for gateway_id, variants in CATALOG
        ],
        "scenarios": scenarios,
    }


EXAMPLE = results_doc()


def set_version(doc, variant_id, version):
    for gateway in doc["gateways"]:
        for variant in gateway["variants"]:
            if variant["id"] == variant_id:
                variant["version"] = version


def make_doc(number, event="schedule", versions=None):
    doc = copy.deepcopy(EXAMPLE)
    doc["run"]["number"] = number
    doc["run"]["url"] = f"https://github.com/owner/repo/actions/runs/{number}"
    doc["run"]["event"] = event
    for variant_id, version in (versions or {}).items():
        set_version(doc, variant_id, version)
    # Tag every result with its run so tests can tell which run was picked.
    for scenario in doc["scenarios"]:
        for result in scenario["results"]:
            for variant in result["variants"]:
                variant["throughput"]["medianRps"] = number
    return doc


def scenario(doc, scenario_id):
    return next(s for s in doc["scenarios"] if s["id"] == scenario_id)


def remove_result(doc, scenario_id, variant_id):
    found = False
    for result in scenario(doc, scenario_id)["results"]:
        found = found or any(
            variant["variant"] == variant_id for variant in result["variants"]
        )
        result["variants"] = [
            variant for variant in result["variants"]
            if variant["variant"] != variant_id
        ]
    scenario(doc, scenario_id)["results"] = [
        result for result in scenario(doc, scenario_id)["results"]
        if result["variants"]
    ]
    if not found:
        raise AssertionError(f"missing result for {variant_id} in {scenario_id}")


def mark_result_failed(doc, scenario_id, variant_id):
    for result in scenario(doc, scenario_id)["results"]:
        for index, variant in enumerate(result["variants"]):
            if variant["variant"] == variant_id:
                result["variants"][index] = {
                    "variant": variant_id,
                    "status": "failed",
                }
                return
    raise AssertionError(f"missing result for {variant_id} in {scenario_id}")


def results_of(history, variant_id, scenario_id="constant"):
    entry = next(
        (v for v in scenario(history, scenario_id)["variants"] if v["variant"] == variant_id),
        None,
    )
    if entry is None:
        return None
    return [(v["version"], v["run"]["number"]) for v in entry["results"]]


class BuildHistoryTests(unittest.TestCase):

    def setUp(self):
        self.workdir = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.workdir, True)
        self.runs_dir = os.path.join(self.workdir, "benchmark-runs")
        os.makedirs(self.runs_dir)

    def write_runs(self, *docs):
        for doc in docs:
            run_dir = os.path.join(self.runs_dir, str(doc["run"]["number"]))
            os.makedirs(run_dir, exist_ok=True)
            with open(os.path.join(run_dir, "results.json"), "w") as f:
                json.dump(doc, f)

    def build(self, *docs):
        self.write_runs(*docs)
        output = os.path.join(self.runs_dir, "history.json")
        proc = subprocess.run(
            ["python3", SCRIPT, self.runs_dir, output],
            capture_output=True, text=True, timeout=60,
        )
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        with open(output) as f:
            history = json.load(f)
        return history

    def test_latest_run_and_catalog_come_from_latest_scheduled_run(self):
        self.write_runs(make_doc(9, event="workflow_dispatch"))
        history = self.build(make_doc(7))
        self.assertEqual(history["latestRun"], {
            "number": 7,
            "url": "https://github.com/owner/repo/actions/runs/7",
        })
        self.assertEqual(history["gateways"], EXAMPLE["gateways"])
        variants = {
            variant["id"]: variant
            for gateway in history["gateways"]
            for variant in gateway["variants"]
        }
        self.assertEqual(variants["fusion-nightly"]["label"], "Fusion Nightly")
        self.assertEqual(variants["fusion-nightly-net11"]["label"], "Fusion Nightly")
        self.assertEqual(variants["fusion-nightly-fed"]["label"], "Fusion Nightly")
        self.assertIs(variants["feddi-gateway"]["preview"], True)
        self.assertEqual([s["id"] for s in history["scenarios"]], ["constant", "constant-latency", "burst"])
        self.assertEqual(scenario(history, "constant")["config"], scenario(EXAMPLE, "constant")["config"])

    def test_version_entry_copies_metrics_verbatim(self):
        history = self.build(make_doc(1))
        entry = next(
            v for v in scenario(history, "constant")["variants"] if v["variant"] == "apollo-router-v3"
        )
        self.assertEqual(entry["gateway"], "apollo-router")
        source = next(
            v for r in scenario(make_doc(1), "constant")["results"]
            for v in r["variants"] if v["variant"] == "apollo-router-v3"
        )
        expected = {
            "version": "3.0.0-preview.0",
            "run": entry["results"][0]["run"],
            "platform": {"language": {"name": "Rust"}},
            "subgraphs": EXAMPLE["subgraphs"],
        }
        expected.update((k, v) for k, v in source.items() if k not in ("variant", "status"))
        self.assertEqual(entry["results"], [expected])
        self.assertEqual(list(entry["results"][0]), list(expected))

    def test_variants_follow_catalog_order(self):
        history = self.build(make_doc(1))
        catalog = [v["id"] for g in EXAMPLE["gateways"] for v in g["variants"]]
        emitted = [v["variant"] for v in scenario(history, "constant")["variants"]]
        self.assertEqual(emitted, catalog)
        self.assertEqual(results_of(history, "feddi-gateway", "burst"), [])

    def test_feddi_history_starts_with_request_throughput_implementation(self):
        history = self.build(
            make_doc(399, versions={"feddi-gateway": "5ff8b6165878"}),
            make_doc(400, versions={"feddi-gateway": "e91d605ed222"}),
        )
        self.assertEqual(results_of(history, "feddi-gateway"), [("e91d605ed222", 400)])
        self.assertEqual(results_of(history, "fusion"), [("16.6.8", 399), ("16.6.8", 400)])

    def test_workflow_dispatch_runs_ignored(self):
        history = self.build(
            make_doc(1, versions={"fusion": "16.0.0"}),
            make_doc(2, event="workflow_dispatch", versions={"fusion": "16.1.0"}),
        )
        self.assertEqual(history["latestRun"]["number"], 1)
        self.assertEqual(results_of(history, "fusion"), [("16.0.0", 1)])

    def test_legacy_runs_inferred_from_inputs(self):
        legacy = make_doc(1, versions={"fusion": "16.0.0"})
        del legacy["run"]["event"]
        dispatched = make_doc(2, versions={"fusion": "16.1.0"})
        del dispatched["run"]["event"]
        dispatched["run"]["inputs"] = {"gateway": "fusion"}
        history = self.build(legacy, dispatched, make_doc(3, versions={"fusion": "16.2.0"}))
        self.assertEqual(results_of(history, "fusion"), [("16.0.0", 1), ("16.2.0", 3)])

    def test_failed_scenario_kept_and_missing_variant_excluded(self):
        old = make_doc(1, versions={"fusion": "16.0.0"})
        latest = make_doc(2, versions={"fusion": "16.1.0"})
        scenario(latest, "constant-latency")["status"] = "failed"
        remove_result(latest, "constant-latency", "fusion")
        history = self.build(old, latest)
        self.assertEqual(
            [s["id"] for s in history["scenarios"]],
            ["constant", "constant-latency", "burst"],
        )
        self.assertEqual(
            results_of(history, "fusion", "constant-latency"),
            [("16.0.0", 1)],
        )
        self.assertEqual(
            results_of(history, "caliban", "constant-latency"),
            [("3.2.0", 1), ("3.2.0", 2)],
        )
        self.assertEqual(
            results_of(history, "fusion"),
            [("16.0.0", 1), ("16.1.0", 2)],
        )

    def test_failed_variant_excluded_without_dropping_scenario(self):
        old = make_doc(1, versions={"fusion": "16.0.0"})
        latest = make_doc(2, versions={"fusion": "16.1.0"})
        del scenario(latest, "constant-latency")["status"]
        mark_result_failed(latest, "constant-latency", "fusion")
        history = self.build(old, latest)
        self.assertEqual(
            [s["id"] for s in history["scenarios"]],
            ["constant", "constant-latency", "burst"],
        )
        self.assertEqual(
            results_of(history, "fusion", "constant-latency"),
            [("16.0.0", 1)],
        )
        self.assertEqual(
            results_of(history, "caliban", "constant-latency"),
            [("3.2.0", 1), ("3.2.0", 2)],
        )

    def test_skipped_scenario_omitted(self):
        latest = make_doc(1)
        scenario(latest, "burst")["status"] = "skipped"
        history = self.build(latest)
        self.assertEqual(
            [s["id"] for s in history["scenarios"]],
            ["constant", "constant-latency"],
        )

    def test_non_default_run_counts_skipped(self):
        old = make_doc(1, versions={"fusion": "16.0.0"})
        scenario(old, "constant")["config"]["measuredRuns"] = 3
        warm = make_doc(2, versions={"fusion": "16.1.0"})
        scenario(warm, "constant")["config"]["warmupRuns"] = 0
        history = self.build(old, warm, make_doc(3, versions={"fusion": "16.2.0"}))
        self.assertEqual(results_of(history, "fusion"), [("16.2.0", 3)])

    def test_null_version_skipped(self):
        history = self.build(
            make_doc(1, versions={"fusion": "16.0.0", "caliban": None}),
            make_doc(2, versions={"fusion": None, "caliban": None}),
        )
        self.assertEqual(results_of(history, "fusion"), [("16.0.0", 1)])
        self.assertEqual(results_of(history, "caliban"), [])

    def test_same_version_keeps_every_run(self):
        history = self.build(
            make_doc(1, versions={"fusion": "16.0.0"}),
            make_doc(2, versions={"fusion": "16.1.0"}),
            make_doc(3, versions={"fusion": "16.0.0"}),
            make_doc(4, versions={"fusion": "16.1.0"}),
        )
        self.assertEqual(
            results_of(history, "fusion"),
            [("16.0.0", 1), ("16.1.0", 2), ("16.0.0", 3), ("16.1.0", 4)],
        )
        entry = next(v for v in scenario(history, "constant")["variants"] if v["variant"] == "fusion")
        self.assertEqual(
            [v["throughput"]["medianRps"] for v in entry["results"]],
            [1, 2, 3, 4],
        )

    def test_keeps_every_run_in_the_last_six_months(self):
        history = self.build(*(
            make_doc(n, versions={"fusion": f"16.{n}.0"}) for n in range(1, 6)
        ))
        self.assertEqual(results_of(history, "fusion"), [
            ("16.1.0", 1), ("16.2.0", 2), ("16.3.0", 3),
            ("16.4.0", 4), ("16.5.0", 5),
        ])

    def test_runs_older_than_six_calendar_months_are_excluded(self):
        before_window = make_doc(1, versions={"fusion": "16.0.0"})
        before_window["run"]["startedAt"] = "2026-04-14T21:04:03Z"
        first_in_window = make_doc(2, versions={"fusion": "16.1.0"})
        first_in_window["run"]["startedAt"] = "2026-04-15T21:04:03Z"
        latest = make_doc(3, versions={"fusion": "16.2.0"})
        history = self.build(before_window, first_in_window, latest)
        self.assertEqual(
            results_of(history, "fusion"),
            [("16.1.0", 2), ("16.2.0", 3)],
        )

    def test_config_change_resets_scenario(self):
        old = make_doc(1, versions={"fusion": "16.0.0"})
        latest = make_doc(2, versions={"fusion": "16.1.0"})
        scenario(latest, "constant")["config"]["virtualUsers"] = 100
        history = self.build(old, latest)
        self.assertEqual(results_of(history, "fusion"), [("16.1.0", 2)])
        self.assertEqual(results_of(history, "fusion", "burst"), [("16.0.0", 1), ("16.1.0", 2)])

    def test_cpu_model_change_resets_history(self):
        cpu = make_doc(1, versions={"fusion": "16.0.0"})
        cpu["hardware"]["cpuModel"] = "Other CPU"
        subgraphs = make_doc(2, versions={"fusion": "16.1.0"})
        subgraphs["subgraphs"]["framework"]["version"] = "16.0.0"
        host = make_doc(3, versions={"fusion": "16.2.0"})
        host["hardware"]["host"] = "bench-002"
        history = self.build(cpu, subgraphs, host, make_doc(4, versions={"fusion": "16.3.0"}))
        self.assertEqual(
            results_of(history, "fusion"),
            [("16.1.0", 2), ("16.2.0", 3), ("16.3.0", 4)],
        )

    def test_subgraph_runtime_patch_keeps_history(self):
        old = make_doc(1, versions={"fusion": "16.0.0"})
        old["subgraphs"]["platform"]["runtime"]["version"] = "10.0.12"
        history = self.build(old, make_doc(2, versions={"fusion": "16.1.0"}))
        self.assertEqual(results_of(history, "fusion"), [("16.0.0", 1), ("16.1.0", 2)])

    def test_subgraph_runtime_major_is_recorded_per_run(self):
        old = make_doc(1, versions={"fusion": "16.0.0"})
        old["subgraphs"]["platform"]["runtime"]["version"] = "9.0.13"
        history = self.build(old, make_doc(2, versions={"fusion": "16.1.0"}))
        self.assertEqual(results_of(history, "fusion"), [("16.0.0", 1), ("16.1.0", 2)])
        entry = next(
            v for v in scenario(history, "constant")["variants"]
            if v["variant"] == "fusion"
        )
        self.assertEqual(
            [r["subgraphs"]["platform"]["runtime"]["version"] for r in entry["results"]],
            ["9.0.13", "10.0.13"],
        )

    def test_gateway_runtime_is_recorded_per_run(self):
        old = make_doc(1, versions={"fusion": "16.0.0"})
        latest = make_doc(2, versions={"fusion": "16.1.0"})
        for doc, runtime_version in ((old, "10.0.13"), (latest, "11.0.0")):
            for gateway in doc["gateways"]:
                for variant in gateway["variants"]:
                    if variant["id"] == "fusion":
                        variant["platform"]["runtime"] = {
                            "name": ".NET",
                            "version": runtime_version,
                        }
        history = self.build(old, latest)
        entry = next(
            v for v in scenario(history, "constant")["variants"]
            if v["variant"] == "fusion"
        )
        self.assertEqual(
            [r["platform"]["runtime"]["version"] for r in entry["results"]],
            ["10.0.13", "11.0.0"],
        )

    def test_new_scenario_in_latest_run(self):
        old = make_doc(1, versions={"fusion": "16.0.0"})
        old["scenarios"] = [s for s in old["scenarios"] if s["id"] != "burst"]
        history = self.build(old, make_doc(2, versions={"fusion": "16.1.0"}))
        self.assertEqual(results_of(history, "fusion", "burst"), [("16.1.0", 2)])
        self.assertEqual(results_of(history, "fusion"), [("16.0.0", 1), ("16.1.0", 2)])

    def test_variant_absent_from_latest_catalog_dropped(self):
        latest = make_doc(2)
        for gateway in latest["gateways"]:
            gateway["variants"] = [v for v in gateway["variants"] if v["id"] != "fusion-nightly-fed"]
        for s in latest["scenarios"]:
            for result in s["results"]:
                result["variants"] = [v for v in result["variants"] if v["variant"] != "fusion-nightly-fed"]
            s["results"] = [r for r in s["results"] if r["variants"]]
        history = self.build(make_doc(1), latest)
        self.assertIsNone(results_of(history, "fusion-nightly-fed"))
        self.assertEqual(results_of(history, "fusion"), [("16.6.8", 1), ("16.6.8", 2)])

    def test_non_numeric_and_empty_dirs_ignored(self):
        os.makedirs(os.path.join(self.runs_dir, "5"))
        stray = make_doc(9)
        os.makedirs(os.path.join(self.runs_dir, "draft"))
        with open(os.path.join(self.runs_dir, "draft", "results.json"), "w") as f:
            json.dump(stray, f)
        history = self.build(make_doc(1))
        self.assertEqual(history["latestRun"]["number"], 1)

    def test_output_is_deterministic(self):
        self.build(make_doc(1, versions={"fusion": "16.0.0"}), make_doc(2))
        output = os.path.join(self.runs_dir, "history.json")
        with open(output, "rb") as f:
            first = f.read()
        self.build()
        with open(output, "rb") as f:
            second = f.read()
        self.assertEqual(first, second)
        self.assertTrue(first.endswith(b"}\n"))
        self.assertEqual(first.decode(), json.dumps(json.loads(first), indent=2, ensure_ascii=False) + "\n")

    def test_no_eligible_run_fails(self):
        self.write_runs(make_doc(1, event="workflow_dispatch"))
        output = os.path.join(self.workdir, "history.json")
        proc = subprocess.run(
            ["python3", SCRIPT, self.runs_dir, output],
            capture_output=True, text=True, timeout=60,
        )
        self.assertNotEqual(proc.returncode, 0)
        self.assertIn("No scheduled run", proc.stdout)
        self.assertFalse(os.path.exists(output))

    def test_build_history_without_runs_returns_none(self):
        self.assertIsNone(BUILDER.build_history([]))


if __name__ == "__main__":
    unittest.main()
