# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AgentSpecParam"]


class AgentSpecParam(TypedDict, total=False):
    """Agent specification (user-provided configuration)"""

    status: Required[
        Literal["AGENT_STATUS_UNSPECIFIED", "AGENT_STATUS_DRAFT", "AGENT_STATUS_PUBLISHED", "AGENT_STATUS_ARCHIVED"]
    ]
    """Status of the agent"""

    variation_selection_mode: Required[
        Annotated[
            Literal[
                "VARIATION_SELECTION_MODE_UNSPECIFIED",
                "VARIATION_SELECTION_MODE_RANDOM",
                "VARIATION_SELECTION_MODE_WEIGHTED",
            ],
            PropertyInfo(alias="variationSelectionMode"),
        ]
    ]
    """
    Controls how variations are automatically selected when creating objectives
    Defaults to RANDOM when unspecified
    """

    description: str
    """Description of the agent's purpose"""

    input_data_schema: Annotated[Dict[str, object], PropertyInfo(alias="inputDataSchema")]
    """InputDataSchema is used for enforcing a data input when objectives are created.

    This is valuable when using liquid formatting in agent variation prompts. Input
    data schema is also valuable when using an agent as a sub-agent, as the schema
    is used as the tool's input parameter schema. If omitted, the sub-agent schema
    will be loaded with a simple "prompt" free text string as its schema.
    """

    output_definition: Annotated[Dict[str, object], PropertyInfo(alias="outputDefinition")]
    """
    Optional output definition for objectives created for this agent. When provided,
    Cadenya will append a tool to that will be called by the LLM in use by the
    variant to extract information in the format provided here. Use this option when
    you want structured data to be created by your objectives.
    """

    webhook_events_url: Annotated[str, PropertyInfo(alias="webhookEventsUrl")]
    """The URL that Cadenya will send events for any objective assigned to the agent."""
