# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .tenant_reference import TenantReference
from .subject_reference import SubjectReference
from .shared.bare_metadata import BareMetadata

__all__ = ["WidgetSessionInfo"]


class WidgetSessionInfo(BaseModel):
    """WidgetSessionInfo provides read-only server-derived data about a session."""

    agent: Optional[BareMetadata] = None
    """
    BareMetadata contains the minimal metadata for a resource: the ID and an
    optional human-readable name. These are used for reference fields where the full
    metadata (account scoping, timestamps, labels, external IDs) is not needed —
    e.g., the tool references inside an agent variation spec or the tools assigned
    to an objective. Both fields are server-populated; clients provide IDs through
    sibling fields rather than by constructing a BareMetadata themselves.
    """

    host: Optional[str] = None
    """The widget hostname this session's tokens are bound to.

    Authoritative — clients must use this value rather than constructing the
    hostname.
    """

    last_active_at: Optional[datetime] = FieldInfo(alias="lastActiveAt", default=None)
    """
    When the session last created a conversation, sent a message, or refreshed a
    token.
    """

    message_count: Optional[int] = FieldInfo(alias="messageCount", default=None)
    """
    Number of conversation messages created through this session, counted against
    the session's message cap.
    """

    subject: Optional[SubjectReference] = None
    """
    SubjectReference is the read-only echo of a resource's subject association,
    carrying both Cadenya's canonical id and the customer's own key.
    """

    tenant: Optional[TenantReference] = None
    """
    TenantReference is the read-only echo of a resource's tenant association,
    carrying both Cadenya's canonical id and the customer's own key.
    """

    widget: Optional[BareMetadata] = None
    """
    BareMetadata contains the minimal metadata for a resource: the ID and an
    optional human-readable name. These are used for reference fields where the full
    metadata (account scoping, timestamps, labels, external IDs) is not needed —
    e.g., the tool references inside an agent variation spec or the tools assigned
    to an objective. Both fields are server-populated; clients provide IDs through
    sibling fields rather than by constructing a BareMetadata themselves.
    """
