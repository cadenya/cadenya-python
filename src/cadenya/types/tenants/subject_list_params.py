# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SubjectListParams"]


class SubjectListParams(TypedDict, total=False):
    workspace_id: Annotated[str, PropertyInfo(alias="workspaceId")]

    cursor: str
    """Pagination cursor from previous response."""

    include_info: Annotated[bool, PropertyInfo(alias="includeInfo")]
    """When true, the `info` field on each returned subject is populated."""

    limit: int
    """Maximum number of results to return."""

    query: str
    """Substring match against the subject's name and external_id."""

    sort_order: Annotated[str, PropertyInfo(alias="sortOrder")]
    """Sort order for results (asc or desc by creation time)."""
