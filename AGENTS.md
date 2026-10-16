# AGENTS.md

## Layout

- `k6/benchmark-config.json`: gateways (product → variants) and subgraph metadata. No versions. `k6/build-matrix.py` derives the workflow matrix and the results.json gateway catalog from it.
- Versions are pinned where they are installed (`install.sh`, `package.json`, Caliban's `Main.scala`, `subgraphs-net/build.sh`). Each run records what it actually used in `metadata.json`; `k6/generate-results.py` turns the run artifacts into `RESULTS_*.md` and `results.json`.
- `benchmark-runs/history.json` is rebuilt by `k6/build-history.py` from all scheduled runs' `results.json`.
- Never edit `benchmark-runs/` or the root `RESULTS_*.md` by hand.

## Tests

```sh
python3 -m unittest tests.test_build_matrix tests.test_apollo_gateways tests.test_hive_gateways \
  tests.test_cosmo_grafbase_install tests.test_scripts_runtime tests.test_repo_consistency \
  tests.test_build_history
python3 -m unittest -k ConfigTests tests.test_build_matrix   # -k goes before the module names
```

Also run `bash -n` on changed shell scripts (`sh -n` for `apollo-federation/gateways/cosmo/install.sh`) and `actionlint` on workflow changes.

## Bump a gateway version

1. Change the pin: `VERSION` / `DOWNLOAD_VERSION` in `install.sh` (apollo-router, apollo-router-v3, hive-router, grafbase, cosmo), `FEDDI_REF` (feddi), `Main.scala` (caliban), or `package.json` + `npm i` (apollo-gateway, hive-gateway, hive-gateway-router-runtime).
2. Update the version asserted in `tests/test_apollo_gateways.py`, `tests/test_hive_gateways.py` or `tests/test_cosmo_grafbase_install.py`.

Fusion variants resolve the latest HotChocolate for their `channel` (or the `fusion_version` input) and have no pin.

## Bump a runtime

- .NET: the `dotnet-install` channel in the fusion `install.sh` scripts and both `subgraphs-net/build.sh`. A new major also needs the TargetFramework (csprojs, `composite-schema/Directory.Build.props`), `REQUIRED_DOTNET_MAJOR`, and the `10|11` cases in the fusion `install.sh`. `runtime-async` must stay on exactly the variants with `"dotnet": "11"` (tested).
- JDK: the Temurin URL in the caliban and feddi `install.sh`.
- Node.js: the benchmark machine's `node`; the Node gateways' `install.sh` only installs the latest LTS via nvm when none is present.

## Bump Hot Chocolate for the subgraphs

Update `PINNED_HOTCHOCOLATE_VERSION` in both `subgraphs-net/build.sh`, every `HotChocolate*` `PackageReference` in `*/subgraphs-net/eShop.*/*.csproj`, and `PINNED_VERSION` in `tests/test_scripts_runtime.py`.

## Add a gateway

1. Create `apollo-federation/gateways/<id>/` or `composite-schema/gateways/<id>/` with `install.sh` (writes `version.txt`) and `start.sh`.
2. Add the product and its variant to `k6/benchmark-config.json`.
3. Add the variant id to the workflow_dispatch `gateway` options in `.github/workflows/benchmark.yml`, in config order (tested).
4. If the artifact contains a binary, add its `chmod +x` to the three "Restore prebuilt gateway" steps.
5. Add it to the Gateways list in `README.md`.

## Add a variant

1. Add it to the product's `variants` in `k6/benchmark-config.json`. `label` is an optional display name.
2. If it shares a gateway dir, its `install.sh` selects the variant via `BENCH_GATEWAY_CHANNEL` / `BENCH_GATEWAY_DOTNET` (see fusion).
3. Add the id to the workflow_dispatch `gateway` options.

To remove a gateway or variant, undo the same steps and delete tests that name it.

## Add a scenario

1. `k6/k6.js`: mode handling, VUs, stages / duration.
2. `k6/benchmark.sh`: mode parsing, defaults, and `BENCHMARK_SUBGRAPH_DELAY_MS` if it needs a subgraph delay.
3. `profiles.json`: CPU pinning per k6 mode.
4. `.github/workflows/benchmark.yml`: the `benchmark` input and `run_<mode>` flag, a `benchmark-<mode>` and `generate-results-<mode>` job, and add both to the `needs` (and `SCENARIO_RESULTS_JSON`) of `generate-results-json` and the `needs` of `benchmark-summary` and the `needs` and `if` of `publish-history`.
5. `k6/build-matrix.py`: per-mode exclusions in `is_excluded`.
6. `k6/generate-results.py`: the `RESULTS_<MODE>.md` filename in `main()`, `SCENARIOS`, `JSON_MODES`, and `SUBGRAPH_DELAY_MS` (must match `k6/benchmark.sh`).
