# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .tool_set_adapter_mcp_variant_param import ToolSetAdapterMCPVariantParam
from .tool_set_adapter_bare_variant_param import ToolSetAdapterBareVariantParam
from .tool_set_adapter_http_variant_param import ToolSetAdapterHTTPVariantParam
from .tool_set_adapter_openapi_variant_param import ToolSetAdapterOpenAPIVariantParam

__all__ = ["ToolSetAdapterParam"]

ToolSetAdapterParam: TypeAlias = Union[
    ToolSetAdapterMCPVariantParam,
    ToolSetAdapterHTTPVariantParam,
    ToolSetAdapterOpenAPIVariantParam,
    ToolSetAdapterBareVariantParam,
]
