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

    cursor: str
    """Pagination cursor from previous response"""

    include_info: Annotated[bool, PropertyInfo(alias="includeInfo")]
    """When true, populate each item's info (e.g.

    the AI provider), at the cost of extra lookups.
    """

    is_assigned: Annotated[bool, PropertyInfo(alias="isAssigned")]
    """
    Filter models to only ones assigned to an active agent variation/agent. Draft
    agents count as assigned; archived agents do not. Assignment does not imply
    recent traffic — see ModelInfo.last_used_at for that.
    """

    labels: str
    """Filters by metadata labels.

    Comma-separated key=value pairs, e.g. "env=prod,team=ai". A resource matches
    only if every pair matches exactly (AND semantics).
    """

    limit: int
    """Maximum number of results to return"""

    prefix: str
    """
    Filter by a prefix of the model's display name, external id, or id
    (case-insensitive). A model's external id is the form used in
    modelConfig.modelId, so a caller holding that can narrow the list by it.
    """

    query: str
    """Free-form search query"""

    sort_order: Annotated[str, PropertyInfo(alias="sortOrder")]
    """Sort order for results (asc or desc by creation time)"""

    state: Literal["STATE_UNSPECIFIED", "STATE_ENABLED", "STATE_DISABLED"]
    """Filter by model state"""
