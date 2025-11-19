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
if [[ ${#EXTRA_ARGS[@]} -gt 0 ]]; then
  EXTRA_ARGS_CMD=("${EXTRA_ARGS[@]}")
else
  EXTRA_ARGS_CMD=()
fi

ansible-playbook ansible/playbooks/site.yml \
  -i "${INVENTORY}" \
  -e "linux_hardener_profile=${PROFILE}" \
  "${EXTRA_ARGS_CMD[@]}"
