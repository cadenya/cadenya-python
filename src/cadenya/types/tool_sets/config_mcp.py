# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .mcp_annotations import MCPAnnotations

__all__ = ["ConfigMCP"]


class ConfigMCP(BaseModel):
    annotations: Optional[MCPAnnotations] = None
    """
    Behavior hints synced from the MCP server's tool definition (ToolAnnotations in
    the MCP specification). All hints are advisory: servers are not required to send
    them, and clients should not rely on them for security decisions. Absent hints
    keep the MCP spec defaults (destructiveHint and openWorldHint default to true;
    readOnlyHint and idempotentHint default to false).
    """
