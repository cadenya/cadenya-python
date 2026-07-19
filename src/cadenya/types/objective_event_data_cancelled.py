# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ObjectiveEventDataCancelled", "Cancelled"]


class Cancelled(BaseModel):
    """ObjectiveCancelled is the terminal event written when an objective is
     cancelled.

    After this event, the objective is super-terminal: no further
     iterations, compaction, or continuation are permitted.
    """

    message: Optional[str] = None
    """Optional human-readable note recorded at cancel time.

    Today the workflow sets "Cancelled" but this field leaves room for richer
    reasons (e.g. "Cancelled by user", "Cancelled by schedule sweep", "Credit
    balance exhausted").
    """


class ObjectiveEventDataCancelled(BaseModel):
    cancelled: Cancelled
    """ObjectiveCancelled is the terminal event written when an objective is cancelled.

    After this event, the objective is super-terminal: no further iterations,
    compaction, or continuation are permitted.
    """

    type: Literal["cancelled"]
