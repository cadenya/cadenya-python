# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ToolCallDenyParams"]


class ToolCallDenyParams(TypedDict, total=False):
    workspace_id: Required[Annotated[str, PropertyInfo(alias="workspaceId")]]

    objective_id: Required[Annotated[str, PropertyInfo(alias="objectiveId")]]

    memo: str
    """A memo to associate to the tool call denial.

    Use a memo to steer the LLM to a different decision or usage of the tool.
    """
