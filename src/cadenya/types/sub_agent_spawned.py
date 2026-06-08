# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .shared.resource_metadata import ResourceMetadata
from .shared.operation_metadata import OperationMetadata

__all__ = ["SubAgentSpawned"]


class SubAgentSpawned(BaseModel):
    agent: Optional[ResourceMetadata] = None
    """
    Standard metadata for persistent, named resources (e.g., agents, tools, prompts)
    """

    objective: Optional[OperationMetadata] = None
    """
    Metadata for ephemeral operations and activities (e.g., objectives, executions,
    runs)
    """

    task: Optional[str] = None
