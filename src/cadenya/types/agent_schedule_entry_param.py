# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

from .agents.agent_schedule_spec_param import AgentScheduleSpecParam

__all__ = ["AgentScheduleEntryParam"]


class AgentScheduleEntryParam(TypedDict, total=False):
    name: Required[str]

    spec: Required[AgentScheduleSpecParam]
    """AgentScheduleSpec is the user-provided configuration for a schedule."""

    labels: Dict[str, str]

    state: Literal["STATE_UNSPECIFIED", "STATE_ACTIVE", "STATE_PAUSED", "STATE_ARCHIVED"]
    """Desired lifecycle state for the schedule.

    Defaults to STATE_ACTIVE when unspecified. Declare STATE_PAUSED to provision a
    schedule without it firing. STATE_ARCHIVED is rejected here.
    """
