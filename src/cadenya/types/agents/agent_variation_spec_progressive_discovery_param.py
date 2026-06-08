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

    max_tools: Annotated[int, PropertyInfo(alias="maxTools")]

    rerank_threshold: Annotated[float, PropertyInfo(alias="rerankThreshold")]
    """
    Rerank Threshold is an optional value that instructs whether or not to run a
    search result through a embedding/reranker process which can improve performance
    and reduce context bloat when tools reach the configured threshold. If a tool
    match must exceed 0.8, for example, the tool very closely match the query the
    tool search performed.
    """
