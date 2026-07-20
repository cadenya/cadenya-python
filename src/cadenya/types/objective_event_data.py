# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .objective_event_data_error import ObjectiveEventDataError
from .objective_event_data_notice import ObjectiveEventDataNotice
from .objective_event_data_cancelled import ObjectiveEventDataCancelled
from .objective_event_data_finalized import ObjectiveEventDataFinalized
from .objective_event_data_timed_out import ObjectiveEventDataTimedOut
from .objective_event_data_tool_error import ObjectiveEventDataToolError
from .objective_event_data_memory_read import ObjectiveEventDataMemoryRead
from .objective_event_data_tool_called import ObjectiveEventDataToolCalled
from .objective_event_data_tool_denied import ObjectiveEventDataToolDenied
from .objective_event_data_tool_result import ObjectiveEventDataToolResult
from .objective_event_data_user_message import ObjectiveEventDataUserMessage
from .objective_event_data_tool_approved import ObjectiveEventDataToolApproved
from .objective_event_data_assistant_message import ObjectiveEventDataAssistantMessage
from .objective_event_data_sub_agent_spawned import ObjectiveEventDataSubAgentSpawned
from .objective_event_data_sub_agent_updated import ObjectiveEventDataSubAgentUpdated
from .objective_event_data_tool_approval_requested import ObjectiveEventDataToolApprovalRequested
from .objective_event_data_context_window_compacted import ObjectiveEventDataContextWindowCompacted

__all__ = ["ObjectiveEventData"]

ObjectiveEventData: TypeAlias = Annotated[
    Union[
        ObjectiveEventDataUserMessage,
        ObjectiveEventDataToolApprovalRequested,
        ObjectiveEventDataToolApproved,
        ObjectiveEventDataToolDenied,
        ObjectiveEventDataToolCalled,
        ObjectiveEventDataError,
        ObjectiveEventDataAssistantMessage,
        ObjectiveEventDataToolResult,
        ObjectiveEventDataToolError,
        ObjectiveEventDataContextWindowCompacted,
        ObjectiveEventDataMemoryRead,
        ObjectiveEventDataCancelled,
        ObjectiveEventDataSubAgentSpawned,
        ObjectiveEventDataSubAgentUpdated,
        ObjectiveEventDataFinalized,
        ObjectiveEventDataNotice,
        ObjectiveEventDataTimedOut,
    ],
    PropertyInfo(discriminator="type"),
]
