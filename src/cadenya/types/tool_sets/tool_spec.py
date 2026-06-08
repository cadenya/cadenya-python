# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

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

    status: Literal["TOOL_STATUS_UNSPECIFIED", "TOOL_STATUS_AVAILABLE", "TOOL_STATUS_OMITTED", "TOOL_STATUS_ARCHIVED"]

    requires_approval: Optional[bool] = FieldInfo(alias="requiresApproval", default=None)
