# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .sync_failed import SyncFailed
from .sync_started import SyncStarted
from .sync_completed import SyncCompleted

__all__ = ["ToolSetEventData"]


class ToolSetEventData(BaseModel):
    """Event payload for a tool set operation."""

    sync_completed: Optional[SyncCompleted] = FieldInfo(alias="syncCompleted", default=None)
    """Emitted when a tool set sync operation completes successfully."""

    sync_failed: Optional[SyncFailed] = FieldInfo(alias="syncFailed", default=None)
    """Emitted when a tool set sync operation fails."""

    sync_started: Optional[SyncStarted] = FieldInfo(alias="syncStarted", default=None)
    """Emitted when a tool set sync operation begins."""

    type: Optional[str] = None
    """Type of the event (e.g., "sync_started", "sync_completed", "sync_failed")."""
