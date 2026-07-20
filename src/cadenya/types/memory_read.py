# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MemoryRead"]


class MemoryRead(BaseModel):
    """
    MemoryRead is emitted each time the agent resolves a key against the
     memory cascade and loads an entry. Lookups that miss (key not found in
     any layer) do not emit this event.
    """

    memory_entry_id: Optional[str] = FieldInfo(alias="memoryEntryId", default=None)
    """The specific entry that was read."""

    memory_layer_id: Optional[str] = FieldInfo(alias="memoryLayerId", default=None)
    """The layer the entry resolved to.

    The top-most layer that contained the key — other layers beneath it that also
    contained the key are shadowed and not referenced here.
    """

    message: Optional[str] = None
    """Human-readable description of the read, set by the runtime.

    For example: "Loaded skill", "Resolved context key". Not machine-parsed;
    intended for UI display alongside the other events in an objective's timeline.
    """
