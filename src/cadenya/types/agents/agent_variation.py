# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .agent_variation_info import AgentVariationInfo
from .agent_variation_spec import AgentVariationSpec
from ..shared.resource_metadata import ResourceMetadata

__all__ = ["AgentVariation"]


class AgentVariation(BaseModel):
    """AgentVariation resource"""

    metadata: ResourceMetadata
    """
    Standard metadata for persistent, named resources (e.g., agents, tools, prompts)
    """

    spec: AgentVariationSpec
    """AgentVariationSpec defines the operational configuration for a variation"""

    info: Optional[AgentVariationInfo] = None
    """AgentVariationInfo provides read-only summary information about a variation"""
