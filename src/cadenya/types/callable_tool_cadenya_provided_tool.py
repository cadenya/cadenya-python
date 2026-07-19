# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.resource_metadata import ResourceMetadata

__all__ = ["CallableToolCadenyaProvidedTool"]


class CallableToolCadenyaProvidedTool(BaseModel):
    cadenya_provided_tool: ResourceMetadata = FieldInfo(alias="cadenyaProvidedTool")
    """
    Standard metadata for persistent, named resources (e.g., agents, tools, prompts)
    """

    type: Literal["cadenyaProvidedTool"]
