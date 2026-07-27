# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .widget_session_info import WidgetSessionInfo
from .widget_session_spec import WidgetSessionSpec
from .shared.operation_metadata import OperationMetadata

__all__ = ["WidgetSession", "Secret"]


class Secret(BaseModel):
    """Secret is the name-only echo of a secret attached to the session.

    Values
     are never returned.
    """

    name: Optional[str] = None


class WidgetSession(BaseModel):
    """
    WidgetSession is a delegated, narrowed credential for one visitor's use of
     a widget, minted server-to-server by the customer's backend. The session
     carries all customer-asserted context — tenant, subject, labels, secrets —
     and every conversation (objective) created through the widget inherits it.
     The bearer token returned at mint is short-lived and refreshed at the
     widget host; the session row is what makes revocation possible.
    """

    metadata: OperationMetadata
    """
    Metadata for ephemeral operations and activities (e.g., objectives, executions,
    runs)
    """

    spec: WidgetSessionSpec
    """WidgetSessionSpec is the configuration of a session, fixed at mint."""

    state: Literal["STATE_UNSPECIFIED", "STATE_ACTIVE", "STATE_EXPIRED", "STATE_REVOKED", "STATE_EXHAUSTED"]
    """The current lifecycle state of the session.

    Output only. Sessions are created STATE_ACTIVE; use :revoke to end one early.
    """

    info: Optional[WidgetSessionInfo] = None
    """WidgetSessionInfo provides read-only server-derived data about a session."""

    secrets: Optional[List[Secret]] = None
    """Names of the secrets attached to the session.

    Values are write-only: provided at creation, encrypted at rest, and interpolated
    into tool-call headers server-side — never returned by any API.
    """
