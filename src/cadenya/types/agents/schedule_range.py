# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ScheduleRange"]


class ScheduleRange(BaseModel):
    """
    Inclusive numeric range with optional step.
       {start: 9}                    → 9
       {start: 9, end: 17}           → 9..17
       {start: 0, end: 59, step: 15} → 0,15,30,45
     `end` defaults to `start`; `step` defaults to 1.
    """

    end: Optional[int] = None

    start: Optional[int] = None

    step: Optional[int] = None
