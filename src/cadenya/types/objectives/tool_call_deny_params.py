# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ToolCallDenyParams"]


class ToolCallDenyParams(TypedDict, total=False):
    workspace_id: Annotated[str, PropertyInfo(alias="workspaceId")]

    memo: str
    """A memo to associate to the tool call denial.

    Use a memo to steer the LLM to a different decision or usage of the tool.
    """
