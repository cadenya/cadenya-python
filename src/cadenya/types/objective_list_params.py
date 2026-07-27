# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ObjectiveListParams"]


class ObjectiveListParams(TypedDict, total=False):
    workspace_id: Annotated[str, PropertyInfo(alias="workspaceId")]

    agent_id: Annotated[str, PropertyInfo(alias="agentId")]
    """Agent ID for filtering"""

    agent_schedule_id: Annotated[str, PropertyInfo(alias="agentScheduleId")]
    """Filter to objectives produced by a specific AgentSchedule.

    Accepts canonical as\\__… form or external_id:<value> form.
    """

    cursor: str
    """Pagination cursor from previous response"""

    include_info: Annotated[bool, PropertyInfo(alias="includeInfo")]
    """When set to true you may use more of your alloted API rate-limit"""

    labels: str
    """Filters by metadata labels.

    Comma-separated key=value pairs, e.g. "env=prod,team=ai". A resource matches
    only if every pair matches exactly (AND semantics).
    """

    limit: int
    """Maximum number of results to return"""

    parent_objective_id: Annotated[str, PropertyInfo(alias="parentObjectiveId")]
    """Optional filters"""

    profile_id: Annotated[str, PropertyInfo(alias="profileId")]

    sort_order: Annotated[str, PropertyInfo(alias="sortOrder")]
    """Sort order for results (asc or desc by creation time)"""

    state: Literal[
        "STATE_UNSPECIFIED",
        "STATE_PENDING",
        "STATE_RUNNING",
        "STATE_WAITING",
        "STATE_FAILED",
        "STATE_CANCELLED",
        "STATE_FINALIZED",
        "STATE_TIMED_OUT",
    ]
    """Filter by state"""

    subject_id: Annotated[str, PropertyInfo(alias="subjectId")]
    """Filter to objectives associated with a subject.

    Accepts the canonical `subj_…` form or the `external_id:<value>` form; the
    external_id form is scoped within a tenant and requires `tenant_id` to also be
    set.
    """

    tenant_id: Annotated[str, PropertyInfo(alias="tenantId")]
    """Filter to objectives associated with a tenant.

    Accepts the canonical `tenant_…` form or the `external_id:<value>` form.
    """

    widget_id: Annotated[str, PropertyInfo(alias="widgetId")]
    """Filter to objectives whose conversation ran through a widget.

    Accepts the canonical `wgt_…` form or the `external_id:<value>` form.
    """

    widget_session_id: Annotated[str, PropertyInfo(alias="widgetSessionId")]
    """Filter to objectives created by a specific widget session."""
