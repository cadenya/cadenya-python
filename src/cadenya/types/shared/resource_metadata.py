# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ResourceMetadata"]


class ResourceMetadata(BaseModel):
    """
    Standard metadata for persistent, named resources (e.g., agents, tools, prompts)
    """

    id: str
    """Unique identifier for the resource (prefixed ULID, e.g., "agent_01HXK...")"""

    account_id: str = FieldInfo(alias="accountId")
    """Account this resource belongs to for multi-tenant isolation (prefixed ULID)"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Timestamp when this resource was created"""

    name: str
    """
    Human-readable name for the resource (e.g., "Customer Support Agent", "Email
    Tool") Required for resources that users interact with directly
    """

    profile_id: str = FieldInfo(alias="profileId")
    """ID of the actor (user or service account) that created this resource"""

    workspace_id: str = FieldInfo(alias="workspaceId")
    """Workspace this resource belongs to for organizational grouping (prefixed ULID)"""

    bundle_key: Optional[str] = FieldInfo(alias="bundleKey", default=None)
    """Optional bundle ownership key.

    When set, indicates the resource is managed by a configuration bundle identified
    by this key. Used by BulkWorkspaceResources.Apply to track which resources
    belong to which bundle for reconciliation / soft-delete on re-apply.
    """

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """External ID for the resource (e.g., a workflow ID from an external system)"""

    labels: Optional[Dict[str, str]] = None
    """
    Arbitrary key-value pairs for categorization and filtering Examples:
    {"environment": "production", "team": "platform", "version": "v2"}
    """
