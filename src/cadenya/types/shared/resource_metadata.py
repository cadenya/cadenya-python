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

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """External ID for the resource (e.g., a workflow ID from an external system)"""

    labels: Optional[Dict[str, str]] = None
    """Key-value pairs for categorization and filtering.

    Values are 0-63 alphanumeric characters with "-", "\\__", or "." allowed between;
    keys follow the same shape and additionally accept an optional DNS-subdomain
    prefix (e.g. "cadenya.com/") of at most 253 characters. Examples:
    {"environment": "production", "team": "platform", "version": "v2"}
    """

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """Timestamp when this resource was last updated"""
