# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .tool_filter_param import ToolFilterParam
from .approval_requirement_filter_param import ApprovalRequirementFilterParam

__all__ = ["ToolSetAdapterOpenAPIParam"]


class ToolSetAdapterOpenAPIParam(TypedDict, total=False):
    base_url: Annotated[str, PropertyInfo(alias="baseUrl")]
    """Base URL for dispatching tool calls.

    If set, overrides the server resolved from the spec's servers array.
    """

    exclude_tools: Annotated[ToolFilterParam, PropertyInfo(alias="excludeTools")]
    """Top-level filter with simple boolean logic (no nesting)"""

    headers: Dict[str, str]
    """Headers sent when fetching the spec from a URL and when dispatching tool calls."""

    include_tools: Annotated[ToolFilterParam, PropertyInfo(alias="includeTools")]
    """Top-level filter with simple boolean logic (no nesting)"""

    server_name: Annotated[str, PropertyInfo(alias="serverName")]
    """
    Name of the server entry in the spec's servers array (OpenAPI 3.2 server.name
    field). Used to select which server URL to dispatch to when base_url is not set.
    If unset, the first server is used. Ignored when base_url is set.
    """

    tool_approvals: Annotated[ApprovalRequirementFilterParam, PropertyInfo(alias="toolApprovals")]
    """
    Approval filters that will automatically set the approval requirement on tools
    synced from an external source
    """

    upload_id: Annotated[str, PropertyInfo(alias="uploadId")]
    """ID of a COMPLETE Upload containing the OpenAPI spec document."""

    url: str
    """URL to fetch the OpenAPI spec from. Synced automatically every hour."""
