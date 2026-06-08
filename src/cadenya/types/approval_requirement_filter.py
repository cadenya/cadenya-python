# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .tool_filter import ToolFilter

__all__ = ["ApprovalRequirementFilter"]


class ApprovalRequirementFilter(BaseModel):
    """
    Approval filters that will automatically set the approval requirement on tools synced from an external source
    """

    always: Optional[bool] = None

    only: Optional[ToolFilter] = None
    """Top-level filter with simple boolean logic (no nesting)"""
