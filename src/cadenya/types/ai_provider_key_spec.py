# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .ai_provider_config_openai import AIProviderConfigOpenAI
from .ai_provider_config_openrouter import AIProviderConfigOpenrouter
from .ai_provider_credential_api_key import AIProviderCredentialAPIKey
from .ai_provider_credential_headers import AIProviderCredentialHeaders
from .ai_provider_config_openai_compatible import AIProviderConfigOpenAICompatible

__all__ = ["AIProviderKeySpec", "Config", "Credentials"]

Config: TypeAlias = Annotated[
    Union[AIProviderConfigOpenrouter, AIProviderConfigOpenAI, AIProviderConfigOpenAICompatible],
    PropertyInfo(discriminator="type"),
]

Credentials: TypeAlias = Annotated[
    Union[AIProviderCredentialAPIKey, AIProviderCredentialHeaders], PropertyInfo(discriminator="type")
]


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
