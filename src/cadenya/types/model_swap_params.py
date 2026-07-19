# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ModelSwapParams", "ModelSwap"]


class ModelSwapParams(TypedDict, total=False):
    workspace_id: Annotated[str, PropertyInfo(alias="workspaceId")]

    model_swaps: Annotated[Iterable[ModelSwap], PropertyInfo(alias="modelSwaps")]
    """The swaps to perform."""


class ModelSwap(TypedDict, total=False):
    current_model_id: Annotated[str, PropertyInfo(alias="currentModelId")]
    """The model variations are currently on. Accepts an id or "external_id:" slug."""

    disable_current_after_swap: Annotated[bool, PropertyInfo(alias="disableCurrentAfterSwap")]
    """Whether to disable the current model after the swap."""

    next_model_id: Annotated[str, PropertyInfo(alias="nextModelId")]
    """The model to move variations to. Accepts an id or "external_id:" slug."""
