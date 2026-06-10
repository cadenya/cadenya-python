# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .memory_reference_param import MemoryReferenceParam
from .shared_params.create_operation_metadata import CreateOperationMetadata

__all__ = ["ObjectiveCreateParams", "Secret"]


class ObjectiveCreateParams(TypedDict, total=False):
    agent_id: Required[Annotated[str, PropertyInfo(alias="agentId")]]

    data: Required[Dict[str, object]]
    """Arbitrary data for the objective.

    May be used in liquid templates for prompts configured on the agent variation
    """

    initial_message: Annotated[str, PropertyInfo(alias="initialMessage")]
    """Optional override for the initial message sent to the agent.

    This becomes the first user message in the LLM chat history. When not set, the
    selected variation's user_message_template is rendered with user_data instead.
    If neither this field nor a user_message_template is present, the request is
    rejected with InvalidArgument.
    """

    memory_stack: Annotated[Iterable[MemoryReferenceParam], PropertyInfo(alias="memoryStack")]
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

    metadata: CreateOperationMetadata
    """
    CreateOperationMetadata contains the user-provided fields for creating an
    operation. Read-only fields (id, account_id, workspace_id, created_at,
    profile_id) are excluded since they are set by the server.
    """

    secrets: Iterable[Secret]
    """
    Secrets that can be used in the headers for tool calls using the secret
    interpolation format.
    """

    user_data: Annotated[Dict[str, object], PropertyInfo(alias="userData")]
    """
    Arbitrary data rendered into the selected variation's user_message_template
    (liquid) to produce the initial user message. Separate from `data`, which
    renders the system prompt template.
    """

    variation_id: Annotated[str, PropertyInfo(alias="variationId")]
    """Optional explicit variation selection.

    Overrides the agent's variation_selection_mode.
    """


class Secret(TypedDict, total=False):
    name: str

    value: str
