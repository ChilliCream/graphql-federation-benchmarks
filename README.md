# GraphQL Gateway Benchmarks

Performance benchmarks comparing GraphQL gateway implementations across Apollo Federation and GraphQL Federation.

**Latest Results:** [Real-World](./RESULTS_CONSTANT_LATENCY.md) | [Burst](./RESULTS_BURST.md) | [Synthetic](./RESULTS_CONSTANT.md)

## Test categories

Each benchmark runs a gateway against 4 subgraphs (`Accounts`, `Inventory`, `Products`, `Reviews`) and executes a heavy nested query. There are three test categories, each designed to measure different aspects of gateway performance:

- **Real-World** (`constant-latency`) — Shows how a gateway performs in real-world scenarios where downstream services make database calls and perform other I/O-bound work. Every downstream call adds 4 ms of latency, and the test runs with 50 concurrent VUs for 120 seconds.

- **Burst** (`burst`) — Shows how a gateway responds to rapidly increasing traffic. The benchmark holds a base load of 50 VUs for 10 seconds, ramps to 500 VUs over 40 seconds, and then ramps back to 50 VUs over 10 seconds.

- **Synthetic** (`constant`) — An artificial lab experiment that measures a gateway's theoretical throughput when downstream services make no database calls, perform no other I/O-bound work, and add no latency. This isolates gateway overhead from downstream latency. The test runs with 50 concurrent VUs for 120 seconds.

## Benchmark setup

