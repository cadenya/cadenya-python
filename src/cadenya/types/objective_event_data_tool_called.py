# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .tool_called import ToolCalled

__all__ = ["ObjectiveEventDataToolCalled"]


class ObjectiveEventDataToolCalled(BaseModel):
    tool_called: ToolCalled = FieldInfo(alias="toolCalled")

    type: Literal["toolCalled"]
