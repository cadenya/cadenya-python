# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .tool_set_secret_info import ToolSetSecretInfo
from .tool_set_secret_spec import ToolSetSecretSpec
from ..shared.resource_metadata import ResourceMetadata

__all__ = ["ToolSetSecret"]


class ToolSetSecret(BaseModel):
    metadata: ResourceMetadata
    """
    Standard metadata for persistent, named resources (e.g., agents, tools, prompts)
    """

    spec: ToolSetSecretSpec

    info: Optional[ToolSetSecretInfo] = None
    """Tool set secret information"""
