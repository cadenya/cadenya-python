# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .memory_layer_info import MemoryLayerInfo
from .memory_layer_spec import MemoryLayerSpec
from .shared.resource_metadata import ResourceMetadata

__all__ = ["MemoryLayer"]


class MemoryLayer(BaseModel):
    """
    MemoryLayer is a named container of memory entries that can be composed into
     an objective's memory stack. Layers are workspace-scoped resources. The layer
     type controls how its entries participate in the agent loop — see
     MemoryLayerType for details.

     See "Memory stack composition" above for how layers compose at lookup time.
    """

    metadata: ResourceMetadata
    """
    Standard metadata for persistent, named resources (e.g., agents, tools, prompts)
    """

    spec: MemoryLayerSpec

    info: Optional[MemoryLayerInfo] = None
