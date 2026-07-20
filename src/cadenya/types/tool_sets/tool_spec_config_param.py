# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .tool_spec_config_mcp_param import ToolSpecConfigMCPParam
from .tool_spec_config_bare_param import ToolSpecConfigBareParam
from .tool_spec_config_http_param import ToolSpecConfigHTTPParam
from .tool_spec_config_openapi_param import ToolSpecConfigOpenAPIParam

__all__ = ["ToolSpecConfigParam"]

ToolSpecConfigParam: TypeAlias = Union[
    ToolSpecConfigHTTPParam, ToolSpecConfigMCPParam, ToolSpecConfigOpenAPIParam, ToolSpecConfigBareParam
]
