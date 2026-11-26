#!/usr/bin/env bash
set -Eeuo pipefail

# Nitro Router is released with the HotChocolate version numbers: every
# HotChocolate GitHub release carries a native AOT nitro-router binary per
# platform. The benchmark always runs the latest HotChocolate preview on NuGet.
VERSION="$(curl -fsSL "https://api.nuget.org/v3-flatcontainer/hotchocolate.aspnetcore/index.json" \
  | python3 -I -c '
import json, sys


def key(version):
    core, _, pre = version.partition("-")
    # SemVer 2.0: numeric prerelease identifiers rank below alphanumeric ones
    # and compare numerically.
    return (
        tuple(int(part) for part in core.split(".")),
        tuple((0, int(i), "") if i.isdigit() else (1, 0, i) for i in pre.split(".")),
    )


previews = [
    v for v in json.load(sys.stdin).get("versions", [])
    if "-" in v and all(part.isdigit() for part in v.partition("-")[0].split("."))
]
if previews:
    print(max(previews, key=key))
')"
if [[ -z "$VERSION" ]]; then
  echo "ERROR: could not determine the latest HotChocolate preview version"
  exit 1
fi

case "$(uname -s) $(uname -m)" in
  "Linux x86_64") ASSET="nitro-router-linux-x64.tar.gz" ;;
  "Linux aarch64" | "Linux arm64") ASSET="nitro-router-linux-arm64.tar.gz" ;;
  "Darwin arm64") ASSET="nitro-router-osx-arm64.zip" ;;
  "Darwin x86_64") ASSET="nitro-router-osx-x64.zip" ;;
  *)
    echo "ERROR: no nitro-router release binary for $(uname -s) $(uname -m)"
    exit 1
    ;;
esac

DOWNLOAD_DIR="$(mktemp -d)"
trap 'rm -rf "$DOWNLOAD_DIR"' EXIT

URL="https://github.com/ChilliCream/graphql-platform/releases/download/$VERSION/$ASSET"
echo "Downloading $URL"
curl -fsSL -o "$DOWNLOAD_DIR/$ASSET" "$URL"

case "$ASSET" in
  *.zip) unzip -q -o "$DOWNLOAD_DIR/$ASSET" nitro-router -d "$DOWNLOAD_DIR" ;;
  *) tar -xzf "$DOWNLOAD_DIR/$ASSET" -C "$DOWNLOAD_DIR" nitro-router ;;
esac

mv "$DOWNLOAD_DIR/nitro-router" ./nitro-router
chmod +x ./nitro-router
echo "$VERSION" > version.txt
echo "Nitro Router $VERSION installed."
