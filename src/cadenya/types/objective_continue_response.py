# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .objective_event_data import ObjectiveEventData
from .objective_event_info import ObjectiveEventInfo
from .shared.operation_metadata import OperationMetadata

__all__ = ["ObjectiveContinueResponse"]


class ObjectiveContinueResponse(BaseModel):
    data: ObjectiveEventData

    metadata: OperationMetadata
    """
    Metadata for ephemeral operations and activities (e.g., objectives, executions,
    runs)
    """

    context_window_id: Optional[str] = FieldInfo(alias="contextWindowId", default=None)

    info: Optional[ObjectiveEventInfo] = None
