# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .context_lengths import ContextLengths

__all__ = ["ObjectiveDiagnostics"]


class ObjectiveDiagnostics(BaseModel):
    """
    ObjectiveDiagnostics is the context-usage breakdown measured for a single
     iteration at request-assembly time. It reports how much of the context
     window each component occupies so tool parameters, memory cascades, and
     prompts can be tuned against real token usage.
    """

    cached_input_tokens: int = FieldInfo(alias="cachedInputTokens")
    """
    The portion of input_tokens served from the provider's prompt cache. Lets
    clients distinguish "big but cached" from "big and paid fresh every iteration".
    """

    context_lengths: ContextLengths = FieldInfo(alias="contextLengths")
    """
    ContextLengths is the measured character length of each distinct component of an
    iteration's assembled context window. Values are raw character lengths of the
    component as assembled into the request — token estimates are derived by the
    client against input_tokens (component share = component length / sum of all
    lengths).

    New components are added as new fields — wire-compatible; absent components read
    as 0.
    """

    input_tokens: int = FieldInfo(alias="inputTokens")
    """Input tokens reported by the LLM provider for the iteration's completion."""
