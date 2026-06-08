# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AgentVariationSpecConstraints"]


class AgentVariationSpecConstraints(BaseModel):
    max_sub_objectives: Optional[int] = FieldInfo(alias="maxSubObjectives", default=None)
    """The maximum number of sub-objectives that can be created. 0 means no limit."""

    max_tool_calls: Optional[int] = FieldInfo(alias="maxToolCalls", default=None)
    """The maximum number of tool calls that can be made. 0 means no limit."""
