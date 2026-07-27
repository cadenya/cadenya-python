# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["TenantReference"]


class TenantReference(BaseModel):
    """
    TenantReference is the read-only echo of a resource's tenant association,
     carrying both Cadenya's canonical id and the customer's own key.
    """

    id: str
    """Cadenya's canonical tenant id."""

    external_id: str = FieldInfo(alias="externalId")
    """The tenant identifier in the customer's namespace, as asserted."""

    name: Optional[str] = None
    """Human-readable name of the tenant, when one has been asserted."""
