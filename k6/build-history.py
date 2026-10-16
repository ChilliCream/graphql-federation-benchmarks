#!/usr/bin/env python3
"""Build benchmark-runs/history.json from every benchmark-runs/<run>/results.json.

Only scheduled runs count. The latest such run defines the emitted scenarios,
their config and the gateway catalog; per scenario, a variant keeps its newest
MAX_VERSIONS versions (each from the newest run that measured it) among runs
whose config, hardware.cpu and subgraphs (runtime major only) match the latest
run's.

Usage: build-history.py <benchmark-runs-dir> <output-path>
"""

import json
import os
import sys
from pathlib import Path

MAX_VERSIONS = 3
WARMUP_RUNS = 1
MEASURED_RUNS = 9


def load_runs(runs_dir):
    runs = []
    for entry in Path(runs_dir).iterdir():
        path = entry / "results.json"
        if entry.name.isdigit() and path.is_file():
            with open(path, encoding="utf-8") as f:
                runs.append(json.load(f))
    return sorted(runs, key=lambda doc: doc["run"]["number"])


def is_eligible(doc):
    run = doc["run"]
    if "event" in run:
        return run["event"] == "schedule"
    # Files written before run.event existed: only dispatched runs had inputs.
    return "inputs" not in run


def run_ref(run):
    return {key: run[key] for key in ("number", "url") if key in run}


def subgraphs_key(subgraphs):
    platform = subgraphs["platform"]
    runtime = platform.get("runtime", {})
    # Runtime patch releases are unpinned (e.g. dotnet-install --channel 10.0); only the major counts.
    major = runtime.get("version", "").split(".")[0] or None
    return [subgraphs["framework"], platform["language"], runtime.get("name"), major]


def comparability_key(doc, scenario):
    return json.dumps(
        [scenario["config"], doc["hardware"]["cpu"], subgraphs_key(doc["subgraphs"])],
        sort_keys=True,
    )


def catalog_variants(doc):
    return {
        variant["id"]: (gateway["id"], variant)
        for gateway in doc["gateways"]
        for variant in gateway["variants"]
    }


def build_history(runs):
    runs = [doc for doc in runs if is_eligible(doc)]
    if not runs:
        return None
    latest = runs[-1]
    latest_catalog = catalog_variants(latest)

    scenarios = []
    for latest_scenario in latest["scenarios"]:
        if latest_scenario["status"] != "complete":
            continue
        key = comparability_key(latest, latest_scenario)
        by_variant = {}
        for doc in runs:
            scenario = next(
                (s for s in doc["scenarios"] if s["id"] == latest_scenario["id"]), None
            )
            if (
                scenario is None
                or scenario["status"] != "complete"
                or scenario["config"].get("warmupRuns") != WARMUP_RUNS
                or scenario["config"].get("measuredRuns") != MEASURED_RUNS
                or comparability_key(doc, scenario) != key
            ):
                continue
            catalog = catalog_variants(doc)
            for result in scenario["results"]:
                for variant_result in result["variants"]:
                    variant_id = variant_result["variant"]
                    variant = catalog.get(variant_id, (None, {}))[1]
                    version = variant.get("version")
                    if not version:
                        continue
                    entry = {
                        "version": version,
                        "run": run_ref(doc["run"]),
                        "platform": variant["platform"],
                    }
                    entry.update(
                        (k, v) for k, v in variant_result.items() if k != "variant"
                    )
                    # Runs are in ascending order, so the newest run per version wins.
                    by_variant.setdefault(variant_id, {})[version] = entry

        variants = []
        for variant_id, (gateway_id, _) in latest_catalog.items():
            versions = sorted(
                by_variant.get(variant_id, {}).values(),
                key=lambda entry: entry["run"]["number"],
            )[-MAX_VERSIONS:]
            if versions:
                variants.append(
                    {"variant": variant_id, "gateway": gateway_id, "versions": versions}
                )

        scenarios.append({
            "id": latest_scenario["id"],
            "name": latest_scenario["name"],
            "config": latest_scenario["config"],
            "variants": variants,
        })

    return {
        "latestRun": run_ref(latest["run"]),
        "gateways": latest["gateways"],
        "scenarios": scenarios,
    }


def main():
    if len(sys.argv) != 3:
        print("Usage: build-history.py <benchmark-runs-dir> <output-path>")
        sys.exit(1)

    runs_dir, output_path = sys.argv[1], sys.argv[2]
    history = build_history(load_runs(runs_dir))
    if history is None:
        print(f"No scheduled run with a results.json found in {runs_dir}; nothing to write.")
        sys.exit(1)

    with open(output_path + ".tmp", "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2, ensure_ascii=False)
        f.write("\n")
    os.replace(output_path + ".tmp", output_path)
    print(f"Generated {output_path} from run #{history['latestRun']['number']}")


if __name__ == "__main__":
    main()
