# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel
from .objective_tool_call_result_audio_block import ObjectiveToolCallResultAudioBlock

__all__ = ["ObjectiveToolCallResultContentBlockAudio"]


class ObjectiveToolCallResultContentBlockAudio(BaseModel):
    audio: ObjectiveToolCallResultAudioBlock

    type: Literal["audio"]
