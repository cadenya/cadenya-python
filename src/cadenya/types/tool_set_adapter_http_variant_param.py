# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .tool_set_adapter_http_param import ToolSetAdapterHTTPParam

__all__ = ["ToolSetAdapterHTTPVariantParam"]


class ToolSetAdapterHTTPVariantParam(TypedDict, total=False):
    http: Required[ToolSetAdapterHTTPParam]

    type: Required[Literal["http"]]
