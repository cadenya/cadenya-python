# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ObjectiveListParams"]


class ObjectiveListParams(TypedDict, total=False):
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
    ]
    """Filter by state"""
