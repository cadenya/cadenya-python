# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ApprovalRequirementFilterAlwaysParam"]


class ApprovalRequirementFilterAlwaysParam(TypedDict, total=False):
    always: Required[bool]

    type: Required[Literal["always"]]
