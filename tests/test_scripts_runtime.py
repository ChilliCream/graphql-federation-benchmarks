"""Runtime behavior tests: error paths and result generation.

These exercise the no-SDK prebuilt failure modes and the .NET-only result
output without requiring k6, .NET or network access.
"""

import glob
import importlib.util
import json
import os
import re
import shutil
import subprocess
import tempfile
import unittest
import xml.etree.ElementTree as ET

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_generator():
    spec = importlib.util.spec_from_file_location(
        "generate_results", os.path.join(REPO_ROOT, "k6", "generate-results.py")
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_config():
    spec = importlib.util.spec_from_file_location(
        "build_matrix", os.path.join(REPO_ROOT, "k6", "build-matrix.py")
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_backfill():
    spec = importlib.util.spec_from_file_location(
        "backfill_results", os.path.join(REPO_ROOT, "k6", "backfill-results.py")
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


CONFIG = load_config()
BACKFILL = load_backfill()

SUMMARY = {
    "vus": 50,
    "duration": "120s",
    "metrics": {
        "http_reqs": {"values": {"rate": 1000, "count": 120000}},
        "vus_max": {"values": {"max": 50}},
        "http_req_duration": {"values": {"avg": 5.0, "p(95)": 10.0}},
        "http_req_failed": {"values": {"passes": 0}},
        "success_rate": {"values": {"passes": 120000, "fails": 0}},
    },
}


def assert_results_shape(test, doc):
    def keys(obj, required, optional=(), where=""):
        test.assertIsInstance(obj, dict, where)
        test.assertLessEqual(set(required), set(obj), f"{where}: missing keys")
        test.assertLessEqual(set(obj), set(required) | set(optional), f"{where}: unknown keys")

    def platform(obj, where):
        keys(obj, ["language"], ["runtime", "features"], where)
        keys(obj["language"], ["name"], where=where + ".language")
        if "runtime" in obj:
            keys(obj["runtime"], ["name"], ["version"], where + ".runtime")
        features(obj, where)

    def features(obj, where):
        for feature in obj.get("features", []):
            keys(feature, ["id", "name"], ["description"], where + ".features")

    keys(doc, ["run", "hardware", "subgraphs", "gateways", "scenarios"])
    keys(doc["run"], ["number", "startedAt", "sourceCommit", "event"], ["url", "completedAt", "inputs"], "run")
    test.assertIsInstance(doc["run"]["event"], str)
    test.assertIsInstance(doc["run"]["number"], int)
    test.assertRegex(doc["run"]["sourceCommit"], r"^[0-9a-f]{40}$")
    keys(
        doc["hardware"],
        ["host", "cpuModel", "hardwareThreads", "memoryGb", "os"],
        ["physicalCores", "threadsPerCore", "coreThreads"],
        where="hardware",
    )
    hardware = doc["hardware"]
    test.assertGreater(hardware["hardwareThreads"], 0)
    if "coreThreads" in hardware:
        test.assertIn("physicalCores", hardware)
        test.assertIn("threadsPerCore", hardware)
        test.assertEqual(len(hardware["coreThreads"]), hardware["physicalCores"])
        thread_ids = [thread for core in hardware["coreThreads"] for thread in core]
        test.assertEqual(len(thread_ids), hardware["hardwareThreads"])
        test.assertEqual(len(set(thread_ids)), len(thread_ids))
    keys(doc["subgraphs"], ["framework", "platform"], where="subgraphs")
    keys(doc["subgraphs"]["framework"], ["name"], ["version"], where="subgraphs.framework")
    platform(doc["subgraphs"]["platform"], "subgraphs.platform")

    variants = {}
    for gateway in doc["gateways"]:
        keys(gateway, ["id", "name", "variants"], ["vendor", "repositoryUrl"], "gateway")
        test.assertTrue(gateway["variants"])
        for variant in gateway["variants"]:
            where = f"variant {variant.get('id')}"
            keys(
                variant,
                ["id", "version", "composition", "platform"],
                ["label", "preview", "features", "notes"],
                where,
            )
            if "label" in variant:
                test.assertTrue(variant["label"], where)
            if "preview" in variant:
                test.assertIsInstance(variant["preview"], bool, where)
            test.assertIn(variant["composition"], ("composite-schema", "apollo-federation"))
            if variant["version"] is not None:
                test.assertNotRegex(variant["version"], r"^[vV]", where)
            platform(variant["platform"], where)
            features(variant, where)
            test.assertNotIn(variant["id"], variants, "variant ids are unique across the run")
            variants[variant["id"]] = gateway["id"]

    for scenario in doc["scenarios"]:
        where = f"scenario {scenario.get('id')}"
        keys(scenario, ["id", "name", "config", "results"], ["description"], where)
        test.assertIn(scenario["id"], ("constant", "constant-latency", "burst"))
        has_measurements = any(
            "throughput" in variant
            for result in scenario["results"]
            for variant in result["variants"]
        )
        measured = ["virtualUsers", "measuredRuns"]
        keys(scenario["config"], ["subgraphDelayMs", "warmupRuns"] + (measured if has_measurements else []),
             measured + ["durationSeconds", "cpuAllocation"], where=where + ".config")
        for role, alloc in scenario["config"].get("cpuAllocation", {}).items():
            test.assertIn(role, ("system", "k6", "gateway", "subgraphs"), where)
            keys(
                alloc,
                ["threadIds", "hardwareThreads"],
                ["physicalCores"],
                where=f"{where}.cpuAllocation.{role}",
            )
            test.assertEqual(len(alloc["threadIds"]), alloc["hardwareThreads"])
            test.assertGreater(alloc["hardwareThreads"], 0)
            if "physicalCores" in alloc:
                test.assertGreater(alloc["physicalCores"], 0)
        for result in scenario["results"]:
            keys(result, ["gateway", "variants"], where=where)
            test.assertTrue(result["variants"])
            for variant in result["variants"]:
                vwhere = f"{where} / {variant.get('variant')}"
                keys(variant, ["variant", "status"],
                     ["throughput", "requests", "latencyMs", "memory", "cpu"], vwhere)
                test.assertEqual(variants[variant["variant"]], result["gateway"], vwhere)
                test.assertIn(variant["status"], ("complete", "failed"), vwhere)
                if variant["status"] == "complete":
                    test.assertIn("throughput", variant, vwhere)
                    test.assertIn("requests", variant, vwhere)
                if "throughput" in variant:
                    test.assertIn("requests", variant, vwhere)
                    keys(variant["throughput"], ["medianRps", "bestRps", "worstRps", "cvPercent"],
                         ["runsRps"], vwhere + ".throughput")
                if "latencyMs" in variant:
                    keys(variant["latencyMs"], ["avg", "med", "p90", "p95", "p99_9", "max"],
                         ["min", "p99"], vwhere + ".latencyMs")
                if "requests" in variant:
                    keys(variant["requests"], ["total", "successful", "failed"], where=vwhere + ".requests")
                    test.assertEqual(variant["requests"]["total"],
                                     variant["requests"]["successful"] + variant["requests"]["failed"], vwhere)
                if "memory" in variant:
                    keys(variant["memory"], ["peakRssKiB"], where=vwhere)
                if "cpu" in variant:
                    keys(
                        variant["cpu"],
                        ["avgUtilizationPercent", "maxUtilizationPercent"],
                        where=vwhere + ".cpu",
                    )
                    test.assertLessEqual(
                        variant["cpu"]["avgUtilizationPercent"],
                        variant["cpu"]["maxUtilizationPercent"],
                        vwhere,
                    )
                    test.assertLessEqual(variant["cpu"]["maxUtilizationPercent"], 100, vwhere)


def make_run(artifacts_dir, gateway, display_name, run_index=1, mode="constant", summary=None,
             extra_metadata=None, data_csv=None):
    make_tech_run(
        artifacts_dir,
        gateway,
        display_name,
        subgraph_tech=".net",
        subgraphs="subgraphs-net",
        run_index=run_index,
        mode=mode,
        summary=summary,
        extra_metadata=extra_metadata,
        data_csv=data_csv,
    )


def make_tech_run(
    artifacts_dir, gateway, display_name, subgraph_tech, subgraphs, run_index=1, mode="constant",
    summary=None, extra_metadata=None, data_csv=None,
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
                **(extra_metadata or {}),
            },
            fh,
        )
    if data_csv is not None:
        with open(os.path.join(run_dir, "data.csv"), "w") as fh:
            fh.write(data_csv)
    with open(os.path.join(run_dir, "k6_summary.json"), "w") as fh:
        json.dump(summary or SUMMARY, fh)
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
        for mode in ("constant", "constant-latency", "burst"):
            with self.subTest(mode=mode):
                md = self.run_generator(["fusion-net-10", "cosmo"], mode=mode)
                self.assertIn("### Results\n", md)
                self.assertNotIn("Rust Subgraphs", md)
                self.assertIn("Each benchmark runs a GraphQL gateway with 4 subgraphs and executes", md)
                self.assertIn("| fusion-net-10 |", md)
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
        md = self.run_generator(["fusion-net-10", "grafbase"], with_runs=["fusion-net-10"])
        self.assertIn("| grafbase |", md)
        self.assertIn("benchmark run failed", md)

    def test_excluded_gateway_marked_not_run(self):
        md = self.run_generator(["fusion-net-10", "feddi-gateway"], with_runs=["fusion-net-10"], not_run=("feddi-gateway",))
        feddi_rows = [line for line in md.splitlines() if line.startswith("| feddi-gateway |")]
        self.assertEqual(len(feddi_rows), 1)
        self.assertIn("not run", feddi_rows[0])
        self.assertNotIn("benchmark run failed", feddi_rows[0])

    def test_historical_rust_not_described_as_dotnet(self):
        # Historical Rust artifacts keep their technology labels.
        workdir = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, workdir, True)
        artifacts = os.path.join(workdir, "artifacts")
        os.makedirs(artifacts)
        make_run(artifacts, "fusion-net-10", "fusion-net-10 (HotChocolate subgraphs)")
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
            [expected_entry("fusion-net-10"), expected_entry("cosmo")]
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
        self.assertIn("### Results\n", md)
        self.assertIn("Each benchmark runs a GraphQL gateway with 4 subgraphs and executes", md)


    def test_old_dotnet_display_name_still_parses(self):
        # Backward compatibility: artifacts recorded before the HotChocolate
        # relabel carry display_name "(.NET subgraphs)" with tech ".net" and
        # must still appear in the results table.
        workdir = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, workdir, True)
        artifacts = os.path.join(workdir, "artifacts")
        os.makedirs(artifacts)
        make_tech_run(
            artifacts,
            "fusion-net-10",
            "fusion-net-10 (.NET subgraphs)",
            subgraph_tech=".net",
            subgraphs="subgraphs-net",
        )
        outdir = os.path.join(workdir, "out")
        env = dict(os.environ)
        env["EXPECTED_GATEWAYS_JSON"] = json.dumps([expected_entry("fusion-net-10")])
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
        self.assertIn("### Results\n", md)
        self.assertIn("| fusion-net-10 |", md)

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
        self.assertIn("### Results\n", md)
        self.assertIn("| cosmo |", md)


