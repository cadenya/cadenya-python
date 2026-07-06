# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .tool_set_adapter_mcp_param import ToolSetAdapterMcpParam
from .tool_set_adapter_bare_param import ToolSetAdapterBareParam
from .tool_set_adapter_http_param import ToolSetAdapterHTTPParam
from .tool_set_adapter_openapi_param import ToolSetAdapterOpenAPIParam

__all__ = ["ToolSetAdapterParam"]


class ToolSetAdapterParam(TypedDict, total=False):
    bare: ToolSetAdapterBareParam
    """Bare tool sets define tools without an execution adapter.

    A bare tool call doesn't fire anything: the objective's workflow pauses and
    waits for an external API consumer to set the tool call's content (e.g.
    human-in-the-loop tools, or a reverse harness that polls for pending tool calls,
    executes locally, and reports results back via SetToolCallContent).
    """

    http: ToolSetAdapterHTTPParam

    mcp: ToolSetAdapterMcpParam

    openapi: ToolSetAdapterOpenAPIParam
