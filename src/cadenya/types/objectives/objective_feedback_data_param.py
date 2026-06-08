# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ObjectiveFeedbackDataParam"]


class ObjectiveFeedbackDataParam(TypedDict, total=False):
    comment: str
    """Optional human-readable comment explaining the feedback"""

    score: float
    """
    A score between -1.0 and 1.0 representing the quality of the objective's
    execution. -1.0 is the worst possible score, 0.0 is neutral, and 1.0 is the
    best.
    """
