# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ToolDenied"]


class ToolDenied(BaseModel):
    memo: Optional[str] = None
    """The memo provided by the reviewer when denying the tool call.

    This is passed to the agent to provide further instructions.
    """

    tool_call_id: Optional[str] = FieldInfo(alias="toolCallId", default=None)
    """
    The ID of the objective tool call record that was denied via the DenyToolCall
    RPC.
    """
