# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .config_mcp import ConfigMcp
from .config_bare import ConfigBare
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

    bare: Optional[ConfigBare] = None
    """
    Marks the tool as bare: it has no execution adapter of its own and relies on the
    parent tool set being a Bare tool set. Present so a webhook consumer can tell a
    tool is bare from the tool data alone, without cross-referencing the tool set.
    """

    http: Optional[ConfigHTTP] = None

    mcp: Optional[ConfigMcp] = None

    openapi: Optional[ConfigOpenAPI] = None
