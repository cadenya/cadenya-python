# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .tool_set_adapter_mcp import ToolSetAdapterMcp
from .tool_set_adapter_http import ToolSetAdapterHTTP
from .tool_set_adapter_openapi import ToolSetAdapterOpenAPI

__all__ = ["ToolSetAdapter"]


class ToolSetAdapter(BaseModel):
    http: Optional[ToolSetAdapterHTTP] = None

    mcp: Optional[ToolSetAdapterMcp] = None

    openapi: Optional[ToolSetAdapterOpenAPI] = None
