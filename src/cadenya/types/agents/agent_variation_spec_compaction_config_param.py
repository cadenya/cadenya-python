# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo
from .compaction_config_summarization_strategy_param import CompactionConfigSummarizationStrategyParam
from .compaction_config_tool_result_clearing_strategy_param import CompactionConfigToolResultClearingStrategyParam

__all__ = ["AgentVariationSpecCompactionConfigParam"]


class AgentVariationSpecCompactionConfigParam(TypedDict, total=False):
    """
    CompactionConfig defines how context window compaction behaves for objectives using this variation.
    """

    summarization: CompactionConfigSummarizationStrategyParam
    """
    SummarizationStrategy configures LLM-powered summarization of older conversation
    turns.
    """

    tool_result_clearing: Annotated[
        CompactionConfigToolResultClearingStrategyParam, PropertyInfo(alias="toolResultClearing")
    ]
    """ToolResultClearingStrategy configures clearing of older tool result content."""

    trigger_threshold: Annotated[float, PropertyInfo(alias="triggerThreshold")]
    """
    Trigger threshold as a percentage of the model's context window (0.0 to 1.0).
    When input tokens reach this percentage of the model's limit, compaction
    triggers. Default: 0.75 (75%)
    """
