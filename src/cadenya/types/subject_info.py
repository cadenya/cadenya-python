# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .tenant_reference import TenantReference

__all__ = ["SubjectInfo"]


class SubjectInfo(BaseModel):
    """SubjectInfo provides read-only server-derived data about a subject."""

    objective_count: Optional[int] = FieldInfo(alias="objectiveCount", default=None)
    """Number of objectives associated with this subject."""

    tenant: Optional[TenantReference] = None
    """
    TenantReference is the read-only echo of a resource's tenant association,
    carrying both Cadenya's canonical id and the customer's own key.
    """
