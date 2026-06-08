# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel
from .tool_sets.tool_spec import ToolSpec

__all__ = ["ToolEntry"]


class ToolEntry(BaseModel):
    name: str

    spec: ToolSpec

    labels: Optional[Dict[str, str]] = None
