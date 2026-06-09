# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

from .tool_sets.tool_spec_param import ToolSpecParam

__all__ = ["ToolEntryParam"]


class ToolEntryParam(TypedDict, total=False):
    name: Required[str]

    spec: Required[ToolSpecParam]

    labels: Dict[str, str]

    state: Literal["STATE_UNSPECIFIED", "STATE_AVAILABLE", "STATE_OMITTED", "STATE_ARCHIVED"]
    """Desired lifecycle state for the tool.

    Defaults to STATE_AVAILABLE when unspecified. STATE_ARCHIVED is server-managed
    and is rejected here.
    """
