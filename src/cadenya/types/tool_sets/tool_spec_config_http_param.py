# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .config_http_param import ConfigHTTPParam

__all__ = ["ToolSpecConfigHTTPParam"]


class ToolSpecConfigHTTPParam(TypedDict, total=False):
    http: Required[ConfigHTTPParam]

    type: Required[Literal["http"]]
