# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["MemoryLayerSpecParam"]


class MemoryLayerSpecParam(TypedDict, total=False):
    type: Required[Literal["MEMORY_LAYER_TYPE_UNSPECIFIED", "MEMORY_LAYER_TYPE_EPISODIC", "MEMORY_LAYER_TYPE_SKILLS"]]

    description: str
    """Human-readable description of the layer's purpose.

    Encouraged for user-created layers; system-managed layers may have a generated
    description.
    """
