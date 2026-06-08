# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .memory_entry_info import MemoryEntryInfo
from .memory_entry_spec import MemoryEntrySpec
from ..shared.resource_metadata import ResourceMetadata

__all__ = ["MemoryEntry"]


class MemoryEntry(BaseModel):
    """MemoryEntry is a single keyed value within a MemoryLayer.

    Entries are
     addressed by their key, which follows the S3 object key safe-character
     convention (see MemoryEntrySpec.key for the full rule). Keys are unique
     within a single layer; the same key may appear in multiple layers, in which
     case the LIFO stack-walk determines which one wins for a given objective.

     MemoryEntry is the summary shape, returned by ListMemoryEntries. It does
     not carry the entry body — callers that need the body must fetch the entry
     individually via GetMemoryEntry, which returns a MemoryEntryDetail.
    """

    metadata: ResourceMetadata
    """
    Standard metadata for persistent, named resources (e.g., agents, tools, prompts)
    """

    spec: MemoryEntrySpec
    """
    MemoryEntrySpec is the metadata portion of an entry — the fields that identify
    and describe it, without the body. It appears on both the summary (MemoryEntry)
    and detail (MemoryEntryDetail) views.
    """

    info: Optional[MemoryEntryInfo] = None
