#!/usr/bin/env bash
set -Eeuo pipefail

# Apollo publishes no binaries for its Router 3 development branch, so build its
# head the way Apollo's release pipeline does (`cargo xtask dist` is
# `cargo build --release`). rust-toolchain.toml in the checkout selects the toolchain.
REPOSITORY="https://github.com/apollographql/router.git"
BRANCH="dev-v3.x"

SOURCE_DIR="$(mktemp -d)"
trap 'rm -rf "$SOURCE_DIR"' EXIT

git -C "$SOURCE_DIR" init -q
git -C "$SOURCE_DIR" fetch -q --depth 1 "$REPOSITORY" "$BRANCH"
git -C "$SOURCE_DIR" checkout -q FETCH_HEAD
COMMIT="$(git -C "$SOURCE_DIR" rev-parse --short=8 HEAD)"
CRATE_VERSION="$(sed -n 's/^version = "\(.*\)"$/\1/p' "$SOURCE_DIR/apollo-router/Cargo.toml" | head -n1)"

(cd "$SOURCE_DIR" && cargo build --release)
cp "$SOURCE_DIR/target/release/router" ./router
echo "v${CRATE_VERSION}-nightly.${COMMIT}" > version.txt
