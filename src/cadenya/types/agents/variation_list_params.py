# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["VariationListParams"]


class VariationListParams(TypedDict, total=False):
    workspace_id: Required[Annotated[str, PropertyInfo(alias="workspaceId")]]

    cursor: str
    """Pagination cursor from previous response"""

    include_info: Annotated[bool, PropertyInfo(alias="includeInfo")]
    """
    When true, the `info` field on each returned variation is populated. Requests
    with this flag count more against your rate limit.
    """

    limit: int
    """Maximum number of results to return"""

    sort_order: Annotated[str, PropertyInfo(alias="sortOrder")]
    """Sort order for results (asc or desc by creation time)"""
