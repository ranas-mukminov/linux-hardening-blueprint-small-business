"""Configuration loader and validation helpers for linux-harden."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Optional

import yaml

SUPPORTED_PROFILES = {"workstation", "server", "hardened"}


def _validate_keys(payload: Dict[str, Any]) -> None:
    allowed = {"profile", "inventory", "limit", "check", "extra_vars"}
    unknown = set(payload) - allowed
    if unknown:
        raise ValueError(f"Unsupported config keys: {', '.join(sorted(unknown))}")

    if "profile" in payload and payload["profile"] not in SUPPORTED_PROFILES:
        raise ValueError(
            f"Profile '{payload['profile']}' is invalid. Choose from {sorted(SUPPORTED_PROFILES)}"
        )

    for text_key in ("inventory", "limit", "extra_vars"):
        value = payload.get(text_key)
        if value is not None and not isinstance(value, str):
            raise ValueError(f"'{text_key}' must be a string if provided")

    if "check" in payload and not isinstance(payload["check"], bool):
        raise ValueError("'check' must be a boolean")


@dataclass
class CLIConfig:
    profile: str = "server"
    inventory: str = "ansible/inventories/example_inventory.yml"
    limit: Optional[str] = None
    check: bool = False
    extra_vars: Optional[str] = None

    def merge(self, overrides: Dict[str, Any]) -> "CLIConfig":
        data = {**self.__dict__, **{k: v for k, v in overrides.items() if v is not None}}
        return CLIConfig(**data)


def load_config(path: Optional[str]) -> CLIConfig:
    """Load YAML config from ``path`` if provided, otherwise return defaults."""
    base = CLIConfig()
    if not path:
        return base

    config_path = Path(path)
    if not config_path.exists():
        raise FileNotFoundError(f"Config file '{config_path}' not found")

    with config_path.open("r", encoding="utf-8") as handle:
        payload = yaml.safe_load(handle) or {}
    if not isinstance(payload, dict):
        raise ValueError("Config root must be a mapping")

    _validate_keys(payload)
    return base.merge(payload)
