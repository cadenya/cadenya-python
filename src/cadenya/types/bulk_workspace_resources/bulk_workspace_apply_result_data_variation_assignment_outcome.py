# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..agents.variation_assignment import VariationAssignment

__all__ = ["BulkWorkspaceApplyResultDataVariationAssignmentOutcome", "Error", "ErrorDetail"]


class ErrorDetail(BaseModel):
    """
    Contains an arbitrary serialized message along with a @type that describes the type of the serialized message.
    """

    type: Optional[str] = FieldInfo(alias="@type", default=None)
    """The type of the serialized message."""

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class Error(BaseModel):
    """
    The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors).
    """

    code: Optional[int] = None
    """
    The status code, which should be an enum value of
    [google.rpc.Code][google.rpc.Code].
    """

    details: Optional[List[ErrorDetail]] = None
    """A list of messages that carry the error details.

    There is a common set of message types for APIs to use.
    """

    message: Optional[str] = None
    """A developer-facing error message, which should be in English.

    Any user-facing error message should be localized and sent in the
    [google.rpc.Status.details][google.rpc.Status.details] field, or localized by
    the client.
    """


class BulkWorkspaceApplyResultDataVariationAssignmentOutcome(BaseModel):
    action: Optional[
        Literal[
            "ACTION_UNSPECIFIED",
            "ACTION_CREATED",
            "ACTION_UPDATED",
            "ACTION_UNCHANGED",
            "ACTION_DELETED",
            "ACTION_FAILED",
        ]
    ] = None

    error: Optional[Error] = None
    """
    The `Status` type defines a logical error model that is suitable for different
    programming environments, including REST APIs and RPC APIs. It is used by
    [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of
    data: error code, error message, and error details. You can find out more about
    this error model and how to work with it in the
    [API Design Guide](https://cloud.google.com/apis/design/errors).
    """

    resource: Optional[VariationAssignment] = None
    """
    A read-only reference to a single tool, tool set, or sub-agent attached to a
    variation. Read the full set of assignments via
    `AgentVariationInfo.assignments`; mutations go through the dedicated add/remove
    assignment endpoints.

    The `id` identifies the assignment itself (not the referenced resource) and is
    the handle used to remove the assignment. It is returned by the add endpoint and
    present on every entry in `AgentVariationInfo.assignments`.
    """
