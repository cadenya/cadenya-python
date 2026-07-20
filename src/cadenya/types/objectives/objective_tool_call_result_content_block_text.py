# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel
from .objective_tool_call_result_text_block import ObjectiveToolCallResultTextBlock

__all__ = ["ObjectiveToolCallResultContentBlockText"]


class ObjectiveToolCallResultContentBlockText(BaseModel):
    text: ObjectiveToolCallResultTextBlock

    type: Literal["text"]
