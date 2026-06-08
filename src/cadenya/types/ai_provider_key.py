# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .ai_provider_key_spec import AIProviderKeySpec
from .shared.resource_metadata import ResourceMetadata

__all__ = ["AIProviderKey", "Info"]


class Info(BaseModel):
    """
    AIProviderKeyInfo carries server-derived, read-only details about a key, for
     AI provider management UIs.
    """

    disabled_model_count: Optional[int] = FieldInfo(alias="disabledModelCount", default=None)
    """Number of disabled models provisioned on this key."""

    enabled_model_count: Optional[int] = FieldInfo(alias="enabledModelCount", default=None)
    """Number of enabled models provisioned on this key."""


class AIProviderKey(BaseModel):
    """
    AIProviderKey is a customer-provided (BYOK) credential for an AI provider,
     scoped to a workspace. The secret value is never returned in responses.
    """

    metadata: ResourceMetadata
    """
    Standard metadata for persistent, named resources (e.g., agents, tools, prompts)
    """

    spec: AIProviderKeySpec

    info: Optional[Info] = None
    """
    AIProviderKeyInfo carries server-derived, read-only details about a key, for AI
    provider management UIs.
    """
