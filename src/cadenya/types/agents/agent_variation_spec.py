# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .agent_variation_spec_constraints import AgentVariationSpecConstraints
from .agent_variation_spec_model_config import AgentVariationSpecModelConfig
from .agent_variation_spec_compaction_config import AgentVariationSpecCompactionConfig
from .agent_variation_spec_progressive_discovery import AgentVariationSpecProgressiveDiscovery

__all__ = ["AgentVariationSpec"]


class AgentVariationSpec(BaseModel):
    """AgentVariationSpec defines the operational configuration for a variation"""

    compaction_config: Optional[AgentVariationSpecCompactionConfig] = FieldInfo(alias="compactionConfig", default=None)
    """
    CompactionConfig defines how context window compaction behaves for objectives
    using this variation.
    """

    constraints: Optional[AgentVariationSpecConstraints] = None
    """Execution constraints"""

    description: Optional[str] = None
    """
    Human-readable description of what this variation does or when it should be used
    """

    enable_episodic_memory: Optional[bool] = FieldInfo(alias="enableEpisodicMemory", default=None)
    """
    Enable episodic memory for objectives using this variation. When true, the
    system automatically creates a document namespace for each objective using the
    objective's episodic_key as the external_id, allowing the agent to store and
    retrieve documents specific to that episode.
    """

    episodic_memory_ttl: Optional[int] = FieldInfo(alias="episodicMemoryTtl", default=None)
    """
    How long episodic memories should be retained. After this duration, episodic
    document namespaces can be automatically cleaned up. If not set, episodic
    memories are retained indefinitely.
    """

    api_model_config: Optional[AgentVariationSpecModelConfig] = FieldInfo(alias="modelConfig", default=None)
    """ModelConfig defines the model configuration for a variation"""

    progressive_discovery: Optional[AgentVariationSpecProgressiveDiscovery] = FieldInfo(
        alias="progressiveDiscovery", default=None
    )
    """
    ProgressiveDiscovery is used to indicate that the agent should automatically
    discover tools that are not explicitly assigned to it. Max tools is the maximum
    number of tools that can be discovered per search. Hints are optional hints for
    tool search. These are used in conjunction with the context-aware tool search
    and can help select the best tools for the task.
    """

    system_prompt_template: Optional[str] = FieldInfo(alias="systemPromptTemplate", default=None)
    """
    Liquid template for the system prompt of objectives using this variation.
    Rendered with CreateObjectiveRequest.data into Objective.system_prompt.
    """

    user_message_template: Optional[str] = FieldInfo(alias="userMessageTemplate", default=None)
    """
    Liquid template for the initial user message of objectives using this variation.
    Rendered with CreateObjectiveRequest.user_data and becomes the first user
    message in the LLM chat history. CreateObjectiveRequest.initial_message, when
    set, overrides the rendered result. If neither this template nor initial_message
    is present, objective creation is rejected with InvalidArgument.
    """

    weight: Optional[int] = None
    """Weight for weighted random selection (>= 0).

    P(v) = v.weight / sum(all_weights). Only used when the agent's
    variation_selection_mode is WEIGHTED. A weight of 0 means never auto-selected,
    but can still be chosen explicitly via variation_id on CreateObjectiveRequest.
    """
