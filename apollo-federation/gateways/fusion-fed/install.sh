#!/usr/bin/env bash
set -Eeuo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# The Fusion gateway is benchmarked along three independent axes:
#
#   BENCH_GATEWAY_CHANNEL  which HotChocolate NuGet packages to build against
#                          stable  = latest non-prerelease (default)
#                          preview = newest prerelease (the latest nightly)
#
#   BENCH_GATEWAY_VERSION  exact HotChocolate version to build against instead
#                          of resolving the latest for the channel above
#                          (empty = resolve latest per channel; when set, the
#                          channel is ignored)
#
#   BENCH_GATEWAY_DOTNET   which .NET runtime / target framework to build and run on
#                          10 = bundled latest GA .NET 10 SDK, targets net10.0 (legacy)
#                          11 = bundled latest .NET 11 preview SDK, targets net11.0
#                               with runtime-async opted in (default)
#
#   BENCH_GATEWAY_AOT      0 = framework-dependent JIT build (default)
#                          1 = Native AOT publish on the selected .NET target
#                              (only supported with BENCH_GATEWAY_DOTNET=11;
#                              bench.props sets PublishAot and install.sh runs
#                              `dotnet publish -o` to a controlled publish dir
#                              in addition to the JIT build, so the artifact
#                              carries both outputs at a RID-independent path
#                              and start.sh prefers the native binary when
#                              present — and fails closed for AOT=1 when the
#                              native binary is absent)
#
# Both targets bundle their own SDK inside the gateway directory, so the runtime
# is a property of the prebuilt artifact rather than of the machine running it.
#
# Current benchmark variants use .NET 11; .NET 10 remains supported for older builds.
# This directory hosts the apollo-federation (fed) variants; the composite-schema
# (non-fed) variants share the same axes from composite-schema/gateways/fusion:
#   fusion-fed-net-11            = stable  packages on .NET 11 JIT + runtime-async
#   fusion-fed-aot-11            = stable  packages on .NET 11 Native AOT
#   fusion-nightly-fed-net-11    = preview packages on .NET 11 JIT + runtime-async
#   fusion-nightly-fed-aot-11    = preview packages on .NET 11 Native AOT
# (plus the four fusion-net-* / fusion-nightly-* counterparts).

# --- Resolve the HotChocolate package channel --------------------------------
CHANNEL="${BENCH_GATEWAY_CHANNEL:-stable}"
case "$CHANNEL" in
  stable|preview) ;;
  *)
    echo "ERROR: unknown BENCH_GATEWAY_CHANNEL='$CHANNEL' (expected 'stable' or 'preview')"
    exit 1
    ;;
esac

# --- Validate explicit HotChocolate version override ---------------------------
# BENCH_GATEWAY_VERSION pins the exact HotChocolate version instead of
# resolving the latest for BENCH_GATEWAY_CHANNEL. Validated here — before the
# SDK download — so garbage fails fast without touching the network.
# tests/test_scripts_runtime.py executes this block standalone against
# good/bad BENCH_GATEWAY_VERSION values; keep it self-contained.
# --- Validate explicit HotChocolate version override: begin ---
PINNED_VERSION="${BENCH_GATEWAY_VERSION:-}"
if [[ -n "$PINNED_VERSION" ]]; then
  if [[ ! "$PINNED_VERSION" =~ ^[0-9]+\.[0-9]+\.[0-9]+(-[0-9A-Za-z-]+(\.[0-9A-Za-z-]+)*)?$ ]]; then
    echo "ERROR: invalid BENCH_GATEWAY_VERSION='$PINNED_VERSION' (expected numeric X.Y.Z with optional prerelease suffix, e.g. '16.6.8' or '16.7.0-p.27')"
    exit 1
  fi
  echo "Using pinned HotChocolate version $PINNED_VERSION (channel '$CHANNEL' ignored)."
fi
# --- Validate explicit HotChocolate version override: end ---

# --- Resolve the .NET runtime / target framework -----------------------------
DOTNET_TARGET="${BENCH_GATEWAY_DOTNET:-11}"
case "$DOTNET_TARGET" in
  10|11) ;;
  *)
    echo "ERROR: unknown BENCH_GATEWAY_DOTNET='$DOTNET_TARGET' (expected '10' or '11')"
    exit 1
    ;;
esac

# --- Resolve Native AOT publish ------------------------------------------------
AOT="${BENCH_GATEWAY_AOT:-0}"
case "$AOT" in
  0|1) ;;
  *)
    echo "ERROR: unknown BENCH_GATEWAY_AOT='$AOT' (expected '0' or '1')"
    exit 1
    ;;
