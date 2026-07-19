# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .tool_approval_requested import ToolApprovalRequested

__all__ = ["ObjectiveEventDataToolApprovalRequested"]


class ObjectiveEventDataToolApprovalRequested(BaseModel):
    tool_approval_requested: ToolApprovalRequested = FieldInfo(alias="toolApprovalRequested")

    type: Literal["toolApprovalRequested"]
