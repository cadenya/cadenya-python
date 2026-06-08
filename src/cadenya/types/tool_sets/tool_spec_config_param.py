# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .config_mcp_param import ConfigMcpParam
from .config_http_param import ConfigHTTPParam
from .config_openapi_param import ConfigOpenAPIParam

__all__ = ["ToolSpecConfigParam"]


class ToolSpecConfigParam(TypedDict, total=False):
    """
    Config defines the adapter to use for the tool.
     This is used to determine how the tool is called.
     For example, if the tool is an HTTP tool, the adapter will be Http.
     If the tool is an inline tool, the adapter will be Inline.
    """

    http: ConfigHTTPParam

    mcp: ConfigMcpParam

    openapi: ConfigOpenAPIParam
