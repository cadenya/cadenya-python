# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from ..._utils import PropertyInfo
from .objective_tool_call_result_content_block_text import ObjectiveToolCallResultContentBlockText
from .objective_tool_call_result_content_block_audio import ObjectiveToolCallResultContentBlockAudio
from .objective_tool_call_result_content_block_image import ObjectiveToolCallResultContentBlockImage

__all__ = ["ObjectiveToolCallResultContentBlock"]

ObjectiveToolCallResultContentBlock: TypeAlias = Annotated[
    Union[
        ObjectiveToolCallResultContentBlockText,
        ObjectiveToolCallResultContentBlockImage,
        ObjectiveToolCallResultContentBlockAudio,
    ],
    PropertyInfo(discriminator="type"),
]
