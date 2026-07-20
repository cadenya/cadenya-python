# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AgentVariationSpecConstraintsParam"]


class AgentVariationSpecConstraintsParam(TypedDict, total=False):
    inactivity_timeout: Annotated[str, PropertyInfo(alias="inactivityTimeout")]
    """
    How long an objective may sit with no activity (no user messages, no LLM calls)
    before it is finalized as timed out. Between 1 minute and 24 hours, expressed as
    a duration string in seconds (e.g. "7200s"). When not set, objectives are still
    swept at the system-wide 24 hour maximum — every objective eventually reaches a
    terminal state.

    Note: no gnostic integer hint here on purpose. The Envoy gRPC-JSON transcoder
    only accepts the canonical protobuf JSON form for Durations — a "<seconds>s"
    string — so the SDKs must type this as a string (like AgentScheduleSpec.every),
    not an integer.
    """

    max_sub_objectives: Annotated[int, PropertyInfo(alias="maxSubObjectives")]
    """The maximum number of sub-objectives that can be created. 0 means no limit."""

    max_tool_calls: Annotated[int, PropertyInfo(alias="maxToolCalls")]
    """The maximum number of tool calls that can be made. 0 means no limit."""
