#!/usr/bin/env bash
# Drops gateways whose build produced no prebuilt artifact from the benchmark
# matrices, so a broken gateway build skips that gateway instead of failing the run.
#
# Reads the GATEWAYS, GATEWAYS_CONSTANT and GATEWAYS_BURST matrices from the
# environment and writes the filtered matrices to GITHUB_OUTPUT under the keys
# gateways, gateways_constant and gateways_burst.
set -euo pipefail

: "${GATEWAYS:?}" "${GATEWAYS_CONSTANT:?}" "${GATEWAYS_BURST:?}" "${GITHUB_OUTPUT:?}"

BUILT="$(gh api --paginate "repos/$GITHUB_REPOSITORY/actions/runs/$GITHUB_RUN_ID/artifacts?per_page=100" \
  --jq '.artifacts[].name' | jq -R . | jq -sc .)"

built_only() {
  jq -c --argjson built "$BUILT" '[.[] | select(.gateway_artifact as $a | $built | index($a))]' <<< "$1"
}

jq -r --argjson built "$BUILT" '.[] | select(.gateway_artifact as $a | $built | index($a) | not) | .name' \
  <<< "$GATEWAYS" | while read -r name; do
  echo "::warning::$name has no prebuilt gateway (its build failed); skipping its benchmarks"
done

{
  echo "gateways=$(built_only "$GATEWAYS")"
  echo "gateways_constant=$(built_only "$GATEWAYS_CONSTANT")"
  echo "gateways_burst=$(built_only "$GATEWAYS_BURST")"
} >> "$GITHUB_OUTPUT"
