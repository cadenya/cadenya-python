# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["StringMatcherExactParam"]


class StringMatcherExactParam(TypedDict, total=False):
    exact: Required[str]

    type: Required[Literal["exact"]]

    case_sensitive: Annotated[bool, PropertyInfo(alias="caseSensitive")]
