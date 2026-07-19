# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .tool_filter_param import ToolFilterParam
from .approval_requirement_filter_param import ApprovalRequirementFilterParam

__all__ = ["ToolSetAdapterMCPParam", "JustInTime"]


class JustInTime(TypedDict, total=False):
    """Defines behavior for just-in-time capable tool set adapters (IE: MCP)."""

    enabled: bool

    fail_objective_on_tool_list_error: Annotated[bool, PropertyInfo(alias="failObjectiveOnToolListError")]
    """
    If set, an objective will automatically be failed if tools cannot be loaded in
    the initial stages of an objective being created. Tools are loaded
    asynchronously, so this setting is useful for ensuring that an objective
    continued any further if tools are not available.
    """


class ToolSetAdapterMCPParam(TypedDict, total=False):
    exclude_tools: Annotated[ToolFilterParam, PropertyInfo(alias="excludeTools")]
    """Top-level filter with simple boolean logic (no nesting)"""

    headers: Dict[str, str]

    include_tools: Annotated[ToolFilterParam, PropertyInfo(alias="includeTools")]
    """Top-level filter with simple boolean logic (no nesting)"""

    just_in_time: Annotated[JustInTime, PropertyInfo(alias="justInTime")]
    """Defines behavior for just-in-time capable tool set adapters (IE: MCP)."""

    tool_approvals: Annotated[ApprovalRequirementFilterParam, PropertyInfo(alias="toolApprovals")]
    """
    Approval filters that will automatically set the approval requirement on tools
    synced from an external source
    """

    url: str
