# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ModelListParams"]


class ModelListParams(TypedDict, total=False):
    ai_provider_key_id: Annotated[str, PropertyInfo(alias="aiProviderKeyId")]
    """Filter to models provisioned on a specific AI provider key.

    Accepts the key's id or an "external_id:"-prefixed slug.
    """

    bundle_key: Annotated[str, PropertyInfo(alias="bundleKey")]
    """Filter by bundle_key — return only resources owned by this bundle."""

    cursor: str
    """Pagination cursor from previous response"""

    include_info: Annotated[bool, PropertyInfo(alias="includeInfo")]
    """When true, populate each item's info (e.g.

    the AI provider), at the cost of extra lookups.
    """

    limit: int
    """Maximum number of results to return"""

    prefix: str
    """Filter by name prefix"""

    query: str
    """Free-form search query"""

    sort_order: Annotated[str, PropertyInfo(alias="sortOrder")]
    """Sort order for results (asc or desc by creation time)"""

    status: Literal["MODEL_STATUS_UNSPECIFIED", "MODEL_STATUS_ENABLED", "MODEL_STATUS_DISABLED"]
    """Filter by model status"""
