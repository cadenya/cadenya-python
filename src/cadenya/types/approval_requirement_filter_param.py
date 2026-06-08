# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .tool_filter_param import ToolFilterParam

__all__ = ["ApprovalRequirementFilterParam"]


class ApprovalRequirementFilterParam(TypedDict, total=False):
    """
    Approval filters that will automatically set the approval requirement on tools synced from an external source
    """

    always: bool

    only: ToolFilterParam
    """Top-level filter with simple boolean logic (no nesting)"""
