# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..profile import Profile
from ..._models import BaseModel
from ..shared.operation_metadata import OperationMetadata

__all__ = ["ObjectiveToolCallInfo"]


class ObjectiveToolCallInfo(BaseModel):
    created_by: Optional[Profile] = FieldInfo(alias="createdBy", default=None)
    """
    A profile identifies a user or non-human principal (such as an API key) at the
    account level. Profiles are account-scoped and can be granted access to multiple
    workspaces.
    """

    objective: Optional[OperationMetadata] = None
    """
    Metadata for ephemeral operations and activities (e.g., objectives, executions,
    runs)
    """
