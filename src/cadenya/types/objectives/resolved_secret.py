# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ResolvedSecret"]


class ResolvedSecret(BaseModel):
    """
    ResolvedSecret is a resolved secret value from the workspace, toolset, or objective. When a tool is called, it will rely
     on secrets in the order of:
     - Objective
     - Toolset
     - Workspace
    """

    key: Optional[str] = None

    source: Optional[
        Literal[
            "RESOLVED_SECRET_SOURCE_UNSPECIFIED",
            "RESOLVED_SECRET_SOURCE_WORKSPACE",
            "RESOLVED_SECRET_SOURCE_TOOLSET",
            "RESOLVED_SECRET_SOURCE_OBJECTIVE",
        ]
    ] = None
