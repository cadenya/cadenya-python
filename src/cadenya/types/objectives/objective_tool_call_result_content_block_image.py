# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel
from .objective_tool_call_result_image_block import ObjectiveToolCallResultImageBlock

__all__ = ["ObjectiveToolCallResultContentBlockImage"]


class ObjectiveToolCallResultContentBlockImage(BaseModel):
    image: ObjectiveToolCallResultImageBlock

    type: Literal["image"]
