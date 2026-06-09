# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AgentSpec"]


class AgentSpec(BaseModel):
    """Agent specification (user-provided configuration)"""

    variation_selection_mode: Literal[
        "VARIATION_SELECTION_MODE_UNSPECIFIED", "VARIATION_SELECTION_MODE_RANDOM", "VARIATION_SELECTION_MODE_WEIGHTED"
    ] = FieldInfo(alias="variationSelectionMode")
    """
    Controls how variations are automatically selected when creating objectives
    Defaults to RANDOM when unspecified
    """

    description: Optional[str] = None
    """Description of the agent's purpose"""

    input_data_schema: Optional[Dict[str, object]] = FieldInfo(alias="inputDataSchema", default=None)
    """InputDataSchema is used for enforcing a data input when objectives are created.

    This is valuable when using liquid formatting in agent variation prompts. Input
    data schema is also valuable when using an agent as a sub-agent, as the schema
    is used as the tool's input parameter schema. If omitted, the sub-agent schema
    will be loaded with a simple "prompt" free text string as its schema.
    """

    output_definition: Optional[Dict[str, object]] = FieldInfo(alias="outputDefinition", default=None)
    """
    Optional output definition for objectives created for this agent. When provided,
    Cadenya will append a tool to that will be called by the LLM in use by the
    variant to extract information in the format provided here. Use this option when
    you want structured data to be created by your objectives.
    """

    webhook_events_url: Optional[str] = FieldInfo(alias="webhookEventsUrl", default=None)
    """The URL that Cadenya will send events for any objective assigned to the agent."""
