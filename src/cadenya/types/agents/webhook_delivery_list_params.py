# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["WebhookDeliveryListParams"]


class WebhookDeliveryListParams(TypedDict, total=False):
    workspace_id: Required[Annotated[str, PropertyInfo(alias="workspaceId")]]

    cursor: str
    """Pagination cursor from previous response"""

    event_type: Annotated[
        Literal[
            "OBJECTIVE_EVENT_TYPE_UNSPECIFIED",
            "OBJECTIVE_EVENT_TYPE_USER_MESSAGE",
            "OBJECTIVE_EVENT_TYPE_TOOL_APPROVAL_REQUESTED",
            "OBJECTIVE_EVENT_TYPE_TOOL_APPROVED",
            "OBJECTIVE_EVENT_TYPE_TOOL_DENIED",
            "OBJECTIVE_EVENT_TYPE_TOOL_CALLED",
            "OBJECTIVE_EVENT_TYPE_ERROR",
            "OBJECTIVE_EVENT_TYPE_ASSISTANT_MESSAGE",
            "OBJECTIVE_EVENT_TYPE_TOOL_RESULT",
            "OBJECTIVE_EVENT_TYPE_TOOL_ERROR",
            "OBJECTIVE_EVENT_TYPE_CONTEXT_WINDOW_COMPACTED",
            "OBJECTIVE_EVENT_TYPE_MEMORY_READ",
            "OBJECTIVE_EVENT_TYPE_CANCELLED",
            "OBJECTIVE_EVENT_TYPE_SUB_AGENT_SPAWNED",
            "OBJECTIVE_EVENT_TYPE_SUB_AGENT_UPDATED",
            "OBJECTIVE_EVENT_TYPE_FINALIZED",
            "OBJECTIVE_EVENT_TYPE_NOTICE",
            "OBJECTIVE_EVENT_TYPE_TIMED_OUT",
        ],
        PropertyInfo(alias="eventType"),
    ]
    """Optional filter by event type"""

    labels: str
    """Filters by metadata labels.

    Comma-separated key=value pairs, e.g. "env=prod,team=ai". A resource matches
    only if every pair matches exactly (AND semantics).
    """

    limit: int
    """Maximum number of results to return"""

    objective_id: Annotated[str, PropertyInfo(alias="objectiveId")]
    """Optional filter by objective ID"""
