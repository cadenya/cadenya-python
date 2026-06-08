# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .api_key import APIKey
from .._models import BaseModel

__all__ = ["AccountInfo"]


class AccountInfo(BaseModel):
    """Server-populated information about the account."""

    global_api_key: Optional[APIKey] = FieldInfo(alias="globalApiKey", default=None)
    """An API key for the account.

    Use workspace-association RPCs to grant the key access to specific workspaces; a
    key with zero workspaces is valid but cannot access workspace-scoped resources.
    """

    webhook_events_hmac_secret: Optional[str] = FieldInfo(alias="webhookEventsHmacSecret", default=None)
    """
    The generated secret that will sign all webhooks that are sent to your
    configured Webhook URL. Formatted as "wh_asdf1234" per the
    https://www.standardwebhooks.com/ format.
    """
