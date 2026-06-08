# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .agent_info import AgentInfo
from .agent_spec import AgentSpec
from .shared.resource_metadata import ResourceMetadata

__all__ = ["Agent"]


class Agent(BaseModel):
    """Agent resource"""

    metadata: ResourceMetadata
    """
    Standard metadata for persistent, named resources (e.g., agents, tools, prompts)
    """

    spec: AgentSpec
    """Agent specification (user-provided configuration)"""

    info: Optional[AgentInfo] = None
    """
    AgentInfo contains simple information about an agent for display or quick
    reference
    """
