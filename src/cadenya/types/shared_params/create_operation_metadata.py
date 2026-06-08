# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CreateOperationMetadata"]


class CreateOperationMetadata(TypedDict, total=False):
    """
    CreateOperationMetadata contains the user-provided fields for creating
     an operation. Read-only fields (id, account_id, workspace_id, created_at, profile_id)
     are excluded since they are set by the server.
    """

    external_id: Annotated[str, PropertyInfo(alias="externalId")]
    """External ID for the operation (e.g., a workflow ID from an external system)"""

    labels: Dict[str, str]
    """
    Arbitrary key-value pairs for categorization and filtering Examples:
    {"priority": "high", "source": "api", "workflow": "onboarding"}
    """
