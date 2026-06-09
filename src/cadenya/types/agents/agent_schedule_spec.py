# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .agent_schedule_spec_schedule import AgentScheduleSpecSchedule

__all__ = ["AgentScheduleSpec"]


class AgentScheduleSpec(BaseModel):
    """AgentScheduleSpec is the user-provided configuration for a schedule."""

    initial_message: str = FieldInfo(alias="initialMessage")
    """The initial message passed to CreateObjective on each fire.

    Becomes the first user message in the objective's chat history.
    """

    schedule: AgentScheduleSpecSchedule
    """Schedule defines WHEN the schedule fires.

    Temporal-style structured form: a list of calendar rules (wall-clock) and/or
    interval rules (duration), OR'd together. At least one rule is required.
    """

    data: Optional[object] = None
    """Optional input data passed to the objective.

    If the agent has an input_data_schema, this must satisfy it.
    """

    overlap_policy: Optional[Literal["OVERLAP_POLICY_UNSPECIFIED", "OVERLAP_POLICY_ALLOW", "OVERLAP_POLICY_SKIP"]] = (
        FieldInfo(alias="overlapPolicy", default=None)
    )
    """What to do when the previous run is still in flight. Defaults to SKIP."""

    variation_id: Optional[str] = FieldInfo(alias="variationId", default=None)
    """Optional explicit variation.

    When unset, the agent's variation_selection_mode chooses per fire.
    """
