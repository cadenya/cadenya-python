# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AIProviderConfigOpenrouter", "Openrouter"]


class Openrouter(BaseModel):
    """OpenRouterConfig holds OpenRouter-specific settings."""

    region: Optional[str] = None
    """Data-residency region (e.g. "us", "eu"). Empty uses the provider default."""


class AIProviderConfigOpenrouter(BaseModel):
    openrouter: Openrouter
    """OpenRouterConfig holds OpenRouter-specific settings."""

    type: Literal["openrouter"]
