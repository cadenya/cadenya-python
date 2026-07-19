# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .tool_denied import ToolDenied

__all__ = ["ObjectiveEventDataToolDenied"]


class ObjectiveEventDataToolDenied(BaseModel):
    tool_denied: ToolDenied = FieldInfo(alias="toolDenied")

    type: Literal["toolDenied"]
