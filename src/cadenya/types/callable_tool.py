# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.resource_metadata import ResourceMetadata

__all__ = ["CallableTool"]


class CallableTool(BaseModel):
    """CallableTool is a union that represents a tool that can be called by an agent.

    In Cadenya, a tool that is used within an agent objective
     might be a user-defined tool (IE: MCP, HTTP), another Agent (useful to separate context), or a Cadenya Tool (one Cadenya provides).
    """

    agent: Optional[ResourceMetadata] = None
    """
    Standard metadata for persistent, named resources (e.g., agents, tools, prompts)
    """

    cadenya_provided_tool: Optional[ResourceMetadata] = FieldInfo(alias="cadenyaProvidedTool", default=None)
    """
    Standard metadata for persistent, named resources (e.g., agents, tools, prompts)
    """

    tool: Optional[ResourceMetadata] = None
    """
    Standard metadata for persistent, named resources (e.g., agents, tools, prompts)
    """
