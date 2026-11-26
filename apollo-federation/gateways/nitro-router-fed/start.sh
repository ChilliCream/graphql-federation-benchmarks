#!/usr/bin/env bash
set -Eeuo pipefail

# The router loads ./gateway.far from its working directory.
# OTEL_SDK_DISABLED turns off its logs, metrics and traces.
exec env -i \
  ASPNETCORE_URLS=http://localhost:5220 \
  OTEL_SDK_DISABLED=true \
  ./nitro-router > ./gateway_log.txt 2>&1
