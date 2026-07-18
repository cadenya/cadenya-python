# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .api_key_spec_param import APIKeySpecParam

__all__ = ["APIKeyUpdateParams", "Metadata"]


class APIKeyUpdateParams(TypedDict, total=False):
    workspace_id: Required[Annotated[str, PropertyInfo(alias="workspaceId")]]

    metadata: Metadata
    """
    UpdateAccountResourceMetadata contains the user-provided fields for updating an
    account-scoped resource. Read-only fields (id, account_id, profile_id) are
    excluded since they are set by the server.
    """

    spec: APIKeySpecParam
    """Configuration for an API key."""

    update_mask: Annotated[str, PropertyInfo(alias="updateMask")]
    """Fields to update."""


class Metadata(TypedDict, total=False):
    """
    UpdateAccountResourceMetadata contains the user-provided fields for updating
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
    """Key-value pairs for categorization and filtering.

    Values are 0-63 alphanumeric characters with "-", "\\__", or "." allowed between;
    keys follow the same shape and additionally accept an optional DNS-subdomain
    prefix (e.g. "cadenya.com/") of at most 253 characters. Examples:
    {"environment": "production", "team": "platform", "version": "v2"}
    """
