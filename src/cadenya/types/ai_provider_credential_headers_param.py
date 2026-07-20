# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AIProviderCredentialHeadersParam", "Headers"]


class Headers(TypedDict, total=False):
    """
    CredentialHeaders carries arbitrary HTTP headers sent with every request to
     the provider (e.g. {"Authorization": "Bearer ...", "X-Api-Key": "..."}).
    """

    headers: Dict[str, str]


class AIProviderCredentialHeadersParam(TypedDict, total=False):
    headers: Required[Headers]
    """
    CredentialHeaders carries arbitrary HTTP headers sent with every request to the
    provider (e.g. {"Authorization": "Bearer ...", "X-Api-Key": "..."}).
    """

    type: Required[Literal["headers"]]
