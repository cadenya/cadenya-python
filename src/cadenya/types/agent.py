# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

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

    state: Literal["STATE_UNSPECIFIED", "STATE_DRAFT", "STATE_PUBLISHED", "STATE_ARCHIVED"]
    """The current lifecycle state of the agent.

    Output only. Agents are created in STATE_DRAFT; use the :publish, :unpublish,
    :archive, and :unarchive actions to transition between states.
    """

    info: Optional[AgentInfo] = None
    """
    AgentInfo contains simple information about an agent for display or quick
    reference
    """
