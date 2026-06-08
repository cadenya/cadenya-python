# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .profile import Profile
from .._models import BaseModel
from .shared.bare_metadata import BareMetadata

__all__ = ["APIKeyInfo"]


class APIKeyInfo(BaseModel):
    created_by: Optional[Profile] = FieldInfo(alias="createdBy", default=None)
    """
    A profile identifies a user or non-human principal (such as an API key) at the
    account level. Profiles are account-scoped and can be granted access to multiple
    workspaces.
    """

    workspaces_preview: Optional[List[BareMetadata]] = FieldInfo(alias="workspacesPreview", default=None)
    """
    Up to a small number of workspaces this key has access to, intended for display
    ("Workspace 1, Workspace 2, and 4 more"). Use ListAPIKeyWorkspaces for the full
    paginated list.
    """

    workspaces_total: Optional[int] = FieldInfo(alias="workspacesTotal", default=None)
    """Total number of workspaces this key has access to."""
