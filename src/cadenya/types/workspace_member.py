# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WorkspaceMember"]


class WorkspaceMember(BaseModel):
    """
    A member of a workspace: the profile granted access plus the actor row that
     links it to the workspace. Returned by member list/add operations.
    """

    actor_id: str = FieldInfo(alias="actorId")
    """The actor row linking the profile to the workspace (the junction record)."""

    profile_id: str = FieldInfo(alias="profileId")
    """The account profile that has access to the workspace."""

    added_at: Optional[datetime] = FieldInfo(alias="addedAt", default=None)
    """When the member was added to the workspace."""

    email: Optional[str] = None
    """Email address of the member's profile."""

    name: Optional[str] = None
    """Display name of the member's profile."""
