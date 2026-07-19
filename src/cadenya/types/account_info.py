# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AccountInfo"]


class AccountInfo(BaseModel):
    """Server-populated information about the account."""

    challenge_token: Optional[str] = FieldInfo(alias="challengeToken", default=None)
    """
    The challenge token Cadenya sends in the X-Cadenya-Challenge-Token header on
    every MCP tools/list request. Server implementations can accept a valid
    challenge token in place of per-user auth when listing tools, while still
    requiring real auth on tools/call. Rotate with RotateChallengeToken; update any
    servers validating the token before rotating.
    """

    webhook_events_hmac_secret: Optional[str] = FieldInfo(alias="webhookEventsHmacSecret", default=None)
    """
    The generated secret that will sign all webhooks that are sent to your
    configured Webhook URL. Formatted as "wh_asdf1234" per the
    https://www.standardwebhooks.com/ format.
    """
