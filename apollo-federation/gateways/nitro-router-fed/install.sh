#!/usr/bin/env bash
set -Eeuo pipefail

# Same release binary as the GraphQL Federation variant; only gateway.far differs.
exec bash "$(dirname "${BASH_SOURCE[0]}")/../../../graphql-federation/gateways/nitro-router/install.sh"
