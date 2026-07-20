# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .sync_failed import SyncFailed

__all__ = ["ToolSetEventDataSyncFailed"]


class ToolSetEventDataSyncFailed(BaseModel):
    sync_failed: SyncFailed = FieldInfo(alias="syncFailed")
    """Emitted when a tool set sync operation fails."""

    type: Literal["syncFailed"]
