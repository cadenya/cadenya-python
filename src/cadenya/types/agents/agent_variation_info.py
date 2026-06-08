# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..profile import Profile
from ..._models import BaseModel
from .variation_assignment import VariationAssignment
from ..shared.resource_metadata import ResourceMetadata
from .variation_memory_layer_assignment import VariationMemoryLayerAssignment

__all__ = ["AgentVariationInfo"]


class AgentVariationInfo(BaseModel):
    """AgentVariationInfo provides read-only summary information about a variation"""

    assignments: Optional[List[VariationAssignment]] = None
    """
    All tools, tool sets, and sub-agents assigned to this variation. Populated on
    reads so clients can render a variation's full assignment list without calling
    the add/remove endpoints just to enumerate.
    """

    created_by: Optional[Profile] = FieldInfo(alias="createdBy", default=None)
    """
    A profile identifies a user or non-human principal (such as an API key) at the
    account level. Profiles are account-scoped and can be granted access to multiple
    workspaces.
    """

    feedback_count: Optional[int] = FieldInfo(alias="feedbackCount", default=None)
    """Total number of objective feedbacks received for this variation"""

    memory_layer_assignments: Optional[List[VariationMemoryLayerAssignment]] = FieldInfo(
        alias="memoryLayerAssignments", default=None
    )
    """
    Read-only list of memory layer assignments for this variation, returned in
    ascending `position` (bottom → top). Capped at 10 entries.
    """

    memory_layer_count: Optional[int] = FieldInfo(alias="memoryLayerCount", default=None)
    """Count of memory layer assignments."""

    model: Optional[ResourceMetadata] = None
    """
    Standard metadata for persistent, named resources (e.g., agents, tools, prompts)
    """

    score: Optional[float] = None
    """
    Thompson Sampling score: posterior mean of Beta(ts_alpha, ts_beta). Range [0, 1]
    where 0.5 = neutral, >0.5 = positive, <0.5 = negative.
    """

    sub_agent_count: Optional[int] = FieldInfo(alias="subAgentCount", default=None)
    """Number of sub-agents assigned to this variation"""

    tool_count: Optional[int] = FieldInfo(alias="toolCount", default=None)
    """Number of individual tools assigned to this variation"""

    tool_set_count: Optional[int] = FieldInfo(alias="toolSetCount", default=None)
    """Number of tool sets assigned to this variation"""
