# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ToolApproved"]


class ToolApproved(BaseModel):
    tool_call_id: Optional[str] = FieldInfo(alias="toolCallId", default=None)
    """
    The ID of the objective tool call record that was approved via the
    ApproveToolCall RPC.
    """
