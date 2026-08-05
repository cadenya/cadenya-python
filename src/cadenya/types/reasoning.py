# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["Reasoning"]


class Reasoning(BaseModel):
    """
    Reasoning carries the human-readable reasoning text a model produced while
     working on an iteration — extended thinking (Anthropic, Gemini) or reasoning
     summaries (OpenAI). It is emitted alongside the assistant message from the
     same model response and is purely informational: the text shown here is
     never sent back to the model.
    """

    content: str
    """The reasoning text.

    May be a verbatim chain of thought or a provider-generated summary depending on
    the model.
    """
