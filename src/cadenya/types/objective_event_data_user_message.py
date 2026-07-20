# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .user_message import UserMessage

__all__ = ["ObjectiveEventDataUserMessage"]


class ObjectiveEventDataUserMessage(BaseModel):
    type: Literal["userMessage"]

    user_message: UserMessage = FieldInfo(alias="userMessage")
