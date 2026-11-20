#!/usr/bin/env bash
set -Eeuo pipefail

# Apollo publishes no binaries for its Router 3 development branch, so build its
# head the way Apollo's release pipeline does (`cargo xtask dist` is
# `cargo build --release`). rust-toolchain.toml in the checkout selects the toolchain.
REPOSITORY="https://github.com/apollographql/router.git"
BRANCH="dev-v3.x"
# apollo-router's build script compiles .proto files with prost-build, which needs protoc.
# https://github.com/protocolbuffers/protobuf/releases
PROTOC_VERSION="36.2"

WORK_DIR="$(mktemp -d)"
trap 'rm -rf "$WORK_DIR"' EXIT
SOURCE_DIR="$WORK_DIR/source"
PROTOC_DIR="$WORK_DIR/protoc"
mkdir -p "$SOURCE_DIR" "$PROTOC_DIR"

case "$(uname -s)-$(uname -m)" in
  Linux-x86_64) PROTOC_PLATFORM="linux-x86_64" ;;
  Linux-aarch64) PROTOC_PLATFORM="linux-aarch_64" ;;
  Darwin-*) PROTOC_PLATFORM="osx-universal_binary" ;;
  *) echo "ERROR: unsupported platform for protoc: $(uname -s)-$(uname -m)"; exit 1 ;;
esac
curl -fsSL -o "$WORK_DIR/protoc.zip" \
  "https://github.com/protocolbuffers/protobuf/releases/download/v${PROTOC_VERSION}/protoc-${PROTOC_VERSION}-${PROTOC_PLATFORM}.zip"
unzip -q "$WORK_DIR/protoc.zip" -d "$PROTOC_DIR"
export PROTOC="$PROTOC_DIR/bin/protoc"

git -C "$SOURCE_DIR" init -q
git -C "$SOURCE_DIR" fetch -q --depth 1 "$REPOSITORY" "$BRANCH"
git -C "$SOURCE_DIR" checkout -q FETCH_HEAD
COMMIT="$(git -C "$SOURCE_DIR" rev-parse --short=8 HEAD)"
CRATE_VERSION="$(sed -n 's/^version = "\(.*\)"$/\1/p' "$SOURCE_DIR/apollo-router/Cargo.toml" | head -n1)"

(cd "$SOURCE_DIR" && cargo build --release)
cp "$SOURCE_DIR/target/release/router" ./router
echo "v${CRATE_VERSION}-nightly.${COMMIT}" > version.txt
