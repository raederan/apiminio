"""Init file for the Apiminio package."""

import importlib.metadata

from .main import Apiminio, MinioConfig

__version__ = importlib.metadata.version("apiminio")

__all__ = ["Apiminio", "MinioConfig", "__version__"]
