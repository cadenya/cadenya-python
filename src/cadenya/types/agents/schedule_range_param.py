# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ScheduleRangeParam"]


class ScheduleRangeParam(TypedDict, total=False):
    """
    Inclusive numeric range with optional step.
       {start: 9}                    → 9
       {start: 9, end: 17}           → 9..17
       {start: 0, end: 59, step: 15} → 0,15,30,45
     `end` defaults to `start`; `step` defaults to 1.
    """

    end: int

    start: int

    step: int
