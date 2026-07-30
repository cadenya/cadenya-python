# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TenantRetrieveParams"]


class TenantRetrieveParams(TypedDict, total=False):
    workspace_id: Annotated[str, PropertyInfo(alias="workspaceId")]

    include_info: Annotated[bool, PropertyInfo(alias="includeInfo")]
    """When true, the `info` field is populated."""
