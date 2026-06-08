# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["APIKeySpecParam"]


class APIKeySpecParam(TypedDict, total=False):
    """Configuration for an API key."""

    description: str
    """Free-form description of what this API key is used for."""

    permissions: SequenceNotStr[str]
    """Permissions granted to this key.

    Each entry is a colon-separated verb:resource string (e.g. "manage:agents").
    Currently has no enforced effect; reserved for future fine-grained
    authorization.
    """
