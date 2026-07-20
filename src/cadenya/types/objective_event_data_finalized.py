# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ObjectiveEventDataFinalized", "Finalized"]


class Finalized(BaseModel):
    """ObjectiveFinalized is the terminal event written when an objective is
     finalized.

    After this event, the objective is super-terminal: no further
     iterations, compaction, or continuation are permitted.
    """

    output: Optional[object] = None
    """
    If the objective was created with an output schema, and the agent successfully
    completed the objective, this field will contain the structured output of the
    objective.
    """


class ObjectiveEventDataFinalized(BaseModel):
    finalized: Finalized
    """ObjectiveFinalized is the terminal event written when an objective is finalized.

    After this event, the objective is super-terminal: no further iterations,
    compaction, or continuation are permitted.
    """

    type: Literal["finalized"]
