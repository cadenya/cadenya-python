# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["UploadSpec"]


class UploadSpec(BaseModel):
    content_type: str = FieldInfo(alias="contentType")
    """MIME type the client will send.

    Baked into the presigned URL's signature — the PUT must match exactly or object
    storage will reject it.
    """

    filename: str
    """Client-supplied filename.

    Used for audit and display only; does not control the object's storage path.
    """

    size_bytes: str = FieldInfo(alias="sizeBytes")
    """Expected size of the upload in bytes.

    Baked into the presigned URL as a Content-Length constraint.
    """
