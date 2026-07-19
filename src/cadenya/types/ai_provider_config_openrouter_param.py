# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AIProviderConfigOpenrouterParam", "Openrouter"]


class Openrouter(TypedDict, total=False):
    """OpenRouterConfig holds OpenRouter-specific settings."""

    region: str
    """Data-residency region (e.g. "us", "eu"). Empty uses the provider default."""


class AIProviderConfigOpenrouterParam(TypedDict, total=False):
    openrouter: Required[Openrouter]
    """OpenRouterConfig holds OpenRouter-specific settings."""

    type: Required[Literal["openrouter"]]
