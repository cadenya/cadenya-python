# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .tool_error import ToolError
from .memory_read import MemoryRead
from .tool_called import ToolCalled
from .tool_denied import ToolDenied
from .tool_result import ToolResult
from .user_message import UserMessage
from .tool_approved import ToolApproved
from .objective_error import ObjectiveError
from .assistant_message import AssistantMessage
from .sub_agent_spawned import SubAgentSpawned
from .sub_agent_updated import SubAgentUpdated
from .tool_approval_requested import ToolApprovalRequested
from .context_window_compacted import ContextWindowCompacted

__all__ = ["ObjectiveEventData", "Cancelled", "Finalized"]


class Cancelled(BaseModel):
    """ObjectiveCancelled is the terminal event written when an objective is
     cancelled.

    After this event, the objective is super-terminal: no further
     iterations, compaction, or continuation are permitted.
    """

    message: Optional[str] = None
    """Optional human-readable note recorded at cancel time.

    Today the workflow sets "Cancelled" but this field leaves room for richer
    reasons (e.g. "Cancelled by user", "Cancelled by schedule sweep", "Credit
    balance exhausted").
    """


class Finalized(BaseModel):
    """ObjectiveFinalized is the terminal event written when an objective is
     finalized.

    After this event, the objective is super-terminal: no further
     iterations, compaction, or continuation are permitted.
    """

    output: Optional[object] = None
    """
    If the objective was created with an output schema, and the agent successfully
    completed the objective, this field will contain the structured output of the
    objective.
    """


class ObjectiveEventData(BaseModel):
    assistant_message: Optional[AssistantMessage] = FieldInfo(alias="assistantMessage", default=None)

    cancelled: Optional[Cancelled] = None
    """ObjectiveCancelled is the terminal event written when an objective is cancelled.

    After this event, the objective is super-terminal: no further iterations,
    compaction, or continuation are permitted.
    """

    context_window_compacted: Optional[ContextWindowCompacted] = FieldInfo(alias="contextWindowCompacted", default=None)

    error: Optional[ObjectiveError] = None

    finalized: Optional[Finalized] = None
    """ObjectiveFinalized is the terminal event written when an objective is finalized.

    After this event, the objective is super-terminal: no further iterations,
    compaction, or continuation are permitted.
    """

    memory_read: Optional[MemoryRead] = FieldInfo(alias="memoryRead", default=None)
    """
    MemoryRead is emitted each time the agent resolves a key against the memory
    cascade and loads an entry. Lookups that miss (key not found in any layer) do
    not emit this event.
    """

    sub_agent_spawned: Optional[SubAgentSpawned] = FieldInfo(alias="subAgentSpawned", default=None)

    sub_agent_updated: Optional[SubAgentUpdated] = FieldInfo(alias="subAgentUpdated", default=None)

    tool_approval_requested: Optional[ToolApprovalRequested] = FieldInfo(alias="toolApprovalRequested", default=None)

    tool_approved: Optional[ToolApproved] = FieldInfo(alias="toolApproved", default=None)

    tool_called: Optional[ToolCalled] = FieldInfo(alias="toolCalled", default=None)

    tool_denied: Optional[ToolDenied] = FieldInfo(alias="toolDenied", default=None)

    tool_error: Optional[ToolError] = FieldInfo(alias="toolError", default=None)

    tool_result: Optional[ToolResult] = FieldInfo(alias="toolResult", default=None)

    type: Optional[str] = None

    user_message: Optional[UserMessage] = FieldInfo(alias="userMessage", default=None)
