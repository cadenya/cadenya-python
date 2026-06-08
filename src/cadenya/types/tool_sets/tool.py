# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .tool_info import ToolInfo
from .tool_spec import ToolSpec
from ..shared.resource_metadata import ResourceMetadata

__all__ = ["Tool"]


class Tool(BaseModel):
    metadata: ResourceMetadata
    """
    Standard metadata for persistent, named resources (e.g., agents, tools, prompts)
    """

    spec: ToolSpec

    info: Optional[ToolInfo] = None
