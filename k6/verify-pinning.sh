#!/usr/bin/env bash
set -euo pipefail

# Verify CPU affinity of benchmark processes.
# Usage: verify-pinning.sh <gateway-pid> <subgraph-pid> [gateway-cpuset] [subgraph-cpuset] [system-cpuset]

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
SYSTEM_CPUSET="${5:-}"

if [[ -n "$GATEWAY_PID" ]]; then
  check_affinity "Gateway" "$GATEWAY_PID" "$GATEWAY_CPUSET"
fi

if [[ -n "$SUBGRAPH_PID" ]]; then
  check_affinity "Subgraph" "$SUBGRAPH_PID" "$SUBGRAPH_CPUSET"
fi

# Check for stray processes that use CPU on benchmark cores (every core outside
# the system cpuset). Only processes busy for at least 5% of a core over a
# 1 s sample count: idle daemons that last ran on a benchmark core don't
# compete with the benchmark, and a warning that always fires gets ignored.
# Kernel threads (PID 2 and its children) and everything benchmark.sh started
# (gateway, subgraphs, this script) are skipped.
echo "  Checking for stray processes on benchmark cores..."
STRAY="$(python3 - "$(expand_cpus "$SYSTEM_CPUSET")" "$(list_tree "$PPID" | tr '\n' ' ')" "$$" <<'PY' || true
import os, sys, time

system_cpus = {int(c) for c in sys.argv[1].split(",") if c}
own = {int(p) for p in sys.argv[2].split()}
own.add(int(sys.argv[3]))
ticks_per_second = os.sysconf("SC_CLK_TCK")

def snapshot():
    procs = {}
    for entry in os.listdir("/proc"):
        if not entry.isdigit():
            continue
        try:
            with open(f"/proc/{entry}/stat") as f:
                data = f.read()
        except OSError:
            continue
        comm = data[data.index("(") + 1:data.rindex(")")]
        fields = data[data.rindex(")") + 2:].split()
        pid, ppid = int(entry), int(fields[1])
        procs[pid] = (ppid, comm, int(fields[11]) + int(fields[12]), int(fields[36]))
    return procs

before = snapshot()
time.sleep(1)
after = snapshot()
me = os.getpid()
for pid, (ppid, comm, ticks, cpu) in sorted(after.items()):
    if pid == 2 or ppid == 2 or pid in own or ppid in own or pid == me:
        continue
    if cpu in system_cpus or pid not in before:
        continue
    busy = 100.0 * (ticks - before[pid][2]) / ticks_per_second
    if busy >= 5.0:
        print(f"{pid:>7} {cpu:>3} {busy:5.1f}% {comm}")
PY
)"
if [[ -n "$STRAY" ]]; then
  echo "  ⚠️  Found busy processes on benchmark cores (pid, core, CPU over 1 s, name):"
  printf '%s\n' "$STRAY" | head -10 | sed 's/^/    /'
else
  echo "  ✅ No busy stray processes on benchmark cores"
fi
