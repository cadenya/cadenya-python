# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..profile import Profile
from ..._models import BaseModel
from ..shared.resource_metadata import ResourceMetadata

__all__ = ["ToolInfo"]


class ToolInfo(BaseModel):
    created_by: Optional[Profile] = FieldInfo(alias="createdBy", default=None)
    """
    A profile identifies a user or non-human principal (such as an API key) at the
    account level. Profiles are account-scoped and can be granted access to multiple
    workspaces.
    """

    signature: Optional[str] = None
    """
    Content signature identifying the tool within its tool set: a hash of the
    sanitized llm_tool_name, description, and canonical parameters. Two tools with
    the same llm_tool_name but different parameters or description (as MCP servers
    may return per user) have distinct signatures.
    """

    tool_set: Optional[ResourceMetadata] = FieldInfo(alias="toolSet", default=None)
    """
    Standard metadata for persistent, named resources (e.g., agents, tools, prompts)
    """
