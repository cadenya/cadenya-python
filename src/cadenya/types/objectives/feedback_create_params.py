# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .objective_feedback_data_param import ObjectiveFeedbackDataParam
from ..shared_params.create_operation_metadata import CreateOperationMetadata

__all__ = ["FeedbackCreateParams"]


class FeedbackCreateParams(TypedDict, total=False):
    workspace_id: Annotated[str, PropertyInfo(alias="workspaceId")]

    data: Required[ObjectiveFeedbackDataParam]

    metadata: Required[CreateOperationMetadata]
    """
    CreateOperationMetadata contains the user-provided fields for creating an
    operation. Read-only fields (id, account_id, workspace_id, created_at,
    profile_id) are excluded since they are set by the server.
    """
