# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .objective_task_data import ObjectiveTaskData
from ..shared.bare_metadata import BareMetadata

__all__ = ["ObjectiveTask"]


class ObjectiveTask(BaseModel):
    """
    ObjectiveTask represents a task within an objective, typically created and managed by an AI agent
     to track progress toward completing the objective.
    """

    data: ObjectiveTaskData

    metadata: BareMetadata
    """
    BareMetadata contains the minimal metadata for a resource: the ID and an
    optional human-readable name. These are used for reference fields where the full
    metadata (account scoping, timestamps, labels, external IDs) is not needed —
    e.g., the tool references inside an agent variation spec or the tools assigned
    to an objective. Both fields are server-populated; clients provide IDs through
    sibling fields rather than by constructing a BareMetadata themselves.
    """
