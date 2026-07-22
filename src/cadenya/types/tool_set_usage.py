# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.resource_metadata import ResourceMetadata

__all__ = ["ToolSetUsage"]


class ToolSetUsage(BaseModel):
    """
    ToolSetUsage describes one agent variation that uses the tool set (or, when
     filtering by tool, an individual tool within it).
    """

    assigned_at: datetime = FieldInfo(alias="assignedAt")
    """When the assignment was created."""

    agent: Optional[ResourceMetadata] = None
    """
    Standard metadata for persistent, named resources (e.g., agents, tools, prompts)
    """

    agent_variation: Optional[ResourceMetadata] = FieldInfo(alias="agentVariation", default=None)
    """
    Standard metadata for persistent, named resources (e.g., agents, tools, prompts)
    """

    model: Optional[ResourceMetadata] = None
    """
    Standard metadata for persistent, named resources (e.g., agents, tools, prompts)
    """
