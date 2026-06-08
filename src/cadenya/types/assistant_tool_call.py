# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .callable_tool import CallableTool

__all__ = ["AssistantToolCall"]


class AssistantToolCall(BaseModel):
    arguments: Optional[str] = None

    function_name: Optional[str] = FieldInfo(alias="functionName", default=None)

    tool: Optional[CallableTool] = None
    """CallableTool is a union that represents a tool that can be called by an agent.

    In Cadenya, a tool that is used within an agent objective might be a
    user-defined tool (IE: MCP, HTTP), another Agent (useful to separate context),
    or a Cadenya Tool (one Cadenya provides).
    """
