# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .config_bare_param import ConfigBareParam

__all__ = ["ToolSpecConfigBareParam"]


class ToolSpecConfigBareParam(TypedDict, total=False):
    bare: Required[ConfigBareParam]
    """
    Marks the tool as bare: it has no execution adapter of its own and relies on the
    parent tool set being a Bare tool set. Present so a webhook consumer can tell a
    tool is bare from the tool data alone, without cross-referencing the tool set.
    """

    type: Required[Literal["bare"]]
