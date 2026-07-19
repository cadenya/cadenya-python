# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .string_matcher_exact import StringMatcherExact
from .string_matcher_regex import StringMatcherRegex
from .string_matcher_contains import StringMatcherContains
from .string_matcher_ends_with import StringMatcherEndsWith
from .string_matcher_starts_with import StringMatcherStartsWith

__all__ = ["StringMatcher"]

StringMatcher: TypeAlias = Annotated[
    Union[
        StringMatcherExact, StringMatcherStartsWith, StringMatcherEndsWith, StringMatcherContains, StringMatcherRegex
    ],
    PropertyInfo(discriminator="type"),
]
