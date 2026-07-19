# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.bare_metadata import BareMetadata

__all__ = ["VariationAssignmentToolSet"]


class VariationAssignmentToolSet(BaseModel):
    tool_set: BareMetadata = FieldInfo(alias="toolSet")
    """
    BareMetadata contains the minimal metadata for a resource: the ID and an
    optional human-readable name. These are used for reference fields where the full
    metadata (account scoping, timestamps, labels, external IDs) is not needed —
    e.g., the tool references inside an agent variation spec or the tools assigned
    to an objective. Both fields are server-populated; clients provide IDs through
    sibling fields rather than by constructing a BareMetadata themselves.
    """

    type: Literal["toolSet"]

    id: Optional[str] = None
