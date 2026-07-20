# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AIProviderConfigOpenAI", "OpenAI"]


class OpenAI(BaseModel):
    """OpenAIConfig holds OpenAI-specific settings."""

    organization_id: Optional[str] = FieldInfo(alias="organizationId", default=None)
    """Sent as the OpenAI-Organization header when set."""

    project_id: Optional[str] = FieldInfo(alias="projectId", default=None)
    """Sent as the OpenAI-Project header when set."""


class AIProviderConfigOpenAI(BaseModel):
    openai: OpenAI
    """OpenAIConfig holds OpenAI-specific settings."""

    type: Literal["openai"]
