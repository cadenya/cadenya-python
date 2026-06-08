# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .tool_filter_param import ToolFilterParam
from .approval_requirement_filter_param import ApprovalRequirementFilterParam

__all__ = ["ToolSetAdapterMcpParam"]


class ToolSetAdapterMcpParam(TypedDict, total=False):
    exclude_tools: Annotated[ToolFilterParam, PropertyInfo(alias="excludeTools")]
    """Top-level filter with simple boolean logic (no nesting)"""

    headers: Dict[str, str]

    include_tools: Annotated[ToolFilterParam, PropertyInfo(alias="includeTools")]
    """Top-level filter with simple boolean logic (no nesting)"""

    tool_approvals: Annotated[ApprovalRequirementFilterParam, PropertyInfo(alias="toolApprovals")]
    """
    Approval filters that will automatically set the approval requirement on tools
    synced from an external source
    """

    url: str
