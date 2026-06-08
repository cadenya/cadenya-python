# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["StringMatcherParam"]


class StringMatcherParam(TypedDict, total=False):
    """String matching operations"""

    case_sensitive: Annotated[bool, PropertyInfo(alias="caseSensitive")]

    contains: str

    ends_with: Annotated[str, PropertyInfo(alias="endsWith")]

    exact: str

    regex: str

    starts_with: Annotated[str, PropertyInfo(alias="startsWith")]
