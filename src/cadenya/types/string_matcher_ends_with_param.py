# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["StringMatcherEndsWithParam"]


class StringMatcherEndsWithParam(TypedDict, total=False):
    ends_with: Required[Annotated[str, PropertyInfo(alias="endsWith")]]

    type: Required[Literal["endsWith"]]

    case_sensitive: Annotated[bool, PropertyInfo(alias="caseSensitive")]
