#!/usr/bin/env bash
set -Eeuo pipefail

# =============================================================================
# install.sh — Install the feddi Gateway (https://feddi.dev / feddi-dev/feddi-gateway)
#
# feddi Gateway is a JVM-native GraphQL federation gateway built on
# GraphQL Java. This script installs a released distribution from feddi.dev:
#
#   1. Bundle a JDK 25 into ./.jdk (feddi Gateway requires Java 25+). Bundling — rather
#      than relying on a system JDK — keeps the runtime reproducible and lets the
#      built artifact travel for prebuilt-gateway runs (start.sh prefers ./.jdk).
#   2. Resolve the release: the latest one (from feddi.dev/releases/latest/manifest.json),
#      or the exact version in BENCH_GATEWAY_VERSION (calver YYYY-MM-DD-HHMM).
#   3. Download that release's distribution ZIP, check it against the sha256 in the
#      release manifest, and extract it to ./dist (./dist/feddi-gateway/bin/feddi-gateway
#      + app.jar).
#   4. Refresh the subgraph SDLs and assemble ./subgraphs.zip from ./subgraph-config
#      (uploaded by start.sh).
#
# feddi.dev keeps the newest releases (at least the last 10 and all of the last 30
# days), so an older BENCH_GATEWAY_VERSION may no longer be downloadable.
#
# The script is idempotent: an already-present valid JDK / distribution is reused.
# =============================================================================

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

RELEASES_URL="https://feddi.dev/releases"

JDK_DIR="$SCRIPT_DIR/.jdk"
DIST_DIR="$SCRIPT_DIR/dist"
DIST_VERSION_FILE="$DIST_DIR/.feddi-gateway-version"

# --- 1. Ensure a bundled JDK 25 ----------------------------------------------

jdk_java_home() {
  # Temurin tarballs extract to <java_home> on Linux and <home>/Contents/Home on macOS.
  if [[ -x "$JDK_DIR/bin/java" ]]; then
    echo "$JDK_DIR"
  elif [[ -x "$JDK_DIR/Contents/Home/bin/java" ]]; then
    echo "$JDK_DIR/Contents/Home"
  fi
}

jdk_is_25() {
  local jh="$1"
  [[ -n "$jh" && -x "$jh/bin/java" ]] || return 1
  local major
  major="$("$jh/bin/java" -version 2>&1 | head -1 | sed -E 's/.*version "([0-9]+).*/\1/')"
  [[ "$major" == "25" ]]
}

JAVA_HOME_LOCAL="$(jdk_java_home || true)"
if jdk_is_25 "$JAVA_HOME_LOCAL"; then
  echo "Bundled JDK already present: $("$JAVA_HOME_LOCAL/bin/java" -version 2>&1 | head -1)"
else
  case "$(uname -s)" in
    Linux)  JDK_OS="linux" ;;
    Darwin) JDK_OS="mac" ;;
    *) echo "ERROR: unsupported OS for JDK download: $(uname -s)"; exit 1 ;;
  esac
  case "$(uname -m)" in
    x86_64|amd64)  JDK_ARCH="x64" ;;
    arm64|aarch64) JDK_ARCH="aarch64" ;;
    *) echo "ERROR: unsupported arch for JDK download: $(uname -m)"; exit 1 ;;
  esac

  JDK_URL="https://api.adoptium.net/v3/binary/latest/25/ga/${JDK_OS}/${JDK_ARCH}/jdk/hotspot/normal/eclipse"
  echo "Downloading Temurin JDK 25 ($JDK_OS/$JDK_ARCH) ..."
  rm -rf "$JDK_DIR"
  mkdir -p "$JDK_DIR"
  TMP_TGZ="$SCRIPT_DIR/.jdk.tar.gz"
  curl -fSL "$JDK_URL" -o "$TMP_TGZ"
  tar -xzf "$TMP_TGZ" -C "$JDK_DIR" --strip-components=1
  rm -f "$TMP_TGZ"

  JAVA_HOME_LOCAL="$(jdk_java_home || true)"
  if ! jdk_is_25 "$JAVA_HOME_LOCAL"; then
    echo "ERROR: bundled JDK is not a usable Java 25 (got: ${JAVA_HOME_LOCAL:-none})"
    exit 1
  fi
  echo "Bundled JDK: $("$JAVA_HOME_LOCAL/bin/java" -version 2>&1 | head -1)"
fi

export JAVA_HOME="$JAVA_HOME_LOCAL"
export PATH="$JAVA_HOME/bin:$PATH"

# --- 2. Resolve the feddi release ---------------------------------------------

# Prints the value of a top-level or nested key path from a JSON document on stdin.
json_value() {
  python3 -c 'import json, sys
value = json.load(sys.stdin)
for key in sys.argv[1:]:
    value = value[key]
print(value)' "$@"
}

FEDDI_GATEWAY_VERSION="${BENCH_GATEWAY_VERSION:-}"
if [[ -z "$FEDDI_GATEWAY_VERSION" ]]; then
  echo "Resolving the latest feddi release ..."
  FEDDI_GATEWAY_VERSION="$(curl -fsSL "$RELEASES_URL/latest/manifest.json" | json_value version)"
