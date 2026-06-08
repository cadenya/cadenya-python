# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["VariationUpdateMemoryLayerParams"]


class VariationUpdateMemoryLayerParams(TypedDict, total=False):
    workspace_id: Required[Annotated[str, PropertyInfo(alias="workspaceId")]]

    agent_id: Required[Annotated[str, PropertyInfo(alias="agentId")]]

    variation_id: Required[Annotated[str, PropertyInfo(alias="variationId")]]

    position: int
    """New position. Only field currently updatable on an assignment."""
