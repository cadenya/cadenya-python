# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AIProviderCredentialHeaders", "Headers"]


class Headers(BaseModel):
    """
    CredentialHeaders carries arbitrary HTTP headers sent with every request to
     the provider (e.g. {"Authorization": "Bearer ...", "X-Api-Key": "..."}).
    """

    headers: Optional[Dict[str, str]] = None


class AIProviderCredentialHeaders(BaseModel):
    headers: Headers
    """
    CredentialHeaders carries arbitrary HTTP headers sent with every request to the
    provider (e.g. {"Authorization": "Bearer ...", "X-Api-Key": "..."}).
    """

    type: Literal["headers"]
