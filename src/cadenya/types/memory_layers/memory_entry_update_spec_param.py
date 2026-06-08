# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MemoryEntryUpdateSpecParam"]


class MemoryEntryUpdateSpecParam(TypedDict, total=False):
    """MemoryEntryUpdateSpec is the input shape for UpdateMemoryEntry.

    Fields
     present in the request's update_mask are applied; unset fields are left
     alone. The source oneof is optional for updates — omit it to leave the
     body untouched, or set exactly one branch to replace it.
    """

    content: str

    description: str

    key: str

    upload_id: Annotated[str, PropertyInfo(alias="uploadId")]
