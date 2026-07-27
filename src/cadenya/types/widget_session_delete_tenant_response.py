# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WidgetSessionDeleteTenantResponse"]


class WidgetSessionDeleteTenantResponse(BaseModel):
    """Delete tenant widget sessions response."""

    objectives_deleted: Optional[int] = FieldInfo(alias="objectivesDeleted", default=None)
    """Number of conversations (objectives) deleted along with the sessions."""

    sessions_deleted: Optional[int] = FieldInfo(alias="sessionsDeleted", default=None)
    """Number of sessions deleted."""
