# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .tool_set_adapter_mcp_param import ToolSetAdapterMCPParam

__all__ = ["ToolSetAdapterMCPVariantParam"]


class ToolSetAdapterMCPVariantParam(TypedDict, total=False):
    mcp: Required[ToolSetAdapterMCPParam]

    type: Required[Literal["mcp"]]
