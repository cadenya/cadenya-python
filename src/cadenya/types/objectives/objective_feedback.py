# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .objective_feedback_data import ObjectiveFeedbackData
from .objective_feedback_info import ObjectiveFeedbackInfo
from ..shared.operation_metadata import OperationMetadata

__all__ = ["ObjectiveFeedback"]


class ObjectiveFeedback(BaseModel):
    """
    ObjectiveFeedback represents feedback submitted for an objective's execution.
     Feedback is used to score agent variations and improve agent performance over time.
    """

    data: ObjectiveFeedbackData

    metadata: OperationMetadata
    """
    Metadata for ephemeral operations and activities (e.g., objectives, executions,
    runs)
    """

    info: Optional[ObjectiveFeedbackInfo] = None
