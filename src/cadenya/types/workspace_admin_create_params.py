# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .workspace_spec_param import WorkspaceSpecParam

__all__ = ["WorkspaceAdminCreateParams", "Metadata"]


class WorkspaceAdminCreateParams(TypedDict, total=False):
    metadata: Required[Metadata]
    """
    CreateAccountResourceMetadata contains the user-provided fields for creating an
    account-scoped resource. Read-only fields (id, account_id, profile_id) are
    excluded since they are set by the server.
    """

    spec: Required[WorkspaceSpecParam]


class Metadata(TypedDict, total=False):
    """
    CreateAccountResourceMetadata contains the user-provided fields for creating
     an account-scoped resource. Read-only fields (id, account_id, profile_id) are excluded
     since they are set by the server.
    """

    name: Required[str]
    """
    Human-readable name for the resource (e.g., "Production API Key", "Staging
    Workspace")
    """

    external_id: Annotated[str, PropertyInfo(alias="externalId")]
    """External ID for the resource (e.g., a workflow ID from an external system)"""

    labels: Dict[str, str]
    """
    Arbitrary key-value pairs for categorization and filtering Examples:
    {"environment": "production", "team": "platform", "version": "v2"}
    """
