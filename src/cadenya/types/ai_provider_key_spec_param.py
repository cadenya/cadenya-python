# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "AIProviderKeySpecParam",
    "Config",
    "ConfigOpenAI",
    "ConfigOpenAICompatible",
    "ConfigOpenrouter",
    "Credentials",
    "CredentialsAPIKey",
    "CredentialsHeaders",
]


class ConfigOpenAI(TypedDict, total=False):
    """OpenAIConfig holds OpenAI-specific settings."""

    organization_id: Annotated[str, PropertyInfo(alias="organizationId")]
    """Sent as the OpenAI-Organization header when set."""

    project_id: Annotated[str, PropertyInfo(alias="projectId")]
    """Sent as the OpenAI-Project header when set."""


class ConfigOpenAICompatible(TypedDict, total=False):
    """
    OpenAICompatibleConfig configures a generic endpoint that speaks the OpenAI
     Chat Completions API. The base URL is required and its model catalog is
     discovered live via GET {base_url}/models.
    """

    base_url: Annotated[str, PropertyInfo(alias="baseUrl")]


class ConfigOpenrouter(TypedDict, total=False):
    """OpenRouterConfig holds OpenRouter-specific settings."""

    region: str
    """Data-residency region (e.g. "us", "eu"). Empty uses the provider default."""


class Config(TypedDict, total=False):
    """AIProviderConfig holds non-secret, provider-specific settings.

    The set case
     must correspond to AIProviderKeySpec.provider. Providers with no settings
     (Anthropic, Gemini) simply leave this unset. The endpoint of a named provider
     is fixed and intentionally not overridable here; use the OpenAI-compatible
     provider to target a custom endpoint.
    """

    openai: ConfigOpenAI
    """OpenAIConfig holds OpenAI-specific settings."""

    openai_compatible: Annotated[ConfigOpenAICompatible, PropertyInfo(alias="openaiCompatible")]
    """
    OpenAICompatibleConfig configures a generic endpoint that speaks the OpenAI Chat
    Completions API. The base URL is required and its model catalog is discovered
    live via GET {base_url}/models.
    """

    openrouter: ConfigOpenrouter
    """OpenRouterConfig holds OpenRouter-specific settings."""


class CredentialsAPIKey(TypedDict, total=False):
    """CredentialAPIKey carries a single bearer/header API key."""

    api_key: Annotated[str, PropertyInfo(alias="apiKey")]


class CredentialsHeaders(TypedDict, total=False):
    """
    CredentialHeaders carries arbitrary HTTP headers sent with every request to
     the provider (e.g. {"Authorization": "Bearer ...", "X-Api-Key": "..."}).
    """

    headers: Dict[str, str]


class Credentials(TypedDict, total=False):
    """
    AIProviderCredential is the secret material used to authenticate with a
     provider. The set case must correspond to AIProviderKeySpec.provider. The
     server encrypts the serialized message at rest and never returns it on reads.
    """

    api_key: Annotated[CredentialsAPIKey, PropertyInfo(alias="apiKey")]
    """CredentialAPIKey carries a single bearer/header API key."""

    headers: CredentialsHeaders
    """
    CredentialHeaders carries arbitrary HTTP headers sent with every request to the
    provider (e.g. {"Authorization": "Bearer ...", "X-Api-Key": "..."}).
    """


class AIProviderKeySpecParam(TypedDict, total=False):
    config: Config
    """AIProviderConfig holds non-secret, provider-specific settings.

    The set case must correspond to AIProviderKeySpec.provider. Providers with no
    settings (Anthropic, Gemini) simply leave this unset. The endpoint of a named
    provider is fixed and intentionally not overridable here; use the
    OpenAI-compatible provider to target a custom endpoint.
    """

    credentials: Credentials
    """
    AIProviderCredential is the secret material used to authenticate with a
    provider. The set case must correspond to AIProviderKeySpec.provider. The server
    encrypts the serialized message at rest and never returns it on reads.
    """

    provider: Literal[
        "AI_PROVIDER_UNSPECIFIED",
        "AI_PROVIDER_OPENROUTER",
        "AI_PROVIDER_OPENAI",
        "AI_PROVIDER_ANTHROPIC",
        "AI_PROVIDER_GEMINI",
        "AI_PROVIDER_OPENAI_COMPATIBLE",
    ]
    """The AI provider this key authenticates against."""
