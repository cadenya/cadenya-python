# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .objective_tool_call_data import ObjectiveToolCallData
from .objective_tool_call_info import ObjectiveToolCallInfo
from ..shared.operation_metadata import OperationMetadata
from .objective_tool_call_result import ObjectiveToolCallResult

__all__ = ["ObjectiveToolCallWithResult"]


class ObjectiveToolCallWithResult(BaseModel):
    """
    ObjectiveToolCallWithResult is an ObjectiveToolCall plus the content the
     tool returned. Returned by GetObjectiveToolCall.
    """

    data: ObjectiveToolCallData

    execution_status: Literal[
        "TOOL_CALL_EXECUTION_STATUS_UNSPECIFIED",
        "TOOL_CALL_EXECUTION_STATUS_PENDING",
        "TOOL_CALL_EXECUTION_STATUS_RUNNING",
        "TOOL_CALL_EXECUTION_STATUS_COMPLETED",
        "TOOL_CALL_EXECUTION_STATUS_ERRORED",
    ] = FieldInfo(alias="executionStatus")

    info: ObjectiveToolCallInfo

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

    result: Optional[ObjectiveToolCallResult] = None
    """
    ObjectiveToolCallResult is the content a tool returned after execution. Tools
    can return multiple content blocks, and blocks can be multi-modal (text, image,
    audio). Media blocks are stored by Cadenya and served as short-lived signed URLs
    rather than inline bytes.
    """
