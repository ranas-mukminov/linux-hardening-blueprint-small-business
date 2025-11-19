import pytest

from linux_hardener.config_schema import CLIConfig, load_config


def test_load_config_defaults():
    config = load_config(None)
    assert isinstance(config, CLIConfig)
    assert config.profile == "server"


def test_load_config_from_file(tmp_path):
    cfg_file = tmp_path / "config.yml"
    cfg_file.write_text("profile: workstation\ncheck: true\n", encoding="utf-8")
    config = load_config(str(cfg_file))
    assert config.profile == "workstation"
    assert config.check is True


def test_load_config_invalid_key(tmp_path):
    cfg_file = tmp_path / "bad.yml"
    cfg_file.write_text("unknown: value\n", encoding="utf-8")
    with pytest.raises(ValueError):
        load_config(str(cfg_file))
