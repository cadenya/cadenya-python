# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .sync_started import SyncStarted

__all__ = ["ToolSetEventDataSyncStarted"]


class ToolSetEventDataSyncStarted(BaseModel):
    sync_started: SyncStarted = FieldInfo(alias="syncStarted")
    """Emitted when a tool set sync operation begins."""

    type: Literal["syncStarted"]
