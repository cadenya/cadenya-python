# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .variation_assignment_entry import VariationAssignmentEntry
from .agents.agent_variation_spec import AgentVariationSpec
from .variation_memory_layer_entry import VariationMemoryLayerEntry

__all__ = ["AgentVariationEntry"]


class AgentVariationEntry(BaseModel):
    name: str

    spec: AgentVariationSpec
    """AgentVariationSpec defines the operational configuration for a variation"""

    assignments: Optional[List[VariationAssignmentEntry]] = None
    """
    Reconciled list — server adjusts the variation's assignments to exactly this set
    when the variation is bundle-owned.
    """

    labels: Optional[Dict[str, str]] = None

    memory_layers: Optional[List[VariationMemoryLayerEntry]] = FieldInfo(alias="memoryLayers", default=None)
    """Reconciled list of memory layer assignments. Up to 10 entries."""
