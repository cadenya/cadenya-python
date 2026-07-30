# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["TenantInfo"]


class TenantInfo(BaseModel):
    """TenantInfo provides read-only server-derived data about a tenant."""

    objective_count: Optional[int] = FieldInfo(alias="objectiveCount", default=None)
    """
    Number of objectives associated with this tenant, across every surface — widget
    conversations and objectives created directly against the API alike. This is the
    footprint a delete would destroy, which is why it is worth the count query that
    populating `info` costs.
    """

    subject_count: Optional[int] = FieldInfo(alias="subjectCount", default=None)
    """Number of subjects asserted under this tenant."""

    widget_session_count: Optional[int] = FieldInfo(alias="widgetSessionCount", default=None)
    """Number of widget sessions minted for this tenant that still exist."""
