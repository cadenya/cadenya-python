# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .account_info import AccountInfo
from .account_spec import AccountSpec
from .shared.account_resource_metadata import AccountResourceMetadata

__all__ = ["Account"]


class Account(BaseModel):
    """An account, the top-level organizational unit.

    Contains workspaces and
     account-wide settings such as the webhook signing secret.
    """

    info: AccountInfo
    """Server-populated information about the account."""

    metadata: AccountResourceMetadata
    """
    AccountResourceMetadata is used to represent a resource that is associated to an
    account but not to a workspace.
    """

    spec: AccountSpec
    """Configuration for an account."""
