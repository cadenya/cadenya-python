# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CreateOperationMetadata"]


class CreateOperationMetadata(BaseModel):
    """
    CreateOperationMetadata contains the user-provided fields for creating
     an operation. Read-only fields (id, account_id, workspace_id, created_at, profile_id)
     are excluded since they are set by the server.
    """

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """External ID for the operation (e.g., a workflow ID from an external system)"""

    labels: Optional[Dict[str, str]] = None
    """
    Arbitrary key-value pairs for categorization and filtering Examples:
    {"priority": "high", "source": "api", "workflow": "onboarding"}
    """
