# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .agent_entry_param import AgentEntryParam
from .tool_set_entry_param import ToolSetEntryParam
from .memory_layer_entry_param import MemoryLayerEntryParam

__all__ = ["BulkWorkspaceApplyDataParam"]


class BulkWorkspaceApplyDataParam(TypedDict, total=False):
    bundle_key: Required[Annotated[str, PropertyInfo(alias="bundleKey")]]
    """Required.

    Bundle ownership key. Resources created or updated by an Apply have their
    `metadata.bundle_key` set to this value. On subsequent applies with the same
    bundle_key, resources currently bearing this bundle_key but absent from the spec
    are soft-deleted.
    """

    agents: Dict[str, AgentEntryParam]
    """Agents to upsert, keyed by external_id."""

    automatically_publish_agents: Annotated[bool, PropertyInfo(alias="automaticallyPublishAgents")]
    """
    When true, every agent created or updated by this Apply has its state forced to
    STATE_PUBLISHED, regardless of the state declared on the agent's entry. Useful
    when the bundle represents a production configuration and you want all of its
    agents live without setting state: STATE_PUBLISHED on each entry.

    Default false: each agent entry's `state` controls (which is STATE_DRAFT on
    create when unspecified).
    """

    memory_layers: Annotated[Dict[str, MemoryLayerEntryParam], PropertyInfo(alias="memoryLayers")]
    """Memory layers to upsert, keyed by external_id."""

    source_url: Annotated[str, PropertyInfo(alias="sourceUrl")]
    """
    Optional URL pointing to the source of this apply (GitHub PR, Jenkins build,
    GitLab pipeline, etc.). Surfaced in the dashboard so users can jump from an
    apply back to the change that produced it. Free-form HTTPS URI; not interpreted
    by the server.
    """

    tool_sets: Annotated[Dict[str, ToolSetEntryParam], PropertyInfo(alias="toolSets")]
    """Tool sets to upsert, keyed by external_id."""
