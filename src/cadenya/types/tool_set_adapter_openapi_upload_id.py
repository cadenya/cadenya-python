# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .tool_filter import ToolFilter
from .approval_requirement_filter import ApprovalRequirementFilter

__all__ = ["ToolSetAdapterOpenAPIUploadID"]


class ToolSetAdapterOpenAPIUploadID(BaseModel):
    type: Literal["uploadId"]

    upload_id: str = FieldInfo(alias="uploadId")
    """ID of a COMPLETE Upload containing the OpenAPI spec document."""

    base_url: Optional[str] = FieldInfo(alias="baseUrl", default=None)
    """Base URL for dispatching tool calls.

    If set, overrides the server resolved from the spec's servers array.
    """

    exclude_tools: Optional[ToolFilter] = FieldInfo(alias="excludeTools", default=None)
    """Top-level filter with simple boolean logic (no nesting)"""

    headers: Optional[Dict[str, str]] = None
    """Headers sent when fetching the spec from a URL and when dispatching tool calls."""

    include_tools: Optional[ToolFilter] = FieldInfo(alias="includeTools", default=None)
    """Top-level filter with simple boolean logic (no nesting)"""

    server_name: Optional[str] = FieldInfo(alias="serverName", default=None)
    """
    Name of the server entry in the spec's servers array (OpenAPI 3.2 server.name
    field). Used to select which server URL to dispatch to when base_url is not set.
    If unset, the first server is used. Ignored when base_url is set.
    """

    tool_approvals: Optional[ApprovalRequirementFilter] = FieldInfo(alias="toolApprovals", default=None)
    """
    Approval filters that will automatically set the approval requirement on tools
    synced from an external source
    """
