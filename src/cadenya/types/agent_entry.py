# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .agent_spec import AgentSpec
from .agent_schedule_entry import AgentScheduleEntry
from .agent_variation_entry import AgentVariationEntry

__all__ = ["AgentEntry"]


class AgentEntry(BaseModel):
    name: str

    spec: AgentSpec
    """Agent specification (user-provided configuration)"""

    labels: Optional[Dict[str, str]] = None

    schedules: Optional[Dict[str, AgentScheduleEntry]] = None
    """Schedules under this agent, keyed by external_id."""

    state: Optional[Literal["STATE_UNSPECIFIED", "STATE_DRAFT", "STATE_PUBLISHED", "STATE_ARCHIVED"]] = None
    """Desired lifecycle state for the agent.

    Defaults to STATE_DRAFT when unspecified. STATE_PUBLISHED publishes the agent
    once its variations exist; see also
    BulkWorkspaceApplyData.automatically_publish_agents.
    """

    variations: Optional[Dict[str, AgentVariationEntry]] = None
    """Variations under this agent, keyed by external_id."""
