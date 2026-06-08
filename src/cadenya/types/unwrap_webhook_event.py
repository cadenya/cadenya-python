# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .objective_event_data import ObjectiveEventData
from .objective_event_info import ObjectiveEventInfo
from .shared.resource_metadata import ResourceMetadata
from .shared.operation_metadata import OperationMetadata

__all__ = ["UnwrapWebhookEvent", "Data", "DataObjectiveEvent"]


class DataObjectiveEvent(BaseModel):
    data: ObjectiveEventData

    metadata: OperationMetadata
    """
    Metadata for ephemeral operations and activities (e.g., objectives, executions,
    runs)
    """

    context_window_id: Optional[str] = FieldInfo(alias="contextWindowId", default=None)

    info: Optional[ObjectiveEventInfo] = None


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

    objective_event: DataObjectiveEvent = FieldInfo(alias="objectiveEvent")


class UnwrapWebhookEvent(BaseModel):
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
