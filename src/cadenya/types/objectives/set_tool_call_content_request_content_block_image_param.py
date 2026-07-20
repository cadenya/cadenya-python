# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .set_tool_call_content_request_image_block_param import SetToolCallContentRequestImageBlockParam

__all__ = ["SetToolCallContentRequestContentBlockImageParam"]


class SetToolCallContentRequestContentBlockImageParam(TypedDict, total=False):
    image: Required[SetToolCallContentRequestImageBlockParam]

    type: Required[Literal["image"]]
