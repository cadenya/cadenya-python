# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .tool_set_adapter_openapi_param import ToolSetAdapterOpenAPIParam

__all__ = ["ToolSetAdapterOpenAPIVariantParam"]


class ToolSetAdapterOpenAPIVariantParam(TypedDict, total=False):
    openapi: Required[ToolSetAdapterOpenAPIParam]

    type: Required[Literal["openapi"]]
