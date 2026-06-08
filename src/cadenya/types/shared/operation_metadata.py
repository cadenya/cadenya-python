# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["OperationMetadata"]


class OperationMetadata(BaseModel):
    """
    Metadata for ephemeral operations and activities (e.g., objectives, executions, runs)
    """

    id: str
    """Unique identifier for the operation (prefixed ULID, e.g., "obj_01HXK...")"""

    account_id: str = FieldInfo(alias="accountId")
    """Account this operation belongs to for multi-tenant isolation (prefixed ULID)"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """
    Timestamp when this operation was created ULID includes timestamp information,
    but this explicit field enables easier querying
    """

    profile_id: str = FieldInfo(alias="profileId")
    """ID of the actor (user or service account) that created this operation"""

    workspace_id: str = FieldInfo(alias="workspaceId")
    """Workspace this operation belongs to for organizational grouping (prefixed ULID)"""

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """External ID for the operation (e.g., a workflow ID from an external system)"""

    labels: Optional[Dict[str, str]] = None
    """
    Arbitrary key-value pairs for categorization and filtering Examples:
    {"priority": "high", "source": "api", "workflow": "onboarding"}
    """
