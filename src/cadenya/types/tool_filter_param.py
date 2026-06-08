# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from .attribute_filter_param import AttributeFilterParam

__all__ = ["ToolFilterParam"]


class ToolFilterParam(TypedDict, total=False):
    """Top-level filter with simple boolean logic (no nesting)"""

    operator: Required[Literal["OPERATOR_UNSPECIFIED", "OPERATOR_AND", "OPERATOR_OR"]]

    filters: Iterable[AttributeFilterParam]
