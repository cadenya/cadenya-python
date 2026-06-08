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
    """Permissions granted to this key.

    Each entry is a colon-separated verb:resource string (e.g. "manage:agents").
    Currently has no enforced effect; reserved for future fine-grained
    authorization.
    """

    system: Optional[bool] = None
    """True when this key is managed by the system (e.g.

    the auto-provisioned global account key). System keys cannot be deleted but can
    be rotated.
    """
