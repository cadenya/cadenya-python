# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .widget_spec_param import WidgetSpecParam
from .shared_params.update_resource_metadata import UpdateResourceMetadata

__all__ = ["WidgetUpdateParams"]


class WidgetUpdateParams(TypedDict, total=False):
    workspace_id: Annotated[str, PropertyInfo(alias="workspaceId")]

    metadata: UpdateResourceMetadata
    """
    UpdateResourceMetadata contains the user-provided fields for updating a
    workspace-scoped resource. Read-only fields (id, account_id, workspace_id,
    profile_id, created_at) are excluded since they are set by the server.
    """

    spec: WidgetSpecParam
    """WidgetSpec is the user-provided configuration for a widget."""

    update_mask: Annotated[str, PropertyInfo(alias="updateMask")]
    """Fields to update."""
