# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel
from .config_openapi import ConfigOpenAPI

__all__ = ["ToolSpecConfigOpenAPI"]


class ToolSpecConfigOpenAPI(BaseModel):
    openapi: ConfigOpenAPI

    type: Literal["openapi"]
