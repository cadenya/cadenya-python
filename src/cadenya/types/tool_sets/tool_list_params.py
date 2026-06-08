# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["ToolListParams"]


class ToolListParams(TypedDict, total=False):
    workspace_id: Required[Annotated[str, PropertyInfo(alias="workspaceId")]]

    bundle_key: Annotated[str, PropertyInfo(alias="bundleKey")]
    """Filter by bundle_key — return only resources owned by this bundle."""

    cursor: str
    """Pagination cursor from previous response"""

    include_info: Annotated[bool, PropertyInfo(alias="includeInfo")]
    """When set to true you may use more of your alloted API rate-limit"""

    limit: int
    """Maximum number of results to return"""

    names: SequenceNotStr[str]
    """Filter by tool name (exact match). Multiple values are OR'd together."""

    prefix: str
    """Filter expression (query param: prefix)"""

    query: str
    """Free-form search query"""

    requires_approval: Annotated[bool, PropertyInfo(alias="requiresApproval")]
    """Filter by approval requirement.

    Omitted = no filter; true = only tools requiring approval; false = only tools
    not requiring approval.
    """

    sort_order: Annotated[str, PropertyInfo(alias="sortOrder")]
    """Sort order for results (asc or desc by creation time)"""

    statuses: List[
        Literal["TOOL_STATUS_UNSPECIFIED", "TOOL_STATUS_AVAILABLE", "TOOL_STATUS_OMITTED", "TOOL_STATUS_ARCHIVED"]
    ]
    """Filter by tool status. Multiple values are OR'd together."""
