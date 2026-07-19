# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MemberAddParams"]


class MemberAddParams(TypedDict, total=False):
    workspace_id: Annotated[str, PropertyInfo(alias="workspaceId")]

    email: str
    """Email address to add (resolve-or-invite). Mutually exclusive with profile_id."""

    profile_id: Annotated[str, PropertyInfo(alias="profileId")]
    """An existing account profile to add. Mutually exclusive with email."""