class GenerateResultsJsonTests(unittest.TestCase):

    def run_json_generator(self, artifacts, env_overrides):
        outdir = os.path.join(os.path.dirname(artifacts), "out")
        env = dict(os.environ)
        env.update({
            "GITHUB_RUN_NUMBER": "42",
            "GITHUB_RUN_ID": "1234",
            "GITHUB_REPOSITORY": "owner/repo",
            "GITHUB_SERVER_URL": "https://github.com",
            "GITHUB_SHA": "a" * 40,
            "GITHUB_EVENT_NAME": "schedule",
            "RUN_STARTED_AT": "2026-01-01T00:00:00Z",
        })
        env.update(env_overrides)
        proc = subprocess.run(
            ["python3", os.path.join(REPO_ROOT, "k6", "generate-results.py"), "--json", artifacts, outdir],
            env=env,
            capture_output=True,
            text=True,
            timeout=120,
            cwd=REPO_ROOT,
        )
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        self.assertFalse(glob.glob(os.path.join(outdir, "*.md")))
        with open(os.path.join(outdir, "results.json")) as fh:
            doc = json.load(fh)
        assert_results_shape(self, doc)
        return doc

    def make_artifacts(self):
        workdir = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, workdir, True)
        artifacts = os.path.join(workdir, "artifacts")
        os.makedirs(artifacts)
        return artifacts

    @staticmethod
    def results_by_variant(doc, mode):
        scenario = next(s for s in doc["scenarios"] if s["id"] == mode)
        return scenario, {
            v["variant"]: v for r in scenario["results"] for v in r["variants"]
        }

    def test_scenarios_and_variant_statuses_follow_job_results_and_matrix(self):
        artifacts = self.make_artifacts()
        make_run(artifacts, "fusion-net-10", "fusion-net-10 (HotChocolate subgraphs)", mode="constant")
        make_run(artifacts, "fusion-net-10", "fusion-net-10 (HotChocolate subgraphs)", mode="burst")
        doc = self.run_json_generator(artifacts, {
            "EXPECTED_GATEWAYS_JSON": json.dumps(
                [expected_entry(g) for g in ("fusion-net-10", "grafbase", "feddi-gateway")]
            ),
            "SCENARIO_RESULTS_JSON": json.dumps(
                {"constant": "success", "burst": "failure", "constant-latency": "skipped"}
            ),
            "RUN_INPUTS_JSON": json.dumps({"gateway": "all", "diagnostic_run": False}),
            "GITHUB_EVENT_NAME": "workflow_dispatch",
        })

        self.assertEqual(doc["run"]["number"], 42)
        self.assertEqual(doc["run"]["event"], "workflow_dispatch")
        self.assertEqual(doc["run"]["url"], "https://github.com/owner/repo/actions/runs/1234")
        self.assertEqual(doc["run"]["inputs"], {"gateway": "all", "diagnostic_run": False})
        self.assertEqual(doc["hardware"]["hardwareThreads"], 16)
        self.assertNotIn("physicalCores", doc["hardware"])
        self.assertEqual(doc["hardware"]["memoryGb"], 32)

        versions = {v["id"]: v["version"] for g in doc["gateways"] for v in g["variants"]}
        self.assertEqual(versions, {"fusion-net-10": "16.6.0", "grafbase": None, "feddi-gateway": None})

        constant, results = self.results_by_variant(doc, "constant")
        self.assertNotIn("status", constant)
        self.assertEqual(results["fusion-net-10"]["throughput"]["medianRps"], 1000)
        self.assertEqual(results["fusion-net-10"]["throughput"]["runsRps"], [1000])
        self.assertEqual(results["fusion-net-10"]["requests"], {"total": 120000, "successful": 120000, "failed": 0})
        self.assertEqual(results["fusion-net-10"]["status"], "complete")
        self.assertEqual(results["grafbase"], {"variant": "grafbase", "status": "failed"})
        self.assertEqual(results["feddi-gateway"], {"variant": "feddi-gateway", "status": "failed"})
        self.assertEqual(set(results), {"fusion-net-10", "grafbase", "feddi-gateway"})

        burst, results = self.results_by_variant(doc, "burst")
        self.assertNotIn("status", burst)
        self.assertEqual(results["fusion-net-10"]["status"], "complete")
        self.assertEqual(results["grafbase"]["status"], "failed")
        self.assertEqual(results["feddi-gateway"]["status"], "failed")

        self.assertNotIn("constant-latency", [s["id"] for s in doc["scenarios"]])

    def test_incompatible_response_gets_full_entry_over_all_runs(self):
        artifacts = self.make_artifacts()
        for run_index, (rate, passes, fails) in enumerate([(900, 90, 10), (1000, 100, 0), (1100, 80, 20)], 1):
            summary = json.loads(json.dumps(SUMMARY))
            summary["metrics"]["http_reqs"]["values"]["rate"] = rate
            summary["metrics"]["success_rate"]["values"] = {"passes": passes, "fails": fails}
            make_run(artifacts, "grafbase", "grafbase (HotChocolate subgraphs)",
                     run_index=run_index, summary=summary)
        doc = self.run_json_generator(artifacts, {
            "EXPECTED_GATEWAYS_JSON": json.dumps([expected_entry("grafbase")]),
        })
        _, results = self.results_by_variant(doc, "constant")
        grafbase = results["grafbase"]
        self.assertEqual(grafbase["throughput"]["medianRps"], 1000)
        self.assertEqual(grafbase["throughput"]["bestRps"], 1100)
        self.assertEqual(grafbase["throughput"]["worstRps"], 900)
        self.assertEqual(grafbase["throughput"]["runsRps"], [900, 1000, 1100])
        self.assertEqual(grafbase["requests"], {"total": 300, "successful": 270, "failed": 30})
        self.assertNotIn("failure", grafbase)
        self.assertEqual(grafbase["status"], "complete")

    def test_all_incompatible_runs_keep_complete_execution_status(self):
        artifacts = self.make_artifacts()
        for run_index, rate in enumerate((900, 1000, 1100), 1):
            summary = json.loads(json.dumps(SUMMARY))
            summary["metrics"]["http_reqs"]["values"]["rate"] = rate
            summary["metrics"]["success_rate"]["values"] = {"passes": 90, "fails": 10}
            make_run(
                artifacts,
                "grafbase",
                "grafbase (HotChocolate subgraphs)",
                run_index=run_index,
                summary=summary,
            )
        doc = self.run_json_generator(artifacts, {
            "EXPECTED_GATEWAYS_JSON": json.dumps([expected_entry("grafbase")]),
        })
        _, results = self.results_by_variant(doc, "constant")
        self.assertEqual(results["grafbase"]["status"], "complete")
        self.assertEqual(results["grafbase"]["throughput"]["runsRps"], [900, 1000, 1100])
        self.assertEqual(
            results["grafbase"]["requests"],
            {"total": 300, "successful": 270, "failed": 30},
        )

    def test_incomplete_gateway_execution_is_failed_with_partial_metrics(self):
        artifacts = self.make_artifacts()
        make_run(
            artifacts,
            "fusion-net-10",
            "fusion-net-10 (HotChocolate subgraphs)",
            extra_metadata={"total_runs": 3},
        )
        doc = self.run_json_generator(artifacts, {
            "EXPECTED_GATEWAYS_JSON": json.dumps([expected_entry("fusion-net-10")]),
        })
        _, results = self.results_by_variant(doc, "constant")
        self.assertEqual(results["fusion-net-10"]["status"], "failed")
        self.assertEqual(results["fusion-net-10"]["throughput"]["runsRps"], [1000])

    def test_cpuset_parsing_and_cpu_utilization(self):
        gen = load_generator()
        self.assertEqual(gen.parse_cpuset("2-3,10-11"), {2, 3, 10, 11})
        self.assertEqual(gen.parse_cpuset("0"), {0})
        self.assertEqual(gen.parse_cpuset("2-4"), {2, 3, 4})
        self.assertEqual(gen.parse_cpuset(""), set())
        self.assertEqual(gen.run_cpuset({"gateway_cpuset": "5"}, "gateway"), "5")
        self.assertEqual(gen.run_cpuset({"gateway_cpuset": ""}, "gateway"), "")
        with open(os.path.join(REPO_ROOT, "profiles.json")) as fh:
            profiles = json.load(fh)
        self.assertEqual(
            gen.run_cpuset({"machine_cores": "16 logical (16 CPUs)", "mode": "constant-latency"}, "gateway"),
            profiles["16"]["constant"]["gateway"],
        )
        self.assertEqual(
            gen.run_cpuset({"machine_cores": "8 logical", "mode": "burst"}, "gateway"),
            profiles["8"]["ramping"]["gateway"],
        )
        run = {
            "gateway_core_pct": [50.0, 100.0, 60.0],
            "metadata": {"gateway_cpuset": "2-3,10-11"},
        }
        self.assertEqual(
            gen.json_cpu(run),
            {"avgUtilizationPercent": 70.0, "maxUtilizationPercent": 100.0},
        )
        self.assertIsNone(gen.json_cpu({"gateway_core_pct": [], "metadata": {"gateway_cpuset": "2"}}))

    def test_cpu_and_run_settings_from_median_run(self):
        artifacts = self.make_artifacts()
        header = "Seconds,VUs,RPS,P95_ms,Req_success_rate,Total_CPU,K6_Core_CPU,Subgraph_Core_CPU,Gateway_Core_CPU,Total_RSS_KB\n"
        make_run(
            artifacts, "fusion-net-10", "fusion-net-10 (HotChocolate subgraphs)", mode="constant-latency",
            extra_metadata={"gateway_cpuset": "2-3", "subgraph_delay_ms": 7},
            data_csv=header + "1,50,1,1,1,400,10,10,25.00,1\n2,50,1,1,1,400,10,10,75.00,1\n",
        )
        doc = self.run_json_generator(artifacts, {
            "EXPECTED_GATEWAYS_JSON": json.dumps([expected_entry("fusion-net-10")]),
        })
        scenario, results = self.results_by_variant(doc, "constant-latency")
        self.assertEqual(
            results["fusion-net-10"]["cpu"],
            {"avgUtilizationPercent": 50.0, "maxUtilizationPercent": 75.0},
        )
        self.assertEqual(
            scenario["config"].pop("cpuAllocation")["gateway"],
            {"threadIds": [2, 3], "hardwareThreads": 2},
        )
        self.assertEqual(scenario["config"], {
            "durationSeconds": 120, "virtualUsers": 50, "subgraphDelayMs": 7,
            "warmupRuns": 1, "measuredRuns": 1,
        })
        self.assertEqual(
            scenario["description"],
            "This scenario executes a constant load of 50 VUs over 120s "
            "with a simulated 7ms IO delay on each subgraph request.",
        )

    def test_zero_subgraph_delay_from_run_metadata(self):
        artifacts = self.make_artifacts()
        make_run(
            artifacts,
            "fusion-net-10",
            "fusion-net-10 (HotChocolate subgraphs)",
            extra_metadata={"subgraph_delay_ms": 0},
        )
        doc = self.run_json_generator(artifacts, {
            "EXPECTED_GATEWAYS_JSON": json.dumps([expected_entry("fusion-net-10")]),
        })
        constant, _ = self.results_by_variant(doc, "constant")
        self.assertEqual(constant["config"]["subgraphDelayMs"], 0)

    def test_cpu_allocation_from_run_metadata(self):
        artifacts = self.make_artifacts()
        pins = {
            "system_cpuset": "0,8",
            "k6_cpuset": "1,9",
            "gateway_cpuset": "2",
            "subgraphs_cpuset": "3-5",
        }
        make_run(artifacts, "fusion-net-10", "fusion-net-10 (HotChocolate subgraphs)", run_index=1, extra_metadata=pins)
        make_run(artifacts, "fusion-net-10", "fusion-net-10 (HotChocolate subgraphs)", run_index=2, extra_metadata=pins)
        make_run(artifacts, "fusion-net-10", "fusion-net-10 (HotChocolate subgraphs)", run_index=3,
                 extra_metadata={
                     "system_cpuset": "6", "k6_cpuset": "9",
                     "gateway_cpuset": "7", "subgraphs_cpuset": "8",
                 })
        doc = self.run_json_generator(artifacts, {
            "EXPECTED_GATEWAYS_JSON": json.dumps([expected_entry("fusion-net-10")]),
        })
        constant, _ = self.results_by_variant(doc, "constant")
        self.assertEqual(constant["config"]["cpuAllocation"], {
            "system": {"threadIds": [0, 8], "hardwareThreads": 2},
            "k6": {"threadIds": [1, 9], "hardwareThreads": 2},
            "gateway": {"threadIds": [2], "hardwareThreads": 1},
            "subgraphs": {"threadIds": [3, 4, 5], "hardwareThreads": 3},
        })
        artifacts = self.make_artifacts()
        make_run(artifacts, "fusion-net-10", "fusion-net-10 (HotChocolate subgraphs)",
                 extra_metadata={
                     "system_cpuset": "", "k6_cpuset": "",
                     "gateway_cpuset": "", "subgraphs_cpuset": "",
                 })
        doc = self.run_json_generator(artifacts, {
            "EXPECTED_GATEWAYS_JSON": json.dumps([expected_entry("fusion-net-10")]),
        })
        constant, _ = self.results_by_variant(doc, "constant")
        self.assertNotIn("cpuAllocation", constant["config"])

    def test_cpu_allocation_falls_back_to_profiles(self):
        artifacts = self.make_artifacts()
        make_run(artifacts, "fusion-net-10", "fusion-net-10 (HotChocolate subgraphs)", mode="burst")
        doc = self.run_json_generator(artifacts, {
            "EXPECTED_GATEWAYS_JSON": json.dumps([expected_entry("fusion-net-10")]),
        })
        burst, _ = self.results_by_variant(doc, "burst")
        with open(os.path.join(REPO_ROOT, "profiles.json")) as fh:
            profile = json.load(fh)["16"]["ramping"]  # fixture: "16 logical"
        gen = load_generator()
        self.assertEqual(burst["config"]["cpuAllocation"], {
            role: {
                "threadIds": sorted(gen.parse_cpuset(profile[role])),
                "hardwareThreads": len(gen.parse_cpuset(profile[role])),
            }
            for role in ("system", "k6", "gateway", "subgraphs")
        })

    def test_recorded_cpu_topology_reports_physical_cores(self):
        artifacts = self.make_artifacts()
        topology = [[thread, thread % 8] for thread in range(16)]
        make_run(
            artifacts,
            "fusion-net-10",
            "fusion-net-10 (HotChocolate subgraphs)",
            extra_metadata={
                "cpu_topology": topology,
                "system_cpuset": "0,8",
                "k6_cpuset": "1,9",
                "gateway_cpuset": "2-3,10-11",
                "subgraphs_cpuset": "4-7,12-15",
            },
        )
        doc = self.run_json_generator(artifacts, {
            "EXPECTED_GATEWAYS_JSON": json.dumps([expected_entry("fusion-net-10")]),
        })
        self.assertEqual(doc["hardware"], {
            "host": "test-host",
            "cpuModel": "Test CPU",
            "hardwareThreads": 16,
            "physicalCores": 8,
            "threadsPerCore": 2,
            "coreThreads": [[core, core + 8] for core in range(8)],
            "memoryGb": 32,
            "os": "Linux",
        })
        constant, _ = self.results_by_variant(doc, "constant")
        self.assertEqual(constant["config"]["cpuAllocation"], {
            "system": {
                "threadIds": [0, 8], "hardwareThreads": 2, "physicalCores": 1,
            },
            "k6": {
                "threadIds": [1, 9], "hardwareThreads": 2, "physicalCores": 1,
            },
            "gateway": {
                "threadIds": [2, 3, 10, 11], "hardwareThreads": 4, "physicalCores": 2,
            },
            "subgraphs": {
                "threadIds": [4, 5, 6, 7, 12, 13, 14, 15],
                "hardwareThreads": 8,
                "physicalCores": 4,
            },
        })

    def test_scenario_config_for_older_artifacts(self):
        artifacts = self.make_artifacts()
        for mode in ("burst", "constant-latency"):
            make_run(artifacts, "fusion-net-10", "fusion-net-10 (HotChocolate subgraphs)", mode=mode)
        doc = self.run_json_generator(artifacts, {
            "EXPECTED_GATEWAYS_JSON": json.dumps([expected_entry("fusion-net-10")]),
        })
        configs = {s["id"]: s["config"] for s in doc["scenarios"]}
        self.assertEqual(configs["constant-latency"]["subgraphDelayMs"], 4)
        self.assertEqual(configs["burst"]["subgraphDelayMs"], 0)
        # The old burst summary's "120s" is BENCH_OVER_TIME, not the stage sum.
        self.assertNotIn("durationSeconds", configs["burst"])
        self.assertNotIn("description", next(s for s in doc["scenarios"] if s["id"] == "burst"))
        self.assertEqual(configs["constant-latency"]["durationSeconds"], 120)
        self.assertEqual(configs["burst"]["warmupRuns"], 1)

    def test_started_at_null_when_unknown(self):
        artifacts = self.make_artifacts()
        make_run(artifacts, "fusion-net-10", "fusion-net-10 (HotChocolate subgraphs)")
        doc = self.run_json_generator(artifacts, {
            "EXPECTED_GATEWAYS_JSON": json.dumps([expected_entry("fusion-net-10")]),
            "RUN_STARTED_AT": "",
        })
        self.assertIsNone(doc["run"]["startedAt"])

    def test_planned_duration_from_k6_summary(self):
        artifacts = self.make_artifacts()
        summary = json.loads(json.dumps(SUMMARY))
        summary.update({"duration": "60s", "plannedDurationSeconds": 60})
        make_run(artifacts, "fusion-net-10", "fusion-net-10 (HotChocolate subgraphs)", mode="burst", summary=summary)
        doc = self.run_json_generator(artifacts, {
            "EXPECTED_GATEWAYS_JSON": json.dumps([expected_entry("fusion-net-10")]),
        })
        burst = next(s for s in doc["scenarios"] if s["id"] == "burst")
        self.assertEqual(burst["config"]["durationSeconds"], 60)
        self.assertIn("over 60s", burst["description"])

    def test_captured_versions_reported_without_fallbacks(self):
        artifacts = self.make_artifacts()
        make_run(artifacts, "fusion-net-10", "fusion-net-10 (HotChocolate subgraphs)", extra_metadata={
            "runtime_version": "10.0.13", "subgraphs_runtime_version": "10.0.13",
            "subgraphs_hotchocolate_version": "16.6.8",
        })
        make_run(artifacts, "cosmo", "cosmo (HotChocolate subgraphs)")
        doc = self.run_json_generator(artifacts, {
            "EXPECTED_GATEWAYS_JSON": json.dumps([expected_entry("fusion-net-10"), expected_entry("cosmo")]),
        })
        variants = {v["id"]: v for g in doc["gateways"] for v in g["variants"]}
        self.assertEqual(variants["fusion-net-10"]["platform"]["runtime"], {"name": ".NET", "version": "10.0.13"})
        self.assertEqual(variants["cosmo"]["platform"]["runtime"], {"name": "Go"})
        self.assertEqual(doc["subgraphs"]["framework"], {"name": "Hot Chocolate", "version": "16.6.8"})
        self.assertEqual(doc["subgraphs"]["platform"]["runtime"], {"name": ".NET", "version": "10.0.13"})

    def test_variant_display_metadata_passed_through(self):
        artifacts = self.make_artifacts()
        make_run(artifacts, "fusion-nightly-fed-net-10", "fusion-nightly-fed-net-10 (HotChocolate subgraphs)")
        doc = self.run_json_generator(artifacts, {
            "EXPECTED_GATEWAYS_JSON": json.dumps([
                expected_entry(variant_id)
                for variant_id in (
                    "fusion-net-10", "fusion-nightly-net-10", "fusion-nightly-net-11",
                    "fusion-nightly-fed-net-10", "feddi-gateway",
                )
            ]),
        })
        variants = {v["id"]: v for g in doc["gateways"] for v in g["variants"]}
        self.assertEqual(variants["fusion-nightly-net-10"]["label"], "Fusion Nightly")
        self.assertEqual(variants["fusion-nightly-net-11"]["label"], "Fusion Nightly")
        self.assertEqual(variants["fusion-nightly-fed-net-10"]["label"], "Fusion Nightly")
        self.assertIs(variants["feddi-gateway"]["preview"], True)
        self.assertNotIn("label", variants["fusion-net-10"])
        self.assertNotIn("preview", variants["fusion-net-10"])

    def test_median_run_tie_broken_by_execution_order(self):
        artifacts = self.make_artifacts()
        for run_index in (3, 1, 2):
            summary = json.loads(json.dumps(SUMMARY))
            summary["metrics"]["http_req_duration"]["values"] = {
                stat: float(run_index) for stat in ("avg", "min", "med", "max", "p(90)", "p(95)", "p(99.9)")
            }
            make_run(
                artifacts, "fusion-net-10", "fusion-net-10 (HotChocolate subgraphs)",
                run_index=run_index, summary=summary,
            )
        doc = self.run_json_generator(artifacts, {
            "EXPECTED_GATEWAYS_JSON": json.dumps([expected_entry("fusion-net-10")]),
        })
        _, results = self.results_by_variant(doc, "constant")
        self.assertEqual(results["fusion-net-10"]["latencyMs"]["avg"], 2.0)


