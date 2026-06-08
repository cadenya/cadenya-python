# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .tool_set_adapter_mcp_param import ToolSetAdapterMcpParam
from .tool_set_adapter_http_param import ToolSetAdapterHTTPParam
from .tool_set_adapter_openapi_param import ToolSetAdapterOpenAPIParam

__all__ = ["ToolSetAdapterParam"]


class ToolSetAdapterParam(TypedDict, total=False):
    http: ToolSetAdapterHTTPParam

    mcp: ToolSetAdapterMcpParam

    openapi: ToolSetAdapterOpenAPIParam
