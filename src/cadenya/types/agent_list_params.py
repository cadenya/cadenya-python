# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AgentListParams"]


class AgentListParams(TypedDict, total=False):
    bundle_key: Annotated[str, PropertyInfo(alias="bundleKey")]
    """Filter by bundle_key — return only resources owned by this bundle."""

    cursor: str
    """Pagination cursor from previous response"""

    include_info: Annotated[bool, PropertyInfo(alias="includeInfo")]
    """When true, the `info` field on each returned agent is populated.

    Requests with this flag count more against your rate limit.
    """

    limit: int
    """Maximum number of results to return"""

    prefix: str
    """Filter expression (query param: prefix)"""

    query: str
    """Free-form search query"""

    sort_order: Annotated[str, PropertyInfo(alias="sortOrder")]
    """Sort order for results (asc or desc by creation time)"""

    status: Literal["AGENT_STATUS_UNSPECIFIED", "AGENT_STATUS_DRAFT", "AGENT_STATUS_PUBLISHED", "AGENT_STATUS_ARCHIVED"]
    """Filter by agent publication status"""

    variation_selection_mode: Annotated[
        Literal[
            "VARIATION_SELECTION_MODE_UNSPECIFIED",
            "VARIATION_SELECTION_MODE_RANDOM",
            "VARIATION_SELECTION_MODE_WEIGHTED",
        ],
        PropertyInfo(alias="variationSelectionMode"),
    ]
    """Filter by variation selection mode"""
