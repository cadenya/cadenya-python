# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["ToolListParams"]


class ToolListParams(TypedDict, total=False):
    workspace_id: Required[Annotated[str, PropertyInfo(alias="workspaceId")]]

    cursor: str
    """Pagination cursor from previous response"""

    include_info: Annotated[bool, PropertyInfo(alias="includeInfo")]
    """When set to true you may use more of your alloted API rate-limit"""

    labels: str
    """Filters by metadata labels.

    Comma-separated key=value pairs, e.g. "env=prod,team=ai". A resource matches
    only if every pair matches exactly (AND semantics).
    """

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

    states: List[Literal["STATE_UNSPECIFIED", "STATE_AVAILABLE", "STATE_OMITTED", "STATE_ARCHIVED"]]
    """Filter by tool state. Multiple values are OR'd together."""
