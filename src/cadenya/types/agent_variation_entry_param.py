# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .variation_assignment_entry_param import VariationAssignmentEntryParam
from .agents.agent_variation_spec_param import AgentVariationSpecParam
from .variation_memory_layer_entry_param import VariationMemoryLayerEntryParam

__all__ = ["AgentVariationEntryParam"]


class AgentVariationEntryParam(TypedDict, total=False):
    name: Required[str]

    spec: Required[AgentVariationSpecParam]
    """AgentVariationSpec defines the operational configuration for a variation"""

    assignments: Iterable[VariationAssignmentEntryParam]
    """
    Reconciled list — server adjusts the variation's assignments to exactly this set
    when the variation is bundle-owned.
    """

    labels: Dict[str, str]

    memory_layers: Annotated[Iterable[VariationMemoryLayerEntryParam], PropertyInfo(alias="memoryLayers")]
    """Reconciled list of memory layer assignments. Up to 10 entries."""
