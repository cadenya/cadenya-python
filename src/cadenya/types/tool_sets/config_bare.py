# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["ConfigBare"]


class ConfigBare(BaseModel):
    """
    Marks the tool as bare: it has no execution adapter of its own and
     relies on the parent tool set being a Bare tool set. Present so a
     webhook consumer can tell a tool is bare from the tool data alone,
     without cross-referencing the tool set.
    """

    pass
