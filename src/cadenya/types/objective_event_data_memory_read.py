# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .memory_read import MemoryRead

__all__ = ["ObjectiveEventDataMemoryRead"]


class ObjectiveEventDataMemoryRead(BaseModel):
    memory_read: MemoryRead = FieldInfo(alias="memoryRead")
    """
    MemoryRead is emitted each time the agent resolves a key against the memory
    cascade and loads an entry. Lookups that miss (key not found in any layer) do
    not emit this event.
    """

    type: Literal["memoryRead"]
