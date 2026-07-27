# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .profile import Profile
from .._models import BaseModel
from .shared.bare_metadata import BareMetadata

__all__ = ["WidgetInfo"]


class WidgetInfo(BaseModel):
    """WidgetInfo provides read-only server-derived data about a widget."""

    agent: Optional[BareMetadata] = None
    """
    BareMetadata contains the minimal metadata for a resource: the ID and an
    optional human-readable name. These are used for reference fields where the full
    metadata (account scoping, timestamps, labels, external IDs) is not needed —
    e.g., the tool references inside an agent variation spec or the tools assigned
    to an objective. Both fields are server-populated; clients provide IDs through
    sibling fields rather than by constructing a BareMetadata themselves.
    """

    created_by: Optional[Profile] = FieldInfo(alias="createdBy", default=None)
    """
    A profile identifies a user or non-human principal (such as an API key) at the
    account level. Profiles are account-scoped and can be granted access to multiple
    workspaces.
    """

    dns_label: Optional[str] = FieldInfo(alias="dnsLabel", default=None)
    """The widget's DNS label — the single hostname label under the widgets domain.

    Server-generated at creation, globally unique, immutable, and deliberately
    unrelated to the widget's id.
    """

    host: Optional[str] = None
    """The full hostname browsers talk to.

    Authoritative — clients must use this value rather than constructing the
    hostname themselves.
    """
