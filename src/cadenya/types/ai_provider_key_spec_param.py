# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AIProviderKeySpecParam"]


class AIProviderKeySpecParam(TypedDict, total=False):
    api_key: Annotated[str, PropertyInfo(alias="apiKey")]
    """The provider credential.

    Accepted on create/update; never populated in responses (the server returns an
    empty value to avoid leaking it).
    """

    openrouter: object
    """OpenRouterConfig holds OpenRouter-specific settings.

    Empty for now; it exists as the oneof seam so provider-specific options (region,
    base URL, etc.) can be added later without restructuring the spec.
    """

    provider: Literal["AI_PROVIDER_UNSPECIFIED", "AI_PROVIDER_OPENROUTER"]
    """The AI provider this key authenticates against."""
