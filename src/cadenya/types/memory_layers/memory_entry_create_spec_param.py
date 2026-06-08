# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MemoryEntryCreateSpecParam"]


class MemoryEntryCreateSpecParam(TypedDict, total=False):
    """MemoryEntryCreateSpec is the input shape for CreateMemoryEntry.

    It accepts
     either inline content or a reference to a completed Upload; exactly one of
     the two must be set.
    """

    key: Required[str]
    """See MemoryEntrySpec.key for the full rule set. Same constraints apply here."""

    content: str
    """Inline content, written directly into the entry."""

    description: str

    upload_id: Annotated[str, PropertyInfo(alias="uploadId")]
    """ID of a COMPLETE Upload.

    The server reads the object from storage, copies its bytes into the entry, and
    marks the upload consumed.
    """
