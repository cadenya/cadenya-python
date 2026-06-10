# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo
from .agent_variation_spec_constraints_param import AgentVariationSpecConstraintsParam
from .agent_variation_spec_model_config_param import AgentVariationSpecModelConfigParam
from .agent_variation_spec_compaction_config_param import AgentVariationSpecCompactionConfigParam
from .agent_variation_spec_progressive_discovery_param import AgentVariationSpecProgressiveDiscoveryParam

__all__ = ["AgentVariationSpecParam"]


class AgentVariationSpecParam(TypedDict, total=False):
    """AgentVariationSpec defines the operational configuration for a variation"""

    compaction_config: Annotated[AgentVariationSpecCompactionConfigParam, PropertyInfo(alias="compactionConfig")]
    """
    CompactionConfig defines how context window compaction behaves for objectives
    using this variation.
    """

    constraints: AgentVariationSpecConstraintsParam
    """Execution constraints"""

    description: str
    """
    Human-readable description of what this variation does or when it should be used
    """

    enable_episodic_memory: Annotated[bool, PropertyInfo(alias="enableEpisodicMemory")]
    """
    Enable episodic memory for objectives using this variation. When true, the
    system automatically creates a document namespace for each objective using the
    objective's episodic_key as the external_id, allowing the agent to store and
    retrieve documents specific to that episode.
    """

    episodic_memory_ttl: Annotated[int, PropertyInfo(alias="episodicMemoryTtl")]
    """
    How long episodic memories should be retained. After this duration, episodic
    document namespaces can be automatically cleaned up. If not set, episodic
    memories are retained indefinitely.
    """

    model_config: Annotated[AgentVariationSpecModelConfigParam, PropertyInfo(alias="modelConfig")]
    """ModelConfig defines the model configuration for a variation"""

    progressive_discovery: Annotated[
        AgentVariationSpecProgressiveDiscoveryParam, PropertyInfo(alias="progressiveDiscovery")
    ]
    """
    ProgressiveDiscovery is used to indicate that the agent should automatically
    discover tools that are not explicitly assigned to it. Max tools is the maximum
    number of tools that can be discovered per search. Hints are optional hints for
    tool search. These are used in conjunction with the context-aware tool search
    and can help select the best tools for the task.
    """

    system_prompt_template: Annotated[str, PropertyInfo(alias="systemPromptTemplate")]
    """
    Liquid template for the system prompt of objectives using this variation.
    Rendered with CreateObjectiveRequest.data into Objective.system_prompt.
    """

    user_message_template: Annotated[str, PropertyInfo(alias="userMessageTemplate")]
    """
    Liquid template for the initial user message of objectives using this variation.
    Rendered with CreateObjectiveRequest.user_data and becomes the first user
    message in the LLM chat history. CreateObjectiveRequest.initial_message, when
    set, overrides the rendered result. If neither this template nor initial_message
    is present, objective creation is rejected with InvalidArgument.
    """

    weight: int
    """Weight for weighted random selection (>= 0).

    P(v) = v.weight / sum(all_weights). Only used when the agent's
    variation_selection_mode is WEIGHTED. A weight of 0 means never auto-selected,
    but can still be chosen explicitly via variation_id on CreateObjectiveRequest.
    """
