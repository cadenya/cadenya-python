# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .bulk_workspace_apply_result_data_tool_outcome import BulkWorkspaceApplyResultDataToolOutcome
from .bulk_workspace_apply_result_data_agent_outcome import BulkWorkspaceApplyResultDataAgentOutcome
from .bulk_workspace_apply_result_data_tool_set_outcome import BulkWorkspaceApplyResultDataToolSetOutcome
from .bulk_workspace_apply_result_data_memory_entry_outcome import BulkWorkspaceApplyResultDataMemoryEntryOutcome
from .bulk_workspace_apply_result_data_memory_layer_outcome import BulkWorkspaceApplyResultDataMemoryLayerOutcome
from .bulk_workspace_apply_result_data_agent_schedule_outcome import BulkWorkspaceApplyResultDataAgentScheduleOutcome
from .bulk_workspace_apply_result_data_agent_variation_outcome import BulkWorkspaceApplyResultDataAgentVariationOutcome
from .bulk_workspace_apply_result_data_variation_assignment_outcome import (
    BulkWorkspaceApplyResultDataVariationAssignmentOutcome,
)
from .bulk_workspace_apply_result_data_variation_memory_layer_outcome import (
    BulkWorkspaceApplyResultDataVariationMemoryLayerOutcome,
)

__all__ = ["BulkWorkspaceApplyResultData"]


class BulkWorkspaceApplyResultData(BaseModel):
    """Outcome for a single resource within a bulk apply.

    The `type` field is
     the discriminator string naming the populated `outcome` oneof variant
     (e.g., "toolSet", "memoryEntry"). Every outcome shell carries an
     `action` enum and either a resulting resource snapshot (for
     ACTION_CREATED, ACTION_UPDATED, ACTION_UNCHANGED, ACTION_DELETED) or a
     google.rpc.Status (for ACTION_FAILED).
    """

    agent: Optional[BulkWorkspaceApplyResultDataAgentOutcome] = None

    agent_schedule: Optional[BulkWorkspaceApplyResultDataAgentScheduleOutcome] = FieldInfo(
        alias="agentSchedule", default=None
    )

    agent_variation: Optional[BulkWorkspaceApplyResultDataAgentVariationOutcome] = FieldInfo(
        alias="agentVariation", default=None
    )

    memory_entry: Optional[BulkWorkspaceApplyResultDataMemoryEntryOutcome] = FieldInfo(
        alias="memoryEntry", default=None
    )

    memory_layer: Optional[BulkWorkspaceApplyResultDataMemoryLayerOutcome] = FieldInfo(
        alias="memoryLayer", default=None
    )

    tool: Optional[BulkWorkspaceApplyResultDataToolOutcome] = None

    tool_set: Optional[BulkWorkspaceApplyResultDataToolSetOutcome] = FieldInfo(alias="toolSet", default=None)

    type: Optional[str] = None

    variation_assignment: Optional[BulkWorkspaceApplyResultDataVariationAssignmentOutcome] = FieldInfo(
        alias="variationAssignment", default=None
    )

    variation_memory_layer: Optional[BulkWorkspaceApplyResultDataVariationMemoryLayerOutcome] = FieldInfo(
        alias="variationMemoryLayer", default=None
    )
