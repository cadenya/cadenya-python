# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .agent_schedule_spec_schedule_param import AgentScheduleSpecScheduleParam

__all__ = ["AgentScheduleSpecParam"]


class AgentScheduleSpecParam(TypedDict, total=False):
    """AgentScheduleSpec is the user-provided configuration for a schedule."""

    schedule: Required[AgentScheduleSpecScheduleParam]
    """Schedule defines WHEN the schedule fires.

    Temporal-style structured form: a list of calendar rules (wall-clock) and/or
    interval rules (duration), OR'd together. At least one rule is required.
    """

    first_user_message: Annotated[str, PropertyInfo(alias="firstUserMessage")]
    """
    Optional explicit first user message passed to CreateObjective on each fire.
    Becomes the first user message in the objective's chat history. When unset, the
    fired objective defers to the selected variation's first_user_message_template.
    """

    first_user_message_data: Annotated[object, PropertyInfo(alias="firstUserMessageData")]
    """
    Optional data rendered into the variation's first_user_message_template when
    each fired objective is created. Separate from `system_prompt_data`, which
    renders the system prompt template.
    """

    overlap_policy: Annotated[
        Literal["OVERLAP_POLICY_UNSPECIFIED", "OVERLAP_POLICY_ALLOW", "OVERLAP_POLICY_SKIP"],
        PropertyInfo(alias="overlapPolicy"),
    ]
    """What to do when the previous run is still in flight. Defaults to SKIP."""

    system_prompt_data: Annotated[object, PropertyInfo(alias="systemPromptData")]
    """
    Optional data rendered into the variation's system_prompt_template when each
    fired objective is created. If the agent has a system_prompt_data_schema, this
    must satisfy it.
    """

    variation_id: Annotated[str, PropertyInfo(alias="variationId")]
    """Optional explicit variation.

    When unset, the agent's variation_selection_mode chooses per fire.
    """
