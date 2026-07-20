# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from ..._utils import PropertyInfo
from .tool_spec_config_mcp import ToolSpecConfigMCP
from .tool_spec_config_bare import ToolSpecConfigBare
from .tool_spec_config_http import ToolSpecConfigHTTP
from .tool_spec_config_openapi import ToolSpecConfigOpenAPI

__all__ = ["ToolSpecConfig"]

ToolSpecConfig: TypeAlias = Annotated[
    Union[ToolSpecConfigHTTP, ToolSpecConfigMCP, ToolSpecConfigOpenAPI, ToolSpecConfigBare],
    PropertyInfo(discriminator="type"),
]
