# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

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

    variations: Optional[Dict[str, AgentVariationEntry]] = None
    """Variations under this agent, keyed by external_id."""
