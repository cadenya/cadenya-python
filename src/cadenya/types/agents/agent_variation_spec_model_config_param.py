# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AgentVariationSpecModelConfigParam"]


class AgentVariationSpecModelConfigParam(TypedDict, total=False):
    """ModelConfig defines the model configuration for a variation"""

    model_id: Annotated[str, PropertyInfo(alias="modelId")]
    """
    The model identifier in family/model format (e.g., "claude/opus-4.6",
    "claude/sonnet-4.5")
    """

    temperature: float
    """
    Sampling temperature for model inference (0.0 to 1.0) Lower values produce more
    deterministic outputs, higher values increase randomness
    """
