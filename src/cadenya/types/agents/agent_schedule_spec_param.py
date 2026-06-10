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

    data: object
    """Optional input data passed to the objective.

    If the agent has an input_data_schema, this must satisfy it.
    """

    initial_message: Annotated[str, PropertyInfo(alias="initialMessage")]
    """Optional initial message passed to CreateObjective on each fire.

    Becomes the first user message in the objective's chat history. When unset, the
    fired objective defers to the selected variation's user_message_template.
    """

    overlap_policy: Annotated[
        Literal["OVERLAP_POLICY_UNSPECIFIED", "OVERLAP_POLICY_ALLOW", "OVERLAP_POLICY_SKIP"],
        PropertyInfo(alias="overlapPolicy"),
    ]
    """What to do when the previous run is still in flight. Defaults to SKIP."""

    user_data: Annotated[object, PropertyInfo(alias="userData")]
    """
    Optional data rendered into the variation's user_message_template when each
    fired objective is created. Separate from `data`, which renders the system
    prompt template.
    """

    variation_id: Annotated[str, PropertyInfo(alias="variationId")]
    """Optional explicit variation.

    When unset, the agent's variation_selection_mode chooses per fire.
    """
