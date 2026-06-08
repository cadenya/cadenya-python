# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .tool_set_adapter import ToolSetAdapter

__all__ = ["ToolSetSpec"]


class ToolSetSpec(BaseModel):
    adapter: Optional[ToolSetAdapter] = None

    description: Optional[str] = None
