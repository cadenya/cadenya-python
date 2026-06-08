# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel
from .agents.agent_schedule_spec import AgentScheduleSpec

__all__ = ["AgentScheduleEntry"]


class AgentScheduleEntry(BaseModel):
    name: str

    spec: AgentScheduleSpec
    """AgentScheduleSpec is the user-provided configuration for a schedule."""

    labels: Optional[Dict[str, str]] = None
