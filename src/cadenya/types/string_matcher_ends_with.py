# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["StringMatcherEndsWith"]


class StringMatcherEndsWith(BaseModel):
    ends_with: str = FieldInfo(alias="endsWith")

    type: Literal["endsWith"]

    case_sensitive: Optional[bool] = FieldInfo(alias="caseSensitive", default=None)
