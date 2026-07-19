# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .set_tool_call_content_request_text_block_param import SetToolCallContentRequestTextBlockParam

__all__ = ["SetToolCallContentRequestContentBlockTextParam"]


class SetToolCallContentRequestContentBlockTextParam(TypedDict, total=False):
    text: Required[SetToolCallContentRequestTextBlockParam]

    type: Required[Literal["text"]]
