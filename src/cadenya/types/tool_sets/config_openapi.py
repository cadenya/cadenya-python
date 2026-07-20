# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ConfigOpenAPI"]


class ConfigOpenAPI(BaseModel):
    method: Optional[str] = None

    path: Optional[str] = None
