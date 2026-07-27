# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["WidgetSpecParam"]


class WidgetSpecParam(TypedDict, total=False):
    """WidgetSpec is the user-provided configuration for a widget."""

    agent_id: Required[Annotated[str, PropertyInfo(alias="agentId")]]
    """Agent this widget is bound to.

    Accepts the canonical `agent_…` form or the `external_id:<value>` form. Sessions
    copy the agent at mint: re-pointing a widget's agent affects new sessions only.
    """

    origin_allowlist: Annotated[SequenceNotStr[str], PropertyInfo(alias="originAllowlist")]
    """
    Web origins allowed to embed and use this widget, enforced at the edge on every
    browser request. Exact origins only (scheme + host + optional port), no paths,
    no wildcard subdomains.
    """

    variation_id: Annotated[str, PropertyInfo(alias="variationId")]
    """Optional explicit variation pin.

    Must belong to the widget's agent. When set, every objective created through the
    widget runs this variation — bypassing the agent's variation_selection_mode
    (staged rollout: pin in production, follow in staging, promote by clearing).
    When unset, the agent's selection mode chooses per conversation.
    """
