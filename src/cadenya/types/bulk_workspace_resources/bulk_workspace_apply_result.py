# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from ..shared.operation_metadata import OperationMetadata
from .bulk_workspace_apply_result_data import BulkWorkspaceApplyResultData

__all__ = ["BulkWorkspaceApplyResult"]


class BulkWorkspaceApplyResult(BaseModel):
    """
    One row of the per-resource result list for a BulkWorkspaceApply.
     Each row is itself an operation that can be paginated, sorted by
     created_at, and addressed individually.
    """

    data: BulkWorkspaceApplyResultData
    """Outcome for a single resource within a bulk apply.

    The `type` field is the discriminator string naming the populated `outcome`
    oneof variant (e.g., "toolSet", "memoryEntry"). Every outcome shell carries an
    `action` enum and either a resulting resource snapshot (for ACTION_CREATED,
    ACTION_UPDATED, ACTION_UNCHANGED, ACTION_DELETED) or a google.rpc.Status (for
    ACTION_FAILED).
    """

    metadata: OperationMetadata
    """
    Metadata for ephemeral operations and activities (e.g., objectives, executions,
    runs)
    """