class BackfillRuntimeVersionTests(unittest.TestCase):

    def test_missing_versions_use_current_runtime_for_matching_target(self):
        document = {
            "run": {"number": 298},
            "subgraphs": {
                "platform": {
                    "runtime": {"name": ".NET"},
                },
            },
            "gateways": [{
                "variants": [
                    {
                        "id": "fusion-net-10",
                        "platform": {"runtime": {"name": ".NET"}},
                    },
                    {
                        "id": "fusion-nightly-net-11",
                        "platform": {"runtime": {"name": ".NET"}},
                    },
                ],
            }],
        }
        baseline = {
            "subgraphs": {
                "platform": {
                    "runtime": {"name": ".NET", "version": "10.0.13"},
                },
            },
            "gateways": [{
                "variants": [
                    {
                        "id": "fusion-net-10",
                        "platform": {
                            "runtime": {"name": ".NET", "version": "10.0.13"},
                        },
                    },
                    {
                        "id": "fusion-nightly-net-11",
                        "platform": {
                            "runtime": {
                                "name": ".NET",
                                "version": "11.0.0-rc.2.26504.105",
                            },
                        },
                    },
                ],
            }],
        }

        BACKFILL.apply_assumed_runtime_versions(document, baseline)

        self.assertEqual(
            document["subgraphs"]["platform"]["runtime"]["version"],
            "10.0.13",
        )
        variants = document["gateways"][0]["variants"]
        self.assertEqual(variants[0]["platform"]["runtime"]["version"], "10.0.13")
        self.assertEqual(
            variants[1]["platform"]["runtime"]["version"],
            "11.0.0-preview.6.26359.118",
        )

    def test_captured_version_is_preserved(self):
        document = {
            "run": {"number": 298},
            "subgraphs": {
                "platform": {
                    "runtime": {"name": ".NET", "version": "10.0.12"},
                },
            },
            "gateways": [],
        }
        baseline = {
            "subgraphs": {
                "platform": {
                    "runtime": {"name": ".NET", "version": "10.0.13"},
                },
            },
            "gateways": [],
        }

        BACKFILL.apply_assumed_runtime_versions(document, baseline)

        self.assertEqual(
            document["subgraphs"]["platform"]["runtime"]["version"],
            "10.0.12",
        )

    def test_net11_runtime_changes_follow_retained_build_logs(self):
        expected = {
            298: "11.0.0-preview.6.26359.118",
            317: "11.0.0-preview.7.26381.103",
            343: "11.0.0-rc.1.26425.128",
            400: "11.0.0-rc.2.26504.105",
        }
        self.assertEqual(
            {run: BACKFILL.inferred_net11_runtime(run) for run in expected},
            expected,
        )


