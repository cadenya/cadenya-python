# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ScheduleListParams"]


class ScheduleListParams(TypedDict, total=False):
    workspace_id: Required[Annotated[str, PropertyInfo(alias="workspaceId")]]

    bundle_key: Annotated[str, PropertyInfo(alias="bundleKey")]
    """Filter by bundle_key — return only resources owned by this bundle."""

    cursor: str
    """Pagination cursor from previous response."""

    include_info: Annotated[bool, PropertyInfo(alias="includeInfo")]
    """
    When true, the `info` field on each returned schedule is populated. Requests
    with this flag count more against your rate limit.
    """

    limit: int
    """Maximum number of results to return."""

    prefix: str
    """Filter expression (query param: prefix)."""

    query: str
    """Free-form search query."""

    sort_order: Annotated[str, PropertyInfo(alias="sortOrder")]
    """Sort order for results (asc or desc by creation time)."""
