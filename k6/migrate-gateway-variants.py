#!/usr/bin/env python3
"""Migrate historical gateway variant ids to their canonical tags.

Fusion (explicit runtime/channel/AOT scheme):
  fusion                -> fusion-net-10             (stable, composite, .NET 10 JIT)
  fusion-nightly        -> fusion-nightly-net-10     (preview, composite, .NET 10 JIT)
  fusion-nightly-net11  -> fusion-nightly-net-11     (preview, composite, .NET 11 + runtime-async)
  fusion-nightly-fed    -> fusion-nightly-fed-net-10 (preview, federation, .NET 10 JIT)

Feddi (rename commit a9becec):
  feddi                 -> feddi-gateway             (product id/name, variant id,
                                                     and every scenario gateway/variant
                                                     reference; measured values untouched)

Each Fusion variant is verified against its actual run properties
(composition, .NET runtime major, HotChocolate channel, runtime-async
feature) before it is renamed. Each Feddi variant is verified as a
composite-schema Java/JVM preview variant. Mismatches and collisions
(a document already containing the target id) are reported and left
untouched.

Rewrites benchmark-runs/<run>/results.json (structured: gateway catalog
ids/names, variant ids, scenario gateway/variant ids) and the
RESULTS_*.md tables (token replacement, longest id first) in place.
Regenerate benchmark-runs/history.json afterwards with k6/build-history.py;
the root RESULTS_*.md files are the latest run's tables (as the workflow
copies them) and are migrated in place by the same run.

Usage: migrate-gateway-variants.py [--runs-dir benchmark-runs] [--check]
"""

import argparse
import importlib.util
import json
import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent


