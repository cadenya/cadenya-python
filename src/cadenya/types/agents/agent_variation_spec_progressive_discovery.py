# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AgentVariationSpecProgressiveDiscovery"]


class AgentVariationSpecProgressiveDiscovery(BaseModel):
    """
    ProgressiveDiscovery is used to indicate that the agent should automatically discover tools that are not explicitly assigned to it.
     Max tools is the maximum number of tools that can be discovered per search.
     Hints are optional hints for tool search. These are used in conjunction with the context-aware tool search and can help select the best tools for the task.
    """

    hints: Optional[List[str]] = None
    """
    Free-text guidance appended to the discoverable-tools appendix in the system
    prompt. Hints steer the model's choice of tool names; they do not filter or rank
    anything, because tool_search matches names exactly rather than searching.
    """

    max_tools: Optional[int] = FieldInfo(alias="maxTools", default=None)
    """The most tool names tool_search will load in a single call.

    Requesting more than this returns an error telling the model to retry in smaller
    batches -- it is a per-call batch limit, not a ceiling on how many tools an
    objective may end up with.
    """
