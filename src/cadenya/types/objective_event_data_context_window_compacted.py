# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .context_window_compacted import ContextWindowCompacted

__all__ = ["ObjectiveEventDataContextWindowCompacted"]


class ObjectiveEventDataContextWindowCompacted(BaseModel):
    context_window_compacted: ContextWindowCompacted = FieldInfo(alias="contextWindowCompacted")

    type: Literal["contextWindowCompacted"]
