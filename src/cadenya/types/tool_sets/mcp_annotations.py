# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["McpAnnotations"]


class McpAnnotations(BaseModel):
    """
    Behavior hints synced from the MCP server's tool definition
     (ToolAnnotations in the MCP specification). All hints are advisory:
     servers are not required to send them, and clients should not rely
     on them for security decisions. Absent hints keep the MCP spec
     defaults (destructiveHint and openWorldHint default to true;
     readOnlyHint and idempotentHint default to false).
    """

    destructive_hint: Optional[bool] = FieldInfo(alias="destructiveHint", default=None)
    """
    If true, the tool may perform destructive updates to its environment. Only
    meaningful when read_only_hint is false.
    """

    idempotent_hint: Optional[bool] = FieldInfo(alias="idempotentHint", default=None)
    """
    If true, calling the tool repeatedly with the same arguments has no additional
    effect. Only meaningful when read_only_hint is false.
    """

    open_world_hint: Optional[bool] = FieldInfo(alias="openWorldHint", default=None)
    """If true, the tool may interact with an "open world" of external entities (e.g.

    web search); if false, its domain is closed.
    """

    read_only_hint: Optional[bool] = FieldInfo(alias="readOnlyHint", default=None)
    """If true, the tool does not modify its environment."""

    title: Optional[str] = None
    """A human-readable title for the tool."""
