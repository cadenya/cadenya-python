# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .objective_info import ObjectiveInfo
from .memory_reference import MemoryReference
from .objective_secret import ObjectiveSecret
from .objective_config_snapshot import ObjectiveConfigSnapshot
from .shared.operation_metadata import OperationMetadata

__all__ = ["Objective", "EpisodicMemory"]


class EpisodicMemory(BaseModel):
    """Episodic is used to configure the episodic memory for the objective"""

    key: str
    """The caller-supplied episodic key.

    Objectives created with the same key (for the same agent) share one episodic
    memory layer.
    """

    memory_layer_id: Optional[str] = FieldInfo(alias="memoryLayerId", default=None)
    """The episodic memory layer resolved (created or reused) for this objective's key.

    Populated by the system at objective creation.
    """


class Objective(BaseModel):
    """Objective is the data for an objective.

    It contains the snapshotted fields for the selected agent and variation. Secrets are returned
     only with their names, and the output definition is copied from the agent's configuration.
    """

    config_snapshot: ObjectiveConfigSnapshot = FieldInfo(alias="configSnapshot")
    """
    ObjectiveConfigSnapshot is the point-in-time snapshot of the agent, variation,
    and (when applicable) schedule that an objective was started with.
    """

    first_user_message: str = FieldInfo(alias="firstUserMessage")
    """
    The first user message in the LLM chat history, either provided explicitly at
    creation or rendered from the variation's first_user_message_template.
    """

    metadata: OperationMetadata
    """
    Metadata for ephemeral operations and activities (e.g., objectives, executions,
    runs)
    """

    state: Literal[
        "STATE_UNSPECIFIED",
        "STATE_PENDING",
        "STATE_RUNNING",
        "STATE_WAITING",
        "STATE_FAILED",
        "STATE_CANCELLED",
        "STATE_FINALIZED",
        "STATE_TIMED_OUT",
    ]
    """The current lifecycle state of the objective."""

    system_prompt: str = FieldInfo(alias="systemPrompt")
    """system_prompt is read-only, derived from the selected variation's prompt"""

    episodic_memory: Optional[EpisodicMemory] = FieldInfo(alias="episodicMemory", default=None)
    """Episodic is used to configure the episodic memory for the objective"""

    first_user_message_data: Optional[Dict[str, object]] = FieldInfo(alias="firstUserMessageData", default=None)
    """Arbitrary data rendered into the variation's first_user_message_template"""

    info: Optional[ObjectiveInfo] = None
    """
    ObjectiveInfo provides read-only aggregated statistics about an objective's
    execution
    """

    memory_cascade: Optional[List[MemoryReference]] = FieldInfo(alias="memoryCascade", default=None)
    """
    Memory layers/entries layered over the baseline cascade inherited from the
    selected variation — element-level rules over inherited styles, in CSS terms.

    Array order is resolution order: EARLIER elements are more specific and are
    consulted first. Entries pinned via memory_entry_id behave as single-entry
    layers at their position.

    System-managed layers (e.g., episodic) cannot be referenced here; they attach
    themselves automatically based on the episodic key.

    Size cap: the TOTAL effective cascade (this field + the variation's memory layer
    assignments) must not exceed 10 entries. A request that would produce a larger
    cascade is rejected with InvalidArgument.
    """

    output: Optional[Dict[str, object]] = None
    """The output of the objective, populated when the objective completes.

    Will match the schema of output_json_schema or output_json_inferred. This will
    only be set if the state of the objective is set to STATE_FINALIZED
    """

    parent_objective_id: Optional[str] = FieldInfo(alias="parentObjectiveId", default=None)
    """
    A parent objective means the objective was spawned off using a separate agent to
    complete an objective
    """

    pinned_parameters: Optional[Dict[str, str]] = FieldInfo(alias="pinnedParameters", default=None)
    """Parameters forced onto this objective's tool calls, as provided at creation.

    See CreateObjectiveRequest.pinned_parameters for semantics.
    """

    secrets: Optional[List[ObjectiveSecret]] = None
    """
    Secrets that can be used in the headers for tool calls using the secret
    interpolation format.
    """

    state_message: Optional[str] = FieldInfo(alias="stateMessage", default=None)
    """Optional human-readable detail about the current state (e.g. a failure reason)."""

    system_prompt_data: Optional[Dict[str, object]] = FieldInfo(alias="systemPromptData", default=None)
    """Arbitrary data rendered into the variation's system_prompt_template"""
