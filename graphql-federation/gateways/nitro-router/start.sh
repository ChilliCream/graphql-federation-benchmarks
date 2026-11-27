#!/usr/bin/env bash
set -Eeuo pipefail

# The router loads ./gateway.far and ./config.yaml from its working directory.
exec env -i ./nitro-router > ./gateway_log.txt 2>&1
