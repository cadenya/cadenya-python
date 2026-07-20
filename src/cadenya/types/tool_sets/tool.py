# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

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

    state: Literal["STATE_UNSPECIFIED", "STATE_AVAILABLE", "STATE_OMITTED", "STATE_ARCHIVED"]
    """The current lifecycle state of the tool.

    Output only. Use the :omit and :restore actions to transition; tool set syncs
    may also update it.
    """

    info: Optional[ToolInfo] = None
