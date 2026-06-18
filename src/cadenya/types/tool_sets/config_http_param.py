# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ConfigHTTPParam"]


class ConfigHTTPParam(TypedDict, total=False):
    request_method: Required[
        Annotated[
            Literal["HTTP_METHOD_UNSPECIFIED", "GET", "POST", "PUT", "PATCH", "DELETE"],
            PropertyInfo(alias="requestMethod"),
        ]
    ]

    headers: Dict[str, str]

    path: str

    query: str

    request_body_content_type: Annotated[str, PropertyInfo(alias="requestBodyContentType")]

    request_body_template: Annotated[str, PropertyInfo(alias="requestBodyTemplate")]
    """These are only used when the request method is a POST, PUT, or PATCH"""
