# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel
from .config_bare import ConfigBare

__all__ = ["ToolSpecConfigBare"]


class ToolSpecConfigBare(BaseModel):
    bare: ConfigBare
    """
    Marks the tool as bare: it has no execution adapter of its own and relies on the
    parent tool set being a Bare tool set. Present so a webhook consumer can tell a
    tool is bare from the tool data alone, without cross-referencing the tool set.
    """

    type: Literal["bare"]
