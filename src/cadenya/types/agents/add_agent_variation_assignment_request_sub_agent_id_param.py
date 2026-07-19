# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AddAgentVariationAssignmentRequestSubAgentIDParam"]


class AddAgentVariationAssignmentRequestSubAgentIDParam(TypedDict, total=False):
    sub_agent_id: Required[Annotated[str, PropertyInfo(alias="subAgentId")]]

    type: Required[Literal["subAgentId"]]
