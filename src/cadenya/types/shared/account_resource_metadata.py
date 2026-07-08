# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AccountResourceMetadata"]


class AccountResourceMetadata(BaseModel):
    """
    AccountResourceMetadata is used to represent a resource that is associated to an account but not to a workspace.
    """

    id: str
    """Unique identifier for the resource (prefixed ULID, e.g., "apikey_01HXK...")"""

    account_id: str = FieldInfo(alias="accountId")
    """Account this resource belongs to for multi-tenant isolation (prefixed ULID)"""

    name: str
    """
    Human-readable name for the resource (e.g., "Customer Support Agent", "Email
    Tool") Required for resources that users interact with directly
    """

    profile_id: str = FieldInfo(alias="profileId")

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """External ID for the resource (e.g., a workflow ID from an external system)"""

    labels: Optional[Dict[str, str]] = None
    """Key-value pairs for categorization and filtering.

    Values are 0-63 alphanumeric characters with "-", "\\__", or "." allowed between;
    keys follow the same shape and additionally accept an optional DNS-subdomain
    prefix (e.g. "cadenya.com/") of at most 253 characters. Examples:
    {"environment": "production", "team": "platform", "version": "v2"}
    """
