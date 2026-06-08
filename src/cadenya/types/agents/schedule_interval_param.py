# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ScheduleIntervalParam"]


class ScheduleIntervalParam(TypedDict, total=False):
    """Interval is a duration-based rule.

    Fires every `every` from a stable
     anchor (workspace epoch), optionally phase-shifted by `offset`.
    """

    every: str

    offset: str
    """Phase shift within `every`. Must be < `every` (enforced at runtime)."""
