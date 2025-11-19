#!/usr/bin/env bash
set -euo pipefail

pip-audit || true
bandit -qr cli
