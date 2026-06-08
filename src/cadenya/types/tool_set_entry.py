# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel
from .tool_entry import ToolEntry
from .tool_set_spec import ToolSetSpec

__all__ = ["ToolSetEntry"]


class ToolSetEntry(BaseModel):
    name: str

    spec: ToolSetSpec

    labels: Optional[Dict[str, str]] = None

    tools: Optional[Dict[str, ToolEntry]] = None
    """Tools in this tool set, keyed by external_id."""
