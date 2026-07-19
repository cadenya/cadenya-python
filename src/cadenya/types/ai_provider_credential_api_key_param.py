# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AIProviderCredentialAPIKeyParam", "APIKey"]


class APIKey(TypedDict, total=False):
    """CredentialAPIKey carries a single bearer/header API key."""

    api_key: Annotated[str, PropertyInfo(alias="apiKey")]


class AIProviderCredentialAPIKeyParam(TypedDict, total=False):
    api_key: Required[Annotated[APIKey, PropertyInfo(alias="apiKey")]]
    """CredentialAPIKey carries a single bearer/header API key."""

    type: Required[Literal["apiKey"]]
