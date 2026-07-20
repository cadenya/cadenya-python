# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["MemoryEntrySpec"]


class MemoryEntrySpec(BaseModel):
    """
    MemoryEntrySpec is the metadata portion of an entry — the fields that
     identify and describe it, without the body. It appears on both the summary
     (MemoryEntry) and detail (MemoryEntryDetail) views.
    """

    key: str
    """The lookup key for this entry within its layer.

    Must conform to the S3 object key safe-characters spec: ASCII alphanumerics and
    the special characters !, -, \\__, ., \\**, ', (, ), and /. Forward slashes may be
    used to suggest hierarchy (e.g., "skills/postmortem/write"), but lookups are
    flat — the key is a single opaque string, not a path.

    Additional rules enforced by the service:

    - May not begin or end with /
    - May not contain consecutive slashes (//)
    - May not begin with reserved prefixes (cadenya/, system/)
    - Case-sensitive
    - Unique within the parent layer

    For skills entries, this key is what the model passes to get_memory to load the
    entry's content.
    """

    description: Optional[str] = None
    """
    One-line "when to use this" hint shown in the frontmatter manifest for skills
    entries. The model uses this to decide whether to load the body, so it should be
    written for the model as the audience. Ignored for layer types that do not
    advertise frontmatter.
    """
