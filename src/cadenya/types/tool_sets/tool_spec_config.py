# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .config_http import ConfigHTTP
from .config_openapi import ConfigOpenAPI

__all__ = ["ToolSpecConfig"]


class ToolSpecConfig(BaseModel):
    """
    Config defines the adapter to use for the tool.
     This is used to determine how the tool is called.
     For example, if the tool is an HTTP tool, the adapter will be Http.
     If the tool is an inline tool, the adapter will be Inline.
    """

    http: Optional[ConfigHTTP] = None

    mcp: Optional[object] = None

    openapi: Optional[ConfigOpenAPI] = None
