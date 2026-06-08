# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .profile import Profile
from .._models import BaseModel

__all__ = ["UploadInfo"]


class UploadInfo(BaseModel):
    created_by: Optional[Profile] = FieldInfo(alias="createdBy", default=None)
    """
    A profile identifies a user or non-human principal (such as an API key) at the
    account level. Profiles are account-scoped and can be granted access to multiple
    workspaces.
    """

    status: Optional[
        Literal[
            "UPLOAD_STATUS_UNSPECIFIED",
            "UPLOAD_STATUS_PENDING",
            "UPLOAD_STATUS_COMPLETE",
            "UPLOAD_STATUS_CONSUMED",
            "UPLOAD_STATUS_EXPIRED",
        ]
    ] = None
    """Lifecycle state.

    Transitions PENDING → COMPLETE (storage confirms the object exists) → CONSUMED
    (a resource referenced this upload), or → EXPIRED (URL elapsed without a PUT).
    """

    upload_url: Optional[str] = FieldInfo(alias="uploadUrl", default=None)
    """Presigned PUT URL.

    Short-lived. The client must PUT with the exact Content-Type declared in the
    spec, and the body length must match size_bytes.
    """

    upload_url_expires_at: Optional[datetime] = FieldInfo(alias="uploadUrlExpiresAt", default=None)
    """Absolute time at which upload_url stops working."""
