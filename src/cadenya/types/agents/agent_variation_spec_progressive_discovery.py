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

    max_tools: Optional[int] = FieldInfo(alias="maxTools", default=None)

    rerank_threshold: Optional[float] = FieldInfo(alias="rerankThreshold", default=None)
    """
    Rerank Threshold is an optional value that instructs whether or not to run a
    search result through a embedding/reranker process which can improve performance
    and reduce context bloat when tools reach the configured threshold. If a tool
    match must exceed 0.8, for example, the tool very closely match the query the
    tool search performed.
    """
