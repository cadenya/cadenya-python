# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .objectives.objective_tool_call_result import ObjectiveToolCallResult

__all__ = ["ToolResult"]


class ToolResult(BaseModel):
    result: ObjectiveToolCallResult
    """
    ObjectiveToolCallResult is the content a tool returned after execution. Tools
    can return multiple content blocks, and blocks can be multi-modal (text, image,
    audio). Media blocks are stored by Cadenya and served as short-lived signed URLs
    rather than inline bytes.
    """

    tool_call_id: str = FieldInfo(alias="toolCallId")
