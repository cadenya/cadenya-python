# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

from .memory_entry_item_param import MemoryEntryItemParam
from .memory_layer_spec_param import MemoryLayerSpecParam

__all__ = ["MemoryLayerEntryParam"]


class MemoryLayerEntryParam(TypedDict, total=False):
    name: Required[str]

    spec: Required[MemoryLayerSpecParam]

    entries: Dict[str, MemoryEntryItemParam]
    """Memory entries in this layer, keyed by external_id."""

    labels: Dict[str, str]
