# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["RotateWebhookSigningKeyResponse"]


class RotateWebhookSigningKeyResponse(BaseModel):
    """Response containing the newly generated webhook signing secret."""

    webhook_events_hmac_secret: Optional[str] = FieldInfo(alias="webhookEventsHmacSecret", default=None)
