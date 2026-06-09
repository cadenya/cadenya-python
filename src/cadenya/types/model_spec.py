# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ModelSpec"]


class ModelSpec(BaseModel):
    family: Optional[str] = None
    """The model family (e.g., "claude-sonnet-4.6", "gpt-5.4", "gemini-2.5-flash")"""

    input_price_per_million_tokens: Optional[str] = FieldInfo(alias="inputPricePerMillionTokens", default=None)
    """Cost per million input tokens in cents (e.g., 300 = $3.00)"""

    max_input_tokens: Optional[int] = FieldInfo(alias="maxInputTokens", default=None)
    """Maximum number of input tokens the model supports"""

    max_output_tokens: Optional[int] = FieldInfo(alias="maxOutputTokens", default=None)
    """Maximum number of output tokens the model can generate"""

    output_price_per_million_tokens: Optional[str] = FieldInfo(alias="outputPricePerMillionTokens", default=None)
    """Cost per million output tokens in cents (e.g., 1500 = $15.00)"""

    provider: Optional[str] = None
    """The model provider (e.g., "anthropic", "openai", "google")"""