class RuntimeVersionTests(unittest.TestCase):

    SCRIPT = os.path.join(REPO_ROOT, "k6", "runtime-version.py")

    def run_script(self, *args, path=None):
        env = dict(os.environ)
        if path:
            env["PATH"] = path + os.pathsep + env["PATH"]
        proc = subprocess.run(["python3", self.SCRIPT, *args], capture_output=True, text=True,
                              timeout=30, env=env)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        return proc.stdout.strip()

    def component(self):
        directory = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, directory, True)
        return directory

    def test_dotnet_shared_runtime_not_sdk(self):
        directory = self.component()
        for version in ("10.0.12", "10.0.13", "11.0.0-rc.2.26504.105"):
            os.makedirs(os.path.join(directory, ".dotnet", "shared", "Microsoft.NETCore.App", version))
        os.makedirs(os.path.join(directory, ".dotnet", "sdk", "10.0.402"))
        self.assertEqual(self.run_script(directory), "11.0.0-rc.2.26504.105")

    def test_jvm_release_file_normalized_to_semver(self):
        directory = self.component()
        os.makedirs(os.path.join(directory, ".jdk"))
        with open(os.path.join(directory, ".jdk", "release"), "w") as fh:
            fh.write('IMPLEMENTOR="Eclipse Adoptium"\nJAVA_VERSION="25.0.4.1"\n')
        self.assertEqual(self.run_script(directory), "25.0.4")

    def test_node_version_from_path(self):
        directory = self.component()
        with open(os.path.join(directory, "package.json"), "w") as fh:
            fh.write("{}")
        bindir = self.component()
        with open(os.path.join(bindir, "node"), "w") as fh:
            fh.write("#!/bin/sh\necho v22.23.3\n")
        os.chmod(os.path.join(bindir, "node"), 0o755)
        self.assertEqual(self.run_script(directory, path=bindir), "22.23.3")

    def test_native_binary_has_no_runtime_version(self):
        directory = self.component()
        with open(os.path.join(directory, "router"), "wb") as fh:
            fh.write(b"\x7fELF" + b"\0" * 64)
        os.chmod(os.path.join(directory, "router"), 0o755)
        self.assertEqual(self.run_script(directory), "")

    def test_package_version_from_deps_json(self):
        directory = self.component()
        build = os.path.join(directory, "eShop.Accounts", "bin", "Release", "net10.0")
        os.makedirs(build)
        with open(os.path.join(build, "eShop.Accounts.deps.json"), "w") as fh:
            json.dump({"libraries": {"HotChocolate.AspNetCore/16.6.8": {}, "eShop.Accounts/1.0.0": {}}}, fh)
        self.assertEqual(self.run_script("--package", "HotChocolate.AspNetCore", directory), "16.6.8")
        self.assertEqual(self.run_script("--package", "Missing.Package", directory), "")


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
                self.assertNotIn("sed -i", content)
                # The pin check fails fast instead of mutating tracked files.
                self.assertIn("not pinned to", content)
                self.assertIn("exit 1", content)
                # Pin validation must use an XML parser, not regex, so
                # single-quoted attributes parse and comments are ignored.
                self.assertIn("xml.etree.ElementTree", content)

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
            "fusion-fed",
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


