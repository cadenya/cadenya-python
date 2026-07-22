# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .objective_event_data import ObjectiveEventData
from .objective_event_info import ObjectiveEventInfo
from .shared.operation_metadata import OperationMetadata

__all__ = ["ObjectiveEvent"]


class ObjectiveEvent(BaseModel):
    data: ObjectiveEventData

    metadata: OperationMetadata
    """
    Metadata for ephemeral operations and activities (e.g., objectives, executions,
    runs)
    """

    context_window_id: Optional[str] = FieldInfo(alias="contextWindowId", default=None)

    duration: Optional[str] = None
    """
    Elapsed time of the work this event records, when it is known at write time
    (e.g. assistant message generation, tool execution for result/error events).
    Unset means the event is instantaneous or the duration is not measurable.
    Serialized as a canonical duration string (e.g. "4.1s"). Always set together
    with started_at.
    """

    info: Optional[ObjectiveEventInfo] = None

    started_at: Optional[datetime] = FieldInfo(alias="startedAt", default=None)
    """When the work this event records began.

    Set together with duration, so the work interval is [started_at, started_at +
    duration]. The event's created_at remains the time the event was persisted.
    """
