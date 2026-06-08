# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["WebhookDeliveryData"]


class WebhookDeliveryData(BaseModel):
    agent_id: str = FieldInfo(alias="agentId")
    """Related resources"""

    attempt_count: int = FieldInfo(alias="attemptCount")

    event_type: Literal[
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
    ] = FieldInfo(alias="eventType")
    """The type of objective event that triggered this webhook delivery"""

    http_status_code: int = FieldInfo(alias="httpStatusCode")
    """Response details. The response body is not retained."""

    last_attempt_at: datetime = FieldInfo(alias="lastAttemptAt")

    latency_ms: int = FieldInfo(alias="latencyMs")

    objective_event_id: str = FieldInfo(alias="objectiveEventId")

    objective_id: str = FieldInfo(alias="objectiveId")

    response_content_length: str = FieldInfo(alias="responseContentLength")
    """Content length of the response body in bytes"""

    status: Literal[
        "WEBHOOK_DELIVERY_STATUS_UNSPECIFIED",
        "WEBHOOK_DELIVERY_STATUS_PENDING",
        "WEBHOOK_DELIVERY_STATUS_COMPLETED",
        "WEBHOOK_DELIVERY_STATUS_FAILED",
        "WEBHOOK_DELIVERY_STATUS_DISABLED",
    ]

    webhook_id: str = FieldInfo(alias="webhookId")

    webhook_url: str = FieldInfo(alias="webhookUrl")
    """Webhook delivery details"""

    error_message: Optional[str] = FieldInfo(alias="errorMessage", default=None)

    response_headers: Optional[Dict[str, str]] = FieldInfo(alias="responseHeaders", default=None)
    """Response headers received from the webhook endpoint"""
