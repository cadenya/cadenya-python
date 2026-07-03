# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .tool_filter import ToolFilter
from .approval_requirement_filter import ApprovalRequirementFilter

__all__ = ["ToolSetAdapterMcp", "JustInTime"]


class JustInTime(BaseModel):
    """Defines behavior for just-in-time capable tool set adapters (IE: MCP)."""

    enabled: Optional[bool] = None

    fail_objective_on_tool_list_error: Optional[bool] = FieldInfo(alias="failObjectiveOnToolListError", default=None)
    """
    If set, an objective will automatically be failed if tools cannot be loaded in
    the initial stages of an objective being created. Tools are loaded
    asynchronously, so this setting is useful for ensuring that an objective
    continued any further if tools are not available.
    """


class ToolSetAdapterMcp(BaseModel):
    exclude_tools: Optional[ToolFilter] = FieldInfo(alias="excludeTools", default=None)
    """Top-level filter with simple boolean logic (no nesting)"""

    headers: Optional[Dict[str, str]] = None

    include_tools: Optional[ToolFilter] = FieldInfo(alias="includeTools", default=None)
    """Top-level filter with simple boolean logic (no nesting)"""

    just_in_time: Optional[JustInTime] = FieldInfo(alias="justInTime", default=None)
    """Defines behavior for just-in-time capable tool set adapters (IE: MCP)."""

    tool_approvals: Optional[ApprovalRequirementFilter] = FieldInfo(alias="toolApprovals", default=None)
    """
    Approval filters that will automatically set the approval requirement on tools
    synced from an external source
    """

    url: Optional[str] = None
