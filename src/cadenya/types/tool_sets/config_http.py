# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ConfigHTTP"]


class ConfigHTTP(BaseModel):
    request_method: Literal["HTTP_METHOD_UNSPECIFIED", "GET", "POST", "PUT", "PATCH", "DELETE"] = FieldInfo(
        alias="requestMethod"
    )

    headers: Optional[Dict[str, str]] = None

    path: Optional[str] = None

    query: Optional[str] = None

    request_body_content_type: Optional[str] = FieldInfo(alias="requestBodyContentType", default=None)

    request_body_template: Optional[str] = FieldInfo(alias="requestBodyTemplate", default=None)
    """These are only used when the request method is a POST, PUT, or PATCH"""

    tool_name: Optional[str] = FieldInfo(alias="toolName", default=None)
    """
    The tool name (commonly an "operation id" in OpenAPI specs) to call on the HTTP
    adapter. This is used to match the tool spec to the correct endpoint on the HTTP
    adapter. it will be derived from the name of the tool if not provided.
    """
