# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .assistant_tool_call import AssistantToolCall

__all__ = ["AssistantMessage"]


class AssistantMessage(BaseModel):
    content: Optional[str] = None

    tool_calls: Optional[List[AssistantToolCall]] = FieldInfo(alias="toolCalls", default=None)
