# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ToolApprovalRequested"]


class ToolApprovalRequested(BaseModel):
    tool_call_id: Optional[str] = FieldInfo(alias="toolCallId", default=None)
    """The ID of the objective tool call record.

    Use this ID with the ApproveToolCall or DenyToolCall RPCs to approve or deny the
    tool call.
    """
