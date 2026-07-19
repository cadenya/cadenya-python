# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ObjectiveEventDataNotice", "Notice"]


class Notice(BaseModel):
    """
    Notice is a non-terminal diagnostic emitted by the runtime when something
     noteworthy but non-fatal happens during an objective — for example a
     just-in-time tool set failing to load, or a previously loaded tool being
     dropped because it was archived. Notices carry no structured payload; they
     exist to make the objective timeline self-explanatory.
    """

    key: Optional[str] = None
    """
    Stable machine-readable identifier for the notice kind (for example
    "tool_set_load_failed", "tool_archived"). Clients can switch on it or use it as
    an i18n key; the message is the English fallback.
    """

    level: Optional[Literal["LEVEL_UNSPECIFIED", "LEVEL_INFO", "LEVEL_WARN"]] = None

    message: Optional[str] = None
    """Human-readable description of what happened."""


class ObjectiveEventDataNotice(BaseModel):
    notice: Notice
    """
    Notice is a non-terminal diagnostic emitted by the runtime when something
    noteworthy but non-fatal happens during an objective — for example a
    just-in-time tool set failing to load, or a previously loaded tool being dropped
    because it was archived. Notices carry no structured payload; they exist to make
    the objective timeline self-explanatory.
    """

    type: Literal["notice"]
