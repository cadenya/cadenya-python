# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .memory_entry_create_spec_content_param import MemoryEntryCreateSpecContentParam
from .memory_entry_create_spec_upload_id_param import MemoryEntryCreateSpecUploadIDParam

__all__ = ["MemoryEntryCreateSpecParam"]

MemoryEntryCreateSpecParam: TypeAlias = Union[MemoryEntryCreateSpecContentParam, MemoryEntryCreateSpecUploadIDParam]
