# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

from .agents.agent_schedule_spec_param import AgentScheduleSpecParam

__all__ = ["AgentScheduleEntryParam"]


class AgentScheduleEntryParam(TypedDict, total=False):
    name: Required[str]

    spec: Required[AgentScheduleSpecParam]
    """AgentScheduleSpec is the user-provided configuration for a schedule."""

    labels: Dict[str, str]
