# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .tool_set_adapter_openapi_url import ToolSetAdapterOpenAPIURL
from .tool_set_adapter_openapi_upload_id import ToolSetAdapterOpenAPIUploadID

__all__ = ["ToolSetAdapterOpenAPI"]

ToolSetAdapterOpenAPI: TypeAlias = Annotated[
    Union[ToolSetAdapterOpenAPIURL, ToolSetAdapterOpenAPIUploadID], PropertyInfo(discriminator="type")
]
