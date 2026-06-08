# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AgentVariationSpecConstraintsParam"]


class AgentVariationSpecConstraintsParam(TypedDict, total=False):
    max_sub_objectives: Annotated[int, PropertyInfo(alias="maxSubObjectives")]
    """The maximum number of sub-objectives that can be created. 0 means no limit."""

    max_tool_calls: Annotated[int, PropertyInfo(alias="maxToolCalls")]
    """The maximum number of tool calls that can be made. 0 means no limit."""
