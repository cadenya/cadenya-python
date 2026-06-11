# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MemoryReferenceParam"]


class MemoryReferenceParam(TypedDict, total=False):
    """
    MemoryReference identifies a memory layer or a specific entry within
     one, for composition into a memory cascade. Used on objectives (where
     entry pinning is permitted).

     memory_layer_id accepts both the canonical form (memlyr_…) and the
     external-id form (external_id:my-custom-id). The same applies to
     memory_entry_id when set.
    """

    memory_entry_id: Annotated[str, PropertyInfo(alias="memoryEntryId")]
    """
    When set, inserts only this entry from memory_layer_id into the cascade —
    behaves as a single-entry layer (only this key resolves at this position). The
    entry must belong to memory_layer_id; mismatches are rejected with
    InvalidArgument.
    """

    memory_layer_id: Annotated[str, PropertyInfo(alias="memoryLayerId")]
