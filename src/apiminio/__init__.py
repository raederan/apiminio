"""Init file for the Apiminio package."""

import importlib.metadata

from .main import Apiminio, McpConfig, MinioConfig

__version__ = importlib.metadata.version("apiminio")

__all__ = ["Apiminio", "McpConfig", "MinioConfig", "__version__"]
