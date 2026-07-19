# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .tool_set_secret_spec_param import ToolSetSecretSpecParam
from ..shared_params.create_resource_metadata import CreateResourceMetadata

__all__ = ["SecretCreateParams"]


class SecretCreateParams(TypedDict, total=False):
    workspace_id: Annotated[str, PropertyInfo(alias="workspaceId")]

    metadata: Required[CreateResourceMetadata]
    """
    CreateResourceMetadata contains the user-provided fields for creating a
    workspace-scoped resource. Read-only fields (id, account_id, workspace_id,
    profile_id, created_at) are excluded since they are set by the server.
    """

    spec: Required[ToolSetSecretSpecParam]
