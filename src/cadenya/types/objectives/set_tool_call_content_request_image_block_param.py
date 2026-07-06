# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SetToolCallContentRequestImageBlockParam"]


class SetToolCallContentRequestImageBlockParam(TypedDict, total=False):
    data: Required[str]
    """Base64-encoded image bytes."""

    mime_type: Required[Annotated[str, PropertyInfo(alias="mimeType")]]
    """IANA media type of the image, e.g. image/png."""
