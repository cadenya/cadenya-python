# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["McpAnnotationsParam"]


class McpAnnotationsParam(TypedDict, total=False):
    """
    Behavior hints synced from the MCP server's tool definition
     (ToolAnnotations in the MCP specification). All hints are advisory:
     servers are not required to send them, and clients should not rely
     on them for security decisions. Absent hints keep the MCP spec
     defaults (destructiveHint and openWorldHint default to true;
     readOnlyHint and idempotentHint default to false).
    """

    destructive_hint: Annotated[bool, PropertyInfo(alias="destructiveHint")]
    """
    If true, the tool may perform destructive updates to its environment. Only
    meaningful when read_only_hint is false.
    """

    idempotent_hint: Annotated[bool, PropertyInfo(alias="idempotentHint")]
    """
    If true, calling the tool repeatedly with the same arguments has no additional
    effect. Only meaningful when read_only_hint is false.
    """

    open_world_hint: Annotated[bool, PropertyInfo(alias="openWorldHint")]
    """If true, the tool may interact with an "open world" of external entities (e.g.

    web search); if false, its domain is closed.
    """

    read_only_hint: Annotated[bool, PropertyInfo(alias="readOnlyHint")]
    """If true, the tool does not modify its environment."""

    title: str
    """A human-readable title for the tool."""
