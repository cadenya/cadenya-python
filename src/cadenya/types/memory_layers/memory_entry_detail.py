# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .memory_entry_info import MemoryEntryInfo
from .memory_entry_spec import MemoryEntrySpec
from ..shared.resource_metadata import ResourceMetadata

__all__ = ["MemoryEntryDetail"]


class MemoryEntryDetail(BaseModel):
    """
    MemoryEntryDetail is the full representation of an entry, including the
     resolved content body. Returned by GetMemoryEntry, CreateMemoryEntry, and
     UpdateMemoryEntry.
    """

    content: str
    """The resolved body of the entry.

    For entries created or updated via an upload_id, this is the ingested content,
    not the original upload handle. May be empty; an entry with only a key and
    description is valid (e.g., a stub skill being drafted, or an entry where the
    frontmatter alone is the payload).
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
