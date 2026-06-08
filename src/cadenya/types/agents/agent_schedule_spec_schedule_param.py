# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

from .schedule_calendar_param import ScheduleCalendarParam
from .schedule_interval_param import ScheduleIntervalParam

__all__ = ["AgentScheduleSpecScheduleParam"]


class AgentScheduleSpecScheduleParam(TypedDict, total=False):
    """Schedule defines WHEN the schedule fires.

    Temporal-style structured form:
     a list of calendar rules (wall-clock) and/or interval rules (duration),
     OR'd together. At least one rule is required.
    """

    calendars: Iterable[ScheduleCalendarParam]
    """Wall-clock rules. May be empty if `intervals` is non-empty."""

    intervals: Iterable[ScheduleIntervalParam]
    """Duration-based rules. May be empty if `calendars` is non-empty."""

    timezone: str
    """IANA tz name (e.g.

    "America/New_York"). Required. Applies to calendars; intervals fire on
    wall-clock cadence anchored in this zone.
    """
