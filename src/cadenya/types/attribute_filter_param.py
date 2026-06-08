# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .string_matcher_param import StringMatcherParam

__all__ = ["AttributeFilterParam"]


class AttributeFilterParam(TypedDict, total=False):
    """Single attribute filter"""

    attribute: Required[Literal["ATTRIBUTE_UNSPECIFIED", "ATTRIBUTE_NAME", "ATTRIBUTE_TITLE", "ATTRIBUTE_DESCRIPTION"]]

    matcher: StringMatcherParam
    """String matching operations"""
