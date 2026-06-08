# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["VariationMemoryLayerEntryParam"]


class VariationMemoryLayerEntryParam(TypedDict, total=False):
    memory_layer_id: Annotated[str, PropertyInfo(alias="memoryLayerId")]
    """external_id:<value> form. Canonical IDs are rejected."""

    position: int
