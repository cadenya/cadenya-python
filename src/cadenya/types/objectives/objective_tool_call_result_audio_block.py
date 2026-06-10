# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ObjectiveToolCallResultAudioBlock"]


class ObjectiveToolCallResultAudioBlock(BaseModel):
    expires_at: datetime = FieldInfo(alias="expiresAt")
    """When the signed URL expires."""

    mime_type: str = FieldInfo(alias="mimeType")
    """IANA media type of the stored audio, e.g. audio/wav."""

    size_bytes: str = FieldInfo(alias="sizeBytes")
    """Size of the stored audio in bytes."""

    url: str
    """Short-lived signed URL to download the stored audio."""
