# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .agents.agent_schedule_spec import AgentScheduleSpec

__all__ = ["AgentScheduleEntry"]


class AgentScheduleEntry(BaseModel):
    name: str

    spec: AgentScheduleSpec
    """AgentScheduleSpec is the user-provided configuration for a schedule."""

    labels: Optional[Dict[str, str]] = None

    state: Optional[Literal["STATE_UNSPECIFIED", "STATE_ACTIVE", "STATE_PAUSED", "STATE_ARCHIVED"]] = None
    """Desired lifecycle state for the schedule.

    Defaults to STATE_ACTIVE when unspecified. Declare STATE_PAUSED to provision a
    schedule without it firing. STATE_ARCHIVED is rejected here.
    """
