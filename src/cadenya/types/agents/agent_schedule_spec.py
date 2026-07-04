# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .agent_schedule_spec_schedule import AgentScheduleSpecSchedule

__all__ = ["AgentScheduleSpec"]


class AgentScheduleSpec(BaseModel):
    """AgentScheduleSpec is the user-provided configuration for a schedule."""

    schedule: AgentScheduleSpecSchedule
    """Schedule defines WHEN the schedule fires.

    Temporal-style structured form: a list of calendar rules (wall-clock) and/or
    interval rules (duration), OR'd together. At least one rule is required.
    """

    first_user_message: Optional[str] = FieldInfo(alias="firstUserMessage", default=None)
    """
    Optional explicit first user message passed to CreateObjective on each fire.
    Becomes the first user message in the objective's chat history. When unset, the
    fired objective defers to the selected variation's first_user_message_template.
    """

    first_user_message_data: Optional[object] = FieldInfo(alias="firstUserMessageData", default=None)
    """
    Optional data rendered into the variation's first_user_message_template when
    each fired objective is created. Separate from `system_prompt_data`, which
    renders the system prompt template.
    """

    overlap_policy: Optional[Literal["OVERLAP_POLICY_UNSPECIFIED", "OVERLAP_POLICY_ALLOW", "OVERLAP_POLICY_SKIP"]] = (
        FieldInfo(alias="overlapPolicy", default=None)
    )
    """What to do when the previous run is still in flight. Defaults to SKIP."""

    system_prompt_data: Optional[object] = FieldInfo(alias="systemPromptData", default=None)
    """
    Optional data rendered into the variation's system_prompt_template when each
    fired objective is created. If the agent has a system_prompt_data_schema, this
    must satisfy it.
    """

    variation_id: Optional[str] = FieldInfo(alias="variationId", default=None)
    """Optional explicit variation.

    When unset, the agent's variation_selection_mode chooses per fire.
    """
