# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FeedbackListParams"]


class FeedbackListParams(TypedDict, total=False):
    workspace_id: Required[Annotated[str, PropertyInfo(alias="workspaceId")]]

    agent_variation_id: Annotated[str, PropertyInfo(alias="agentVariationId")]
    """
    Optional filter to limit results to feedback on objectives run by a single agent
    variation. Supports "external_id:" prefix for external IDs.
    """

    created_after: Annotated[Union[str, datetime], PropertyInfo(alias="createdAfter", format="iso8601")]
    """Inclusive lower bound on feedback creation time."""

    created_before: Annotated[Union[str, datetime], PropertyInfo(alias="createdBefore", format="iso8601")]
    """Exclusive upper bound on feedback creation time."""

    cursor: str
    """Pagination cursor from previous response."""

    include_info: Annotated[bool, PropertyInfo(alias="includeInfo")]
    """When set to true you may use more of your alloted API rate-limit"""

    labels: str
    """Filters by metadata labels.

    Comma-separated key=value pairs, e.g. "env=prod,team=ai". A resource matches
    only if every pair matches exactly (AND semantics).
    """

    limit: int
    """Maximum number of results to return."""

    query: str
    """Free-text search applied to the feedback comment.

    Case-insensitive substring match.
    """

    sentiment: Literal["FEEDBACK_SENTIMENT_UNSPECIFIED", "FEEDBACK_SENTIMENT_POSITIVE", "FEEDBACK_SENTIMENT_NEGATIVE"]
    """Filter by sentiment. UNSPECIFIED returns feedback regardless of score."""