esac
if [[ "$AOT" == "1" && "$DOTNET_TARGET" != "11" ]]; then
  echo "ERROR: BENCH_GATEWAY_AOT=1 requires BENCH_GATEWAY_DOTNET=11 (AOT variants are .NET 11 only)"
  exit 1
fi

# --- Target-specific build inputs --------------------------------------------
# The benchmark machine runs the *prebuilt* artifact and never executes this
# script, so the artifact itself must carry the runtime it is meant to be
# measured on — otherwise whatever SDK happens to be installed on the machine
# would silently decide the result. Every target therefore installs its own SDK
# *inside* the gateway directory, where it travels with the artifact:
#   10 = latest GA .NET 10 SDK,      gateway targets net10.0
#   11 = latest .NET 11 preview SDK, gateway targets net11.0 + runtime-async
#
# Generated here (all gitignored):
#   - $SCRIPT_DIR/.dotnet            bundled SDK (start.sh requires it at launch)
#   - $SCRIPT_DIR/global.json        pins the bundled SDK (overrides the repo-root
#                                    global.json, which pins .NET 10 / latestMinor)
#   - eShop.Gateway/bench.props      generated only when needed (imported by the
#                                    csproj only when present): net11 retarget +
#                                    runtime-async for the .NET 11 target,
#                                    PublishAot for BENCH_GATEWAY_AOT=1, and
#                                    FUSION_16_7_OR_GREATER when the resolved
#                                    HotChocolate version is 16.7 or greater
BUNDLED_DOTNET_DIR="$SCRIPT_DIR/.dotnet"
GATEWAY_GLOBAL_JSON="$SCRIPT_DIR/global.json"
BENCH_PROPS="$SCRIPT_DIR/eShop.Gateway/bench.props"

if [[ "$DOTNET_TARGET" == "11" ]]; then
  # .NET 11 has no GA release yet, so the preview quality band is the only source.
  DOTNET_INSTALL_ARGS=(--channel 11.0 --quality preview)
  ALLOW_PRERELEASE=true
else
  # No --quality: dotnet-install.sh then resolves the latest GA patch of the band.
  DOTNET_INSTALL_ARGS=(--channel 10.0)
  ALLOW_PRERELEASE=false
fi

# --- Install the target SDK, bundled into the gateway dir --------------------
# Clear the previous target's generated inputs up front, before anything that can
# fail: a download that dies half way then leaves a neutral tree instead of one
# whose global.json pins an SDK that is no longer installed and whose bench.props
# still carries the other target's settings. global.json is rewritten below on
# success; bench.props is regenerated after the HotChocolate version resolves.
# CI uses fresh checkouts; local runs may reuse the tree.
echo "Installing the .NET $DOTNET_TARGET SDK into $BUNDLED_DOTNET_DIR ..."
rm -rf "$BUNDLED_DOTNET_DIR"
rm -f "$GATEWAY_GLOBAL_JSON" "$BENCH_PROPS"
curl -sSL https://dot.net/v1/dotnet-install.sh \
  | bash -s -- "${DOTNET_INSTALL_ARGS[@]}" --install-dir "$BUNDLED_DOTNET_DIR"

export DOTNET_ROOT="$BUNDLED_DOTNET_DIR"
export PATH="$BUNDLED_DOTNET_DIR:$PATH"
DOTNET="$BUNDLED_DOTNET_DIR/dotnet"

# --list-sdks ignores global.json and (with multi-level lookup off) only lists
# SDKs in the bundled dir, so this is the version we actually installed.
SDK_VERSION="$("$DOTNET" --list-sdks | awk '{print $1}' | sort -V | tail -n1)"
SDK_MAJOR="${SDK_VERSION%%.*}"
if [[ "$SDK_MAJOR" != "$DOTNET_TARGET" ]]; then
  echo "ERROR: target .NET $DOTNET_TARGET requires a .NET $DOTNET_TARGET SDK but installed '${SDK_VERSION:-none}'"
  exit 1
fi
echo "Bundled .NET SDK: $SDK_VERSION"

# Pin the bundled SDK so the selected runtime is used at build *and* run time.
# The repo-root global.json pins .NET 10 with rollForward=latestMinor, which
# would otherwise steer SDK resolution here — a nearer global.json takes
# precedence.
cat > "$GATEWAY_GLOBAL_JSON" <<EOF
{
  "sdk": {
    "version": "$SDK_VERSION",
    "rollForward": "latestMinor",
    "allowPrerelease": $ALLOW_PRERELEASE
  }
}
EOF

# NOTE: eShop.Gateway/bench.props is (re)generated below, after the HotChocolate
# version is resolved — its contents depend on both the .NET target and the
# resolved package version.

if [[ -n "$PINNED_VERSION" ]]; then
  SELECTED_VERSION="$PINNED_VERSION"
