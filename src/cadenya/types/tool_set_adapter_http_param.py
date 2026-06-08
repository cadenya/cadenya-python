# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ToolSetAdapterHTTPParam"]


class ToolSetAdapterHTTPParam(TypedDict, total=False):
    base_url: Annotated[str, PropertyInfo(alias="baseUrl")]

    headers: Dict[str, str]
