# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["CompactionConfigSummarizationStrategy"]


class CompactionConfigSummarizationStrategy(BaseModel):
    """
    SummarizationStrategy configures LLM-powered summarization of older conversation turns.
    """

    instructions: Optional[str] = None
    """
    Custom instructions that guide what the summarizer preserves. Replaces the
    default summarization prompt entirely. Example: "Preserve all code snippets,
    variable names, and technical decisions."
    """
