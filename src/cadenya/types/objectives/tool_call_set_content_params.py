# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .set_tool_call_content_request_content_block_param import SetToolCallContentRequestContentBlockParam

__all__ = ["ToolCallSetContentParams"]


class ToolCallSetContentParams(TypedDict, total=False):
    workspace_id: Required[Annotated[str, PropertyInfo(alias="workspaceId")]]

    objective_id: Required[Annotated[str, PropertyInfo(alias="objectiveId")]]

    content: Required[Iterable[SetToolCallContentRequestContentBlockParam]]
    """The content to set on the tool call.

    Mirrors ObjectiveToolCallResult.ContentBlock but writable: media blocks carry
    raw data on input where the result-side carries a signed url on output.
    """
