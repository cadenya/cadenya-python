# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .agent_entry import AgentEntry
from .tool_set_entry import ToolSetEntry
from .memory_layer_entry import MemoryLayerEntry

__all__ = ["BulkWorkspaceApplyData"]


class BulkWorkspaceApplyData(BaseModel):
    bundle_key: str = FieldInfo(alias="bundleKey")
    """Required.

    Bundle ownership key. Resources created or updated by an Apply have their
    `metadata.bundle_key` set to this value. On subsequent applies with the same
    bundle_key, resources currently bearing this bundle_key but absent from the spec
    are soft-deleted.
    """

    agents: Optional[Dict[str, AgentEntry]] = None
    """Agents to upsert, keyed by external_id."""

    automatically_publish_agents: Optional[bool] = FieldInfo(alias="automaticallyPublishAgents", default=None)
    """
    When true, every agent created or updated by this Apply has its status forced to
    AGENT_STATUS_PUBLISHED, regardless of the status declared in the agent's
    AgentSpec. Useful when the bundle represents a production configuration and you
    want all of its agents live without setting status: AGENT_STATUS_PUBLISHED on
    each entry.

    Default false: each agent's AgentSpec.status controls (which is
    AGENT_STATUS_DRAFT on create when unspecified).
    """

    memory_layers: Optional[Dict[str, MemoryLayerEntry]] = FieldInfo(alias="memoryLayers", default=None)
    """Memory layers to upsert, keyed by external_id."""

    source_url: Optional[str] = FieldInfo(alias="sourceUrl", default=None)
    """
    Optional URL pointing to the source of this apply (GitHub PR, Jenkins build,
    GitLab pipeline, etc.). Surfaced in the dashboard so users can jump from an
    apply back to the change that produced it. Free-form HTTPS URI; not interpreted
    by the server.
    """

    tool_sets: Optional[Dict[str, ToolSetEntry]] = FieldInfo(alias="toolSets", default=None)
    """Tool sets to upsert, keyed by external_id."""
