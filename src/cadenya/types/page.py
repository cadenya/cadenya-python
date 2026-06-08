# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Page"]


class Page(BaseModel):
    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)

    total: Optional[int] = None
