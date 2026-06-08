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

__all__ = ["Objective"]


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

    initial_message: str = FieldInfo(alias="initialMessage")
    """The initial message sent to the agent.

    This becomes the first user message in the LLM chat history.
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
    ]
    """The current lifecycle state of the objective."""

    system_prompt: str = FieldInfo(alias="systemPrompt")
    """system_prompt is read-only, derived from the selected variation's prompt"""

    data: Optional[Dict[str, object]] = None
    """Arbitrary data for the objective"""

    info: Optional[ObjectiveInfo] = None
    """
    ObjectiveInfo provides read-only aggregated statistics about an objective's
    execution
    """

    memory_stack: Optional[List[MemoryReference]] = FieldInfo(alias="memoryStack", default=None)
    """
    Memory layers/entries to push onto this objective's memory stack on top of the
    baseline stack inherited from the selected variation.

    Array order is push order: the first element sits lower in the objective's
    contribution to the stack; the LAST element ends up on top of the effective
    stack. Entries pinned via memory_entry_id behave as single-entry layers at their
    position.

    System-managed layers (e.g., episodic) cannot be referenced here; they attach
    themselves automatically based on episodic_key.

    Stack size cap: the TOTAL effective stack (variation's memory layers

    - this field) must not exceed 10 entries. A request that would produce an
      effective stack larger than 10 is rejected with InvalidArgument.
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

    secrets: Optional[List[ObjectiveSecret]] = None
    """
    Secrets that can be used in the headers for tool calls using the secret
    interpolation format.
    """

    state_message: Optional[str] = FieldInfo(alias="stateMessage", default=None)
    """Optional human-readable detail about the current state (e.g. a failure reason)."""
