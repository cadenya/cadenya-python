# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .tool_filter import ToolFilter

__all__ = ["ApprovalRequirementFilterOnly"]


class ApprovalRequirementFilterOnly(BaseModel):
    only: ToolFilter
    """Top-level filter with simple boolean logic (no nesting)"""

    type: Literal["only"]
