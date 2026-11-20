#!/usr/bin/env bash
set -Eeuo pipefail

# Hive Router publishes binaries only for releases, so build the head of its main
# branch the way its release pipeline does (`cargo build --release`, LTO per the
# workspace's release profile). rust-toolchain.toml in the checkout selects the toolchain.
REPOSITORY="https://github.com/graphql-hive/router.git"
BRANCH="main"

SOURCE_DIR="$(mktemp -d)"
trap 'rm -rf "$SOURCE_DIR"' EXIT

git -C "$SOURCE_DIR" init -q
git -C "$SOURCE_DIR" fetch -q --depth 1 "$REPOSITORY" "$BRANCH"
git -C "$SOURCE_DIR" checkout -q FETCH_HEAD
COMMIT="$(git -C "$SOURCE_DIR" rev-parse --short=8 HEAD)"
CRATE_VERSION="$(sed -n 's/^version = "\(.*\)"$/\1/p' "$SOURCE_DIR/bin/router/Cargo.toml" | head -n1)"

(cd "$SOURCE_DIR" && cargo build --release -p hive-router --bin hive_router)
cp "$SOURCE_DIR/target/release/hive_router" ./hive_router
echo "v${CRATE_VERSION}-nightly.${COMMIT}" > version.txt
