# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .set_tool_call_content_request_content_block_text_param import SetToolCallContentRequestContentBlockTextParam
from .set_tool_call_content_request_content_block_audio_param import SetToolCallContentRequestContentBlockAudioParam
from .set_tool_call_content_request_content_block_image_param import SetToolCallContentRequestContentBlockImageParam

__all__ = ["SetToolCallContentRequestContentBlockParam"]

SetToolCallContentRequestContentBlockParam: TypeAlias = Union[
    SetToolCallContentRequestContentBlockTextParam,
    SetToolCallContentRequestContentBlockImageParam,
    SetToolCallContentRequestContentBlockAudioParam,
]
