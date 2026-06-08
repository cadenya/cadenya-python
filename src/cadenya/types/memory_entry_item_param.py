# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MemoryEntryItemParam"]


class MemoryEntryItemParam(TypedDict, total=False):
    key: Required[str]

    content: str

    description: str

    upload_id: Annotated[str, PropertyInfo(alias="uploadId")]
