# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .tool_filter import ToolFilter
from .approval_requirement_filter import ApprovalRequirementFilter

__all__ = ["ToolSetAdapterMcp"]


class ToolSetAdapterMcp(BaseModel):
    exclude_tools: Optional[ToolFilter] = FieldInfo(alias="excludeTools", default=None)
    """Top-level filter with simple boolean logic (no nesting)"""

    headers: Optional[Dict[str, str]] = None

    include_tools: Optional[ToolFilter] = FieldInfo(alias="includeTools", default=None)
    """Top-level filter with simple boolean logic (no nesting)"""

    tool_approvals: Optional[ApprovalRequirementFilter] = FieldInfo(alias="toolApprovals", default=None)
    """
    Approval filters that will automatically set the approval requirement on tools
    synced from an external source
    """

    url: Optional[str] = None
