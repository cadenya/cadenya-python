# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .tool_set_adapter_openapi import ToolSetAdapterOpenAPI

__all__ = ["ToolSetAdapterOpenAPIVariant"]


class ToolSetAdapterOpenAPIVariant(BaseModel):
    openapi: ToolSetAdapterOpenAPI

    type: Literal["openapi"]