fi
if [[ ! "$FEDDI_GATEWAY_VERSION" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}-[0-9]{4}$ ]]; then
  echo "ERROR: feddi release version '$FEDDI_GATEWAY_VERSION' is not calver YYYY-MM-DD-HHMM"
  exit 1
fi
echo "feddi release: $FEDDI_GATEWAY_VERSION"

# --- 3. Download, verify and extract the distribution ------------------------

dist_is_complete() {
  [[ -x "$DIST_DIR/feddi-gateway/bin/feddi-gateway" ]] && [[ -f "$DIST_DIR/feddi-gateway/app.jar" ]]
}

if dist_is_complete && [[ "$(cat "$DIST_VERSION_FILE" 2>/dev/null || true)" == "$FEDDI_GATEWAY_VERSION" ]]; then
  echo "feddi Gateway $FEDDI_GATEWAY_VERSION already extracted in $DIST_DIR"
else
  DOWNLOAD_DIR="$(mktemp -d)"
  trap 'rm -rf "$DOWNLOAD_DIR"' EXIT

  # Download the versioned manifest and ZIP (not latest/), so a release published
  # meanwhile can't mix versions.
  if ! curl -fsSL "$RELEASES_URL/$FEDDI_GATEWAY_VERSION/manifest.json" -o "$DOWNLOAD_DIR/manifest.json"; then
    echo "ERROR: feddi release $FEDDI_GATEWAY_VERSION not found at $RELEASES_URL (older releases are pruned)"
    exit 1
  fi
  EXPECTED_SHA256="$(json_value sha256 gateway < "$DOWNLOAD_DIR/manifest.json")"

  echo "Downloading feddi Gateway $FEDDI_GATEWAY_VERSION ..."
  curl -fSL "$RELEASES_URL/$FEDDI_GATEWAY_VERSION/gateway" -o "$DOWNLOAD_DIR/feddi-gateway.zip"

  if command -v sha256sum >/dev/null 2>&1; then
    ACTUAL_SHA256="$(sha256sum "$DOWNLOAD_DIR/feddi-gateway.zip" | cut -d' ' -f1)"
  else
    ACTUAL_SHA256="$(shasum -a 256 "$DOWNLOAD_DIR/feddi-gateway.zip" | cut -d' ' -f1)"
  fi
  if [[ "$ACTUAL_SHA256" != "$EXPECTED_SHA256" ]]; then
    echo "ERROR: feddi-gateway.zip sha256 $ACTUAL_SHA256 does not match the release manifest ($EXPECTED_SHA256)"
    exit 1
  fi

  echo "Extracting distribution to $DIST_DIR ..."
  rm -rf "$DIST_DIR"
  mkdir -p "$DIST_DIR"
  unzip -q "$DOWNLOAD_DIR/feddi-gateway.zip" -d "$DIST_DIR"

  if ! dist_is_complete; then
    echo "ERROR: extracted distribution is incomplete in $DIST_DIR"
    exit 1
  fi
  echo "$FEDDI_GATEWAY_VERSION" > "$DIST_VERSION_FILE"
fi

# --- 4. Refresh subgraph SDLs from the canonical .NET source schemas ---------
#
# feddi Gateway composes from subgraph-config/<name>/schema.graphqls. Rather than keep
# hand-maintained copies (which silently drift from the subgraphs the benchmark
# actually runs), copy the canonical HotChocolate exports straight in. Since
# HotChocolate 16.3+ emits @key(fields:…) on entities natively, the raw export
# composes in feddi Gateway as-is — no directive trimming needed. Each subgraph's
# config.yaml (the feddi Gateway specific subgraph URL) stays source-controlled; only the
# .graphqls SDL is generated here.

SUBGRAPHS_NET="$SCRIPT_DIR/../../subgraphs-net"
SUBGRAPH_MAP=(
  "accounts:eShop.Accounts"
  "inventory:eShop.Inventory"
  "products:eShop.Products"
  "reviews:eShop.Reviews"
)
echo "Refreshing subgraph SDLs from $SUBGRAPHS_NET ..."
for entry in "${SUBGRAPH_MAP[@]}"; do
  name="${entry%%:*}"
  proj="${entry##*:}"
  src="$SUBGRAPHS_NET/$proj/schema.graphql"
  dst="$SCRIPT_DIR/subgraph-config/$name/schema.graphqls"
  if [[ ! -f "$src" ]]; then
    echo "ERROR: canonical subgraph schema not found: $src"
    exit 1
  fi
  cp "$src" "$dst"
  echo "  $proj/schema.graphql -> subgraph-config/$name/schema.graphqls"
done

# --- 5. Assemble the subgraph-definition ZIP (uploaded by start.sh) ----------

echo "Assembling subgraphs.zip from subgraph-config/ ..."
rm -f "$SCRIPT_DIR/subgraphs.zip"
( cd "$SCRIPT_DIR/subgraph-config" && zip -qr "$SCRIPT_DIR/subgraphs.zip" . )

# --- 6. Record version -------------------------------------------------------

echo "$FEDDI_GATEWAY_VERSION" > "$SCRIPT_DIR/version.txt"
echo "feddi Gateway install complete (version: $FEDDI_GATEWAY_VERSION)."
