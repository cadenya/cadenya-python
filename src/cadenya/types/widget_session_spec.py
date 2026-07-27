# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .tenant_assertion import TenantAssertion
from .subject_assertion import SubjectAssertion

__all__ = ["WidgetSessionSpec"]


class WidgetSessionSpec(BaseModel):
    """WidgetSessionSpec is the configuration of a session, fixed at mint."""

    widget_id: str = FieldInfo(alias="widgetId")
    """Widget this session is minted against.

    Accepts the canonical `wgt_…` form or the `external_id:<value>` form.
    """

    token: Optional[str] = None
    """The session bearer token.

    Returned only on creation — subsequent reads omit it. The token is short-lived;
    the widget refreshes it at the widget host without involving the customer's
    backend.
    """

    expires_at: Optional[datetime] = FieldInfo(alias="expiresAt", default=None)
    """Hard session expiry.

    Tokens never outlive it; after it passes the session transitions to
    STATE_EXPIRED. Defaults to a server-chosen horizon when unset.
    """

    pinned_parameters: Optional[Dict[str, str]] = FieldInfo(alias="pinnedParameters", default=None)
    """
    Parameters forced onto tool calls made by this session's conversations. A pinned
    parameter is an overlay on a tool's JSON schema: the parameter is removed from
    what the LLM sees, and its value is always overwritten server-side with the
    pinned value — so the model cannot be tricked into calling a tool with a
    different id than the one the session was minted for (e.g. pin "workspaceId" for
    an OpenAPI tool with a /workspaces/{workspaceId} path). Flows to every objective
    the session creates.
    """

    subject: Optional[SubjectAssertion] = None
    """
    SubjectAssertion identifies a person within a tenant in the customer's own
    namespace — typically their user id. Asserting a subject upserts the subject
    record under the asserted tenant and associates the created resource with it. A
    subject assertion is only valid alongside a tenant assertion: subject
    identifiers are scoped to their tenant.
    """

    tenant: Optional[TenantAssertion] = None
    """
    TenantAssertion identifies a tenant in the customer's own namespace — their org,
    company, or team identifier for an end user. Asserting a tenant upserts the
    tenant record in the workspace (keyed on `id` as the tenant's external_id) and
    associates the created resource with it.
    """

    token_expires_at: Optional[datetime] = FieldInfo(alias="tokenExpiresAt", default=None)
    """Expiry of the token returned in `token`.

    Distinct from `expires_at`, which bounds the session itself.
    """
