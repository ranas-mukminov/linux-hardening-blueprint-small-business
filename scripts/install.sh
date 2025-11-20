#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV_PATH="${ROOT_DIR}/.venv"

python3 -m venv "${VENV_PATH}"
# shellcheck disable=SC1091
source "${VENV_PATH}/bin/activate"

pip install --upgrade pip wheel
pip install -e "${ROOT_DIR}/cli" \
  'ansible>=8.7,<9.0' \
  'molecule[docker]>=6.0' \
  'ansible-lint>=24.2' \
  yamllint \
  ruff \
  black \
  bandit \
  'pytest pytest-mock' \
  pip-audit

ansible-galaxy collection install community.general ansible.posix

echo "Tooling installed in ${VENV_PATH}. Activate it with 'source ${VENV_PATH}/bin/activate'."
