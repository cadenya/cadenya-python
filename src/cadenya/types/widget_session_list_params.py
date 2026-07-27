# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["WidgetSessionListParams"]


class WidgetSessionListParams(TypedDict, total=False):
    workspace_id: Annotated[str, PropertyInfo(alias="workspaceId")]

    cursor: str
    """Pagination cursor from previous response."""

    include_info: Annotated[bool, PropertyInfo(alias="includeInfo")]
    """
    When true, the `info` field on each returned session is populated. Requests with
    this flag count more against your rate limit.
    """

    labels: str
    """Filters by metadata labels.

    Comma-separated key=value pairs, e.g. "env=prod,team=ai". A resource matches
    only if every pair matches exactly (AND semantics).
    """

    limit: int
    """Maximum number of results to return."""

    sort_order: Annotated[str, PropertyInfo(alias="sortOrder")]
    """Sort order for results (asc or desc by creation time)."""

    state: Literal["STATE_UNSPECIFIED", "STATE_ACTIVE", "STATE_EXPIRED", "STATE_REVOKED", "STATE_EXHAUSTED"]
    """Filter by state."""

    subject_id: Annotated[str, PropertyInfo(alias="subjectId")]
    """Filter to sessions asserted for a subject.

    Accepts the canonical `subj_…` form or the `external_id:<value>` form; the
    external_id form is scoped within a tenant and requires `tenant_id` to also be
    set.
    """

    tenant_id: Annotated[str, PropertyInfo(alias="tenantId")]
    """Filter to sessions belonging to a tenant.

    Accepts the canonical `tenant_…` form or the `external_id:<value>` form.
    """

    widget_id: Annotated[str, PropertyInfo(alias="widgetId")]
    """Filter to sessions on a specific widget.

    Accepts the canonical `wgt_…` form or the `external_id:<value>` form.
    """
