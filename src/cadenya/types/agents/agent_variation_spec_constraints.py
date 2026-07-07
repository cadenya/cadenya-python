# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AgentVariationSpecConstraints"]


class AgentVariationSpecConstraints(BaseModel):
    inactivity_timeout: Optional[int] = FieldInfo(alias="inactivityTimeout", default=None)
    """
    How long an objective may sit with no activity (no user messages, no LLM calls)
    before it is finalized as timed out. Between 1 minute and 24 hours. When not
    set, objectives are still swept at the system-wide 24 hour maximum — every
    objective eventually reaches a terminal state.
    """

    max_sub_objectives: Optional[int] = FieldInfo(alias="maxSubObjectives", default=None)
    """The maximum number of sub-objectives that can be created. 0 means no limit."""

    max_tool_calls: Optional[int] = FieldInfo(alias="maxToolCalls", default=None)
    """The maximum number of tool calls that can be made. 0 means no limit."""
