# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .schedule_calendar import ScheduleCalendar
from .schedule_interval import ScheduleInterval

__all__ = ["AgentScheduleSpecSchedule"]


class AgentScheduleSpecSchedule(BaseModel):
    """Schedule defines WHEN the schedule fires.

    Temporal-style structured form:
     a list of calendar rules (wall-clock) and/or interval rules (duration),
     OR'd together. At least one rule is required.
    """

    calendars: Optional[List[ScheduleCalendar]] = None
    """Wall-clock rules. May be empty if `intervals` is non-empty."""

    intervals: Optional[List[ScheduleInterval]] = None
    """Duration-based rules. May be empty if `calendars` is non-empty."""

    timezone: Optional[str] = None
    """IANA tz name (e.g.

    "America/New_York"). Required. Applies to calendars; intervals fire on
    wall-clock cadence anchored in this zone.
    """