else
  echo "Fetching latest $CHANNEL HotChocolate version from NuGet..."
  SELECTED_VERSION=$(curl -s "https://api.nuget.org/v3-flatcontainer/hotchocolate.aspnetcore/index.json" \
    | CHANNEL="$CHANNEL" python3 -c '
# --- Resolve latest HotChocolate version for channel: begin ---
import json, os, sys

channel = os.environ["CHANNEL"]
versions = json.load(sys.stdin).get("versions", [])


def parse_core(core):
    nums = []
    for part in core.split("."):
        if not part.isdigit():
            return None
        nums.append(int(part))
    return tuple(nums)


def prerelease_key(pre):
    # SemVer 2.0 precedence: numeric identifiers compare numerically and rank
    # below alphanumeric identifiers; a shorter identifier set ranks lower when
    # all preceding identifiers are equal.
    key = []
    for ident in pre.split("."):
        if ident.isdigit():
            key.append((0, int(ident), ""))
        else:
            key.append((1, 0, ident))
    return tuple(key)


candidates = []
for raw in versions:
    core, sep, pre = raw.partition("-")
    core_tuple = parse_core(core)
    if core_tuple is None:
        continue
    is_pre = bool(sep)
    if channel == "stable" and is_pre:
        continue
    if channel == "preview" and not is_pre:
        continue
    sort_key = (core_tuple, prerelease_key(pre) if is_pre else ())
    candidates.append((sort_key, raw))

if not candidates:
    sys.exit(0)

candidates.sort(key=lambda item: item[0])
print(candidates[-1][1])
# --- Resolve latest HotChocolate version for channel: end ---
')
fi

if [[ -z "$SELECTED_VERSION" ]]; then
  echo "ERROR: Could not determine latest $CHANNEL HotChocolate version"
  exit 1
fi

echo "Selected HotChocolate version: $SELECTED_VERSION (channel: $CHANNEL)"

# --- Update HotChocolate package versions in gateway .csproj ---
echo "Updating HotChocolate* package references to $SELECTED_VERSION..."
for csproj in "$SCRIPT_DIR"/*/*.csproj; do
  if [ -f "$csproj" ] && grep -q 'Include="HotChocolate' "$csproj"; then
    sed -i.bak -E 's/(Include="HotChocolate[^"]*" Version=")[^"]+(")/\1'"$SELECTED_VERSION"'\2/g' "$csproj"
    rm -f "$csproj.bak"
    echo "  Updated: $(basename "$(dirname "$csproj")")/$(basename "$csproj")"
  fi
done

# --- Generate eShop.Gateway/bench.props (gitignored) ---------------------------
# Imported by eShop.Gateway.csproj only when present, so a plain `dotnet build`
# without install.sh (stable pins below 16.7) compiles with no extra settings
# and the ModifyCostOptions call in Program.cs compiled out. Contents depend on
# the benchmark axes:
#   - .NET 11 target: retarget the gateway to net11.0 and opt into .NET 11
#     runtime-async, clearing the plural TargetFrameworks inherited from
#     Directory.Build.props. A multi-targeted (outer/inner dispatch) build
#     never engages the Native AOT compiler on publish, silently yielding a
#     JIT-only artifact even for BENCH_GATEWAY_AOT=1 (which start.sh then
#     refuses to run); an empty plural plus the singular TargetFramework
#     gives a plain single-targeted net11.0 build for both JIT and AOT.
#     runtime-async replaces compiler-generated async state
#     machines with the runtime-provided async feature. Since .NET 11 Preview 3
#     the feature switch alone is enough — the [RequiresPreviewFeatures] gate
#     was removed, so <EnablePreviewFeatures> is intentionally NOT set (we
#     always install the latest preview SDK, so the modern opt-in always
#     applies). Scope: this flag only affects async methods compiled in THIS
#     project (eShop.Gateway); the prebuilt HotChocolate packages must be
#     compiled with runtime-async=on upstream to exercise it through
#     HotChocolate's execution pipeline.
#   - BENCH_GATEWAY_AOT=1: set PublishAot so `dotnet publish -o` emits a native
#     binary to a controlled publish dir (the csproj already sets
#     IsAotCompatible). The JIT build is still produced first so the artifact
#     carries the single TFM dir benchmark.sh expects; start.sh prefers the
#     native publish output when present and fails closed for AOT=1 when it
#     is absent. Publishing with `-o` (instead of publish's default output)
#     keeps the path RID-independent: the default qualifies it with the build
#     RID (bin/Release/net11.0/<rid>/publish), which start.sh must not guess.
#   - HotChocolate 16.7 or greater: define FUSION_16_7_OR_GREATER so Program.cs
#     compiles in the ModifyCostOptions call that disables gateway-side cost
#     enforcement. The major.minor comparison is numeric, so 16.7 previews
#     count and so does 16.10+.
# A .NET 10 JIT build against HotChocolate below 16.7 needs none of these, so
# no file is written and the csproj import stays dormant.
VERSION_CORE="${SELECTED_VERSION%%-*}"
VERSION_MAJOR="${VERSION_CORE%%.*}"
VERSION_TAIL="${VERSION_CORE#*.}"
VERSION_MINOR="${VERSION_TAIL%%.*}"
FUSION_COST_DEFINE=""
if [[ "$VERSION_MAJOR" =~ ^[0-9]+$ && "$VERSION_MINOR" =~ ^[0-9]+$ ]] \
  && (( VERSION_MAJOR > 16 || (VERSION_MAJOR == 16 && VERSION_MINOR >= 7) )); then
  FUSION_COST_DEFINE="FUSION_16_7_OR_GREATER"
fi

# tests/test_scripts_runtime.py executes this block standalone for each
# benchmark axis combination; keep it self-contained (inputs: DOTNET_TARGET,
# AOT, FUSION_COST_DEFINE, BENCH_PROPS).
# --- Generate bench.props: begin ---
if [[ "$DOTNET_TARGET" == "11" || "$AOT" == "1" || -n "$FUSION_COST_DEFINE" ]]; then
  {
    echo '<Project>'
    echo '  <PropertyGroup>'
    if [[ "$DOTNET_TARGET" == "11" ]]; then
      echo '    <TargetFramework>net11.0</TargetFramework>'
      echo '    <!-- Clear the plural TargetFrameworks inherited from'
      echo '         Directory.Build.props (see above): an empty plural plus the'
      echo '         singular TargetFramework keeps the build single-targeted. -->'
      echo '    <TargetFrameworks></TargetFrameworks>'
      echo '    <Features>$(Features);runtime-async=on</Features>'
    fi
    if [[ "$AOT" == "1" ]]; then
      echo '    <PublishAot>true</PublishAot>'
    fi
    if [[ -n "$FUSION_COST_DEFINE" ]]; then
      echo "    <DefineConstants>\$(DefineConstants);${FUSION_COST_DEFINE}</DefineConstants>"
    fi
    echo '  </PropertyGroup>'
    echo '</Project>'
  } > "$BENCH_PROPS"
  echo "Generated bench.props (dotnet: $DOTNET_TARGET, aot: $AOT, cost define: ${FUSION_COST_DEFINE:-none})."
fi
# --- Generate bench.props: end ---

# --- Build ---
# `dotnet build` never removes another target framework's output, so a reused
# tree that was last built for a different BENCH_GATEWAY_DOTNET would keep that
# stale TFM directory around. The benchmark machine derives the runtime the
# artifact expects from the TFM directory under bin/Release, so leave exactly one.
GATEWAY_BIN_DIR="$SCRIPT_DIR/eShop.Gateway/bin/Release"
if [[ -d "$GATEWAY_BIN_DIR" ]]; then
  find "$GATEWAY_BIN_DIR" -mindepth 1 -maxdepth 1 -type d -name 'net*' \
    ! -name "net${DOTNET_TARGET}.0" -exec rm -rf {} +
fi

# Native AOT publish target: a controlled `-o` dir rather than publish's
# default, which qualifies the path with the build RID
# (bin/Release/net11.0/<rid>/publish) so start.sh could never address it
# directly and would silently fall back to the JIT build. Cleared on every
# build so a JIT rebuild never inherits a stale native binary; recreated by
# `dotnet publish` only for BENCH_GATEWAY_AOT=1.
AOT_PUBLISH_DIR="$SCRIPT_DIR/eShop.Gateway/bin/Release/net${DOTNET_TARGET}.0/publish"
rm -rf "$AOT_PUBLISH_DIR"

echo "Building Fusion gateway ($CHANNEL channel, .NET $DOTNET_TARGET, AOT=$AOT)..."
cd "$SCRIPT_DIR/eShop.Gateway" && "$DOTNET" build -c Release --nologo -v quiet

if [[ "$AOT" == "1" ]]; then
  echo "Publishing Fusion gateway as Native AOT (.NET $DOTNET_TARGET)..."
  cd "$SCRIPT_DIR/eShop.Gateway" && "$DOTNET" publish -c Release --nologo -v quiet -o "$AOT_PUBLISH_DIR"
fi

echo "$SELECTED_VERSION" > "$SCRIPT_DIR/version.txt"
echo "Fusion gateway build complete (channel: $CHANNEL, dotnet: $DOTNET_TARGET, aot: $AOT, version: $SELECTED_VERSION)."
