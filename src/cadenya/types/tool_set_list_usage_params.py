# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ToolSetListUsageParams"]


class ToolSetListUsageParams(TypedDict, total=False):
    workspace_id: Annotated[str, PropertyInfo(alias="workspaceId")]

    cursor: str
    """Pagination cursor from previous response"""

    limit: int
    """Maximum number of results to return"""

    sort_order: Annotated[str, PropertyInfo(alias="sortOrder")]
    """Sort order for results (asc or desc by assignment creation time)"""

    tool_id: Annotated[str, PropertyInfo(alias="toolId")]
    """
    When set, lists only variations with a direct assignment of this individual
    tool. When unset, lists variations assigned the whole tool set. The tool must
    belong to the tool set.
    """
