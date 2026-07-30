# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TenantListParams"]


class TenantListParams(TypedDict, total=False):
    workspace_id: Annotated[str, PropertyInfo(alias="workspaceId")]

    cursor: str
    """Pagination cursor from previous response."""

    include_info: Annotated[bool, PropertyInfo(alias="includeInfo")]
    """When true, the `info` field on each returned tenant is populated.

    This costs several count queries per tenant, so it is off by default.
    """

    labels: str
    """Filters by metadata labels.

    Comma-separated key=value pairs, e.g. "env=prod,team=ai". A resource matches
    only if every pair matches exactly (AND semantics).
    """

    limit: int
    """Maximum number of results to return."""

    query: str
    """Substring match against the tenant's name and external_id.

    Built for type-ahead filter pickers, where the operator knows the customer's own
    identifier rather than Cadenya's.
    """

    sort_order: Annotated[str, PropertyInfo(alias="sortOrder")]
    """Sort order for results (asc or desc by creation time)."""
