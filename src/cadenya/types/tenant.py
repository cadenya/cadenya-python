# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .tenant_info import TenantInfo
from .shared.resource_metadata import ResourceMetadata

__all__ = ["Tenant"]


class Tenant(BaseModel):
    """Tenant is the customer's organization as a readable record rather than an
     echo.

    It carries no spec: a tenant is never configured, only asserted, so
     everything about it lives in the metadata envelope — `external_id` is the key
     the customer asserted it under, `name` is the most recent name they asserted,
     and `updated_at` is therefore when the tenant was last asserted.
    """

    metadata: ResourceMetadata
    """
    Standard metadata for persistent, named resources (e.g., agents, tools, prompts)
    """

    state: Literal["STATE_UNSPECIFIED", "STATE_ACTIVE", "STATE_ERASING"]
    """The current lifecycle state of the tenant. Output only."""

    info: Optional[TenantInfo] = None
    """TenantInfo provides read-only server-derived data about a tenant."""
