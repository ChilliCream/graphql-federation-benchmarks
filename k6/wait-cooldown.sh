#!/usr/bin/env bash
# wait-cooldown.sh [target_celsius] [max_seconds]
# wait-cooldown.sh --read
#
# Waits until the CPU package temperature is at or below target_celsius (default 45) or until
# max_seconds (default 180) have passed, whichever comes first. Progress goes to stderr every
# 10 seconds so a tailed CI log shows the machine is cooling, not stuck. Always exits 0 so it
# can sit between benchmark runs; the single stdout line says which condition ended the wait:
#   cooldown: reached <temp> °C after <n>s
#   cooldown: timeout after <n>s at <temp> °C
#
# --read prints the current temperature in °C (one decimal) and exits; nothing if no sensor.
#
# env:
#   COOLDOWN_SENSOR    temperature file in millidegrees (default: auto-detect the CPU package sensor)
#   COOLDOWN_INTERVAL  seconds between reads (default 1)
#   COOLDOWN_QUIET     1 = print only the final line
set -u

find_sensor() {
  local hw name label
  # AMD (k10temp/zenpower): Tctl or Tdie; Intel (coretemp): "Package id 0".
  for hw in /sys/class/hwmon/hwmon*; do
    name=$(cat "$hw/name" 2>/dev/null) || continue
    case "$name" in
      k10temp|zenpower|coretemp)
        for label in "$hw"/temp*_label; do
          [ -e "$label" ] || continue
          case "$(cat "$label")" in
            Tdie|Tctl|"Package id 0") echo "${label%_label}_input"; return 0 ;;
          esac
        done
        [ -e "$hw/temp1_input" ] && { echo "$hw/temp1_input"; return 0; }
        ;;
    esac
  done
  # Fallback: thermal zones of the CPU package.
  for hw in /sys/class/thermal/thermal_zone*; do
    case "$(cat "$hw/type" 2>/dev/null)" in
      x86_pkg_temp|cpu-thermal|cpu_thermal|soc_thermal) echo "$hw/temp"; return 0 ;;
    esac
  done
  return 1
}

sensor=${COOLDOWN_SENSOR:-$(find_sensor)}
read_temp() { awk '{ printf "%.1f", $1 / 1000 }' "$sensor"; }

if [ "${1:-}" = "--read" ]; then
  if [ -n "$sensor" ] && [ -r "$sensor" ]; then
    read_temp
    echo
  fi
  exit 0
fi

target=${1:-45}
max=${2:-180}
interval=${COOLDOWN_INTERVAL:-1}
quiet=${COOLDOWN_QUIET:-0}

if [ -z "$sensor" ] || [ ! -r "$sensor" ]; then
  echo "No CPU temperature sensor found, cooling down for ${max}s" >&2
  sleep "$max"
  echo "cooldown: timeout after ${max}s (no sensor)"
  exit 0
fi

start=$SECONDS
next_report=0
while :; do
  temp=$(read_temp)
  elapsed=$((SECONDS - start))
  if awk -v t="$temp" -v g="$target" 'BEGIN { exit !(t <= g) }'; then
    echo "cooldown: reached ${temp} °C after ${elapsed}s"
    exit 0
  fi
  if [ "$elapsed" -ge "$max" ]; then
    echo "cooldown: timeout after ${elapsed}s at ${temp} °C"
    exit 0
  fi
  if [ "$quiet" != 1 ] && [ "$elapsed" -ge "$next_report" ]; then
    echo "System at ${temp} °C, cooling down to ${target} °C (${elapsed}s of max ${max}s)" >&2
    next_report=$((elapsed + 10))
  fi
  sleep "$interval"
done
