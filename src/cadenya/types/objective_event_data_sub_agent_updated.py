# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .sub_agent_updated import SubAgentUpdated

__all__ = ["ObjectiveEventDataSubAgentUpdated"]


class ObjectiveEventDataSubAgentUpdated(BaseModel):
    sub_agent_updated: SubAgentUpdated = FieldInfo(alias="subAgentUpdated")

    type: Literal["subAgentUpdated"]
