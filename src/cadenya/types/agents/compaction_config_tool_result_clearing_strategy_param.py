# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CompactionConfigToolResultClearingStrategyParam"]


class CompactionConfigToolResultClearingStrategyParam(TypedDict, total=False):
    """ToolResultClearingStrategy configures clearing of older tool result content."""

    preserve_recent_results: Annotated[int, PropertyInfo(alias="preserveRecentResults")]
    """
    Number of most recent tool call results to keep intact. Older tool results have
    their content replaced with "[result cleared]" while preserving the assistant
    tool call message (function name, arguments). Default: 2
    """
