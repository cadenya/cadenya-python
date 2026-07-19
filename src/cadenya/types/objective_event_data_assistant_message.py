# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .assistant_message import AssistantMessage

__all__ = ["ObjectiveEventDataAssistantMessage"]


class ObjectiveEventDataAssistantMessage(BaseModel):
    assistant_message: AssistantMessage = FieldInfo(alias="assistantMessage")

    type: Literal["assistantMessage"]
