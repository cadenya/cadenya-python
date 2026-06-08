# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .compaction_config_summarization_strategy import CompactionConfigSummarizationStrategy
from .compaction_config_tool_result_clearing_strategy import CompactionConfigToolResultClearingStrategy

__all__ = ["AgentVariationSpecCompactionConfig"]


class AgentVariationSpecCompactionConfig(BaseModel):
    """
    CompactionConfig defines how context window compaction behaves for objectives using this variation.
    """

    summarization: Optional[CompactionConfigSummarizationStrategy] = None
    """
    SummarizationStrategy configures LLM-powered summarization of older conversation
    turns.
    """

    tool_result_clearing: Optional[CompactionConfigToolResultClearingStrategy] = FieldInfo(
        alias="toolResultClearing", default=None
    )
    """ToolResultClearingStrategy configures clearing of older tool result content."""

    trigger_threshold: Optional[float] = FieldInfo(alias="triggerThreshold", default=None)
    """
    Trigger threshold as a percentage of the model's context window (0.0 to 1.0).
    When input tokens reach this percentage of the model's limit, compaction
    triggers. Default: 0.75 (75%)
    """
