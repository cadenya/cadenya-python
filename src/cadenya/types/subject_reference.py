# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SubjectReference"]


class SubjectReference(BaseModel):
    """
    SubjectReference is the read-only echo of a resource's subject association,
     carrying both Cadenya's canonical id and the customer's own key.
    """

    id: str
    """Cadenya's canonical subject id."""

    external_id: str = FieldInfo(alias="externalId")
    """The subject identifier in the customer's namespace, as asserted.

    Unique within the subject's tenant.
    """

    name: Optional[str] = None
    """Human-readable name of the subject, when one has been asserted."""
