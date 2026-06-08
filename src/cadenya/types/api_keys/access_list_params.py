# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AccessListParams"]


class AccessListParams(TypedDict, total=False):
    cursor: str
    """Pagination cursor from previous response."""

    limit: int
    """Maximum number of results to return."""
