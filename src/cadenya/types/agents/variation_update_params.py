# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .agent_variation_spec_param import AgentVariationSpecParam
from ..shared_params.update_resource_metadata import UpdateResourceMetadata

__all__ = ["VariationUpdateParams"]


class VariationUpdateParams(TypedDict, total=False):
    workspace_id: Required[Annotated[str, PropertyInfo(alias="workspaceId")]]

    agent_id: Required[Annotated[str, PropertyInfo(alias="agentId")]]

    metadata: UpdateResourceMetadata
    """
    UpdateResourceMetadata contains the user-provided fields for updating a
    workspace-scoped resource. Read-only fields (id, account_id, workspace_id,
    profile_id, created_at) are excluded since they are set by the server.
    """

    spec: AgentVariationSpecParam
    """AgentVariationSpec defines the operational configuration for a variation"""

    update_mask: Annotated[str, PropertyInfo(alias="updateMask")]
    """Fields to update"""
