# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .objective_event import ObjectiveEvent
from .shared.resource_metadata import ResourceMetadata
from .shared.operation_metadata import OperationMetadata

__all__ = ["UnsafeUnwrapWebhookEvent", "Data"]


class Data(BaseModel):
    """
    The webhook data payload with flat top-level keys for agent, variation, objective, and event.
    """

    agent: ResourceMetadata
    """
    Standard metadata for persistent, named resources (e.g., agents, tools, prompts)
    """

    agent_variation: ResourceMetadata = FieldInfo(alias="agentVariation")
    """
    Standard metadata for persistent, named resources (e.g., agents, tools, prompts)
    """

    objective: OperationMetadata
    """
    Metadata for ephemeral operations and activities (e.g., objectives, executions,
    runs)
    """

    objective_event: ObjectiveEvent = FieldInfo(alias="objectiveEvent")


class UnsafeUnwrapWebhookEvent(BaseModel):
    """The envelope for an objective event webhook delivery.

    Contains timestamp, event type, and the webhook data payload.
    """

    data: Data
    """
    The webhook data payload with flat top-level keys for agent, variation,
    objective, and event.
    """

    timestamp: datetime

    type: str
    """The event type, prefixed with objective_event.

    (e.g., objective_event.tool_result)
    """
