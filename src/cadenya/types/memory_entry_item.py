# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MemoryEntryItem"]


class MemoryEntryItem(BaseModel):
    key: str

    content: Optional[str] = None

    description: Optional[str] = None

    upload_id: Optional[str] = FieldInfo(alias="uploadId", default=None)
