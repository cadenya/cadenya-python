# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ObjectiveToolCallResultImageBlock"]


class ObjectiveToolCallResultImageBlock(BaseModel):
    expires_at: datetime = FieldInfo(alias="expiresAt")
    """When the signed URL expires."""

    mime_type: str = FieldInfo(alias="mimeType")
    """IANA media type of the stored image, e.g. image/png."""

    size_bytes: str = FieldInfo(alias="sizeBytes")
    """Size of the stored image in bytes."""

    url: str
    """Short-lived signed URL to download the stored image."""
