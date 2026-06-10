# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from pydantic import Field as FieldInfo

from ..profile import Profile
from ..._models import BaseModel
from ..callable_tool import CallableTool

__all__ = ["ObjectiveToolCallData"]


class ObjectiveToolCallData(BaseModel):
    callable: CallableTool
    """CallableTool is a union that represents a tool that can be called by an agent.

    In Cadenya, a tool that is used within an agent objective might be a
    user-defined tool (IE: MCP, HTTP), another Agent (useful to separate context),
    or a Cadenya Tool (one Cadenya provides).
    """

    arguments: Optional[Dict[str, object]] = None
    """The arguments passed to the tool"""

    memo: Optional[str] = None
    """A memo supplied by the reviewer when denying the tool call"""

    status_changed_by: Optional[Profile] = FieldInfo(alias="statusChangedBy", default=None)
    """
    A profile identifies a user or non-human principal (such as an API key) at the
    account level. Profiles are account-scoped and can be granted access to multiple
    workspaces.
    """
