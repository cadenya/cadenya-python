# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ContextLengths"]


class ContextLengths(BaseModel):
    """
    ContextLengths is the measured character length of each distinct component
     of an iteration's assembled context window. Values are raw character
     lengths of the component as assembled into the request — token estimates
     are derived by the client against input_tokens (component share =
     component length / sum of all lengths).

     New components are added as new fields — wire-compatible; absent
     components read as 0.
    """

    assistant_messages: int = FieldInfo(alias="assistantMessages")
    """Chat history messages with the assistant role."""

    available_tools: int = FieldInfo(alias="availableTools")
    """The discoverable/available-tools appendix attached to the system prompt."""

    episodic_memory: int = FieldInfo(alias="episodicMemory")
    """The episodic memory appendix attached to the system prompt."""

    skills_memory: int = FieldInfo(alias="skillsMemory")
    """The skills memory appendix attached to the system prompt."""

    system_prompt: int = FieldInfo(alias="systemPrompt")
    """The objective's base system prompt (rendered variation template)."""

    tool_definitions: int = FieldInfo(alias="toolDefinitions")
    """
    Serialized tool definitions sent with the completion request (names,
    descriptions, and JSON-schema parameters).
    """

    tool_results: int = FieldInfo(alias="toolResults")
    """Tool results present in the chat history."""

    user_messages: int = FieldInfo(alias="userMessages")
    """Chat history messages with the user role."""
