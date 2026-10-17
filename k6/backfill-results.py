#!/usr/bin/env python3
"""Backfill results.json from retained GitHub Actions benchmark artifacts.

Historical artifacts contain both Rust and .NET subgraph measurements, while
the current results format describes one subgraph stack per document. This
utility deliberately keeps only the .NET measurements. Hardware and scenario
configuration are copied from a current baseline results.json so the historical
runs remain comparable with the current benchmark setup.

Usage:
  backfill-results.py \
    --artifacts-dir /tmp/benchmark-artifacts \
    --runs-json /tmp/github-runs.json \
    --baseline benchmark-runs/402/results.json \
    --runs-dir benchmark-runs \
    293 298 299

``runs-json`` is the JSON array returned by ``gh run list --json`` and must
include number, url, startedAt, updatedAt, headSha, event, and conclusion.
"""

import argparse
import copy
import importlib.util
import json
import os
import sys
from collections import Counter
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent


def load_generator():
    path = SCRIPT_DIR / "generate-results.py"
    spec = importlib.util.spec_from_file_location("generate_results", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def github_run_info(run):
    """Convert gh's run representation to the results.json run object."""
    info = {
        "number": run["number"],
        "url": run["url"],
        "startedAt": run["startedAt"],
        "completedAt": run["updatedAt"],
        "sourceCommit": run["headSha"],
        "event": run["event"],
    }
    return {key: value for key, value in info.items() if value is not None}


def mode_of(result):
    mode = result["metadata"].get("mode")
    return "burst" if mode == "ramping" else mode


def validate_complete_results(generator, results, run_number):
    modes = {mode_of(result) for result in results}
    missing_modes = set(generator.JSON_MODES) - modes
    if missing_modes:
        raise ValueError(
            f"run {run_number}: missing .NET artifacts for: "
            + ", ".join(sorted(missing_modes))
        )

    groups = Counter(
        (mode_of(result), generator.get_gateway_name(result["metadata"]))
        for result in results
    )
    for result in results:
        metadata = result["metadata"]
        key = (mode_of(result), generator.get_gateway_name(metadata))
        expected = int(metadata.get("total_runs") or groups[key])
        if groups[key] != expected:
            raise ValueError(
                f"run {run_number}: incomplete {key[0]} execution for "
                f"{key[1]} ({groups[key]}/{expected} artifacts)"
            )


def fusion_version(document):
    for gateway in document["gateways"]:
        for variant in gateway["variants"]:
            if variant["id"] == "fusion":
                return variant.get("version")
    return None


def normalize_document(document, run, baseline):
    document["run"] = github_run_info(run)
    document["hardware"] = copy.deepcopy(baseline["hardware"])

    # Before runtime-version metadata was recorded, both the stable Fusion
    # gateway and the .NET subgraphs resolved the latest stable Hot Chocolate
    # release. The raw Fusion version therefore identifies the framework
    # release; the unrecorded .NET patch version is intentionally omitted.
    framework = {"name": "Hot Chocolate"}
    if version := fusion_version(document):
        framework["version"] = version
    document["subgraphs"] = {
        "framework": framework,
        "platform": {
            "language": {"name": "C#"},
            "runtime": {"name": ".NET"},
        },
    }

    baseline_scenarios = {
        scenario["id"]: scenario for scenario in baseline["scenarios"]
    }
    for scenario in document["scenarios"]:
        current = baseline_scenarios[scenario["id"]]
        scenario["name"] = current["name"]
        scenario["config"] = copy.deepcopy(current["config"])
        if "description" in current:
            scenario["description"] = current["description"]
        else:
            scenario.pop("description", None)


def generate_run(generator, artifacts_dir, run, baseline):
    all_results = generator.find_results(artifacts_dir)
    results = [
        result
        for result in all_results
        if generator.get_subgraph_tech(result["metadata"]) == ".net"
    ]
    if not results:
        raise ValueError(f"run {run['number']}: no .NET benchmark artifacts found")
    validate_complete_results(generator, results, run["number"])

    os.environ.update({
        "GITHUB_RUN_NUMBER": str(run["number"]),
        "GITHUB_RUN_ID": str(run.get("databaseId", "")),
        "GITHUB_REPOSITORY": "ChilliCream/graphql-federation-benchmarks",
        "GITHUB_SHA": run["headSha"],
        "GITHUB_EVENT_NAME": run["event"],
        "RUN_STARTED_AT": run["startedAt"],
        "SCENARIO_RESULTS_JSON": json.dumps({
            mode: "success" for mode in generator.JSON_MODES
        }),
    })
    expected = {mode: [] for mode in generator.JSON_MODES}
    document = generator.generate_results_json(results, expected)
    normalize_document(document, run, baseline)
    return document


def write_document(path, document, force=False):
    if path.exists() and not force:
        raise FileExistsError(f"refusing to overwrite {path}; pass --force")
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    with open(temporary, "w", encoding="utf-8") as f:
        json.dump(document, f, indent=2, ensure_ascii=False)
        f.write("\n")
    os.replace(temporary, path)


def parse_args(argv):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--artifacts-dir", required=True, type=Path)
    parser.add_argument("--runs-json", required=True, type=Path)
    parser.add_argument("--baseline", required=True, type=Path)
    parser.add_argument("--runs-dir", required=True, type=Path)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("runs", nargs="+", type=int)
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv or sys.argv[1:])
    generator = load_generator()
    baseline = load_json(args.baseline)
    metadata = {run["number"]: run for run in load_json(args.runs_json)}

    for run_number in args.runs:
        run = metadata.get(run_number)
        if run is None:
            raise ValueError(f"run {run_number}: missing GitHub run metadata")
        if run.get("event") != "schedule" or run.get("conclusion") != "success":
            raise ValueError(
                f"run {run_number}: expected a successful scheduled run, got "
                f"event={run.get('event')!r}, conclusion={run.get('conclusion')!r}"
            )
        artifacts_dir = args.artifacts_dir / str(run_number)
        document = generate_run(generator, artifacts_dir, run, baseline)
        output = args.runs_dir / str(run_number) / "results.json"
        write_document(output, document, force=args.force)
        print(f"Generated {output}")


if __name__ == "__main__":
    main()
