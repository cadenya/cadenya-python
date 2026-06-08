# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ObjectiveFeedbackData"]


class ObjectiveFeedbackData(BaseModel):
    comment: Optional[str] = None
    """Optional human-readable comment explaining the feedback"""

    score: Optional[float] = None
    """
    A score between -1.0 and 1.0 representing the quality of the objective's
    execution. -1.0 is the worst possible score, 0.0 is neutral, and 1.0 is the
    best.
    """
