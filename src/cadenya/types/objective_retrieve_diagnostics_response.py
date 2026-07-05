# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .objective_diagnostics import ObjectiveDiagnostics

__all__ = ["ObjectiveRetrieveDiagnosticsResponse"]


class ObjectiveRetrieveDiagnosticsResponse(BaseModel):
    diagnostics: ObjectiveDiagnostics
    """
    ObjectiveDiagnostics is the context-usage breakdown measured for a single
    iteration at request-assembly time. It reports how much of the context window
    each component occupies so tool parameters, memory cascades, and prompts can be
    tuned against real token usage.
    """
