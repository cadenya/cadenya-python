# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel
from .config_mcp import ConfigMCP

__all__ = ["ToolSpecConfigMCP"]


class ToolSpecConfigMCP(BaseModel):
    mcp: ConfigMCP

    type: Literal["mcp"]
