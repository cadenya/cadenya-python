# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .api_key_info import APIKeyInfo
from .api_key_spec import APIKeySpec
from .shared.account_resource_metadata import AccountResourceMetadata

__all__ = ["APIKey"]


class APIKey(BaseModel):
    """An API key.

    Every key belongs to exactly one workspace and is managed via
     the workspace-scoped API key routes. The only exception is the
     system-managed global account key, which spans all workspaces and is
     managed via the account global_api_key routes.
    """

    metadata: AccountResourceMetadata
    """
    AccountResourceMetadata is used to represent a resource that is associated to an
    account but not to a workspace.
    """

    spec: APIKeySpec
    """Configuration for an API key."""

    state: Literal["STATE_UNSPECIFIED", "STATE_ENABLED", "STATE_DISABLED"]
    """The current lifecycle state of the API key.

    Output only. Keys are created STATE_ENABLED; use the :disable and :enable
    actions to transition between states.
    """

    info: Optional[APIKeyInfo] = None
