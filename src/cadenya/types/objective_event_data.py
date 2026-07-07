# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

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

__all__ = ["ObjectiveEventData", "Cancelled", "Finalized", "Notice", "TimedOut"]


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


class Notice(BaseModel):
    """
    Notice is a non-terminal diagnostic emitted by the runtime when something
     noteworthy but non-fatal happens during an objective — for example a
     just-in-time tool set failing to load, or a previously loaded tool being
     dropped because it was archived. Notices carry no structured payload; they
     exist to make the objective timeline self-explanatory.
    """

    key: Optional[str] = None
    """
    Stable machine-readable identifier for the notice kind (for example
    "tool_set_load_failed", "tool_archived"). Clients can switch on it or use it as
    an i18n key; the message is the English fallback.
    """

    level: Optional[Literal["LEVEL_UNSPECIFIED", "LEVEL_INFO", "LEVEL_WARN"]] = None

    message: Optional[str] = None
    """Human-readable description of what happened."""


class TimedOut(BaseModel):
    """
    ObjectiveTimedOut is the terminal event written when an objective is
     finalized by the inactivity sweep because it saw no activity (no user
     messages, no LLM calls) within its variation's inactivity timeout — or the
     system-wide 24 hour maximum when no timeout is configured. The objective
     produces no output. After this event, the objective is super-terminal: no
     further iterations, compaction, or continuation are permitted.
    """

    message: Optional[str] = None
    """Human-readable note recorded at timeout time (e.g.

    "Timed out after 2h of inactivity").
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

    notice: Optional[Notice] = None
    """
    Notice is a non-terminal diagnostic emitted by the runtime when something
    noteworthy but non-fatal happens during an objective — for example a
    just-in-time tool set failing to load, or a previously loaded tool being dropped
    because it was archived. Notices carry no structured payload; they exist to make
    the objective timeline self-explanatory.
    """

    sub_agent_spawned: Optional[SubAgentSpawned] = FieldInfo(alias="subAgentSpawned", default=None)

    sub_agent_updated: Optional[SubAgentUpdated] = FieldInfo(alias="subAgentUpdated", default=None)

    timed_out: Optional[TimedOut] = FieldInfo(alias="timedOut", default=None)
    """
    ObjectiveTimedOut is the terminal event written when an objective is finalized
    by the inactivity sweep because it saw no activity (no user messages, no LLM
    calls) within its variation's inactivity timeout — or the system-wide 24 hour
    maximum when no timeout is configured. The objective produces no output. After
    this event, the objective is super-terminal: no further iterations, compaction,
    or continuation are permitted.
    """

    tool_approval_requested: Optional[ToolApprovalRequested] = FieldInfo(alias="toolApprovalRequested", default=None)

    tool_approved: Optional[ToolApproved] = FieldInfo(alias="toolApproved", default=None)

    tool_called: Optional[ToolCalled] = FieldInfo(alias="toolCalled", default=None)

    tool_denied: Optional[ToolDenied] = FieldInfo(alias="toolDenied", default=None)

    tool_error: Optional[ToolError] = FieldInfo(alias="toolError", default=None)

    tool_result: Optional[ToolResult] = FieldInfo(alias="toolResult", default=None)

    type: Optional[str] = None

    user_message: Optional[UserMessage] = FieldInfo(alias="userMessage", default=None)
