# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["APIKeySpec"]


class APIKeySpec(BaseModel):
    """Configuration for an API key."""

    token: Optional[str] = None
    """The bearer token used to authenticate as this API key.

    Returned only on creation and rotation; subsequent reads omit this field.
    """

    description: Optional[str] = None
    """Free-form description of what this API key is used for."""

    permissions: Optional[List[str]] = None
    """Scopes granted to this key.

    Each entry is a colon-separated resource:verb string (e.g. "objectives:manage").

    Resources: agents, objectives, tools, memory, api_keys, workspaces, widgets,
    widget_sessions, secrets, account. Verbs: read and manage, where manage implies
    read — a stored scope set is normalized to drop "x:read" when "x:manage" is
    present. The secrets and account resources support only manage. "\\**" is an
    explicit full-access grant.

    Scopes are deny-by-default: a key with an empty list can call only scope-free
    endpoints. Full access is always an explicit "\\**" grant.
    """

    system: Optional[bool] = None
    """True when this key is managed by the system (i.e.

    the auto-provisioned global account key). System keys cannot be deleted but can
    be rotated.
    """
