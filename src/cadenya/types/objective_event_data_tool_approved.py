# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .tool_approved import ToolApproved

__all__ = ["ObjectiveEventDataToolApproved"]


class ObjectiveEventDataToolApproved(BaseModel):
    tool_approved: ToolApproved = FieldInfo(alias="toolApproved")

    type: Literal["toolApproved"]
