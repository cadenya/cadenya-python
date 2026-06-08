# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .workspace_secret_info import WorkspaceSecretInfo
from .workspace_secret_spec import WorkspaceSecretSpec
from .shared.resource_metadata import ResourceMetadata

__all__ = ["WorkspaceSecret"]


class WorkspaceSecret(BaseModel):
    metadata: ResourceMetadata
    """
    Standard metadata for persistent, named resources (e.g., agents, tools, prompts)
    """

    spec: WorkspaceSecretSpec

    info: Optional[WorkspaceSecretInfo] = None
    """Workspace secret information"""
