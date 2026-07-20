# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ObjectiveContinueParams"]


class ObjectiveContinueParams(TypedDict, total=False):
    workspace_id: Annotated[str, PropertyInfo(alias="workspaceId")]

    message: Required[str]
    """The message to continue an objective that has completed (or you are enqueing)"""

    enqueue: bool
    """
    When set to true, the message will be enqueued for when the agent loop is
    available to process it.
    """
