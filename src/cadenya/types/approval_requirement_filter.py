# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .approval_requirement_filter_only import ApprovalRequirementFilterOnly
from .approval_requirement_filter_always import ApprovalRequirementFilterAlways

__all__ = ["ApprovalRequirementFilter"]

ApprovalRequirementFilter: TypeAlias = Annotated[
    Union[ApprovalRequirementFilterAlways, ApprovalRequirementFilterOnly], PropertyInfo(discriminator="type")
]
