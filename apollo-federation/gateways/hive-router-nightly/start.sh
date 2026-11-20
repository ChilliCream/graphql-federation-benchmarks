#!/usr/bin/env bash
set -Eeuo pipefail

exec env -i \
  LOG_LEVEL=error \
  PORT=5220 \
  SUPERGRAPH_FILE_PATH="./supergraph.graphql" \
  ./hive_router > ./gateway_log.txt 2>&1
