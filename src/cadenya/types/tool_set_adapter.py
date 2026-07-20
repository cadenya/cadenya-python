# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .tool_set_adapter_mcp_variant import ToolSetAdapterMCPVariant
from .tool_set_adapter_bare_variant import ToolSetAdapterBareVariant
from .tool_set_adapter_http_variant import ToolSetAdapterHTTPVariant
from .tool_set_adapter_openapi_variant import ToolSetAdapterOpenAPIVariant

__all__ = ["ToolSetAdapter"]

ToolSetAdapter: TypeAlias = Annotated[
    Union[ToolSetAdapterMCPVariant, ToolSetAdapterHTTPVariant, ToolSetAdapterOpenAPIVariant, ToolSetAdapterBareVariant],
    PropertyInfo(discriminator="type"),
]
