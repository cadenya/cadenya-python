# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .callable_tool_tool import CallableToolTool
from .callable_tool_agent import CallableToolAgent
from .callable_tool_cadenya_provided_tool import CallableToolCadenyaProvidedTool

__all__ = ["CallableTool"]

CallableTool: TypeAlias = Annotated[
    Union[CallableToolTool, CallableToolAgent, CallableToolCadenyaProvidedTool], PropertyInfo(discriminator="type")
]
