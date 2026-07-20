# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .workspace_spec import WorkspaceSpec
from .shared.account_resource_metadata import AccountResourceMetadata

__all__ = ["Workspace", "Info"]


class Info(BaseModel):
    """WorkspaceInfo returns counts"""

    total_agents: Optional[int] = FieldInfo(alias="totalAgents", default=None)

    total_agent_variations: Optional[int] = FieldInfo(alias="totalAgentVariations", default=None)

    total_available_tools: Optional[int] = FieldInfo(alias="totalAvailableTools", default=None)

    total_memory_entries: Optional[int] = FieldInfo(alias="totalMemoryEntries", default=None)


class Workspace(BaseModel):
    metadata: AccountResourceMetadata
    """
    AccountResourceMetadata is used to represent a resource that is associated to an
    account but not to a workspace.
    """

    spec: WorkspaceSpec

    info: Optional[Info] = None
    """WorkspaceInfo returns counts"""

    status: Optional[Literal["STATUS_ENABLED", "STATUS_DISABLED", "STATUS_ARCHIVED"]] = None
    """Lifecycle status of the workspace.

    Archived workspaces reject all requests scoped to them. Server-populated.
    """
