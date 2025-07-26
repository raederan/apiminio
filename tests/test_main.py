"""Tests for the Apiminio class."""

# https://stackoverflow.com/a/71791662
# https://pook.readthedocs.io/en/latest/index.html#supported-http-clients

from apiminio.main import Apiminio, MinioConfig


def test_apiminio_class():
    """Test instantiation of MinioConfig and Apiminio."""
    config = MinioConfig()
    apiminio = Apiminio(config=config)
    assert isinstance(config, MinioConfig)
    assert isinstance(apiminio, Apiminio)
