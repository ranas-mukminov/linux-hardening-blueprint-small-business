"""Console entry point for the linux-harden CLI."""

from __future__ import annotations

from pathlib import Path
from typing import Optional

import subprocess
import typer

from .config_schema import CLIConfig, SUPPORTED_PROFILES, load_config
from .runner import build_command, run_playbook

app = typer.Typer(
    add_completion=False, help="Automation-friendly Linux hardening wrapper"
)


def _resolve_config(
    profile: Optional[str],
    inventory: Optional[str],
    limit: Optional[str],
    check: bool,
    extra_vars: Optional[str],
    config_file: Optional[str],
) -> CLIConfig:
    base = load_config(config_file)
    if profile and profile not in SUPPORTED_PROFILES:
        raise ValueError(
            f"Profile '{profile}' is invalid. Choose from {', '.join(sorted(SUPPORTED_PROFILES))}"
        )
    overrides = {
        "profile": profile,
        "inventory": inventory,
        "limit": limit,
        "check": check if check else None,
        "extra_vars": extra_vars,
    }
    overrides = {k: v for k, v in overrides.items() if v is not None}
    if "profile" not in overrides:
        overrides["profile"] = base.profile
    return base.merge(overrides)


@app.command(context_settings={"help_option_names": ["-h", "--help"]})
def main(
    profile: Optional[str] = typer.Option(
        None,
        "--profile",
        help="Profile to apply (workstation/server/hardened)",
        show_default=False,
        autocompletion=lambda incomplete: [
            p for p in SUPPORTED_PROFILES if p.startswith(incomplete)
        ],
    ),
    inventory: Optional[str] = typer.Option(
        None,
        "--inventory",
        "-i",
        help="Inventory path",
    ),
    limit: Optional[str] = typer.Option(
        None,
        "--limit",
        "-l",
        help="Host pattern to limit execution to",
    ),
    check: bool = typer.Option(
        False, "--check", help="Run Ansible in check (dry-run) mode"
    ),
    extra_vars: Optional[Path] = typer.Option(
        None,
        "--extra-vars",
        exists=True,
        readable=True,
        dir_okay=False,
        path_type=Path,
        help="YAML file with ansible extra vars",
    ),
    config_file: Optional[Path] = typer.Option(
        None,
        "--config",
        dir_okay=False,
        path_type=Path,
        help="Optional CLI config YAML",
    ),
) -> None:
    """Run the hardening playbook via ansible-playbook."""
    try:
        config = _resolve_config(
            profile,
            inventory,
            limit,
            check,
            str(extra_vars) if extra_vars else None,
            str(config_file) if config_file else None,
        )
    except Exception as exc:  # pragma: no cover - typed error display
        typer.secho(f"Configuration error: {exc}", fg=typer.colors.RED)
        raise typer.Exit(code=2) from exc

    command = build_command(config)
    typer.secho(
        f"Applying profile '{config.profile}' using inventory '{config.inventory}'",
        fg=typer.colors.CYAN,
    )
    try:
        run_playbook(command)
    except subprocess.CalledProcessError as exc:  # type: ignore[name-defined]
        typer.secho(
            f"ansible-playbook failed with exit code {exc.returncode}",
            fg=typer.colors.RED,
        )
        raise typer.Exit(code=exc.returncode)


def run() -> None:  # pragma: no cover - console script entry
    app()


if __name__ == "__main__":  # pragma: no cover
    run()
