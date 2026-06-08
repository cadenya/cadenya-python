# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ProfileSpec"]


class ProfileSpec(BaseModel):
    """Configuration for a profile."""

    type: Literal["PROFILE_TYPE_UNSPECIFIED", "PROFILE_TYPE_USER", "PROFILE_TYPE_API_KEY", "PROFILE_TYPE_SYSTEM"]
    """
    Whether this profile represents a human user, an API key, or a system principal.
    """

    email: Optional[str] = None
    """Email address of the profile.

    Required and unique within an account for user profiles.
    """

    name: Optional[str] = None
    """Display name (e.g., "Bobby Tables")."""
