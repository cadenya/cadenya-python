# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel
from .config_http import ConfigHTTP

__all__ = ["ToolSpecConfigHTTP"]


class ToolSpecConfigHTTP(BaseModel):
    http: ConfigHTTP

    type: Literal["http"]
