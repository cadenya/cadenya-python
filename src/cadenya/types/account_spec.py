# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .workspace import Workspace

__all__ = ["AccountSpec"]


class AccountSpec(BaseModel):
    """Configuration for an account."""

    billing_email: Optional[str] = FieldInfo(alias="billingEmail", default=None)

    description: Optional[str] = None

    domain: Optional[str] = None

    workspaces: Optional[List[Workspace]] = None
