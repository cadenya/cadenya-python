# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .agent import Agent
from .._models import BaseModel
from .tool_set import ToolSet
from .tool_sets.tool import Tool

__all__ = ["SearchSearchToolsOrToolSetsResponse"]


class SearchSearchToolsOrToolSetsResponse(BaseModel):
    agents: Optional[List[Agent]] = None

    tools: Optional[List[Tool]] = None

    tool_sets: Optional[List[ToolSet]] = FieldInfo(alias="toolSets", default=None)
