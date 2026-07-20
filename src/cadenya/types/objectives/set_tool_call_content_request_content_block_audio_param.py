# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .set_tool_call_content_request_audio_block_param import SetToolCallContentRequestAudioBlockParam

__all__ = ["SetToolCallContentRequestContentBlockAudioParam"]


class SetToolCallContentRequestContentBlockAudioParam(TypedDict, total=False):
    audio: Required[SetToolCallContentRequestAudioBlockParam]

    type: Required[Literal["audio"]]
