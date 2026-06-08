# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["VariationAssignmentEntry"]


class VariationAssignmentEntry(BaseModel):
    sub_agent_id: Optional[str] = FieldInfo(alias="subAgentId", default=None)

    tool_id: Optional[str] = FieldInfo(alias="toolId", default=None)

    tool_set_id: Optional[str] = FieldInfo(alias="toolSetId", default=None)
