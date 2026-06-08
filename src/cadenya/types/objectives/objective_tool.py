# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from ..tool_sets.tool import Tool
from ..shared.bare_metadata import BareMetadata

__all__ = ["ObjectiveTool"]


class ObjectiveTool(BaseModel):
    """ObjectiveTool represents a tool that was assigned to an objective."""

    metadata: BareMetadata
    """
    BareMetadata contains the minimal metadata for a resource: the ID and an
    optional human-readable name. These are used for reference fields where the full
    metadata (account scoping, timestamps, labels, external IDs) is not needed —
    e.g., the tool references inside an agent variation spec or the tools assigned
    to an objective. Both fields are server-populated; clients provide IDs through
    sibling fields rather than by constructing a BareMetadata themselves.
    """

    snapshot: Optional[Tool] = None
    """Snapshot of the tool at the time it was assigned to the objective.

    Because tools can change over time, snapshots are used to ensure tools don't
    change unexpectedly during an objective's lifecycle.
    """
