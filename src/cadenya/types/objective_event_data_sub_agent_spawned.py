# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .sub_agent_spawned import SubAgentSpawned

__all__ = ["ObjectiveEventDataSubAgentSpawned"]


class ObjectiveEventDataSubAgentSpawned(BaseModel):
    sub_agent_spawned: SubAgentSpawned = FieldInfo(alias="subAgentSpawned")

    type: Literal["subAgentSpawned"]
