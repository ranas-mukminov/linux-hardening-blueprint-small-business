"""Utilities to construct and run ansible-playbook commands."""

from __future__ import annotations

import shlex
import subprocess
from pathlib import Path
from typing import List, Sequence

from .config_schema import CLIConfig

ANSIBLE_PLAYBOOK_PATH = Path("ansible") / "playbooks" / "site.yml"


def build_command(config: CLIConfig, playbook: Path | None = None) -> List[str]:
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
    subprocess.run(command, check=True)
