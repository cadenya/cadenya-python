# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .objective_context_window_data import ObjectiveContextWindowData

__all__ = ["ObjectiveCompactResponse"]


class ObjectiveCompactResponse(BaseModel):
    """Compact objective response"""

    context_window: Optional[ObjectiveContextWindowData] = FieldInfo(alias="contextWindow", default=None)
    """The new context window created by the compaction"""
