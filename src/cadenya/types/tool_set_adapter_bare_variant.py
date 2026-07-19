# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .tool_set_adapter_bare import ToolSetAdapterBare

__all__ = ["ToolSetAdapterBareVariant"]


class ToolSetAdapterBareVariant(BaseModel):
    bare: ToolSetAdapterBare
    """Bare tool sets define tools without an execution adapter.

    A bare tool call doesn't fire anything: the objective's workflow pauses and
    waits for an external API consumer to set the tool call's content (e.g.
    human-in-the-loop tools, or a reverse harness that polls for pending tool calls,
    executes locally, and reports results back via SetToolCallContent).
    """

    type: Literal["bare"]
