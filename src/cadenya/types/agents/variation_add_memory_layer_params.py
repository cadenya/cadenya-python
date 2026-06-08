# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["VariationAddMemoryLayerParams"]


class VariationAddMemoryLayerParams(TypedDict, total=False):
    workspace_id: Required[Annotated[str, PropertyInfo(alias="workspaceId")]]

    agent_id: Required[Annotated[str, PropertyInfo(alias="agentId")]]

    memory_layer_id: Annotated[str, PropertyInfo(alias="memoryLayerId")]
    """Layer to attach.

    Accepts the canonical `memlyr_…` form or the `external_id:<value>` form.
    """

    position: int
    """Position in the stack. If omitted, server appends (max existing position + 1)."""
