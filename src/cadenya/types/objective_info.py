# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .profile import Profile
from .._models import BaseModel
from .memory_reference import MemoryReference
from .tenant_reference import TenantReference
from .subject_reference import SubjectReference
from .shared.bare_metadata import BareMetadata
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

    effective_memory_cascade: List[MemoryReference] = FieldInfo(alias="effectiveMemoryCascade")
    """
    The effective memory cascade at objective creation time: the episodic layer
    (when present), then Objective.memory_cascade, then the variation's baseline
    layers by ascending position. Order is resolution order — index 0 is the most
    specific and is consulted first; the first layer containing a key wins. Returned
    on reads so clients can see exactly what the objective resolves against without
    re-joining variation state.
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

    subject: Optional[SubjectReference] = None
    """
    SubjectReference is the read-only echo of a resource's subject association,
    carrying both Cadenya's canonical id and the customer's own key.
    """

    tenant: Optional[TenantReference] = None
    """
    TenantReference is the read-only echo of a resource's tenant association,
    carrying both Cadenya's canonical id and the customer's own key.
    """

    widget: Optional[BareMetadata] = None
    """
    BareMetadata contains the minimal metadata for a resource: the ID and an
    optional human-readable name. These are used for reference fields where the full
    metadata (account scoping, timestamps, labels, external IDs) is not needed —
    e.g., the tool references inside an agent variation spec or the tools assigned
    to an objective. Both fields are server-populated; clients provide IDs through
    sibling fields rather than by constructing a BareMetadata themselves.
    """
