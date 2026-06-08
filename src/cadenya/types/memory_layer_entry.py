# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel
from .memory_entry_item import MemoryEntryItem
from .memory_layer_spec import MemoryLayerSpec

__all__ = ["MemoryLayerEntry"]


class MemoryLayerEntry(BaseModel):
    name: str

    spec: MemoryLayerSpec

    entries: Optional[Dict[str, MemoryEntryItem]] = None
    """Memory entries in this layer, keyed by external_id."""

    labels: Optional[Dict[str, str]] = None
