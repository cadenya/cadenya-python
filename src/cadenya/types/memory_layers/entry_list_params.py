# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["EntryListParams"]


class EntryListParams(TypedDict, total=False):
    workspace_id: Required[Annotated[str, PropertyInfo(alias="workspaceId")]]

    cursor: str
    """Pagination cursor from previous response"""

    include_info: Annotated[bool, PropertyInfo(alias="includeInfo")]
    """When set to true you may use more of your alloted API rate-limit"""

    limit: int
    """Maximum number of results to return"""

    prefix: str
    """
    Filter by key prefix (e.g., "skills/postmortem/" to list all entries under that
    hierarchy). Matches against the entry's key, not its name.
    """

    query: str
    """Free-form search query"""

    sort_order: Annotated[str, PropertyInfo(alias="sortOrder")]
    """Sort order for results (asc or desc by creation time)"""
