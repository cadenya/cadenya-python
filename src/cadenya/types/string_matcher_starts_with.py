# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["StringMatcherStartsWith"]


class StringMatcherStartsWith(BaseModel):
    starts_with: str = FieldInfo(alias="startsWith")

    type: Literal["startsWith"]

    case_sensitive: Optional[bool] = FieldInfo(alias="caseSensitive", default=None)
