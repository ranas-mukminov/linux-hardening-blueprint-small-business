from pathlib import Path

from typer.testing import CliRunner

from linux_hardener import cli

runner = CliRunner()


def test_cli_builds_command(tmp_path, mocker):
    dummy_inventory = tmp_path / "hosts.ini"
    dummy_inventory.write_text("[all]\nlocalhost ansible_connection=local\n", encoding="utf-8")
    subprocess_run = mocker.patch("linux_hardener.runner.subprocess.run")

    result = runner.invoke(
        cli.app,
        [
            "--profile",
            "workstation",
            "--inventory",
            str(dummy_inventory),
            "--limit",
            "localhost",
        ],
    )

    assert result.exit_code == 0, result.output
    subprocess_run.assert_called_once()
    args = subprocess_run.call_args.args[0]
    assert "ansible-playbook" in args[0]
    assert f"linux_hardener_profile=workstation" in args


def test_cli_invalid_profile(mocker):
    mocker.patch("linux_hardener.runner.subprocess.run")
    result = runner.invoke(cli.app, ["--profile", "invalid"])
    assert result.exit_code != 0
    assert "Configuration error" in result.output
