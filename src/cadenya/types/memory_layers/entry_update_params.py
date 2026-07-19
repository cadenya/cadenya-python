# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo
from .memory_entry_update_spec_param import MemoryEntryUpdateSpecParam
from ..shared_params.update_resource_metadata import UpdateResourceMetadata

__all__ = ["EntryUpdateParams"]


class EntryUpdateParams(TypedDict, total=False):
    workspace_id: Annotated[str, PropertyInfo(alias="workspaceId")]

    metadata: UpdateResourceMetadata
    """
    UpdateResourceMetadata contains the user-provided fields for updating a
    workspace-scoped resource. Read-only fields (id, account_id, workspace_id,
    profile_id, created_at) are excluded since they are set by the server.
    """

    spec: MemoryEntryUpdateSpecParam
    """MemoryEntryUpdateSpec is the input shape for UpdateMemoryEntry.

    Fields present in the request's update_mask are applied; unset fields are left
    alone. The source oneof is optional for updates — omit it to leave the body
    untouched, or set exactly one branch to replace it.
    """

    update_mask: Annotated[str, PropertyInfo(alias="updateMask")]
