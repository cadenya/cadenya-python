# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["MemoryEntryCreateSpecContentParam"]


class MemoryEntryCreateSpecContentParam(TypedDict, total=False):
    content: Required[str]
    """Inline content, written directly into the entry."""

    type: Required[Literal["content"]]

    description: str

    key: str
    """See MemoryEntrySpec.key for the full rule set. Same constraints apply here."""
