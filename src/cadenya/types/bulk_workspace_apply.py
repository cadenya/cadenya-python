# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .bulk_workspace_apply_data import BulkWorkspaceApplyData
from .bulk_workspace_apply_info import BulkWorkspaceApplyInfo
from .shared.operation_metadata import OperationMetadata
from .bulk_workspace_apply_status import BulkWorkspaceApplyStatus

__all__ = ["BulkWorkspaceApply"]


class BulkWorkspaceApply(BaseModel):
    """The operation resource produced by a call to
     BulkWorkspaceResources.Apply.

    It carries the input bundle in `data`,
     the lifecycle state in `status`, and aggregate counts in `info`.
    """

    data: BulkWorkspaceApplyData

    metadata: OperationMetadata
    """
    Metadata for ephemeral operations and activities (e.g., objectives, executions,
    runs)
    """

    status: BulkWorkspaceApplyStatus

    info: Optional[BulkWorkspaceApplyInfo] = None
