"""Test DeConz discovery."""

import pytest
import voluptuous as vol

from supervisor.discovery.validate import valid_discovery_config


def test_good_config():
    """Test good deconz config."""

    valid_discovery_config(
        "deconz",
        {"host": "test", "port": 3812, "api_key": "MY_api_KEY99", "serial": "xyz"},
    )


def test_bad_config():
    """Test bad deconz config."""

    with pytest.raises(vol.Invalid):
        valid_discovery_config("deconz", {"host": "test", "port": 8080})
