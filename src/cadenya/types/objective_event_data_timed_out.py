# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ObjectiveEventDataTimedOut", "TimedOut"]


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


class ObjectiveEventDataTimedOut(BaseModel):
    timed_out: TimedOut = FieldInfo(alias="timedOut")
    """
    ObjectiveTimedOut is the terminal event written when an objective is finalized
    by the inactivity sweep because it saw no activity (no user messages, no LLM
    calls) within its variation's inactivity timeout — or the system-wide 24 hour
    maximum when no timeout is configured. The objective produces no output. After
    this event, the objective is super-terminal: no further iterations, compaction,
    or continuation are permitted.
    """

    type: Literal["timedOut"]
