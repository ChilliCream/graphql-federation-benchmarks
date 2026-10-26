#!/usr/bin/env bash
set -euo pipefail

# Verify CPU affinity of benchmark processes.
# Usage: verify-pinning.sh <gateway-pid> <subgraph-pid> [gateway-cpuset] [subgraph-cpuset]

if ! command -v taskset &>/dev/null; then
  echo "Pinning verification: skipped (no taskset)"
  exit 0
fi

echo "=== CPU Affinity Verification ==="

# Expand a CPU list like "2-3,10-11" to "2,3,10,11" so lists compare exactly.
expand_cpus() {
  local part lo hi out=()
  IFS=',' read -r -a parts <<< "$1"
  for part in "${parts[@]}"; do
    if [[ "$part" == *-* ]]; then
      lo="${part%-*}"; hi="${part#*-}"
      for ((c = lo; c <= hi; c++)); do out+=("$c"); done
    elif [[ -n "$part" ]]; then
      out+=("$part")
    fi
  done
  (IFS=','; echo "${out[*]}")
}

list_tree() {
  local queue=("$1") current child
  while [[ ${#queue[@]} -gt 0 ]]; do
    current="${queue[0]}"
    queue=("${queue[@]:1}")
    echo "$current"
    while IFS= read -r child; do
      [[ -n "$child" ]] && queue+=("$child")
    done < <(pgrep -P "$current" 2>/dev/null || true)
  done
}

# Check every process in the launcher's tree. taskset runs inside
# `sudo -u perfrunner`, so the launcher subshell and sudo itself are never
# pinned; only what taskset starts (start.sh and the server it launches) is.
check_affinity() {
  local label="$1"
  local root_pid="$2"
  local expected="$3"
  local pid comm affinity wrapper mismatches=0

  if ! kill -0 "$root_pid" 2>/dev/null; then
    echo "  ${label} (PID $root_pid): not running"
    return 0
  fi

  while IFS= read -r pid; do
    comm="$(ps -o comm= -p "$pid" 2>/dev/null || true)"
    [[ -z "$comm" ]] && continue
    affinity="$(taskset -cp "$pid" 2>/dev/null | awk -F': ' '{print $2}' || true)"
    wrapper=""
    case "$comm" in
      sudo|env) wrapper=" (wrapper, not pinned by design)" ;;
    esac
    if [[ "$pid" == "$root_pid" && "$comm" == bash ]]; then
      wrapper=" (launcher subshell, not pinned by design)"
    fi
    echo "  ${label} ${comm} (PID $pid): ${affinity:-affinity unavailable}${wrapper}"
    if [[ -z "$wrapper" && -n "$expected" && -n "$affinity" ]] \
      && [[ "$(expand_cpus "$affinity")" != "$(expand_cpus "$expected")" ]]; then
      mismatches=$((mismatches + 1))
    fi
  done < <(list_tree "$root_pid")

  if [[ -n "$expected" ]]; then
    if (( mismatches > 0 )); then
      echo "  ⚠️  ${label}: $mismatches process(es) not pinned to $expected"
    else
      echo "  ✅ ${label}: all pinned processes on $expected"
    fi
  fi
}

GATEWAY_PID="${1:-}"
SUBGRAPH_PID="${2:-}"
GATEWAY_CPUSET="${3:-}"
SUBGRAPH_CPUSET="${4:-}"

if [[ -n "$GATEWAY_PID" ]]; then
  check_affinity "Gateway" "$GATEWAY_PID" "$GATEWAY_CPUSET"
fi

if [[ -n "$SUBGRAPH_PID" ]]; then
  check_affinity "Subgraph" "$SUBGRAPH_PID" "$SUBGRAPH_CPUSET"
fi

# Check for stray processes on benchmark cores
echo "  Checking for stray processes on benchmark cores..."
STRAY=$(ps -eo pid,psr,comm --sort=-psr 2>/dev/null \
  | awk '$2 >= 1 && $2 <= 7 && $3 !~ /^(migration|watchdog|ksoftirq|kworker|rcu_)/ {print}' \
  | head -5 || true)
if [[ -n "$STRAY" ]]; then
  echo "  ⚠️  Found processes on benchmark cores:"
  echo "$STRAY" | sed 's/^/    /'
else
  echo "  ✅ No stray userspace processes on benchmark cores"
fi
