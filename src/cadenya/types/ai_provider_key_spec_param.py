# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, TypeAlias, TypedDict

from .ai_provider_config_openai_param import AIProviderConfigOpenAIParam
from .ai_provider_config_openrouter_param import AIProviderConfigOpenrouterParam
from .ai_provider_credential_api_key_param import AIProviderCredentialAPIKeyParam
from .ai_provider_credential_headers_param import AIProviderCredentialHeadersParam
from .ai_provider_config_openai_compatible_param import AIProviderConfigOpenAICompatibleParam

__all__ = ["AIProviderKeySpecParam", "Config", "Credentials"]

Config: TypeAlias = Union[
    AIProviderConfigOpenrouterParam, AIProviderConfigOpenAIParam, AIProviderConfigOpenAICompatibleParam
]

Credentials: TypeAlias = Union[AIProviderCredentialAPIKeyParam, AIProviderCredentialHeadersParam]


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
