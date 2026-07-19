# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AIProviderCredentialAPIKey", "APIKey"]


class APIKey(BaseModel):
    """CredentialAPIKey carries a single bearer/header API key."""

    api_key: Optional[str] = FieldInfo(alias="apiKey", default=None)


class AIProviderCredentialAPIKey(BaseModel):
    api_key: APIKey = FieldInfo(alias="apiKey")
    """CredentialAPIKey carries a single bearer/header API key."""

    type: Literal["apiKey"]
