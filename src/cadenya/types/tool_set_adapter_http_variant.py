# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .tool_set_adapter_http import ToolSetAdapterHTTP

__all__ = ["ToolSetAdapterHTTPVariant"]


class ToolSetAdapterHTTPVariant(BaseModel):
    http: ToolSetAdapterHTTP

    type: Literal["http"]
