# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["UploadSpecParam"]


class UploadSpecParam(TypedDict, total=False):
    content_type: Required[Annotated[str, PropertyInfo(alias="contentType")]]
    """MIME type the client will send.

    Baked into the presigned URL's signature — the PUT must match exactly or object
    storage will reject it.
    """

    filename: Required[str]
    """Client-supplied filename.

    Used for audit and display only; does not control the object's storage path.
    """

    size_bytes: Required[Annotated[str, PropertyInfo(alias="sizeBytes")]]
    """Expected size of the upload in bytes.

    Baked into the presigned URL as a Content-Length constraint.
    """