def load_migrations():
    path = SCRIPT_DIR / "build-matrix.py"
    spec = importlib.util.spec_from_file_location("build_matrix", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    migration = dict(module.FUSION_VARIANT_MIGRATION)
    migration.update(module.FEDDI_VARIANT_MIGRATION)
    return migration


def runtime_major(platform):
    version = str((platform or {}).get("runtime", {}).get("version", ""))
    match = re.match(r"^(\d+)", version)
    return match.group(1) if match else ""


def has_feature(platform, feature_id):
    return any(
        f.get("id") == feature_id
        for f in (platform or {}).get("features", [])
    )


def is_preview_version(version):
    return "-" in str(version or "")


def expected_fusion_properties(old_id):
    """(composition, dotnet_major, preview, runtime_async) or None if unknown."""
    return {
        "fusion": ("composite-schema", "10", False, False),
        "fusion-nightly": ("composite-schema", "10", True, False),
        "fusion-nightly-net11": ("composite-schema", "11", True, True),
        "fusion-nightly-fed": ("apollo-federation", "10", True, False),
    }.get(old_id)


def verify_fusion_variant(variant):
    old_id = variant.get("id", "")
    expected = expected_fusion_properties(old_id)
    if expected is None:
        return True, ""
    want_composition, want_dotnet, want_preview, want_async = expected
    problems = []
    if variant.get("composition", "") != want_composition:
        problems.append(
            f"composition={variant.get('composition')!r} want {want_composition!r}"
        )
    major = runtime_major(variant.get("platform", {}))
    if major and major != want_dotnet:
        problems.append(f"runtime major={major!r} want {want_dotnet!r}")
    preview = is_preview_version(variant.get("version", ""))
    if preview != want_preview:
        problems.append(
            f"version={variant.get('version')!r} preview={preview} want {want_preview}"
        )
    async_feature = has_feature(variant.get("platform", {}), "runtime-async")
    if async_feature != want_async:
        problems.append(f"runtime-async={async_feature} want {want_async}")
    if problems:
        return False, "; ".join(problems)
    return True, ""


def verify_feddi_variant(variant):
    if variant.get("id") != "feddi":
        return True, ""
    problems = []
    if variant.get("composition", "") != "composite-schema":
        problems.append(
            f"composition={variant.get('composition')!r} want 'composite-schema'"
        )
    language = (variant.get("platform", {}).get("language", {}).get("name", ""))
    if language and language != "Java":
        problems.append(f"language={language!r} want 'Java'")
    runtime = (variant.get("platform", {}).get("runtime", {}).get("name", ""))
    if runtime and runtime != "JVM":
        problems.append(f"runtime={runtime!r} want 'JVM'")
    if variant.get("preview") is not True:
        problems.append(f"preview={variant.get('preview')!r} want True")
    if problems:
        return False, "; ".join(problems)
    return True, ""


def verify_variant(variant):
    old_id = variant.get("id", "")
    if old_id == "feddi":
        return verify_feddi_variant(variant)
    return verify_fusion_variant(variant)


def collect_ids(document):
    gateway_ids = [g.get("id", "") for g in document.get("gateways", [])]
    variant_ids = [
        v.get("id", "")
        for g in document.get("gateways", [])
        for v in g.get("variants", [])
    ]
    scenario_gateways = [
        r.get("gateway", "")
        for s in document.get("scenarios", [])
        for r in s.get("results", [])
    ]
    scenario_variants = [
        vr.get("variant", "")
        for s in document.get("scenarios", [])
        for r in s.get("results", [])
        for vr in r.get("variants", [])
    ]
    return gateway_ids, variant_ids, scenario_gateways, scenario_variants


def migrate_results_json(path, migration):
    with open(path, encoding="utf-8") as fh:
        document = json.load(fh)
    changed = 0
    ambiguous = []

    gateway_ids, variant_ids, scenario_gateways, scenario_variants = collect_ids(document)
    for old_id, new_id in migration.items():
        # Collision: both old and new tags present — renaming would merge two
        # distinct series and lose data. Leave the document untouched.
        if old_id in variant_ids and new_id in variant_ids:
            ambiguous.append(
                f"{path}:{old_id}: collision with existing {new_id}; left untouched"
            )
            return 0, ambiguous
        if old_id in gateway_ids and new_id in gateway_ids:
            ambiguous.append(
                f"{path}:gateway:{old_id}: collision with existing {new_id}; left untouched"
            )
            return 0, ambiguous

    for gateway in document.get("gateways", []):
        if gateway.get("id", "") == "feddi":
            gateway["id"] = migration["feddi"]
            changed += 1
            if gateway.get("name", "") == "feddi":
                gateway["name"] = migration["feddi"]
                changed += 1
        for variant in gateway.get("variants", []):
            old_id = variant.get("id", "")
            if old_id not in migration:
                continue
            ok, reason = verify_variant(variant)
            if not ok:
                ambiguous.append(f"{path}:{old_id}: {reason}")
                continue
            variant["id"] = migration[old_id]
            changed += 1
    for scenario in document.get("scenarios", []):
        for result in scenario.get("results", []):
            # Only the feddi product was renamed (feddi -> feddi-gateway).
            # The fusion product id stays "fusion"; only its variant ids change.
            if result.get("gateway", "") == "feddi":
                result["gateway"] = migration["feddi"]
                changed += 1
            for variant_result in result.get("variants", []):
                old_id = variant_result.get("variant", "")
                if old_id in migration:
                    variant_result["variant"] = migration[old_id]
                    changed += 1
    if changed:
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(document, fh, indent=2, ensure_ascii=False)
            fh.write("\n")
    return changed, ambiguous


# Old ids are matched only as whole tokens (not followed by -/alnum), so
# already-migrated new ids never re-match and the migration is idempotent.
# Longest first as defense in depth.
MARKDOWN_PATTERNS = [
    (r"fusion-nightly-net11(?![-A-Za-z0-9])", "fusion-nightly-net-11"),
    (r"fusion-nightly-fed(?![-A-Za-z0-9])", "fusion-nightly-fed-net-10"),
    (r"fusion-nightly(?![-A-Za-z0-9])", "fusion-nightly-net-10"),
    (r"(?<![-A-Za-z0-9/])fusion(?![-A-Za-z0-9])", "fusion-net-10"),
]


def migrate_markdown(path, migration):
    path = Path(path)
    text = path.read_text(encoding="utf-8")
    original = text
    for pattern, new_id in MARKDOWN_PATTERNS:
        text = re.sub(pattern, new_id, text)
    # Bare "feddi" only in benchmark-table contexts: table rows ("| feddi |")
    # and details summaries ("Summary for: feddi ..."). Vendor prose
    # ("by [feddi](https://feddi.dev)"), repository URLs, and the
    # already-migrated feddi-gateway tag are left untouched.
    text = re.sub(r"^(\| )feddi( \|)", rf"\1{migration['feddi']}\2",
                  text, flags=re.M)
    text = re.sub(r"(Summary for: )feddi(?![-A-Za-z0-9])",
                  rf"\1{migration['feddi']}", text)
    if text != original:
        path.write_text(text, encoding="utf-8")
        return 1
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--runs-dir", default="benchmark-runs", type=Path)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)

    migration = load_migrations()
    runs_dir = args.runs_dir
    json_changed = 0
    md_changed = 0
    ambiguous = []
    runs_touched = set()

    for path in sorted(runs_dir.glob("*/results.json")):
        if args.check:
            with open(path, encoding="utf-8") as fh:
                document = json.load(fh)
            for gateway in document.get("gateways", []):
                for variant in gateway.get("variants", []):
                    if variant.get("id") in migration:
                        ok, reason = verify_variant(variant)
                        if not ok:
                            ambiguous.append(f"{path}:{variant.get('id')}: {reason}")
            continue
        changed, problems = migrate_results_json(path, migration)
        ambiguous.extend(problems)
        if changed:
            json_changed += changed
            runs_touched.add(path.parent.name)

    md_files = sorted(runs_dir.glob("*/RESULTS_*.md"))
    root = runs_dir.parent
    for name in ("RESULTS_CONSTANT.md", "RESULTS_BURST.md", "RESULTS_CONSTANT_LATENCY.md"):
        candidate = root / name
        if candidate.is_file():
            md_files.append(candidate)
    for path in md_files:
        if args.check:
            continue
        md_changed += migrate_markdown(path, migration)

    print(f"results.json replacements: {json_changed} in {len(runs_touched)} runs")
    print(f"markdown files updated: {md_changed} of {len(md_files)}")
    if ambiguous:
        print(f"ambiguous variants left untouched: {len(ambiguous)}")
        for line in ambiguous:
            print(f"  {line}")
        return 1
    print("no ambiguous historical variants")
    return 0


if __name__ == "__main__":
    sys.exit(main())
