# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AIProviderConfigOpenAIParam", "OpenAI"]


class OpenAI(TypedDict, total=False):
    """OpenAIConfig holds OpenAI-specific settings."""

    organization_id: Annotated[str, PropertyInfo(alias="organizationId")]
    """Sent as the OpenAI-Organization header when set."""

    project_id: Annotated[str, PropertyInfo(alias="projectId")]
    """Sent as the OpenAI-Project header when set."""


class AIProviderConfigOpenAIParam(TypedDict, total=False):
    openai: Required[OpenAI]
    """OpenAIConfig holds OpenAI-specific settings."""

    type: Required[Literal["openai"]]
