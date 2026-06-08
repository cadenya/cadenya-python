# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["StringMatcher"]


class StringMatcher(BaseModel):
    """String matching operations"""

    case_sensitive: Optional[bool] = FieldInfo(alias="caseSensitive", default=None)

    contains: Optional[str] = None

    ends_with: Optional[str] = FieldInfo(alias="endsWith", default=None)

    exact: Optional[str] = None

    regex: Optional[str] = None

    starts_with: Optional[str] = FieldInfo(alias="startsWith", default=None)
