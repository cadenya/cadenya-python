# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .tool_set_adapter_mcp import ToolSetAdapterMCP

__all__ = ["ToolSetAdapterMCPVariant"]


class ToolSetAdapterMCPVariant(BaseModel):
    mcp: ToolSetAdapterMCP

    type: Literal["mcp"]
