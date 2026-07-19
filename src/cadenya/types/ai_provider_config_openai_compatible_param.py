# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AIProviderConfigOpenAICompatibleParam", "OpenAICompatible"]


class OpenAICompatible(TypedDict, total=False):
    """
    OpenAICompatibleConfig configures a generic endpoint that speaks the OpenAI
     Chat Completions API. The base URL is required and its model catalog is
     discovered live via GET {base_url}/models.
    """

    base_url: Required[Annotated[str, PropertyInfo(alias="baseUrl")]]


class AIProviderConfigOpenAICompatibleParam(TypedDict, total=False):
    openai_compatible: Required[Annotated[OpenAICompatible, PropertyInfo(alias="openaiCompatible")]]
    """
    OpenAICompatibleConfig configures a generic endpoint that speaks the OpenAI Chat
    Completions API. The base URL is required and its model catalog is discovered
    live via GET {base_url}/models.
    """

    type: Required[Literal["openaiCompatible"]]
