# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["WorkspaceSecretListParams"]


class WorkspaceSecretListParams(TypedDict, total=False):
    cursor: str
    """Pagination cursor from previous response"""

    include_info: Annotated[bool, PropertyInfo(alias="includeInfo")]
    """When set to true you may use more of your alloted API rate-limit"""

    limit: int
    """Maximum number of results to return"""

    prefix: str
    """Filter expression (query param: prefix)"""

    query: str
    """Free-form search query"""

    sort_order: Annotated[str, PropertyInfo(alias="sortOrder")]
    """Sort order for results (asc or desc by creation time)"""
