# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ToolResult"]


class ToolResult(BaseModel):
    content: Optional[str] = None

    tool_call_id: Optional[str] = FieldInfo(alias="toolCallId", default=None)
