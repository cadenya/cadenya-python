# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TaskListParams"]


class TaskListParams(TypedDict, total=False):
    workspace_id: Annotated[str, PropertyInfo(alias="workspaceId")]

    cursor: str
    """Pagination cursor from previous response"""

    limit: int
    """Maximum number of results to return"""

    sort_order: Annotated[str, PropertyInfo(alias="sortOrder")]
    """Sort order for results"""
