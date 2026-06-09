# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

from .agent_spec_param import AgentSpecParam
from .agent_schedule_entry_param import AgentScheduleEntryParam
from .agent_variation_entry_param import AgentVariationEntryParam

__all__ = ["AgentEntryParam"]


class AgentEntryParam(TypedDict, total=False):
    name: Required[str]

    spec: Required[AgentSpecParam]
    """Agent specification (user-provided configuration)"""

    labels: Dict[str, str]

    schedules: Dict[str, AgentScheduleEntryParam]
    """Schedules under this agent, keyed by external_id."""

    state: Literal["STATE_UNSPECIFIED", "STATE_DRAFT", "STATE_PUBLISHED", "STATE_ARCHIVED"]
    """Desired lifecycle state for the agent.

    Defaults to STATE_DRAFT when unspecified. STATE_PUBLISHED publishes the agent
    once its variations exist; see also
    BulkWorkspaceApplyData.automatically_publish_agents.
    """

    variations: Dict[str, AgentVariationEntryParam]
    """Variations under this agent, keyed by external_id."""
