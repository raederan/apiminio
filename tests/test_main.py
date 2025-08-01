"""Tests for the Apiminio class."""

# https://stackoverflow.com/a/71791662
# https://pook.readthedocs.io/en/latest/index.html#supported-http-clients

from apiminio.main import Apiminio, McpConfig, MinioConfig


def test_apiminio_class():
    """Test instantiation of MinioConfig and Apiminio."""
    minio_config = MinioConfig()
    apiminio = Apiminio(minio_config=minio_config)
    assert isinstance(minio_config, MinioConfig)
    assert isinstance(apiminio, Apiminio)


def test_apiminio_class_mcp_config_http():
    """Test instantiation of Apiminio with MCP configuration."""
    minio_config = MinioConfig()
    mcp_config = McpConfig()  # Default: enabled "http"
    apiminio = Apiminio(minio_config=minio_config, mcp_config=mcp_config)
    assert isinstance(apiminio, Apiminio)


def test_apiminio_class_mcp_config_sse():
    """Test instantiation of Apiminio with MCP configuration using SSE."""
    minio_config = MinioConfig()
    mcp_config = McpConfig(enable_mcp=True, transport="sse")
    apiminio = Apiminio(minio_config=minio_config, mcp_config=mcp_config)
    assert isinstance(apiminio, Apiminio)
