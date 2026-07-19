# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .approval_requirement_filter_only_param import ApprovalRequirementFilterOnlyParam
from .approval_requirement_filter_always_param import ApprovalRequirementFilterAlwaysParam

__all__ = ["ApprovalRequirementFilterParam"]

ApprovalRequirementFilterParam: TypeAlias = Union[
    ApprovalRequirementFilterAlwaysParam, ApprovalRequirementFilterOnlyParam
]
