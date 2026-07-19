# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["StringMatcherRegex"]


class StringMatcherRegex(BaseModel):
    regex: str

    type: Literal["regex"]

    case_sensitive: Optional[bool] = FieldInfo(alias="caseSensitive", default=None)
