# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["WorkspaceAdminListParams"]


class WorkspaceAdminListParams(TypedDict, total=False):
    cursor: str
    """Pagination cursor from previous response"""

    include_archived: Annotated[bool, PropertyInfo(alias="includeArchived")]
    """When true, archived workspaces are included in the results.

    Defaults to false (active workspaces only).
    """

    limit: int
    """Maximum number of results to return"""
