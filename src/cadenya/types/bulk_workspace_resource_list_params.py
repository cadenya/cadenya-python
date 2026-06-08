# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["BulkWorkspaceResourceListParams"]


class BulkWorkspaceResourceListParams(TypedDict, total=False):
    bundle_key: Annotated[str, PropertyInfo(alias="bundleKey")]
    """Filter by bundle_key — list every apply for a given bundle."""

    cursor: str
    """Pagination cursor from previous response"""

    limit: int
    """Maximum number of results to return"""

    sort_order: Annotated[str, PropertyInfo(alias="sortOrder")]
    """Sort order for results (asc or desc by creation time)"""

    state: Literal[
        "STATE_UNSPECIFIED",
        "STATE_PENDING",
        "STATE_VALIDATING",
        "STATE_RUNNING",
        "STATE_SUCCEEDED",
        "STATE_PARTIALLY_APPLIED",
        "STATE_FAILED",
        "STATE_CANCELLED",
    ]
    """Filter by lifecycle state."""
