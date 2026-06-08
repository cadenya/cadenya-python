# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ToolError"]


class ToolError(BaseModel):
    message: Optional[str] = None

    tool_call_id: Optional[str] = FieldInfo(alias="toolCallId", default=None)
    """
    The ID of the objective tool call record that encountered an error during
    execution.
    """
