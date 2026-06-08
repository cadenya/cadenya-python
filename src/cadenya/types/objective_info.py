# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .profile import Profile
from .._models import BaseModel
from .memory_reference import MemoryReference
from .shared.resource_metadata import ResourceMetadata

__all__ = ["ObjectiveInfo"]


class ObjectiveInfo(BaseModel):
    """
    ObjectiveInfo provides read-only aggregated statistics about an objective's execution
    """

    agent: ResourceMetadata
    """
    Standard metadata for persistent, named resources (e.g., agents, tools, prompts)
    """

    agent_variation: ResourceMetadata = FieldInfo(alias="agentVariation")
    """
    Standard metadata for persistent, named resources (e.g., agents, tools, prompts)
    """

    created_by: Profile = FieldInfo(alias="createdBy")
    """
    A profile identifies a user or non-human principal (such as an API key) at the
    account level. Profiles are account-scoped and can be granted access to multiple
    workspaces.
    """

    current_context_window_id: str = FieldInfo(alias="currentContextWindowId")
    """ID of the objective's current (most recent) context window.

    Hydrated on demand; empty when the objective has not yet produced a context
    window.
    """

    effective_memory_stack: List[MemoryReference] = FieldInfo(alias="effectiveMemoryStack")
    """
    The effective memory stack at objective creation time, flattened from the
    variation's baseline plus Objective.memory_stack. Order is push order (last =
    top). Returned on reads so clients can see exactly what stack the objective is
    using without having to re-join variation state.
    """

    total_context_windows: int = FieldInfo(alias="totalContextWindows")
    """Total number of context windows that this objective has generated"""

    total_events: int = FieldInfo(alias="totalEvents")
    """Total number of events generated during this objective's execution"""

    total_input_tokens: int = FieldInfo(alias="totalInputTokens")
    """
    Total input tokens consumed across all LLM completions across all context
    windows
    """

    total_iterations: int = FieldInfo(alias="totalIterations")

    total_output_tokens: int = FieldInfo(alias="totalOutputTokens")
    """
    Total output tokens generated across all LLM completions across all context
    windows
    """

    total_tool_calls: int = FieldInfo(alias="totalToolCalls")
    """Total number of tool calls made during execution"""
