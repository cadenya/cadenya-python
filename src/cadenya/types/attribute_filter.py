# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .string_matcher import StringMatcher

__all__ = ["AttributeFilter"]


class AttributeFilter(BaseModel):
    """Single attribute filter"""

    attribute: Literal["ATTRIBUTE_UNSPECIFIED", "ATTRIBUTE_NAME", "ATTRIBUTE_TITLE", "ATTRIBUTE_DESCRIPTION"]

    matcher: Optional[StringMatcher] = None
    """String matching operations"""
