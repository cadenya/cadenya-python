# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .workspace_spec import WorkspaceSpec
from .shared.account_resource_metadata import AccountResourceMetadata

__all__ = ["Workspace"]


class Workspace(BaseModel):
    metadata: AccountResourceMetadata
    """
    AccountResourceMetadata is used to represent a resource that is associated to an
    account but not to a workspace.
    """

    spec: WorkspaceSpec

    status: Optional[Literal["STATUS_ENABLED", "STATUS_DISABLED", "STATUS_ARCHIVED"]] = None
    """Lifecycle status of the workspace.

    Archived workspaces reject all requests scoped to them. Server-populated.
    """
