# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

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

    state: Literal["STATE_UNSPECIFIED", "STATE_ACTIVE", "STATE_ARCHIVED"]
    """The current lifecycle state of the tool set.

    Output only. Tool sets are created STATE_ACTIVE; use the :archive and :unarchive
    actions to transition between states.
    """

    info: Optional[ToolSetInfo] = None
    """Tool set information"""
