# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["WidgetListParams"]


class WidgetListParams(TypedDict, total=False):
    workspace_id: Annotated[str, PropertyInfo(alias="workspaceId")]

    agent_id: Annotated[str, PropertyInfo(alias="agentId")]
    """Filter to widgets bound to a specific agent.

    Accepts the canonical `agent_…` form or the `external_id:<value>` form.
    """

    cursor: str
    """Pagination cursor from previous response."""

    include_info: Annotated[bool, PropertyInfo(alias="includeInfo")]
    """
    When true, the `info` field on each returned widget is populated. Requests with
    this flag count more against your rate limit.
    """

    labels: str
    """Filters by metadata labels.

    Comma-separated key=value pairs, e.g. "env=prod,team=ai". A resource matches
    only if every pair matches exactly (AND semantics).
    """

    limit: int
    """Maximum number of results to return."""

    sort_order: Annotated[str, PropertyInfo(alias="sortOrder")]
    """Sort order for results (asc or desc by creation time)."""
