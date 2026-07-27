# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["WidgetSessionDeleteTenantParams"]


class WidgetSessionDeleteTenantParams(TypedDict, total=False):
    workspace_id: Annotated[str, PropertyInfo(alias="workspaceId")]

    tenant_id: Annotated[str, PropertyInfo(alias="tenantId")]
    """Tenant whose sessions to delete.

    Required — an empty value is rejected rather than matching everything. Accepts
    the canonical `tenant_…` form or the `external_id:<value>` form.
    """
