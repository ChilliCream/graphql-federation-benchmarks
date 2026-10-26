#!/usr/bin/env bash
set -Eeuo pipefail

VERSION="v0.3.5"
curl -fsSL "https://raw.githubusercontent.com/graphql-hive/router/hive-router/$VERSION/install.sh" | sh -s "$VERSION"
echo "$VERSION" > version.txt
