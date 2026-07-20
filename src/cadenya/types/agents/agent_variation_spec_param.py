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

    first_user_message_template: Annotated[str, PropertyInfo(alias="firstUserMessageTemplate")]
    """
    Liquid template for the first user message of objectives using this variation.
    Rendered with CreateObjectiveRequest.first_user_message_data into
    Objective.first_user_message, the first user message in the LLM chat history.
    CreateObjectiveRequest.first_user_message, when set, overrides the rendered
    result. If neither this template nor first_user_message is present, objective
    creation is rejected with InvalidArgument.
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
    Rendered with CreateObjectiveRequest.system_prompt_data into
    Objective.system_prompt.
    """
