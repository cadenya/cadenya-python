# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ToolSetAdapterHTTP"]


class ToolSetAdapterHTTP(BaseModel):
    base_url: Optional[str] = FieldInfo(alias="baseUrl", default=None)

    headers: Optional[Dict[str, str]] = None
