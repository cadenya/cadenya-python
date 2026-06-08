# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ResultListParams"]


class ResultListParams(TypedDict, total=False):
    workspace_id: Required[Annotated[str, PropertyInfo(alias="workspaceId")]]

    action: Literal[
        "ACTION_UNSPECIFIED", "ACTION_CREATED", "ACTION_UPDATED", "ACTION_UNCHANGED", "ACTION_DELETED", "ACTION_FAILED"
    ]
    """Filter by action."""

    cursor: str
    """Pagination cursor from previous response"""

    limit: int
    """Maximum number of results to return"""

    sort_order: Annotated[str, PropertyInfo(alias="sortOrder")]
    """Sort order for results (asc or desc by creation time)"""

    type: str
    """Filter by data.type discriminator (e.g., "toolSet", "memoryEntry")."""
