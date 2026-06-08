# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["UpdateResourceMetadata"]


class UpdateResourceMetadata(TypedDict, total=False):
    """
    UpdateResourceMetadata contains the user-provided fields for updating
     a workspace-scoped resource. Read-only fields (id, account_id, workspace_id, profile_id,
     created_at) are excluded since they are set by the server.
    """

    name: Required[str]
    """
    Human-readable name for the resource (e.g., "Customer Support Agent", "Email
    Tool")
    """

    bundle_key: Annotated[str, PropertyInfo(alias="bundleKey")]
    """Optional bundle ownership key. See ResourceMetadata.bundle_key."""

    external_id: Annotated[str, PropertyInfo(alias="externalId")]
    """External ID for the resource (e.g., a workflow ID from an external system)"""

    labels: Dict[str, str]
    """
    Arbitrary key-value pairs for categorization and filtering Examples:
    {"environment": "production", "team": "platform", "version": "v2"}
    """
