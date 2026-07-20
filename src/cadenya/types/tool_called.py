# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .callable_tool import CallableTool
from .tool_sets.tool_spec_config import ToolSpecConfig

__all__ = ["ToolCalled"]


class ToolCalled(BaseModel):
    arguments: Optional[Dict[str, object]] = None
    """The arguments passed to the tool."""

    config: Optional[ToolSpecConfig] = None
    """
    Config defines the adapter to use for the tool. This is used to determine how
    the tool is called. For example, if the tool is an HTTP tool, the adapter will
    be Http. If the tool is an inline tool, the adapter will be Inline.
    """

    tool: Optional[CallableTool] = None
    """CallableTool is a union that represents a tool that can be called by an agent.

    In Cadenya, a tool that is used within an agent objective might be a
    user-defined tool (IE: MCP, HTTP), another Agent (useful to separate context),
    or a Cadenya Tool (one Cadenya provides).
    """

    tool_call_id: Optional[str] = FieldInfo(alias="toolCallId", default=None)
    """The ID of the objective tool call record that was executed."""
