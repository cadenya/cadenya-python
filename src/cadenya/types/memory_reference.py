# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MemoryReference"]


class MemoryReference(BaseModel):
    """
    MemoryReference identifies a memory layer or a specific entry within
     one, for composition into a memory stack. Used on objectives (where
     entry pinning is permitted).

     memory_layer_id accepts both the canonical form (memlyr_…) and the
     external-id form (external_id:my-custom-id). The same applies to
     memory_entry_id when set.
    """

    memory_entry_id: Optional[str] = FieldInfo(alias="memoryEntryId", default=None)
    """
    When set, pushes only this entry from memory_layer_id onto the stack — behaves
    as a single-entry layer (only this key resolves at this position). The entry
    must belong to memory_layer_id; mismatches are rejected with InvalidArgument.
    """

    memory_layer_id: Optional[str] = FieldInfo(alias="memoryLayerId", default=None)
