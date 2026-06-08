# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ModelSetStatusParams"]


class ModelSetStatusParams(TypedDict, total=False):
    workspace_id: Required[Annotated[str, PropertyInfo(alias="workspaceId")]]

    status: Literal["MODEL_STATUS_UNSPECIFIED", "MODEL_STATUS_ENABLED", "MODEL_STATUS_DISABLED"]
    """The new status for the model"""
