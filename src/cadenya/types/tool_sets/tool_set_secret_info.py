# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..profile import Profile
from ..._models import BaseModel

__all__ = ["ToolSetSecretInfo"]


class ToolSetSecretInfo(BaseModel):
    created_by: Optional[Profile] = FieldInfo(alias="createdBy", default=None)
    """
    A profile identifies a user or non-human principal (such as an API key) at the
    account level. Profiles are account-scoped and can be granted access to multiple
    workspaces.
    """

    last_used_at: Optional[datetime] = FieldInfo(alias="lastUsedAt", default=None)
