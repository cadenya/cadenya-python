# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .model_spec import ModelSpec
from .ai_provider_key import AIProviderKey
from .shared.resource_metadata import ResourceMetadata

__all__ = ["Model", "Info"]


class Info(BaseModel):
    """ModelInfo carries server-derived, read-only details about a model."""

    agent_variation_count: Optional[int] = FieldInfo(alias="agentVariationCount", default=None)
    """Number of agent variations currently provisioned on this model.

    Useful for previewing how many variations a swap would affect.
    """

    ai_provider_key: Optional[AIProviderKey] = FieldInfo(alias="aiProviderKey", default=None)
    """
    AIProviderKey is a credential for an AI provider, scoped to a workspace. Most
    keys are customer-provided (BYOK); Cadenya also provisions promotional keys (see
    AIProviderKeyInfo.is_promotional), which cannot be modified or deleted by
    account administrators. The secret value is never returned in responses.
    """

    last_used_at: Optional[datetime] = FieldInfo(alias="lastUsedAt", default=None)
    """Represents the last time this model was used in an agent objective"""


class Model(BaseModel):
    metadata: ResourceMetadata
    """
    Standard metadata for persistent, named resources (e.g., agents, tools, prompts)
    """

    spec: ModelSpec
    """Model specification"""

    state: Literal["STATE_UNSPECIFIED", "STATE_ENABLED", "STATE_DISABLED"]
    """Whether the model is usable in this workspace.

    Output only. Use the :enable and :disable actions to transition.
    """

    info: Optional[Info] = None
    """ModelInfo carries server-derived, read-only details about a model."""
