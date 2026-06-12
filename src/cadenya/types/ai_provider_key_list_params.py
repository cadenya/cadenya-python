# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AIProviderKeyListParams"]


class AIProviderKeyListParams(TypedDict, total=False):
    cursor: str
    """Pagination cursor from previous response"""

    include_info: Annotated[bool, PropertyInfo(alias="includeInfo")]
    """
    When true, populate each item's info (model counts), at the cost of extra
    lookups.
    """

    limit: int
    """Maximum number of results to return"""

    prefix: str
    """Filter expression (query param: prefix)"""

    promotional: bool
    """When true, return only promotional keys (provided by Cadenya, e.g.

    for onboarding). Defaults to returning all keys, customer-provided and
    promotional alike.
    """

    query: str
    """Free-form search query"""

    sort_order: Annotated[str, PropertyInfo(alias="sortOrder")]
    """Sort order for results (asc or desc by creation time)"""
