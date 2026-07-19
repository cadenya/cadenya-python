# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .tool_set_adapter_openapi_url_param import ToolSetAdapterOpenAPIURLParam
from .tool_set_adapter_openapi_upload_id_param import ToolSetAdapterOpenAPIUploadIDParam

__all__ = ["ToolSetAdapterOpenAPIParam"]

ToolSetAdapterOpenAPIParam: TypeAlias = Union[ToolSetAdapterOpenAPIURLParam, ToolSetAdapterOpenAPIUploadIDParam]
