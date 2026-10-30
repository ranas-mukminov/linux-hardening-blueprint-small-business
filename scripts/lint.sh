#!/usr/bin/env bash
set -euo pipefail

ruff check cli
black --check cli
ansible-lint ansible
yamllint ansible tests .github
bandit -qr cli
shellcheck scripts/*.sh
