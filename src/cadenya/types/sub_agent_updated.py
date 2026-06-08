# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .shared.bare_metadata import BareMetadata

__all__ = ["SubAgentUpdated"]


class SubAgentUpdated(BaseModel):
    agent: Optional[BareMetadata] = None
    """
    BareMetadata contains the minimal metadata for a resource: the ID and an
    optional human-readable name. These are used for reference fields where the full
    metadata (account scoping, timestamps, labels, external IDs) is not needed —
    e.g., the tool references inside an agent variation spec or the tools assigned
    to an objective. Both fields are server-populated; clients provide IDs through
    sibling fields rather than by constructing a BareMetadata themselves.
    """

    message: Optional[str] = None

    objective: Optional[BareMetadata] = None
    """
    BareMetadata contains the minimal metadata for a resource: the ID and an
    optional human-readable name. These are used for reference fields where the full
    metadata (account scoping, timestamps, labels, external IDs) is not needed —
    e.g., the tool references inside an agent variation spec or the tools assigned
    to an objective. Both fields are server-populated; clients provide IDs through
    sibling fields rather than by constructing a BareMetadata themselves.
    """

    status: Optional[
        Literal[
            "STATUS_UNSPECIFIED",
            "STATUS_PENDING",
            "STATUS_RUNNING",
            "STATUS_COMPLETED",
            "STATUS_FAILED",
            "STATUS_CANCELLED",
        ]
    ] = None
