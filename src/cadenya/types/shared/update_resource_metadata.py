# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["UpdateResourceMetadata"]


class UpdateResourceMetadata(BaseModel):
    """
    UpdateResourceMetadata contains the user-provided fields for updating
     a workspace-scoped resource. Read-only fields (id, account_id, workspace_id, profile_id,
     created_at) are excluded since they are set by the server.
    """

    name: str
    """
    Human-readable name for the resource (e.g., "Customer Support Agent", "Email
    Tool")
    """

    bundle_key: Optional[str] = FieldInfo(alias="bundleKey", default=None)
    """Optional bundle ownership key. See ResourceMetadata.bundle_key."""

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """External ID for the resource (e.g., a workflow ID from an external system)"""

    labels: Optional[Dict[str, str]] = None
    """
    Arbitrary key-value pairs for categorization and filtering Examples:
    {"environment": "production", "team": "platform", "version": "v2"}
    """
