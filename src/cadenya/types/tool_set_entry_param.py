# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

from .tool_entry_param import ToolEntryParam
from .tool_set_spec_param import ToolSetSpecParam

__all__ = ["ToolSetEntryParam"]


class ToolSetEntryParam(TypedDict, total=False):
    name: Required[str]

    spec: Required[ToolSetSpecParam]

    labels: Dict[str, str]

    tools: Dict[str, ToolEntryParam]
    """Tools in this tool set, keyed by external_id."""
