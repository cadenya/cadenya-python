# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..profile import Profile
from ..._models import BaseModel

__all__ = ["AgentScheduleInfo"]


class AgentScheduleInfo(BaseModel):
    """AgentScheduleInfo provides read-only runtime data about a schedule."""

    created_by: Optional[Profile] = FieldInfo(alias="createdBy", default=None)
    """
    A profile identifies a user or non-human principal (such as an API key) at the
    account level. Profiles are account-scoped and can be granted access to multiple
    workspaces.
    """

    last_fire_at: Optional[datetime] = FieldInfo(alias="lastFireAt", default=None)
    """When the schedule last fired (regardless of objective outcome)."""

    last_objective_id: Optional[str] = FieldInfo(alias="lastObjectiveId", default=None)
    """ID of the most recent objective the schedule created."""

    last_skipped_at: Optional[datetime] = FieldInfo(alias="lastSkippedAt", default=None)
    """When the schedule most recently skipped a fire (SKIP policy + prior in flight)."""

    last_skip_reason: Optional[str] = FieldInfo(alias="lastSkipReason", default=None)
    """Reason for the most recent skip (e.g. "previous objective still running")."""

    next_fire_at: Optional[datetime] = FieldInfo(alias="nextFireAt", default=None)
    """When the schedule will next fire.

    Computed from the spec; absent when the schedule is STATE_PAUSED/STATE_ARCHIVED
    or has no future fire times.
    """

    total_fires: Optional[int] = FieldInfo(alias="totalFires", default=None)
    """Lifetime count of objectives created by this schedule."""
