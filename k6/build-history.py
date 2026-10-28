#!/usr/bin/env python3
"""Build benchmark-runs/history.json from every benchmark-runs/<run>/results.json.

Only scheduled runs count. The latest such run defines the emitted scenarios
that were run, their config and the gateway catalog. Failed gateway executions
with measurements are kept with "status": "failed"; those without are excluded.
Per scenario, every variant in the latest catalog gets a chronological result
series containing every comparable run in the six calendar months ending at
the latest run. Comparable runs have matching load config and hardware.cpuModel,
one warmup, and five or nine measured repetitions, recorded on each result.
Gateway and subgraph platform/runtime details are recorded on every result.
A variant that replaced another, which the latest run no longer contains,
continues its history: the series holds the replaced variant's runs, each
tagged with the variant that produced it, followed by the replacing variant's
runs after the replaced variant's last run, and names the replaced variant in
"continues".

Usage: build-history.py <benchmark-runs-dir> <output-path>
"""

import json
import os
import sys
from calendar import monthrange
from datetime import datetime
from pathlib import Path

HISTORY_MONTHS = 6
WARMUP_RUNS = 1
MEASURED_RUNS = {5, 9}
RAN_SCENARIO_STATUSES = {"complete", "failed"}

# feddi-gateway's request-throughput implementation landed before run 400.
# Earlier measurements (roughly 20 RPS) exercise a different request path and
# are not comparable with the implementation benchmarked by the current catalog.
VARIANT_HISTORY_START_RUN = {"feddi-gateway": 400}

# Variants that replaced another variant of the same gateway, mapped to the
# variant they replaced.
VARIANT_CONTINUES = {"fusion-aot-11": "fusion-net-10"}


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


def result_run_ref(run):
    return {
        key: run[key]
        for key in ("number", "url", "startedAt", "completedAt")
        if key in run
    }


def run_timestamp(run):
    value = run.get("startedAt") or run.get("completedAt")
    if not value:
        return None
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def months_before(value, months):
    month_index = value.year * 12 + value.month - 1 - months
    year, zero_based_month = divmod(month_index, 12)
    month = zero_based_month + 1
    day = min(value.day, monthrange(year, month)[1])
    return value.replace(year=year, month=month, day=day)


def comparability_key(doc, scenario):
    config = {k: v for k, v in scenario["config"].items() if k != "measuredRuns"}
    return json.dumps(
        [config, doc["hardware"]["cpuModel"]],
        sort_keys=True,
    )


def catalog_variants(doc):
    return {
        variant["id"]: (gateway["id"], variant)
        for gateway in doc["gateways"]
        for variant in gateway["variants"]
    }


def scenario_was_run(scenario):
    """New documents omit scenario status; accept legacy completed/failed runs."""
    status = scenario.get("status")
    return status is None or status in RAN_SCENARIO_STATUSES


def build_history(runs):
    runs = [doc for doc in runs if is_eligible(doc)]
    if not runs:
        return None
    latest = runs[-1]
    latest_timestamp = run_timestamp(latest["run"])
    if latest_timestamp is None:
        raise ValueError("latest scheduled run has no startedAt or completedAt timestamp")
    history_from = months_before(latest_timestamp, HISTORY_MONTHS)
    runs = [
        doc
        for doc in runs
        if (timestamp := run_timestamp(doc["run"])) is not None
        and history_from <= timestamp <= latest_timestamp
    ]
    latest_catalog = catalog_variants(latest)

    scenarios = []
    for latest_scenario in latest["scenarios"]:
        if not scenario_was_run(latest_scenario):
            continue
        key = comparability_key(latest, latest_scenario)
        by_variant = {}
        for doc in runs:
            scenario = next(
                (s for s in doc["scenarios"] if s["id"] == latest_scenario["id"]), None
            )
            if (
                scenario is None
                or not scenario_was_run(scenario)
                or scenario["config"].get("warmupRuns") != WARMUP_RUNS
                or scenario["config"].get("measuredRuns") not in MEASURED_RUNS
                or comparability_key(doc, scenario) != key
            ):
                continue
            catalog = catalog_variants(doc)
            for result in scenario["results"]:
                for variant_result in result["variants"]:
                    failed = variant_result.get("status") == "failed"
                    if failed and "throughput" not in variant_result:
                        continue
                    variant_id = variant_result["variant"]
                    if doc["run"]["number"] < VARIANT_HISTORY_START_RUN.get(variant_id, 0):
                        continue
                    variant = catalog.get(variant_id, (None, {}))[1]
                    version = variant.get("version")
                    if not version:
                        continue
                    entry = {
                        "version": version,
                        "run": result_run_ref(doc["run"]),
                        "measuredRuns": scenario["config"]["measuredRuns"],
                        "platform": variant["platform"],
                        "subgraphs": doc["subgraphs"],
                    }
                    entry.update(
                        (k, v)
                        for k, v in variant_result.items()
                        if k not in ("variant", "status")
                    )
                    if failed:
                        entry["status"] = "failed"
                    by_variant.setdefault(variant_id, []).append(entry)

        variants = []
        for variant_id, (gateway_id, _) in latest_catalog.items():
            results = sorted(
                by_variant.get(variant_id, []),
                key=lambda entry: entry["run"]["number"],
            )
            series = {"variant": variant_id, "gateway": gateway_id}
            replaced = VARIANT_CONTINUES.get(variant_id)
            earlier = sorted(
                by_variant.get(replaced, []) if replaced not in latest_catalog else [],
                key=lambda entry: entry["run"]["number"],
            )
            if earlier:
                last_run = earlier[-1]["run"]["number"]
                results = [{**entry, "variant": replaced} for entry in earlier] + [
                    entry for entry in results if entry["run"]["number"] > last_run
                ]
                series["continues"] = replaced
            series["results"] = results
            variants.append(series)

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
