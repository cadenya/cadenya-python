# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .agent_spec_param import AgentSpecParam
from .agents.agent_variation_spec_param import AgentVariationSpecParam
from .shared_params.create_resource_metadata import CreateResourceMetadata

__all__ = ["AgentCreateParams", "DefaultVariation"]


class AgentCreateParams(TypedDict, total=False):
    workspace_id: Annotated[str, PropertyInfo(alias="workspaceId")]

    metadata: Required[CreateResourceMetadata]
    """
    CreateResourceMetadata contains the user-provided fields for creating a
    workspace-scoped resource. Read-only fields (id, account_id, workspace_id,
    profile_id, created_at) are excluded since they are set by the server.
    """

    spec: Required[AgentSpecParam]
    """Agent specification (user-provided configuration)"""

    default_variation: Annotated[DefaultVariation, PropertyInfo(alias="defaultVariation")]
    """Create agent variation request"""


class DefaultVariation(TypedDict, total=False):
    """Create agent variation request"""

    metadata: Required[CreateResourceMetadata]
    """
    CreateResourceMetadata contains the user-provided fields for creating a
    workspace-scoped resource. Read-only fields (id, account_id, workspace_id,
    profile_id, created_at) are excluded since they are set by the server.
    """

    spec: Required[AgentVariationSpecParam]
    """AgentVariationSpec defines the operational configuration for a variation"""
