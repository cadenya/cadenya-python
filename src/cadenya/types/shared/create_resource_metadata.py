# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CreateResourceMetadata"]


class CreateResourceMetadata(BaseModel):
    """
    CreateResourceMetadata contains the user-provided fields for creating
     a workspace-scoped resource. Read-only fields (id, account_id, workspace_id, profile_id,
     created_at) are excluded since they are set by the server.
    """

    name: str
    """
    Human-readable name for the resource (e.g., "Customer Support Agent", "Email
    Tool")
    """

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """External ID for the resource (e.g., a workflow ID from an external system)"""

    labels: Optional[Dict[str, str]] = None
    """Key-value pairs for categorization and filtering.

    Values are 0-63 alphanumeric characters with "-", "\\__", or "." allowed between;
    keys follow the same shape and additionally accept an optional DNS-subdomain
    prefix (e.g. "cadenya.com/") of at most 253 characters. Examples:
    {"environment": "production", "team": "platform", "version": "v2"}
    """
