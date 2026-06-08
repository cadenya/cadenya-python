# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["BulkWorkspaceApplyStatus", "PreflightError", "PreflightErrorDetail"]


class PreflightErrorDetail(BaseModel):
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


class PreflightError(BaseModel):
    """
    The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors).
    """

    code: Optional[int] = None
    """
    The status code, which should be an enum value of
    [google.rpc.Code][google.rpc.Code].
    """

    details: Optional[List[PreflightErrorDetail]] = None
    """A list of messages that carry the error details.

    There is a common set of message types for APIs to use.
    """

    message: Optional[str] = None
    """A developer-facing error message, which should be in English.

    Any user-facing error message should be localized and sent in the
    [google.rpc.Status.details][google.rpc.Status.details] field, or localized by
    the client.
    """


class BulkWorkspaceApplyStatus(BaseModel):
    state: Literal[
        "STATE_UNSPECIFIED",
        "STATE_PENDING",
        "STATE_VALIDATING",
        "STATE_RUNNING",
        "STATE_SUCCEEDED",
        "STATE_PARTIALLY_APPLIED",
        "STATE_FAILED",
        "STATE_CANCELLED",
    ]

    message: Optional[str] = None

    preflight_error: Optional[PreflightError] = FieldInfo(alias="preflightError", default=None)
    """
    The `Status` type defines a logical error model that is suitable for different
    programming environments, including REST APIs and RPC APIs. It is used by
    [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of
    data: error code, error message, and error details. You can find out more about
    this error model and how to work with it in the
    [API Design Guide](https://cloud.google.com/apis/design/errors).
    """
