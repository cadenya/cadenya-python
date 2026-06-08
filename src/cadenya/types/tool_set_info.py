# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .profile import Profile
from .._models import BaseModel

__all__ = ["ToolSetInfo"]


class ToolSetInfo(BaseModel):
    agent_count: Optional[int] = FieldInfo(alias="agentCount", default=None)

    created_by: Optional[Profile] = FieldInfo(alias="createdBy", default=None)
    """
    A profile identifies a user or non-human principal (such as an API key) at the
    account level. Profiles are account-scoped and can be granted access to multiple
    workspaces.
    """

    last_sync: Optional[datetime] = FieldInfo(alias="lastSync", default=None)

    tool_count: Optional[int] = FieldInfo(alias="toolCount", default=None)