class FusionBenchPropsTests(unittest.TestCase):
    """Execute install.sh's bench.props generation for each benchmark axis.

    The .NET 11 retarget must clear the plural TargetFrameworks inherited
    from Directory.Build.props: a multi-targeted (outer/inner dispatch)
    build never engages the Native AOT compiler on publish, silently
    yielding a JIT-only artifact that start.sh (fail-closed for AOT=1)
    would then refuse to run.
    """

    INSTALL_SCRIPTS = (
        os.path.join(
            REPO_ROOT, "composite-schema", "gateways", "fusion", "install.sh"
        ),
        os.path.join(
            REPO_ROOT,
            "apollo-federation",
            "gateways",
            "fusion-fed",
            "install.sh",
        ),
    )
    BLOCK_START = "# --- Generate bench.props: begin ---"
    BLOCK_END = "# --- Generate bench.props: end ---"

    def run_gen_block(self, script, dotnet_target, aot, cost_define=""):
        with open(script, encoding="utf-8") as fh:
            content = fh.read()
        start = content.index(self.BLOCK_START) + len(self.BLOCK_START)
        end = content.index(self.BLOCK_END)
        block = content[start:end]
        workdir = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, workdir, True)
        props = os.path.join(workdir, "bench.props")
        wrapper = os.path.join(workdir, "gen-bench-props.sh")
        with open(wrapper, "w", encoding="utf-8") as fh:
            fh.write("set -u\n")
            fh.write(f'DOTNET_TARGET="{dotnet_target}"\n')
            fh.write(f'AOT="{aot}"\n')
            fh.write(f'FUSION_COST_DEFINE="{cost_define}"\n')
            fh.write(f'BENCH_PROPS="{props}"\n')
            fh.write(block + "\n")
        proc = subprocess.run(
            ["bash", wrapper],
            capture_output=True,
            text=True,
            timeout=60,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr + proc.stdout)
        if not os.path.exists(props):
            return None
        with open(props, encoding="utf-8") as fh:
            return fh.read()

    def test_net11_is_singular_with_cleared_plural(self):
        for script in self.INSTALL_SCRIPTS:
            with self.subTest(script=script):
                props = self.run_gen_block(script, "11", "0")
                self.assertIsNotNone(props)
                self.assertIn("<TargetFramework>net11.0</TargetFramework>", props)
                self.assertIn("<TargetFrameworks></TargetFrameworks>", props)
                self.assertNotRegex(props, r"<TargetFrameworks>net")
                self.assertIn("runtime-async=on", props)
                self.assertNotIn("PublishAot", props)
                ET.fromstring(props)

    def test_aot_adds_publish_aot_without_plural_frameworks(self):
        for script in self.INSTALL_SCRIPTS:
            with self.subTest(script=script):
                props = self.run_gen_block(script, "11", "1")
                self.assertIsNotNone(props)
                self.assertIn("<PublishAot>true</PublishAot>", props)
                self.assertIn("<TargetFrameworks></TargetFrameworks>", props)
                self.assertNotRegex(props, r"<TargetFrameworks>net")

    def test_net10_jit_writes_no_file(self):
        for script in self.INSTALL_SCRIPTS:
            with self.subTest(script=script):
                self.assertIsNone(self.run_gen_block(script, "10", "0"))

    def test_net10_with_cost_define_writes_no_target(self):
        for script in self.INSTALL_SCRIPTS:
            with self.subTest(script=script):
                props = self.run_gen_block(
                    script, "10", "0", "FUSION_16_7_OR_GREATER")
                self.assertIsNotNone(props)
                self.assertNotIn("TargetFramework", props)
                self.assertIn("FUSION_16_7_OR_GREATER", props)


