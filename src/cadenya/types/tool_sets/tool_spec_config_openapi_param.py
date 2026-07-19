# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .config_openapi_param import ConfigOpenAPIParam

__all__ = ["ToolSpecConfigOpenAPIParam"]


class ToolSpecConfigOpenAPIParam(TypedDict, total=False):
    openapi: Required[ConfigOpenAPIParam]

    type: Required[Literal["openapi"]]
