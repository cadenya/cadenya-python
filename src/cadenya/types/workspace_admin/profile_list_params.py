# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ProfileListParams"]


class ProfileListParams(TypedDict, total=False):
    cursor: str
    """Pagination cursor from previous response"""

    limit: int
    """Maximum number of results to return"""

    query: str
    """Free-form search over profile name and email.

    Case-insensitive substring match; empty returns all profiles.
    """
