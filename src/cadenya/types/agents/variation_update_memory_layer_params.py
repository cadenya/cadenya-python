# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["VariationUpdateMemoryLayerParams"]


class VariationUpdateMemoryLayerParams(TypedDict, total=False):
    workspace_id: Annotated[str, PropertyInfo(alias="workspaceId")]

    position: int
    """New position. Only field currently updatable on an assignment."""
