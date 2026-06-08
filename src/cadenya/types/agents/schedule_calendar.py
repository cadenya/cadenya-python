# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .schedule_range import ScheduleRange

__all__ = ["ScheduleCalendar"]


class ScheduleCalendar(BaseModel):
    """Calendar is a wall-clock rule.

    Empty field-list semantics:
       - second/minute/hour: empty means [{start: 0}] (top of the unit)
       - day_of_month/month/day_of_week: empty means "any value"
     Fire times = cartesian product across all fields.
    """

    comment: Optional[str] = None

    day_of_month: Optional[List[ScheduleRange]] = FieldInfo(alias="dayOfMonth", default=None)

    day_of_week: Optional[List[ScheduleRange]] = FieldInfo(alias="dayOfWeek", default=None)

    hour: Optional[List[ScheduleRange]] = None

    minute: Optional[List[ScheduleRange]] = None

    month: Optional[List[ScheduleRange]] = None

    second: Optional[List[ScheduleRange]] = None
