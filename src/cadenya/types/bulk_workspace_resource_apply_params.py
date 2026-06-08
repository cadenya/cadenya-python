# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .bulk_workspace_apply_data_param import BulkWorkspaceApplyDataParam

__all__ = ["BulkWorkspaceResourceApplyParams"]


class BulkWorkspaceResourceApplyParams(TypedDict, total=False):
    data: Required[BulkWorkspaceApplyDataParam]
