# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AIProviderConfigOpenAICompatible", "OpenAICompatible"]


class OpenAICompatible(BaseModel):
    """
    OpenAICompatibleConfig configures a generic endpoint that speaks the OpenAI
     Chat Completions API. The base URL is required and its model catalog is
     discovered live via GET {base_url}/models.
    """

    base_url: str = FieldInfo(alias="baseUrl")


class AIProviderConfigOpenAICompatible(BaseModel):
    openai_compatible: OpenAICompatible = FieldInfo(alias="openaiCompatible")
    """
    OpenAICompatibleConfig configures a generic endpoint that speaks the OpenAI Chat
    Completions API. The base URL is required and its model catalog is discovered
    live via GET {base_url}/models.
    """

    type: Literal["openaiCompatible"]
