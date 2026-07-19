# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .tool_set_event_data_sync_failed import ToolSetEventDataSyncFailed
from .tool_set_event_data_sync_started import ToolSetEventDataSyncStarted
from .tool_set_event_data_sync_completed import ToolSetEventDataSyncCompleted

__all__ = ["ToolSetEventData"]

ToolSetEventData: TypeAlias = Annotated[
    Union[ToolSetEventDataSyncStarted, ToolSetEventDataSyncCompleted, ToolSetEventDataSyncFailed],
    PropertyInfo(discriminator="type"),
]
