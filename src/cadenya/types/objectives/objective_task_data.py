# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ObjectiveTaskData"]


class ObjectiveTaskData(BaseModel):
    completed: bool
    """Whether the task has been completed"""

    number: int
    """
    The sequential number of this task within the objective (auto-assigned, 1-based)
    """

    task: str
    """Description of the task to be completed"""

    completed_at: Optional[datetime] = FieldInfo(alias="completedAt", default=None)
    """Timestamp when the task was marked as completed"""
