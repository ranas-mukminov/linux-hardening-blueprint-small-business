#!/usr/bin/env bash
set -euo pipefail

PROFILE=${1:-server}
INVENTORY=${2:-ansible/inventories/example_inventory.yml}
if [[ $# -ge 2 ]]; then
  shift 2
else
  shift $#
fi
EXTRA_ARGS=("$@")

run_once() {
  local logfile=$1
  local start end
  local EXTRA_ARGS_CMD=()
  start=$(date +%s)
  if [[ ${#EXTRA_ARGS[@]} -gt 0 ]]; then
    EXTRA_ARGS_CMD=("${EXTRA_ARGS[@]}")
  fi
  ansible-playbook ansible/playbooks/site.yml \
    -i "${INVENTORY}" \
    -e "linux_hardener_profile=${PROFILE}" \
    "${EXTRA_ARGS_CMD[@]}" | tee "${logfile}"
  end=$(date +%s)
  echo $((end - start))
}

get_changed() {
  local logfile=$1
  grep -Eo 'changed=([0-9]+)' "${logfile}" | tail -n1 | cut -d= -f2
}

FIRST_LOG=$(mktemp)
SECOND_LOG=$(mktemp)
trap 'rm -f "${FIRST_LOG}" "${SECOND_LOG}"' EXIT

FIRST_RUNTIME=$(run_once "${FIRST_LOG}")
SECOND_RUNTIME=$(run_once "${SECOND_LOG}")

FIRST_CHANGED=$(get_changed "${FIRST_LOG}")
SECOND_CHANGED=$(get_changed "${SECOND_LOG}")

echo "First run changed=${FIRST_CHANGED}, runtime=${FIRST_RUNTIME}s"
echo "Second run changed=${SECOND_CHANGED}, runtime=${SECOND_RUNTIME}s"

if [[ -z "${SECOND_CHANGED}" || ${SECOND_CHANGED} -gt 0 ]]; then
  echo "Idempotency check failed: second run still reports changes" >&2
  exit 1
fi
