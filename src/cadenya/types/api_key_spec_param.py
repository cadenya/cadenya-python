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
    """Scopes granted to this key.

    Each entry is a colon-separated resource:verb string (e.g. "objectives:manage").

    Resources: agents, objectives, tools, memory, secrets, account. Verbs: read and
    manage, where manage implies read — a stored scope set is normalized to drop
    "x:read" when "x:manage" is present. The secrets and account resources support
    only manage. "\\**" is an explicit full-access grant.

    An empty list grants full access (grandfathered legacy behavior); new keys
    should be created with explicit scopes.
    """
