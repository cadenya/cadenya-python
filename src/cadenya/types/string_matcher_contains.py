# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["StringMatcherContains"]


class StringMatcherContains(BaseModel):
    contains: str

    type: Literal["contains"]

    case_sensitive: Optional[bool] = FieldInfo(alias="caseSensitive", default=None)
