# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .tenant_assertion_param import TenantAssertionParam
from .subject_assertion_param import SubjectAssertionParam

__all__ = ["WidgetSessionSpecParam"]


class WidgetSessionSpecParam(TypedDict, total=False):
    """WidgetSessionSpec is the configuration of a session, fixed at mint."""

    widget_id: Required[Annotated[str, PropertyInfo(alias="widgetId")]]
    """Widget this session is minted against.

    Accepts the canonical `wgt_…` form or the `external_id:<value>` form.
    """

    expires_at: Annotated[Union[str, datetime], PropertyInfo(alias="expiresAt", format="iso8601")]
    """Hard session expiry.

    Tokens never outlive it; after it passes the session transitions to
    STATE_EXPIRED. Defaults to a server-chosen horizon when unset.
    """

    pinned_parameters: Annotated[Dict[str, str], PropertyInfo(alias="pinnedParameters")]
    """
    Parameters forced onto tool calls made by this session's conversations. A pinned
    parameter is an overlay on a tool's JSON schema: the parameter is removed from
    what the LLM sees, and its value is always overwritten server-side with the
    pinned value — so the model cannot be tricked into calling a tool with a
    different id than the one the session was minted for (e.g. pin "workspaceId" for
    an OpenAPI tool with a /workspaces/{workspaceId} path). Flows to every objective
    the session creates.
    """

    subject: SubjectAssertionParam
    """
    SubjectAssertion identifies a person within a tenant in the customer's own
    namespace — typically their user id. Asserting a subject upserts the subject
    record under the asserted tenant and associates the created resource with it. A
    subject assertion is only valid alongside a tenant assertion: subject
    identifiers are scoped to their tenant.
    """

    tenant: TenantAssertionParam
    """
    TenantAssertion identifies a tenant in the customer's own namespace — their org,
    company, or team identifier for an end user. Asserting a tenant upserts the
    tenant record in the workspace (keyed on `id` as the tenant's external_id) and
    associates the created resource with it.
    """
