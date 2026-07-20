# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "VariationAddAssignmentParams",
    "AddAgentVariationAssignmentRequestToolID",
    "AddAgentVariationAssignmentRequestToolSetID",
    "AddAgentVariationAssignmentRequestSubAgentID",
]


class AddAgentVariationAssignmentRequestToolID(TypedDict, total=False):
    workspace_id: Annotated[str, PropertyInfo(alias="workspaceId")]

    tool_id: Required[Annotated[str, PropertyInfo(alias="toolId")]]

    type: Required[Literal["toolId"]]


class AddAgentVariationAssignmentRequestToolSetID(TypedDict, total=False):
    workspace_id: Annotated[str, PropertyInfo(alias="workspaceId")]

    tool_set_id: Required[Annotated[str, PropertyInfo(alias="toolSetId")]]

    type: Required[Literal["toolSetId"]]


class AddAgentVariationAssignmentRequestSubAgentID(TypedDict, total=False):
    workspace_id: Annotated[str, PropertyInfo(alias="workspaceId")]

    sub_agent_id: Required[Annotated[str, PropertyInfo(alias="subAgentId")]]

    type: Required[Literal["subAgentId"]]


VariationAddAssignmentParams: TypeAlias = Union[
    AddAgentVariationAssignmentRequestToolID,
    AddAgentVariationAssignmentRequestToolSetID,
    AddAgentVariationAssignmentRequestSubAgentID,
]
