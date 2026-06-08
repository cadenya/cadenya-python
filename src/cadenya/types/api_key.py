# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .api_key_info import APIKeyInfo
from .api_key_spec import APIKeySpec
from .shared.account_resource_metadata import AccountResourceMetadata

__all__ = ["APIKey"]


class APIKey(BaseModel):
    """An API key for the account.

    Use workspace-association RPCs to grant the
     key access to specific workspaces; a key with zero workspaces is valid
     but cannot access workspace-scoped resources.
    """

    metadata: AccountResourceMetadata
    """
    AccountResourceMetadata is used to represent a resource that is associated to an
    account but not to a workspace.
    """

    spec: APIKeySpec
    """Configuration for an API key."""

    info: Optional[APIKeyInfo] = None
