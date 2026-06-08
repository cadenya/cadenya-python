# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ConfigOpenAPI"]


class ConfigOpenAPI(BaseModel):
    method: Optional[str] = None

    operation_id: Optional[str] = FieldInfo(alias="operationId", default=None)

    path: Optional[str] = None
