# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .tool_result import ToolResult

__all__ = ["ObjectiveEventDataToolResult"]


class ObjectiveEventDataToolResult(BaseModel):
    tool_result: ToolResult = FieldInfo(alias="toolResult")

    type: Literal["toolResult"]
