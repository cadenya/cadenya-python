# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .mcp_annotations_param import MCPAnnotationsParam

__all__ = ["ConfigMCPParam"]


class ConfigMCPParam(TypedDict, total=False):
    annotations: MCPAnnotationsParam
    """
    Behavior hints synced from the MCP server's tool definition (ToolAnnotations in
    the MCP specification). All hints are advisory: servers are not required to send
    them, and clients should not rely on them for security decisions. Absent hints
    keep the MCP spec defaults (destructiveHint and openWorldHint default to true;
    readOnlyHint and idempotentHint default to false).
    """
