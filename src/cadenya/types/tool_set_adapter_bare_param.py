# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ToolSetAdapterBareParam"]


class ToolSetAdapterBareParam(TypedDict, total=False):
    """Bare tool sets define tools without an execution adapter.

    A bare tool
     call doesn't fire anything: the objective's workflow pauses and waits
     for an external API consumer to set the tool call's content (e.g.
     human-in-the-loop tools, or a reverse harness that polls for pending
     tool calls, executes locally, and reports results back via
     SetToolCallContent).
    """

    content_timeout: Annotated[int, PropertyInfo(alias="contentTimeout")]
    """
    How long to wait for content to be set before the tool call errors. If unset,
    the call waits indefinitely.
    """
