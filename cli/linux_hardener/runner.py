"""Utilities to construct and run ansible-playbook commands."""

from __future__ import annotations

import shlex
import subprocess  # nosec B404: this module's purpose is running ansible-playbook
from collections.abc import Sequence
from pathlib import Path

from .config_schema import CLIConfig

ANSIBLE_PLAYBOOK_PATH = Path("ansible") / "playbooks" / "site.yml"


def build_command(config: CLIConfig, playbook: Path | None = None) -> list[str]:
    """Create the ansible-playbook invocation for the supplied configuration."""
    target_playbook = playbook or ANSIBLE_PLAYBOOK_PATH
    command = [
        "ansible-playbook",
        str(target_playbook),
        "-i",
        config.inventory,
        "-e",
        f"linux_hardener_profile={config.profile}",
    ]
    if config.limit:
        command.extend(["-l", config.limit])
    if config.check:
        command.append("--check")
    if config.extra_vars:
        command.extend(["-e", f"@{config.extra_vars}"])
    return command


def run_playbook(command: Sequence[str]) -> None:
    """Execute the ansible-playbook command and stream output."""
    printable = " ".join(shlex.quote(arg) for arg in command)
    print(f"[linux-harden] executing: {printable}")
    # argv list, no shell, so no shell injection is possible;
    # the variable args are the local operator's own CLI/config values.
    subprocess.run(command, check=True)  # nosec B603