All benchmarks run against 4 [HotChocolate](https://github.com/ChilliCream/graphql-platform) subgraphs in both
benchmark families (`apollo-federation/*` and `composite-schema/*`). The
subgraphs are pinned to HotChocolate `16.7.0` (each `subgraphs-net/build.sh`
verifies the pin and never rewrites package versions).

Each gateway gets one warmup run and 9 measured runs; the published result is
the median RPS. Before every measured run the idle machine cools down to 45 °C (or for
at most 90 seconds), because the CPU boost clock drops as it heats up and would
otherwise make each run slower than the one before.

The committed result tables under `benchmark-runs/` and the root
`RESULTS_*.md` files are historical measurements: the constant and burst
tables still contain Rust-subgraph (`async-graphql` + `axum`) rows from before
the move to HotChocolate subgraphs. Those rows are preserved as measured and are
not relabeled.

## Gateways

### Apollo Federation
- [Apollo Gateway](./apollo-federation/gateways/apollo-gateway) (Node.js)
- [Apollo Router 2](./apollo-federation/gateways/apollo-router) (Rust, latest 2.x stable; benchmark identity `apollo-router`)
- [Apollo Router 3 preview](./apollo-federation/gateways/apollo-router-v3) (Rust, latest 3.x preview; separate benchmark identity `apollo-router-v3`)
- [Caliban](./apollo-federation/gateways/caliban) (Scala)
- [Cosmo](./apollo-federation/gateways/cosmo) (Go)
- [Grafbase](./apollo-federation/gateways/grafbase) (Rust)
- [Hive Gateway](./apollo-federation/gateways/hive-gateway) (Node.js)
- [Hive Gateway Router Runtime](./apollo-federation/gateways/hive-gateway-router-runtime) (Node.js)
- [Hive Router](./apollo-federation/gateways/hive-router) (Rust)

### [GraphQL Federation](https://graphql.github.io/graphql-federation-spec/)
- [Fusion](./composite-schema/gateways/fusion) (.NET) — benchmarked as four stable variants: `fusion-net-11` (.NET 11 JIT with runtime-async), `fusion-aot-11` (.NET 11 Native AOT), plus the federation-composition counterparts `fusion-fed-net-11`, `fusion-fed-aot-11` (built from [fusion-fed](./apollo-federation/gateways/fusion-fed)). When a HotChocolate preview newer than the latest stable exists, the same four builds also run as `fusion-nightly-net-11`, `fusion-nightly-aot-11`, `fusion-nightly-fed-net-11` and `fusion-nightly-fed-aot-11`.
- [feddi-gateway](./composite-schema/gateways/feddi-gateway) (JVM) by [feddi](https://feddi.dev) — built from the open-source repository ([feddi-dev/feddi-gateway](https://github.com/feddi-dev/feddi-gateway), Apache 2.0) at a pinned commit. See its [README](./composite-schema/gateways/feddi-gateway/README.md) for setup.

Version pins and upstream changes for the latest refresh are listed in [Gateway version updates](./GATEWAY_UPDATES.md). Apollo Router 2 and Router 3 preview have independent installs, artifacts, and result rows; both run when `all` is selected, or select `apollo-router` / `apollo-router-v3` individually.

## Running benchmarks locally

### Prerequisites

- **k6**
- **jq** - required by the monitor script
- **python3** - used for JSON parsing
- **curl** - used for health checks
- **bash**, **taskset** (optional, Linux only for pinning)
- Gateway dependencies are handled by each gateway's `install.sh`

### Run

```bash
./k6/benchmark.sh <gateway-path> [subgraphs-dir] [constant|constant-latency|burst|ramping]
```

Examples:

```bash
# composite-schema + HotChocolate subgraphs (default)
./k6/benchmark.sh composite-schema/gateways/fusion

# apollo-federation + HotChocolate subgraphs (default)
./k6/benchmark.sh apollo-federation/gateways/apollo-router

# burst mode
./k6/benchmark.sh apollo-federation/gateways/cosmo burst

# constant-latency mode (HotChocolate subgraphs with simulated 4ms IO delay)
./k6/benchmark.sh apollo-federation/gateways/grafbase constant-latency
```

### What happens

1. Resolves subgraph directory (`subgraphs-net`)
2. Builds subgraphs (`subgraphs-net/build.sh`, which bundles the .NET SDK into the subgraphs directory so the prebuilt artifact carries its own runtime) unless `USE_PREBUILT_SUBGRAPHS=1`
3. Installs/builds gateway (`gateway/install.sh`) unless `USE_PREBUILT_GATEWAY=1`
4. Starts subgraphs and gateway (optionally CPU-pinned)
5. Executes one full-duration warmup run (discarded)
6. Executes measured runs (`BENCH_RUNS`, default `9`), with a CPU cooldown (`k6/wait-cooldown.sh`) before each one
7. Captures monitor + k6 summaries for each run
8. Prints run statistics (median/mean/CV and CPU usage medians)

### Configuration

Environment variables:

| Variable | Default | Description |
|---|---|---|
| `MEASURE_SECONDS` | `120` (constant) / `60` (burst) | Benchmark measurement duration |
| `BENCH_RUNS` | `9` | Measured runs (plus one warmup run) |
| `BENCH_COOLDOWN_TARGET_C` | `45` | CPU temperature (°C) to cool down to before each measured run |
| `BENCH_COOLDOWN_MAX_S` | `90` | Longest cooldown before each measured run, in seconds (`0` disables the cooldown) |
| `BENCH_VUS` | `50` constant / `500` burst | VU target passed to `k6/k6.js` |
| `BENCH_DISPLAY_NAME` | _(auto)_ | Override report display name |
| `BENCH_GATEWAY_NAME` | _(auto)_ | Override gateway identity in result metadata (used to split stable vs preview rows) |
| `BENCH_GATEWAY_CHANNEL` | `stable` | HotChocolate package channel for `fusion`'s `install.sh` (`stable` = latest stable packages; `preview` = latest preview/nightly packages) |
| `BENCH_GATEWAY_DOTNET` | `10` | .NET runtime/target for `fusion`'s `install.sh` (`10` = bundled .NET 10 SDK, targets net10.0; `11` = bundled .NET 11 preview SDK, targets net11.0 with runtime-async) |
| `BENCH_SUBGRAPH_TECH` | _(auto)_ | Subgraph tech label recorded in result metadata (`.net`) |
| `USE_PREBUILT_SUBGRAPHS` | `0` | Skip `build.sh` and expect prebuilt subgraph artifact (with bundled .NET runtime and apphosts; fails on benchmark machines without it — no local rebuild fallback) |
| `USE_PREBUILT_GATEWAY` | `0` | Skip `install.sh` and expect prebuilt gateway artifact |

### CPU pinning

On Linux with `taskset`, `profiles.json` is used to pin:
- `system`
- `k6`
- `gateway`
- `subgraphs`

Profile selection is based on logical core count (8 or 16 profile).

### Output

Each run produces a timestamped results directory:

```text
<gateway-dir>/results/<timestamp>/
  data.csv          # monitor time series
  metadata.json     # gateway/subgraph/machine metadata, cooldown, CPU temp and avg clock
  memory.json       # idle/peak/end RSS + avg core usage (k6/subgraphs)
  k6_summary.json   # full k6 metrics (machine-readable)
  k6_summary.txt    # k6 summary (human-readable)
```

## GitHub Actions workflow

Workflow: [benchmark.yml](./.github/workflows/benchmark.yml)

- Triggers:
  - `workflow_dispatch`
  - scheduled daily at `21:00 UTC`
- Dynamic matrix (`k6/build-matrix.py`):
  - Builds gateway matrix from selected input
  - Each gateway runs against the HotChocolate subgraphs (`subgraphs-net`)
- Build stages on `ubuntu-latest`:
  - `build-subgraphs` (prebuilt artifacts, each bundling its own .NET runtime)
  - `build-gateways` (prebuilt artifacts)
- Benchmark stages on the dedicated `benchmark-runners` runner group:
  - `benchmark-constant-latency` (4ms simulated IO delay)
  - `benchmark-constant` (runs after constant-latency completes)
  - `benchmark-burst` (runs after constant completes)
- Result generation:
  - `generate-results-constant-latency`
  - `generate-results-constant`
  - `generate-results-burst`
  - `generate-results-json` (`benchmark-runs/<run>/results.json`)
  - `publish-history` (scheduled runs only: `benchmark-runs/history.json`)
  - final `benchmark-summary` job publishes all result docs in the run summary
- Result documents are committed back to the branch by the generator jobs

## Acknowledgments

This benchmark repository is based on the work by [The Guild](https://the-guild.dev/) on [graphql-gateways-benchmark](https://github.com/graphql-hive/graphql-gateways-benchmark).
