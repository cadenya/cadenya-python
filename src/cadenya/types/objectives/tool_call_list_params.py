# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ToolCallListParams"]


class ToolCallListParams(TypedDict, total=False):
    workspace_id: Required[Annotated[str, PropertyInfo(alias="workspaceId")]]

    cursor: str
    """Pagination cursor from previous response"""

    include_info: Annotated[bool, PropertyInfo(alias="includeInfo")]
    """When set to true you may use more of your alloted API rate-limit"""

    limit: int
    """Maximum number of results to return"""

    status: Literal[
        "TOOL_CALL_STATUS_UNSPECIFIED",
        "TOOL_CALL_STATUS_AUTO_APPROVED",
        "TOOL_CALL_STATUS_WAITING_FOR_APPROVAL",
        "TOOL_CALL_STATUS_APPROVED",
        "TOOL_CALL_STATUS_DENIED",
    ]
    """Filter by tool call status"""
