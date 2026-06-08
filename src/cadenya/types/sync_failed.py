# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SyncFailed"]


class SyncFailed(BaseModel):
    """Emitted when a tool set sync operation fails."""

    error: Optional[bool] = None
    """Indicates this is an error event."""

    error_type: Optional[str] = FieldInfo(alias="errorType", default=None)
    """Optional error type/code for programmatic handling."""

    message: Optional[str] = None
    """Error message describing what went wrong."""
