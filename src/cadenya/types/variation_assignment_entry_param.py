# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["VariationAssignmentEntryParam"]


class VariationAssignmentEntryParam(TypedDict, total=False):
    sub_agent_id: Annotated[str, PropertyInfo(alias="subAgentId")]

    tool_id: Annotated[str, PropertyInfo(alias="toolId")]

    tool_set_id: Annotated[str, PropertyInfo(alias="toolSetId")]
