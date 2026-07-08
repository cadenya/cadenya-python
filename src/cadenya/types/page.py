# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Page"]


class Page(BaseModel):
    """Page carries cursor-based pagination state.

    There is no total: the cursor
     walks the result set without ever counting it, and a count would cost a second
     query on every list.
    """

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
