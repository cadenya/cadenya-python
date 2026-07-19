# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MemoryEntryCreateSpecUploadIDParam"]


class MemoryEntryCreateSpecUploadIDParam(TypedDict, total=False):
    type: Required[Literal["uploadId"]]

    upload_id: Required[Annotated[str, PropertyInfo(alias="uploadId")]]
    """ID of a COMPLETE Upload.

    The server reads the object from storage, copies its bytes into the entry, and
    marks the upload consumed.
    """

    description: str

    key: str
    """See MemoryEntrySpec.key for the full rule set. Same constraints apply here."""
