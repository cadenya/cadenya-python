# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .subject_info import SubjectInfo
from .shared.resource_metadata import ResourceMetadata

__all__ = ["Subject"]


class Subject(BaseModel):
    """Subject is a person within a tenant as a readable record.

    Like Tenant it
     carries no spec — `metadata.external_id` is the customer's key for them,
     unique within the tenant rather than the workspace.
    """

    metadata: ResourceMetadata
    """
    Standard metadata for persistent, named resources (e.g., agents, tools, prompts)
    """

    info: Optional[SubjectInfo] = None
    """SubjectInfo provides read-only server-derived data about a subject."""
