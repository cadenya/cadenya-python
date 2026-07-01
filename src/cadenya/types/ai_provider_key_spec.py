# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AIProviderKeySpec"]


class AIProviderKeySpec(BaseModel):
    api_key: Optional[str] = FieldInfo(alias="apiKey", default=None)
    """The provider credential.

    Accepted on create/update; never populated in responses (the server returns an
    empty value to avoid leaking it).
    """

    openrouter: Optional[object] = None
    """OpenRouterConfig holds OpenRouter-specific settings.

    Empty for now; it exists as the oneof seam so provider-specific options (region,
    base URL, etc.) can be added later without restructuring the spec.
    """

    provider: Optional[Literal["AI_PROVIDER_UNSPECIFIED", "AI_PROVIDER_OPENROUTER"]] = None
    """The AI provider this key authenticates against."""
