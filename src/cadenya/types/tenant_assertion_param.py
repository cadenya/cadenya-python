# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TenantAssertionParam"]


class TenantAssertionParam(TypedDict, total=False):
    """
    TenantAssertion identifies a tenant in the customer's own namespace — their
     org, company, or team identifier for an end user. Asserting a tenant
     upserts the tenant record in the workspace (keyed on `id` as the tenant's
     external_id) and associates the created resource with it.
    """

    id: Required[str]
    """The tenant identifier in the customer's namespace (e.g.

    "acme-corp"). Stored as the tenant record's external_id; stable across requests.
    """

    name: str
    """Optional human-readable name for the tenant.

    Updates the tenant record's name on every assertion that provides it.
    """
