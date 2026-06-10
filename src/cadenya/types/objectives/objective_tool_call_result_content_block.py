# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .objective_tool_call_result_text_block import ObjectiveToolCallResultTextBlock
from .objective_tool_call_result_audio_block import ObjectiveToolCallResultAudioBlock
from .objective_tool_call_result_image_block import ObjectiveToolCallResultImageBlock

__all__ = ["ObjectiveToolCallResultContentBlock"]


class ObjectiveToolCallResultContentBlock(BaseModel):
    """ContentBlock is a single block of tool result content.

    Exactly one of
     the variants is set.
    """

    audio: Optional[ObjectiveToolCallResultAudioBlock] = None

    image: Optional[ObjectiveToolCallResultImageBlock] = None

    text: Optional[ObjectiveToolCallResultTextBlock] = None
