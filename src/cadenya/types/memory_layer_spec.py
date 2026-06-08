# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MemoryLayerSpec"]


class MemoryLayerSpec(BaseModel):
    type: Literal["MEMORY_LAYER_TYPE_UNSPECIFIED", "MEMORY_LAYER_TYPE_EPISODIC", "MEMORY_LAYER_TYPE_SKILLS"]

    description: Optional[str] = None
    """Human-readable description of the layer's purpose.

    Encouraged for user-created layers; system-managed layers may have a generated
    description.
    """

    expires_at: Optional[datetime] = FieldInfo(alias="expiresAt", default=None)
    """
    For layers with a finite lifetime (e.g., episodic), the time at which the layer
    becomes eligible for cleanup. Set by the system; unset for persistent layers.
    """

    system_managed: Optional[bool] = FieldInfo(alias="systemManaged", default=None)
    """Server-set.

    True for layers managed by the system (e.g., episodic layers created
    automatically when an objective uses an episodic_key). System-managed layers
    cannot be assigned to objective stacks via the API and cannot be mutated by
    clients — their lifecycle is controlled entirely by the runtime.
    """
