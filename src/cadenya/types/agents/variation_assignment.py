# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from ..._utils import PropertyInfo
from .variation_assignment_tool import VariationAssignmentTool
from .variation_assignment_agent import VariationAssignmentAgent
from .variation_assignment_tool_set import VariationAssignmentToolSet

__all__ = ["VariationAssignment"]

VariationAssignment: TypeAlias = Annotated[
    Union[VariationAssignmentTool, VariationAssignmentToolSet, VariationAssignmentAgent],
    PropertyInfo(discriminator="type"),
]
