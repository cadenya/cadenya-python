# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ConfigBareParam"]


class ConfigBareParam(TypedDict, total=False):
    """
    Marks the tool as bare: it has no execution adapter of its own and
     relies on the parent tool set being a Bare tool set. Present so a
     webhook consumer can tell a tool is bare from the tool data alone,
     without cross-referencing the tool set.
    """

    pass
