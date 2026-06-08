# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .agent import Agent
from .._models import BaseModel
from .agents.agent_schedule import AgentSchedule
from .agents.agent_variation import AgentVariation

__all__ = ["ObjectiveConfigSnapshot"]


class ObjectiveConfigSnapshot(BaseModel):
    """
    ObjectiveConfigSnapshot is the point-in-time snapshot of the agent, variation, and
     (when applicable) schedule that an objective was started with.
    """

    agent: Optional[Agent] = None
    """Agent resource"""

    agent_schedule: Optional[AgentSchedule] = FieldInfo(alias="agentSchedule", default=None)
    """
    AgentSchedule resource — a recurring trigger attached to an agent that creates
    objectives on its cadence.
    """

    agent_variation: Optional[AgentVariation] = FieldInfo(alias="agentVariation", default=None)
    """AgentVariation resource"""
