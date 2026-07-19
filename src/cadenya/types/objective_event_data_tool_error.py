# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .tool_error import ToolError

__all__ = ["ObjectiveEventDataToolError"]


class ObjectiveEventDataToolError(BaseModel):
    tool_error: ToolError = FieldInfo(alias="toolError")

    type: Literal["toolError"]
