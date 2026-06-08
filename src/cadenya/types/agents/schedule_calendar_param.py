# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo
from .schedule_range_param import ScheduleRangeParam

__all__ = ["ScheduleCalendarParam"]


class ScheduleCalendarParam(TypedDict, total=False):
    """Calendar is a wall-clock rule.

    Empty field-list semantics:
       - second/minute/hour: empty means [{start: 0}] (top of the unit)
       - day_of_month/month/day_of_week: empty means "any value"
     Fire times = cartesian product across all fields.
    """

    comment: str

    day_of_month: Annotated[Iterable[ScheduleRangeParam], PropertyInfo(alias="dayOfMonth")]

    day_of_week: Annotated[Iterable[ScheduleRangeParam], PropertyInfo(alias="dayOfWeek")]

    hour: Iterable[ScheduleRangeParam]

    minute: Iterable[ScheduleRangeParam]

    month: Iterable[ScheduleRangeParam]

    second: Iterable[ScheduleRangeParam]
