# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .shared.resource_metadata import ResourceMetadata

__all__ = ["CallableToolAgent"]


class CallableToolAgent(BaseModel):
    agent: ResourceMetadata
    """
    Standard metadata for persistent, named resources (e.g., agents, tools, prompts)
    """

    type: Literal["agent"]
