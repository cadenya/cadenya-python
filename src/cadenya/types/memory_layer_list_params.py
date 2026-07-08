# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MemoryLayerListParams"]


class MemoryLayerListParams(TypedDict, total=False):
    agent_id: Annotated[str, PropertyInfo(alias="agentId")]
    """Filter to episodic layers belonging to this agent."""

    cursor: str
    """Pagination cursor from previous response"""

    episodic_key_prefix: Annotated[str, PropertyInfo(alias="episodicKeyPrefix")]
    """Filter to episodic layers whose episodic key starts with this prefix (e.g.

    "customer/" matches "customer/42" and "customer/43"). Useful for namespaced
    keys, similar to a redis key scan.
    """

    include_info: Annotated[bool, PropertyInfo(alias="includeInfo")]
    """When set to true you may use more of your alloted API rate-limit"""

    labels: str
    """Filters by metadata labels.

    Comma-separated key=value pairs, e.g. "env=prod,team=ai". A resource matches
    only if every pair matches exactly (AND semantics).
    """

    limit: int
    """Maximum number of results to return"""

    prefix: str
    """Filter expression (query param: prefix)"""

    query: str
    """Free-form search query"""

    sort_order: Annotated[str, PropertyInfo(alias="sortOrder")]
    """Sort order for results (asc or desc by creation time)"""

    type: Literal["MEMORY_LAYER_TYPE_UNSPECIFIED", "MEMORY_LAYER_TYPE_EPISODIC", "MEMORY_LAYER_TYPE_SKILLS"]
    """Filter by layer type"""
