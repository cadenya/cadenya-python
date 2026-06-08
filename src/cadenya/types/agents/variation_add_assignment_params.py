# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["VariationAddAssignmentParams"]


class VariationAddAssignmentParams(TypedDict, total=False):
    workspace_id: Required[Annotated[str, PropertyInfo(alias="workspaceId")]]

    agent_id: Required[Annotated[str, PropertyInfo(alias="agentId")]]

    sub_agent_id: Annotated[str, PropertyInfo(alias="subAgentId")]

    tool_id: Annotated[str, PropertyInfo(alias="toolId")]

    tool_set_id: Annotated[str, PropertyInfo(alias="toolSetId")]
