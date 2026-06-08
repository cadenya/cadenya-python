# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .profile import Profile
from .._models import BaseModel

__all__ = ["BulkWorkspaceApplyInfo"]


class BulkWorkspaceApplyInfo(BaseModel):
    completed_at: Optional[datetime] = FieldInfo(alias="completedAt", default=None)

    created_by: Optional[Profile] = FieldInfo(alias="createdBy", default=None)
    """
    A profile identifies a user or non-human principal (such as an API key) at the
    account level. Profiles are account-scoped and can be granted access to multiple
    workspaces.
    """

    created_count: Optional[int] = FieldInfo(alias="createdCount", default=None)

    deleted_count: Optional[int] = FieldInfo(alias="deletedCount", default=None)

    failed_count: Optional[int] = FieldInfo(alias="failedCount", default=None)

    started_at: Optional[datetime] = FieldInfo(alias="startedAt", default=None)

    total_count: Optional[int] = FieldInfo(alias="totalCount", default=None)

    unchanged_count: Optional[int] = FieldInfo(alias="unchangedCount", default=None)

    updated_count: Optional[int] = FieldInfo(alias="updatedCount", default=None)
