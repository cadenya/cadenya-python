# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .tool_set_info import ToolSetInfo
from .tool_set_spec import ToolSetSpec
from .shared.resource_metadata import ResourceMetadata

__all__ = ["ToolSet"]


class ToolSet(BaseModel):
    metadata: ResourceMetadata
    """
    Standard metadata for persistent, named resources (e.g., agents, tools, prompts)
    """

    spec: ToolSetSpec

    info: Optional[ToolSetInfo] = None
    """Tool set information"""
