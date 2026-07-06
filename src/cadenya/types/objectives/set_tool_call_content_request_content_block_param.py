# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .set_tool_call_content_request_text_block_param import SetToolCallContentRequestTextBlockParam
from .set_tool_call_content_request_audio_block_param import SetToolCallContentRequestAudioBlockParam
from .set_tool_call_content_request_image_block_param import SetToolCallContentRequestImageBlockParam

__all__ = ["SetToolCallContentRequestContentBlockParam"]


class SetToolCallContentRequestContentBlockParam(TypedDict, total=False):
    """
    ContentBlock is a single block of tool call content supplied on input.
     Exactly one of the variants is set.
    """

    audio: SetToolCallContentRequestAudioBlockParam

    image: SetToolCallContentRequestImageBlockParam

    text: SetToolCallContentRequestTextBlockParam
