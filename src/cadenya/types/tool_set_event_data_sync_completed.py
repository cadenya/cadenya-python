# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .sync_completed import SyncCompleted

__all__ = ["ToolSetEventDataSyncCompleted"]


class ToolSetEventDataSyncCompleted(BaseModel):
    sync_completed: SyncCompleted = FieldInfo(alias="syncCompleted")
    """Emitted when a tool set sync operation completes successfully."""

    type: Literal["syncCompleted"]
