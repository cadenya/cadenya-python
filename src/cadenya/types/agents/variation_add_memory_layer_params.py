# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["VariationAddMemoryLayerParams"]


class VariationAddMemoryLayerParams(TypedDict, total=False):
    workspace_id: Annotated[str, PropertyInfo(alias="workspaceId")]

    memory_layer_id: Required[Annotated[str, PropertyInfo(alias="memoryLayerId")]]
    """Layer to attach.

    Accepts the canonical `memlyr_…` form or the `external_id:<value>` form.
    """

    position: int
    """Position in the baseline cascade (lower = more specific).

    If omitted, the server appends at the most general end (max existing position +
    1).
    """
