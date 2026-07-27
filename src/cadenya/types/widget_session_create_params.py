# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .widget_session_spec_param import WidgetSessionSpecParam
from .shared_params.create_operation_metadata import CreateOperationMetadata

__all__ = ["WidgetSessionCreateParams", "Secret"]


class WidgetSessionCreateParams(TypedDict, total=False):
    workspace_id: Annotated[str, PropertyInfo(alias="workspaceId")]

    spec: Required[WidgetSessionSpecParam]
    """WidgetSessionSpec is the configuration of a session, fixed at mint."""

    metadata: CreateOperationMetadata
    """
    CreateOperationMetadata contains the user-provided fields for creating an
    operation. Read-only fields (id, account_id, workspace_id, created_at,
    profile_id) are excluded since they are set by the server.
    """

    secrets: Iterable[Secret]
    """Secrets to attach to the session."""


class Secret(TypedDict, total=False):
    """
    Secret is a named credential attached to the session — typically a token
     the customer's backend minted for the visitor, so the agent acts against
     their API as that subject. Values are captured at the boundary, encrypted
     at rest, appended to every conversation the session creates (re-synced on
     each turn), and never returned by any API. Session secrets take
     precedence over workspace and tool-set secrets of the same name.
    """

    name: str

    value: str
