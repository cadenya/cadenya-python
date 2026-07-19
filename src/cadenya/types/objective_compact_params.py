# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .agents.agent_variation_spec_compaction_config_param import AgentVariationSpecCompactionConfigParam

__all__ = ["ObjectiveCompactParams"]


class ObjectiveCompactParams(TypedDict, total=False):
    workspace_id: Annotated[str, PropertyInfo(alias="workspaceId")]

    compaction_config: Annotated[AgentVariationSpecCompactionConfigParam, PropertyInfo(alias="compactionConfig")]
    """
    CompactionConfig defines how context window compaction behaves for objectives
    using this variation.
    """
