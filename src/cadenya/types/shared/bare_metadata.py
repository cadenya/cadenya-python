# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["BareMetadata"]


class BareMetadata(BaseModel):
    """
    BareMetadata contains the minimal metadata for a resource: the ID and an
     optional human-readable name. These are used for reference fields where the
     full metadata (account scoping, timestamps, labels, external IDs) is not
     needed — e.g., the tool references inside an agent variation spec or the
     tools assigned to an objective. Both fields are server-populated; clients
     provide IDs through sibling fields rather than by constructing a
     BareMetadata themselves.
    """

    id: Optional[str] = None

    name: Optional[str] = None
    """
    Human-readable name of the referenced resource, populated by the server on reads
    for convenience. Absent on references to resources that do not have a name
    (e.g., objective tasks).
    """
