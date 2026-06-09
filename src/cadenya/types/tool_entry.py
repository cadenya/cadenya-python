# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .tool_sets.tool_spec import ToolSpec

__all__ = ["ToolEntry"]


class ToolEntry(BaseModel):
    name: str

    spec: ToolSpec

    labels: Optional[Dict[str, str]] = None

    state: Optional[Literal["STATE_UNSPECIFIED", "STATE_AVAILABLE", "STATE_OMITTED", "STATE_ARCHIVED"]] = None
    """Desired lifecycle state for the tool.

    Defaults to STATE_AVAILABLE when unspecified. STATE_ARCHIVED is server-managed
    and is rejected here.
    """
