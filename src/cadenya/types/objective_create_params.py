# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .memory_reference_param import MemoryReferenceParam
from .tenant_assertion_param import TenantAssertionParam
from .subject_assertion_param import SubjectAssertionParam
from .shared_params.create_operation_metadata import CreateOperationMetadata

__all__ = ["ObjectiveCreateParams", "EpisodicMemory", "Secret"]


class ObjectiveCreateParams(TypedDict, total=False):
    workspace_id: Annotated[str, PropertyInfo(alias="workspaceId")]

    agent_id: Required[Annotated[str, PropertyInfo(alias="agentId")]]

    system_prompt_data: Required[Annotated[Dict[str, object], PropertyInfo(alias="systemPromptData")]]
    """
    Arbitrary data rendered into the selected variation's system_prompt_template
    (liquid) to produce the objective's system prompt. If the agent has a
    system_prompt_data_schema, this must satisfy it.
    """

    episodic_memory: Annotated[EpisodicMemory, PropertyInfo(alias="episodicMemory")]
    """Episodic is used to configure the episodic memory for the objective"""

    first_user_message: Annotated[str, PropertyInfo(alias="firstUserMessage")]
    """Optional explicit first user message for the LLM chat history.

    When not set, the selected variation's first_user_message_template is rendered
    with first_user_message_data instead. If neither this field nor a
    first_user_message_template is present, the request is rejected with
    InvalidArgument.
    """

    first_user_message_data: Annotated[Dict[str, object], PropertyInfo(alias="firstUserMessageData")]
    """
    Arbitrary data rendered into the selected variation's
    first_user_message_template (liquid) to produce the first user message. Separate
    from `system_prompt_data`, which renders the system prompt template.
    """

    memory_cascade: Annotated[Iterable[MemoryReferenceParam], PropertyInfo(alias="memoryCascade")]
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

    metadata: CreateOperationMetadata
    """
    CreateOperationMetadata contains the user-provided fields for creating an
    operation. Read-only fields (id, account_id, workspace_id, created_at,
    profile_id) are excluded since they are set by the server.
    """

    pinned_parameters: Annotated[Dict[str, str], PropertyInfo(alias="pinnedParameters")]
    """Parameters forced onto this objective's tool calls.

    A pinned parameter is an overlay on a tool's JSON schema: the parameter is
    removed from what the LLM sees, and its value is always overwritten server-side
    with the pinned value — the model cannot choose a different value for it.
    """

    secrets: Iterable[Secret]
    """
    Secrets that can be used in the headers for tool calls using the secret
    interpolation format.
    """

    subject: SubjectAssertionParam
    """
    SubjectAssertion identifies a person within a tenant in the customer's own
    namespace — typically their user id. Asserting a subject upserts the subject
    record under the asserted tenant and associates the created resource with it. A
    subject assertion is only valid alongside a tenant assertion: subject
    identifiers are scoped to their tenant.
    """

    tenant: TenantAssertionParam
    """
    TenantAssertion identifies a tenant in the customer's own namespace — their org,
    company, or team identifier for an end user. Asserting a tenant upserts the
    tenant record in the workspace (keyed on `id` as the tenant's external_id) and
    associates the created resource with it.
    """

    variation_id: Annotated[str, PropertyInfo(alias="variationId")]
    """Optional explicit variation selection.

    Overrides the agent's variation_selection_mode.
    """


class EpisodicMemory(TypedDict, total=False):
    """Episodic is used to configure the episodic memory for the objective"""

    key: Required[str]
    """The caller-supplied episodic key.

    Objectives created with the same key (for the same agent) share one episodic
    memory layer.
    """


class Secret(TypedDict, total=False):
    name: str

    value: str
