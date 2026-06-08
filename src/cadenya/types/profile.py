# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .profile_spec import ProfileSpec
from .shared.account_resource_metadata import AccountResourceMetadata

__all__ = ["Profile"]


class Profile(BaseModel):
    """
    A profile identifies a user or non-human principal (such as an API key)
     at the account level. Profiles are account-scoped and can be granted access
     to multiple workspaces.
    """

    metadata: AccountResourceMetadata
    """
    AccountResourceMetadata is used to represent a resource that is associated to an
    account but not to a workspace.
    """

    spec: ProfileSpec
    """Configuration for a profile."""
