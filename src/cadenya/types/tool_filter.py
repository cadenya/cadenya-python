# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .attribute_filter import AttributeFilter

__all__ = ["ToolFilter"]


class ToolFilter(BaseModel):
    """Top-level filter with simple boolean logic (no nesting)"""

    operator: Literal["OPERATOR_UNSPECIFIED", "OPERATOR_AND", "OPERATOR_OR"]

    filters: Optional[List[AttributeFilter]] = None
