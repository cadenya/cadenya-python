# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["StringMatcherStartsWithParam"]


class StringMatcherStartsWithParam(TypedDict, total=False):
    starts_with: Required[Annotated[str, PropertyInfo(alias="startsWith")]]

    type: Required[Literal["startsWith"]]

    case_sensitive: Annotated[bool, PropertyInfo(alias="caseSensitive")]
