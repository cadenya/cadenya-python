# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["SyncStarted"]


class SyncStarted(BaseModel):
    """Emitted when a tool set sync operation begins."""

    message: Optional[str] = None
    """Human-readable message describing the start of the sync."""
