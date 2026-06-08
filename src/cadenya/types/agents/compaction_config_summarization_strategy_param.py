# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CompactionConfigSummarizationStrategyParam"]


class CompactionConfigSummarizationStrategyParam(TypedDict, total=False):
    """
    SummarizationStrategy configures LLM-powered summarization of older conversation turns.
    """

    instructions: str
    """
    Custom instructions that guide what the summarizer preserves. Replaces the
    default summarization prompt entirely. Example: "Preserve all code snippets,
    variable names, and technical decisions."
    """
