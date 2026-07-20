# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .config_mcp_param import ConfigMCPParam

__all__ = ["ToolSpecConfigMCPParam"]


class ToolSpecConfigMCPParam(TypedDict, total=False):
    mcp: Required[ConfigMCPParam]

    type: Required[Literal["mcp"]]
