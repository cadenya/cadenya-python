# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .objective_tool_call_data import ObjectiveToolCallData
from .objective_tool_call_info import ObjectiveToolCallInfo
from ..shared.operation_metadata import OperationMetadata

__all__ = ["ObjectiveToolCall"]


class ObjectiveToolCall(BaseModel):
    """
    ObjectiveToolCall is a record of a tool call made during an objective's execution.
     Tool calls are mutable — their status changes as they are approved, denied, or executed.
    """

    data: ObjectiveToolCallData

    execution_status: Literal[
        "TOOL_CALL_EXECUTION_STATUS_UNSPECIFIED",
        "TOOL_CALL_EXECUTION_STATUS_PENDING",
        "TOOL_CALL_EXECUTION_STATUS_RUNNING",
        "TOOL_CALL_EXECUTION_STATUS_COMPLETED",
        "TOOL_CALL_EXECUTION_STATUS_ERRORED",
    ] = FieldInfo(alias="executionStatus")

    metadata: OperationMetadata
    """
    Metadata for ephemeral operations and activities (e.g., objectives, executions,
    runs)
    """

    status: Literal[
        "TOOL_CALL_STATUS_UNSPECIFIED",
        "TOOL_CALL_STATUS_AUTO_APPROVED",
        "TOOL_CALL_STATUS_WAITING_FOR_APPROVAL",
        "TOOL_CALL_STATUS_APPROVED",
        "TOOL_CALL_STATUS_DENIED",
    ]
    """Current status of the tool call"""

    info: Optional[ObjectiveToolCallInfo] = None
