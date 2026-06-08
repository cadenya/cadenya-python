# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CompactionConfigToolResultClearingStrategy"]


class CompactionConfigToolResultClearingStrategy(BaseModel):
    """ToolResultClearingStrategy configures clearing of older tool result content."""

    preserve_recent_results: Optional[int] = FieldInfo(alias="preserveRecentResults", default=None)
    """
    Number of most recent tool call results to keep intact. Older tool results have
    their content replaced with "[result cleared]" while preserving the assistant
    tool call message (function name, arguments). Default: 2
    """
