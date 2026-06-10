# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .objective_tool_call_result_content_block import ObjectiveToolCallResultContentBlock

__all__ = ["ObjectiveToolCallResult"]


class ObjectiveToolCallResult(BaseModel):
    """
    ObjectiveToolCallResult is the content a tool returned after execution.
     Tools can return multiple content blocks, and blocks can be multi-modal
     (text, image, audio). Media blocks are stored by Cadenya and served as
     short-lived signed URLs rather than inline bytes.
    """

    content: List[ObjectiveToolCallResultContentBlock]
