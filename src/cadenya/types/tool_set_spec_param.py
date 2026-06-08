# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .tool_set_adapter_param import ToolSetAdapterParam

__all__ = ["ToolSetSpecParam"]


class ToolSetSpecParam(TypedDict, total=False):
    adapter: ToolSetAdapterParam

    description: str
