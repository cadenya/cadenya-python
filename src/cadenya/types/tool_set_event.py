# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .profile import Profile
from .._models import BaseModel
from .tool_set_event_data import ToolSetEventData
from .shared.resource_metadata import ResourceMetadata
from .shared.operation_metadata import OperationMetadata

__all__ = ["ToolSetEvent", "Info"]


class Info(BaseModel):
    created_by: Optional[Profile] = FieldInfo(alias="createdBy", default=None)
    """
    A profile identifies a user or non-human principal (such as an API key) at the
    account level. Profiles are account-scoped and can be granted access to multiple
    workspaces.
    """

    tool_set: Optional[ResourceMetadata] = FieldInfo(alias="toolSet", default=None)
    """
    Standard metadata for persistent, named resources (e.g., agents, tools, prompts)
    """


class ToolSetEvent(BaseModel):
    """A single event in the tool set's operation timeline."""

    metadata: OperationMetadata
    """
    Metadata for ephemeral operations and activities (e.g., objectives, executions,
    runs)
    """

    event: Optional[ToolSetEventData] = None
    """Event payload for a tool set operation."""

    info: Optional[Info] = None

    tool_set_id: Optional[str] = FieldInfo(alias="toolSetId", default=None)
    """The tool set this event is associated with."""
