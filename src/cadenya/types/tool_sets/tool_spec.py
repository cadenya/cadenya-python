# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .tool_spec_config import ToolSpecConfig

__all__ = ["ToolSpec"]


class ToolSpec(BaseModel):
    config: ToolSpecConfig
    """
    Config defines the adapter to use for the tool. This is used to determine how
    the tool is called. For example, if the tool is an HTTP tool, the adapter will
    be Http. If the tool is an inline tool, the adapter will be Inline.
    """

    description: str

    parameters: Dict[str, object]

    requires_approval: bool = FieldInfo(alias="requiresApproval")
