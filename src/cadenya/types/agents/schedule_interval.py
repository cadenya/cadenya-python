# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ScheduleInterval"]


class ScheduleInterval(BaseModel):
    """Interval is a duration-based rule.

    Fires every `every` from a stable
     anchor (workspace epoch), optionally phase-shifted by `offset`.
    """

    every: Optional[str] = None

    offset: Optional[str] = None
    """Phase shift within `every`. Must be < `every` (enforced at runtime)."""
