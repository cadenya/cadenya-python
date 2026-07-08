# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["AgentVariationSpecProgressiveDiscoveryParam"]


class AgentVariationSpecProgressiveDiscoveryParam(TypedDict, total=False):
    """
    ProgressiveDiscovery is used to indicate that the agent should automatically discover tools that are not explicitly assigned to it.
     Max tools is the maximum number of tools that can be discovered per search.
     Hints are optional hints for tool search. These are used in conjunction with the context-aware tool search and can help select the best tools for the task.
    """

    hints: SequenceNotStr[str]
    """
    Free-text guidance appended to the discoverable-tools appendix in the system
    prompt. Hints steer the model's choice of tool names; they do not filter or rank
    anything, because tool_search matches names exactly rather than searching.
    """

    max_tools: Annotated[int, PropertyInfo(alias="maxTools")]
    """The most tool names tool_search will load in a single call.

    Requesting more than this returns an error telling the model to retry in smaller
    batches -- it is a per-call batch limit, not a ceiling on how many tools an
    objective may end up with.
    """
