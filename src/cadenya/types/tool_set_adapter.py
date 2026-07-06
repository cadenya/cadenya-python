# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .tool_set_adapter_mcp import ToolSetAdapterMcp
from .tool_set_adapter_bare import ToolSetAdapterBare
from .tool_set_adapter_http import ToolSetAdapterHTTP
from .tool_set_adapter_openapi import ToolSetAdapterOpenAPI

__all__ = ["ToolSetAdapter"]


class ToolSetAdapter(BaseModel):
    bare: Optional[ToolSetAdapterBare] = None
    """Bare tool sets define tools without an execution adapter.

    A bare tool call doesn't fire anything: the objective's workflow pauses and
    waits for an external API consumer to set the tool call's content (e.g.
    human-in-the-loop tools, or a reverse harness that polls for pending tool calls,
    executes locally, and reports results back via SetToolCallContent).
    """

    http: Optional[ToolSetAdapterHTTP] = None

    mcp: Optional[ToolSetAdapterMcp] = None

    openapi: Optional[ToolSetAdapterOpenAPI] = None
