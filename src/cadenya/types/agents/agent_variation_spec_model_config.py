# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AgentVariationSpecModelConfig"]


class AgentVariationSpecModelConfig(BaseModel):
    """ModelConfig defines the model configuration for a variation"""

    api_model_id: Optional[str] = FieldInfo(alias="modelId", default=None)
    """
    The model identifier in family/model format (e.g., "claude/opus-4.6",
    "claude/sonnet-4.5")
    """

    temperature: Optional[float] = None
    """
    Sampling temperature for model inference (0.0 to 1.0) Lower values produce more
    deterministic outputs, higher values increase randomness
    """
