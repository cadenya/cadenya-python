# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["VariationMemoryLayerEntry"]


class VariationMemoryLayerEntry(BaseModel):
    memory_layer_id: Optional[str] = FieldInfo(alias="memoryLayerId", default=None)
    """external_id:<value> form. Canonical IDs are rejected."""

    position: Optional[int] = None