class FusionGatewayStartScriptTests(unittest.TestCase):
    """Execute both fusion start.sh scripts against fixture artifacts.

    Guards the Native AOT launch path: the controlled publish dir is used
    (RID-qualified publish output is ignored), AOT=1 fails closed when the
    native binary is absent, and the launchSettings applicationUrl is
    preserved explicitly (a directly executed binary never reads
    launchSettings.json, unlike `dotnet run`).
    """

    GATEWAY_DIRS = (
        os.path.join("composite-schema", "gateways", "fusion"),
        os.path.join("apollo-federation", "gateways", "fusion-fed"),
    )
    GATEWAY_URL = "http://localhost:5299"
    # A distinctive port proves the URL is derived from launchSettings.json
    # rather than hardcoded to the benchmark default.

    def make_fixture(self, gateway_dir, native=False, rid_only=False,
                     launch_url=GATEWAY_URL, dotnet=True):
        workdir = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, workdir, True)
        shutil.copy(
            os.path.join(REPO_ROOT, gateway_dir, "start.sh"),
            os.path.join(workdir, "start.sh"),
        )
        project = os.path.join(workdir, "eShop.Gateway")
        os.makedirs(os.path.join(project, "Properties"))
        if launch_url is None:
            settings = {"profiles": {"http": {}}}
        else:
            settings = {
                "profiles": {
                    "http": {
                        "commandName": "Project",
                        "applicationUrl": launch_url,
                    }
                }
            }
        with open(
            os.path.join(project, "Properties", "launchSettings.json"),
            "w",
            encoding="utf-8",
        ) as fh:
            json.dump(settings, fh)
        marker = os.path.join(workdir, "exec-marker.txt")
        native_stub = (
            "#!/usr/bin/env bash\n"
            f'echo "native ASPNETCORE_URLS=$ASPNETCORE_URLS" >> "{marker}"\n'
            "exit 0\n"
        )
        if native:
            publish = os.path.join(
                project, "bin", "Release", "net11.0", "publish")
            os.makedirs(publish)
            binary = os.path.join(publish, "eShop.Gateway")
            with open(binary, "w", encoding="utf-8") as fh:
                fh.write(native_stub)
            os.chmod(binary, 0o755)
        if rid_only:
            # publish's default output qualifies the path with the build RID;
            # start.sh must not resolve the native binary from here.
            publish = os.path.join(
                project, "bin", "Release", "net11.0", "linux-x64", "publish")
            os.makedirs(publish)
            binary = os.path.join(publish, "eShop.Gateway")
            with open(binary, "w", encoding="utf-8") as fh:
                fh.write(native_stub)
            os.chmod(binary, 0o755)
        if dotnet:
            bundled = os.path.join(workdir, ".dotnet")
            os.makedirs(bundled)
            stub = os.path.join(bundled, "dotnet")
            with open(stub, "w", encoding="utf-8") as fh:
                fh.write(
                    "#!/usr/bin/env bash\n"
                    f'echo "dotnet ASPNETCORE_URLS=$ASPNETCORE_URLS args=$*"'
                    f' >> "{marker}"\n'
                    "exit 0\n"
                )
            os.chmod(stub, 0o755)
        return workdir, marker

    def run_start(self, workdir, aot=None):
        env = dict(os.environ)
        if aot is None:
            env.pop("BENCH_GATEWAY_AOT", None)
        else:
            env["BENCH_GATEWAY_AOT"] = aot
        return subprocess.run(
            ["bash", os.path.join(workdir, "start.sh")],
            capture_output=True,
            text=True,
            timeout=60,
            cwd=workdir,
            env=env,
        )

    def read_marker(self, marker):
        if not os.path.exists(marker):
            return ""
        with open(marker, encoding="utf-8") as fh:
            return fh.read()

    def test_native_binary_preferred_with_launch_url(self):
        for gateway_dir in self.GATEWAY_DIRS:
            with self.subTest(gateway=gateway_dir):
                workdir, marker = self.make_fixture(gateway_dir, native=True)
                proc = self.run_start(workdir)
                self.assertEqual(proc.returncode, 0, proc.stderr)
                self.assertIn(
                    f"native ASPNETCORE_URLS={self.GATEWAY_URL}",
                    self.read_marker(marker),
                )
                self.assertNotIn("dotnet ASPNETCORE_URLS", self.read_marker(marker))

    def test_rid_qualified_output_ignored_and_aot_fails_closed(self):
        # Only a RID-qualified publish dir exists (publish's default layout):
        # start.sh must not find a native binary there, and AOT=1 must fail
        # instead of silently running the JIT build.
        for gateway_dir in self.GATEWAY_DIRS:
            with self.subTest(gateway=gateway_dir):
                workdir, marker = self.make_fixture(gateway_dir, rid_only=True)
                proc = self.run_start(workdir, aot="1")
                self.assertNotEqual(proc.returncode, 0)
                self.assertIn("BENCH_GATEWAY_AOT=1", proc.stdout + proc.stderr)
                self.assertNotIn("native ASPNETCORE_URLS", self.read_marker(marker))
                self.assertNotIn("dotnet ASPNETCORE_URLS", self.read_marker(marker))

    def test_aot_requires_native_binary(self):
        for gateway_dir in self.GATEWAY_DIRS:
            with self.subTest(gateway=gateway_dir):
                workdir, marker = self.make_fixture(gateway_dir)
                proc = self.run_start(workdir, aot="1")
                self.assertNotEqual(proc.returncode, 0)
                self.assertIn("BENCH_GATEWAY_AOT=1", proc.stdout + proc.stderr)
                self.assertNotIn("dotnet ASPNETCORE_URLS", self.read_marker(marker))

    def test_jit_fallback_uses_bundled_sdk_with_launch_url(self):
        for gateway_dir in self.GATEWAY_DIRS:
            with self.subTest(gateway=gateway_dir):
                workdir, marker = self.make_fixture(gateway_dir)
                proc = self.run_start(workdir)
                self.assertEqual(proc.returncode, 0, proc.stderr)
                recorded = self.read_marker(marker)
                self.assertIn(
                    "dotnet ASPNETCORE_URLS="
                    f"{self.GATEWAY_URL} args=run -c Release --no-build --no-restore",
                    recorded,
                )

    def test_missing_launch_url_fails_closed(self):
        for gateway_dir in self.GATEWAY_DIRS:
            with self.subTest(gateway=gateway_dir):
                workdir, marker = self.make_fixture(
                    gateway_dir, native=True, launch_url=None)
                proc = self.run_start(workdir)
                self.assertNotEqual(proc.returncode, 0)
                self.assertIn("applicationUrl", proc.stdout + proc.stderr)
                self.assertNotIn("native ASPNETCORE_URLS", self.read_marker(marker))

    def test_invalid_aot_value_rejected(self):
        for gateway_dir in self.GATEWAY_DIRS:
            with self.subTest(gateway=gateway_dir):
                workdir, _ = self.make_fixture(gateway_dir, native=True)
                proc = self.run_start(workdir, aot="banana")
                self.assertNotEqual(proc.returncode, 0)
                self.assertIn(
                    "unknown BENCH_GATEWAY_AOT", proc.stdout + proc.stderr)


if __name__ == "__main__":
    unittest.main()
