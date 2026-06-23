# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["APIKeyListParams"]


class APIKeyListParams(TypedDict, total=False):
    cursor: str
    """Pagination cursor from previous response."""

    include_info: Annotated[bool, PropertyInfo(alias="includeInfo")]
    """When true, included info fields are populated.

    Requests with this flag count more against your rate limit.
    """

    limit: int
    """Maximum number of results to return."""

    prefix: str
    """Filter by ID prefix."""

    query: str
    """Free-form search query."""

    sort_order: Annotated[str, PropertyInfo(alias="sortOrder")]
    """Sort order for results (asc or desc by creation time)."""
