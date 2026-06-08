# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..memory_layers.memory_entry import MemoryEntry

__all__ = ["BulkWorkspaceApplyResultDataMemoryEntryOutcome", "Error", "ErrorDetail"]


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


class BulkWorkspaceApplyResultDataMemoryEntryOutcome(BaseModel):
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

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)

    resource: Optional[MemoryEntry] = None
    """MemoryEntry is a single keyed value within a MemoryLayer.

    Entries are addressed by their key, which follows the S3 object key
    safe-character convention (see MemoryEntrySpec.key for the full rule). Keys are
    unique within a single layer; the same key may appear in multiple layers, in
    which case the LIFO stack-walk determines which one wins for a given objective.

    MemoryEntry is the summary shape, returned by ListMemoryEntries. It does not
    carry the entry body — callers that need the body must fetch the entry
    individually via GetMemoryEntry, which returns a MemoryEntryDetail.
    """
