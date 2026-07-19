# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .tool_filter_param import ToolFilterParam

__all__ = ["ApprovalRequirementFilterOnlyParam"]


class ApprovalRequirementFilterOnlyParam(TypedDict, total=False):
    only: Required[ToolFilterParam]
    """Top-level filter with simple boolean logic (no nesting)"""

    type: Required[Literal["only"]]
