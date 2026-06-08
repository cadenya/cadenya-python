# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SyncCompleted"]


class SyncCompleted(BaseModel):
    """Emitted when a tool set sync operation completes successfully."""

    message: Optional[str] = None
    """Optional message with additional details."""

    tools_synced: Optional[int] = FieldInfo(alias="toolsSynced", default=None)
    """Number of tools synced."""
