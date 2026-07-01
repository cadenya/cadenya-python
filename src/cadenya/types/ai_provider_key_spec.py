# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "AIProviderKeySpec",
    "Config",
    "ConfigOpenAI",
    "ConfigOpenAICompatible",
    "ConfigOpenrouter",
    "Credentials",
    "CredentialsAPIKey",
    "CredentialsHeaders",
]


class ConfigOpenAI(BaseModel):
    """OpenAIConfig holds OpenAI-specific settings."""

    organization_id: Optional[str] = FieldInfo(alias="organizationId", default=None)
    """Sent as the OpenAI-Organization header when set."""

    project_id: Optional[str] = FieldInfo(alias="projectId", default=None)
    """Sent as the OpenAI-Project header when set."""


class ConfigOpenAICompatible(BaseModel):
    """
    OpenAICompatibleConfig configures a generic endpoint that speaks the OpenAI
     Chat Completions API. The base URL is required and its model catalog is
     discovered live via GET {base_url}/models.
    """

    base_url: Optional[str] = FieldInfo(alias="baseUrl", default=None)


class ConfigOpenrouter(BaseModel):
    """OpenRouterConfig holds OpenRouter-specific settings."""

    region: Optional[str] = None
    """Data-residency region (e.g. "us", "eu"). Empty uses the provider default."""


class Config(BaseModel):
    """AIProviderConfig holds non-secret, provider-specific settings.

    The set case
     must correspond to AIProviderKeySpec.provider. Providers with no settings
     (Anthropic, Gemini) simply leave this unset. The endpoint of a named provider
     is fixed and intentionally not overridable here; use the OpenAI-compatible
     provider to target a custom endpoint.
    """

    openai: Optional[ConfigOpenAI] = None
    """OpenAIConfig holds OpenAI-specific settings."""

    openai_compatible: Optional[ConfigOpenAICompatible] = FieldInfo(alias="openaiCompatible", default=None)
    """
    OpenAICompatibleConfig configures a generic endpoint that speaks the OpenAI Chat
    Completions API. The base URL is required and its model catalog is discovered
    live via GET {base_url}/models.
    """

    openrouter: Optional[ConfigOpenrouter] = None
    """OpenRouterConfig holds OpenRouter-specific settings."""


class CredentialsAPIKey(BaseModel):
    """CredentialAPIKey carries a single bearer/header API key."""

    api_key: Optional[str] = FieldInfo(alias="apiKey", default=None)


class CredentialsHeaders(BaseModel):
    """
    CredentialHeaders carries arbitrary HTTP headers sent with every request to
     the provider (e.g. {"Authorization": "Bearer ...", "X-Api-Key": "..."}).
    """

    headers: Optional[Dict[str, str]] = None


class Credentials(BaseModel):
    """
    AIProviderCredential is the secret material used to authenticate with a
     provider. The set case must correspond to AIProviderKeySpec.provider. The
     server encrypts the serialized message at rest and never returns it on reads.
    """

    api_key: Optional[CredentialsAPIKey] = FieldInfo(alias="apiKey", default=None)
    """CredentialAPIKey carries a single bearer/header API key."""

    headers: Optional[CredentialsHeaders] = None
    """
    CredentialHeaders carries arbitrary HTTP headers sent with every request to the
    provider (e.g. {"Authorization": "Bearer ...", "X-Api-Key": "..."}).
    """


class AIProviderKeySpec(BaseModel):
    config: Optional[Config] = None
    """AIProviderConfig holds non-secret, provider-specific settings.

    The set case must correspond to AIProviderKeySpec.provider. Providers with no
    settings (Anthropic, Gemini) simply leave this unset. The endpoint of a named
    provider is fixed and intentionally not overridable here; use the
    OpenAI-compatible provider to target a custom endpoint.
    """

    credentials: Optional[Credentials] = None
    """
    AIProviderCredential is the secret material used to authenticate with a
    provider. The set case must correspond to AIProviderKeySpec.provider. The server
    encrypts the serialized message at rest and never returns it on reads.
    """

    provider: Optional[
        Literal[
            "AI_PROVIDER_UNSPECIFIED",
            "AI_PROVIDER_OPENROUTER",
            "AI_PROVIDER_OPENAI",
            "AI_PROVIDER_ANTHROPIC",
            "AI_PROVIDER_GEMINI",
            "AI_PROVIDER_OPENAI_COMPATIBLE",
        ]
    ] = None
    """The AI provider this key authenticates against."""
