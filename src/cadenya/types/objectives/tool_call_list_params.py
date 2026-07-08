# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ToolCallListParams"]


class ToolCallListParams(TypedDict, total=False):
    workspace_id: Required[Annotated[str, PropertyInfo(alias="workspaceId")]]

    cursor: str
    """Pagination cursor from previous response"""

    execution_status: Annotated[
        Literal[
            "TOOL_CALL_EXECUTION_STATUS_UNSPECIFIED",
            "TOOL_CALL_EXECUTION_STATUS_PENDING",
            "TOOL_CALL_EXECUTION_STATUS_RUNNING",
            "TOOL_CALL_EXECUTION_STATUS_COMPLETED",
            "TOOL_CALL_EXECUTION_STATUS_ERRORED",
            "TOOL_CALL_EXECUTION_STATUS_WAITING_FOR_CONTENT",
        ],
        PropertyInfo(alias="executionStatus"),
    ]
    """Filter by tool call execution status.

    Useful for reverse-harness polling of bare tool calls waiting for externally
    supplied content (TOOL_CALL_EXECUTION_STATUS_WAITING_FOR_CONTENT).
    """

    include_info: Annotated[bool, PropertyInfo(alias="includeInfo")]
    """When set to true you may use more of your alloted API rate-limit"""

    labels: str
    """Filters by metadata labels.

    Comma-separated key=value pairs, e.g. "env=prod,team=ai". A resource matches
    only if every pair matches exactly (AND semantics).
    """

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
