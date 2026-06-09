# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .tool_spec_config_param import ToolSpecConfigParam

__all__ = ["ToolSpecParam"]


class ToolSpecParam(TypedDict, total=False):
    config: Required[ToolSpecConfigParam]
    """
    Config defines the adapter to use for the tool. This is used to determine how
    the tool is called. For example, if the tool is an HTTP tool, the adapter will
    be Http. If the tool is an inline tool, the adapter will be Inline.
    """

    description: Required[str]

    parameters: Required[Dict[str, object]]

    requires_approval: Required[Annotated[bool, PropertyInfo(alias="requiresApproval")]]
