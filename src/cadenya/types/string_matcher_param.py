# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .string_matcher_exact_param import StringMatcherExactParam
from .string_matcher_regex_param import StringMatcherRegexParam
from .string_matcher_contains_param import StringMatcherContainsParam
from .string_matcher_ends_with_param import StringMatcherEndsWithParam
from .string_matcher_starts_with_param import StringMatcherStartsWithParam

__all__ = ["StringMatcherParam"]

StringMatcherParam: TypeAlias = Union[
    StringMatcherExactParam,
    StringMatcherStartsWithParam,
    StringMatcherEndsWithParam,
    StringMatcherContainsParam,
    StringMatcherRegexParam,
]
