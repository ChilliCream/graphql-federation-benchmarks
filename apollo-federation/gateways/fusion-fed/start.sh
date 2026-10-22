#!/usr/bin/env bash
set -Eeuo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

cd "$SCRIPT_DIR/eShop.Gateway"
export ASPNETCORE_ENVIRONMENT=Production

# Native AOT selection: install.sh publishes the ahead-of-time binary to a
# controlled `-o` publish dir (bin/Release/net11.0/publish), so the location
# does not depend on the build RID — publish's default output qualifies the
# path with the RID (bin/Release/net11.0/<rid>/publish) and must not be
# guessed here. BENCH_GATEWAY_AOT=1 requires the native binary and fails
# closed when it is missing: silently measuring the JIT build instead would
# invalidate the AOT variants. Otherwise the native binary is preferred when
# present and the JIT build is the fallback.
AOT="${BENCH_GATEWAY_AOT:-0}"
case "$AOT" in
  0|1) ;;
  *)
    echo "ERROR: unknown BENCH_GATEWAY_AOT='$AOT' (expected '0' or '1')" >&2
    exit 1
    ;;
esac

# `dotnet run` applies Properties/launchSettings.json, but a directly executed
# binary (the Native AOT publish output below) does not — replicate the http
# profile's applicationUrl via ASPNETCORE_URLS so the gateway binds the port
# the benchmark polls (settings.json points at http://localhost:5220). A
# missing URL fails closed instead of binding Kestrel's default port.
# Mirrors subgraphs-net/start.sh.
GATEWAY_URL="$(python3 - "$SCRIPT_DIR/eShop.Gateway/Properties/launchSettings.json" <<'PY'
import json
import sys

with open(sys.argv[1], encoding="utf-8-sig") as fh:
    profiles = json.load(fh).get("profiles", {})
url = profiles.get("http", {}).get("applicationUrl", "")
print(url.split(";")[0].strip())
PY
)"
if [[ -z "$GATEWAY_URL" ]]; then
  echo "ERROR: no http applicationUrl in $SCRIPT_DIR/eShop.Gateway/Properties/launchSettings.json" >&2
  exit 1
fi
export ASPNETCORE_URLS="$GATEWAY_URL"

NATIVE_BINARY=""
for candidate in \
  "$SCRIPT_DIR/eShop.Gateway/bin/Release/net11.0/publish/eShop.Gateway" \
  "$SCRIPT_DIR/eShop.Gateway/bin/Release/net11.0/publish/eShop.Gateway.exe"; do
  if [[ -x "$candidate" && ! -d "$candidate" ]]; then
    NATIVE_BINARY="$candidate"
    break
  fi
done

if [[ "$AOT" == "1" && -z "$NATIVE_BINARY" ]]; then
  echo "ERROR: BENCH_GATEWAY_AOT=1 but no Native AOT binary at $SCRIPT_DIR/eShop.Gateway/bin/Release/net11.0/publish/eShop.Gateway - run install.sh with BENCH_GATEWAY_DOTNET=11 BENCH_GATEWAY_AOT=1 first" >&2
  exit 1
fi

if [[ -n "$NATIVE_BINARY" ]]; then
  exec "$NATIVE_BINARY" > "$SCRIPT_DIR/gateway_log.txt" 2>&1
fi

# install.sh bundles the SDK this build was made for into the artifact, so the
# gateway runs on its intended runtime regardless of what the benchmark machine
# has installed. A missing bundle means a broken artifact: falling back to the
# system dotnet would silently benchmark a different runtime, so fail instead.
if [[ ! -x "$SCRIPT_DIR/.dotnet/dotnet" ]]; then
  echo "ERROR: no bundled .NET SDK at $SCRIPT_DIR/.dotnet/dotnet - run install.sh in $SCRIPT_DIR first" >&2
  exit 1
fi

export DOTNET_ROOT="$SCRIPT_DIR/.dotnet"
export PATH="$SCRIPT_DIR/.dotnet:$PATH"

exec dotnet run -c Release --no-build --no-restore > "$SCRIPT_DIR/gateway_log.txt" 2>&1
