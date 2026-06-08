# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .tool_set_spec_param import ToolSetSpecParam
from .shared_params.update_resource_metadata import UpdateResourceMetadata

__all__ = ["ToolSetUpdateParams"]


class ToolSetUpdateParams(TypedDict, total=False):
    workspace_id: Required[Annotated[str, PropertyInfo(alias="workspaceId")]]

    metadata: UpdateResourceMetadata
    """
    UpdateResourceMetadata contains the user-provided fields for updating a
    workspace-scoped resource. Read-only fields (id, account_id, workspace_id,
    profile_id, created_at) are excluded since they are set by the server.
    """

    spec: ToolSetSpecParam

    update_mask: Annotated[str, PropertyInfo(alias="updateMask")]
