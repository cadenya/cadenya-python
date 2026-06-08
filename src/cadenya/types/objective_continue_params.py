# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ObjectiveContinueParams", "Secret"]


class ObjectiveContinueParams(TypedDict, total=False):
    workspace_id: Required[Annotated[str, PropertyInfo(alias="workspaceId")]]

    enqueue: bool
    """
    When set to true, the message will be enqueued for when the agent loop is
    available to process it.
    """

    message: str
    """The message to continue an objective that has completed (or you are enqueing)"""

    secrets: Iterable[Secret]
    """Secrets that should be included with the message.

    Helpful for when you need to update secrets on the objective (IE: A secret
    expires and needs to be refreshed)
    """


class Secret(TypedDict, total=False):
    name: str

    value: str
