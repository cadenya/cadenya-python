# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ConfigMcp"]


class ConfigMcp(BaseModel):
    tool_description: Optional[str] = FieldInfo(alias="toolDescription", default=None)

    tool_name: Optional[str] = FieldInfo(alias="toolName", default=None)

    tool_title: Optional[str] = FieldInfo(alias="toolTitle", default=None)
