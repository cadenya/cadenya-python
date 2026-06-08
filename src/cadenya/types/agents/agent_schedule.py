# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .agent_schedule_info import AgentScheduleInfo
from .agent_schedule_spec import AgentScheduleSpec
from ..shared.resource_metadata import ResourceMetadata

__all__ = ["AgentSchedule"]


class AgentSchedule(BaseModel):
    """
    AgentSchedule resource — a recurring trigger attached to an agent that
     creates objectives on its cadence.
    """

    metadata: ResourceMetadata
    """
    Standard metadata for persistent, named resources (e.g., agents, tools, prompts)
    """

    spec: AgentScheduleSpec
    """AgentScheduleSpec is the user-provided configuration for a schedule."""

    info: Optional[AgentScheduleInfo] = None
    """AgentScheduleInfo provides read-only runtime data about a schedule."""
