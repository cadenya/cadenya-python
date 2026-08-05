# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .reasoning import Reasoning

__all__ = ["ObjectiveEventDataReasoning"]


class ObjectiveEventDataReasoning(BaseModel):
    reasoning: Reasoning
    """
    Reasoning carries the human-readable reasoning text a model produced while
    working on an iteration — extended thinking (Anthropic, Gemini) or reasoning
    summaries (OpenAI). It is emitted alongside the assistant message from the same
    model response and is purely informational: the text shown here is never sent
    back to the model.
    """

    type: Literal["reasoning"]
