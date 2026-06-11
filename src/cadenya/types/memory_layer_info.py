# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .profile import Profile
from .._models import BaseModel
from .shared.resource_metadata import ResourceMetadata

__all__ = ["MemoryLayerInfo"]


class MemoryLayerInfo(BaseModel):
    agent: Optional[ResourceMetadata] = None
    """
    Standard metadata for persistent, named resources (e.g., agents, tools, prompts)
    """

    created_by: Optional[Profile] = FieldInfo(alias="createdBy", default=None)
    """
    A profile identifies a user or non-human principal (such as an API key) at the
    account level. Profiles are account-scoped and can be granted access to multiple
    workspaces.
    """

    entry_count: Optional[int] = FieldInfo(alias="entryCount", default=None)
    """Number of entries currently in this layer."""

    last_used_at: Optional[datetime] = FieldInfo(alias="lastUsedAt", default=None)
    """
    Timestamp of the most recent objective that resolved against this layer. Useful
    for surfacing unused layers in the dashboard.
    """
