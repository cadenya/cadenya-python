# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .profile import Profile
from .._models import BaseModel

__all__ = ["AgentInfo"]


class AgentInfo(BaseModel):
    """
    AgentInfo contains simple information about an agent for display or quick reference
    """

    created_by: Optional[Profile] = FieldInfo(alias="createdBy", default=None)
    """
    A profile identifies a user or non-human principal (such as an API key) at the
    account level. Profiles are account-scoped and can be granted access to multiple
    workspaces.
    """

    variation_count: Optional[int] = FieldInfo(alias="variationCount", default=None)
