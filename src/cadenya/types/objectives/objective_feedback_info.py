# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..profile import Profile
from ..._models import BaseModel
from ..shared.bare_metadata import BareMetadata

__all__ = ["ObjectiveFeedbackInfo"]


class ObjectiveFeedbackInfo(BaseModel):
    agent_variation: Optional[BareMetadata] = FieldInfo(alias="agentVariation", default=None)
    """
    BareMetadata contains the minimal metadata for a resource: the ID and an
    optional human-readable name. These are used for reference fields where the full
    metadata (account scoping, timestamps, labels, external IDs) is not needed —
    e.g., the tool references inside an agent variation spec or the tools assigned
    to an objective. Both fields are server-populated; clients provide IDs through
    sibling fields rather than by constructing a BareMetadata themselves.
    """

    objective: Optional[BareMetadata] = None
    """
    BareMetadata contains the minimal metadata for a resource: the ID and an
    optional human-readable name. These are used for reference fields where the full
    metadata (account scoping, timestamps, labels, external IDs) is not needed —
    e.g., the tool references inside an agent variation spec or the tools assigned
    to an objective. Both fields are server-populated; clients provide IDs through
    sibling fields rather than by constructing a BareMetadata themselves.
    """

    submitted_by: Optional[Profile] = FieldInfo(alias="submittedBy", default=None)
    """
    A profile identifies a user or non-human principal (such as an API key) at the
    account level. Profiles are account-scoped and can be granted access to multiple
    workspaces.
    """
