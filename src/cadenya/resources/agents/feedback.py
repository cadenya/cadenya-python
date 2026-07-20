# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncCursorPagination, AsyncCursorPagination
from ..._base_client import AsyncPaginator, make_request_options
from ...types.agents import feedback_list_params
from ...types.objectives.objective_feedback import ObjectiveFeedback

__all__ = ["FeedbackResource", "AsyncFeedbackResource"]


class FeedbackResource(SyncAPIResource):
    """Manage AI agents within a workspace. Agents define AI behavior and tool access."""

    @cached_property
    def with_raw_response(self) -> FeedbackResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cadenya/cadenya-python#accessing-raw-response-data-eg-headers
        """
        return FeedbackResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FeedbackResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cadenya/cadenya-python#with_streaming_response
        """
        return FeedbackResourceWithStreamingResponse(self)

    def list(
        self,
        agent_id: str,
        *,
        workspace_id: str | None = None,
        agent_variation_id: str | Omit = omit,
        created_after: Union[str, datetime] | Omit = omit,
        created_before: Union[str, datetime] | Omit = omit,
        cursor: str | Omit = omit,
        include_info: bool | Omit = omit,
        labels: str | Omit = omit,
        limit: int | Omit = omit,
        query: str | Omit = omit,
        sentiment: Literal[
            "FEEDBACK_SENTIMENT_UNSPECIFIED", "FEEDBACK_SENTIMENT_POSITIVE", "FEEDBACK_SENTIMENT_NEGATIVE"
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPagination[ObjectiveFeedback]:
        """Lists feedback submitted across all objectives belonging to an agent.

        Supports
        search by comment, sentiment filter, agent variation filter, and creation date
        range. Results are ordered by creation time, newest first.

        Args:
          agent_variation_id: Optional filter to limit results to feedback on objectives run by a single agent
              variation. Supports "external_id:" prefix for external IDs.

          created_after: Inclusive lower bound on feedback creation time.

          created_before: Exclusive upper bound on feedback creation time.

          cursor: Pagination cursor from previous response.

          include_info: When set to true you may use more of your alloted API rate-limit

          labels: Filters by metadata labels. Comma-separated key=value pairs, e.g.
              "env=prod,team=ai". A resource matches only if every pair matches exactly (AND
              semantics).

          limit: Maximum number of results to return.

          query: Free-text search applied to the feedback comment. Case-insensitive substring
              match.

          sentiment: Filter by sentiment. UNSPECIFIED returns feedback regardless of score.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if workspace_id is None:
            workspace_id = self._client._get_workspace_id_path_param()
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get_api_list(
            path_template(
                "/v1/workspaces/{workspace_id}/agents/{agent_id}/feedback", workspace_id=workspace_id, agent_id=agent_id
            ),
            page=SyncCursorPagination[ObjectiveFeedback],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "agent_variation_id": agent_variation_id,
                        "created_after": created_after,
                        "created_before": created_before,
                        "cursor": cursor,
                        "include_info": include_info,
                        "labels": labels,
                        "limit": limit,
                        "query": query,
                        "sentiment": sentiment,
                    },
                    feedback_list_params.FeedbackListParams,
                ),
            ),
            model=ObjectiveFeedback,
        )


class AsyncFeedbackResource(AsyncAPIResource):
    """Manage AI agents within a workspace. Agents define AI behavior and tool access."""

    @cached_property
    def with_raw_response(self) -> AsyncFeedbackResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cadenya/cadenya-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFeedbackResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFeedbackResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cadenya/cadenya-python#with_streaming_response
        """
        return AsyncFeedbackResourceWithStreamingResponse(self)

    def list(
        self,
        agent_id: str,
        *,
        workspace_id: str | None = None,
        agent_variation_id: str | Omit = omit,
        created_after: Union[str, datetime] | Omit = omit,
        created_before: Union[str, datetime] | Omit = omit,
        cursor: str | Omit = omit,
        include_info: bool | Omit = omit,
        labels: str | Omit = omit,
        limit: int | Omit = omit,
        query: str | Omit = omit,
        sentiment: Literal[
            "FEEDBACK_SENTIMENT_UNSPECIFIED", "FEEDBACK_SENTIMENT_POSITIVE", "FEEDBACK_SENTIMENT_NEGATIVE"
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ObjectiveFeedback, AsyncCursorPagination[ObjectiveFeedback]]:
        """Lists feedback submitted across all objectives belonging to an agent.

        Supports
        search by comment, sentiment filter, agent variation filter, and creation date
        range. Results are ordered by creation time, newest first.

        Args:
          agent_variation_id: Optional filter to limit results to feedback on objectives run by a single agent
              variation. Supports "external_id:" prefix for external IDs.

          created_after: Inclusive lower bound on feedback creation time.

          created_before: Exclusive upper bound on feedback creation time.

          cursor: Pagination cursor from previous response.

          include_info: When set to true you may use more of your alloted API rate-limit

          labels: Filters by metadata labels. Comma-separated key=value pairs, e.g.
              "env=prod,team=ai". A resource matches only if every pair matches exactly (AND
              semantics).

          limit: Maximum number of results to return.

          query: Free-text search applied to the feedback comment. Case-insensitive substring
              match.

          sentiment: Filter by sentiment. UNSPECIFIED returns feedback regardless of score.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if workspace_id is None:
            workspace_id = self._client._get_workspace_id_path_param()
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get_api_list(
            path_template(
                "/v1/workspaces/{workspace_id}/agents/{agent_id}/feedback", workspace_id=workspace_id, agent_id=agent_id
            ),
            page=AsyncCursorPagination[ObjectiveFeedback],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "agent_variation_id": agent_variation_id,
                        "created_after": created_after,
                        "created_before": created_before,
                        "cursor": cursor,
                        "include_info": include_info,
                        "labels": labels,
                        "limit": limit,
                        "query": query,
                        "sentiment": sentiment,
                    },
                    feedback_list_params.FeedbackListParams,
                ),
            ),
            model=ObjectiveFeedback,
        )


class FeedbackResourceWithRawResponse:
    def __init__(self, feedback: FeedbackResource) -> None:
        self._feedback = feedback

        self.list = to_raw_response_wrapper(
            feedback.list,
        )


class AsyncFeedbackResourceWithRawResponse:
    def __init__(self, feedback: AsyncFeedbackResource) -> None:
        self._feedback = feedback

        self.list = async_to_raw_response_wrapper(
            feedback.list,
        )


class FeedbackResourceWithStreamingResponse:
    def __init__(self, feedback: FeedbackResource) -> None:
        self._feedback = feedback

        self.list = to_streamed_response_wrapper(
            feedback.list,
        )


class AsyncFeedbackResourceWithStreamingResponse:
    def __init__(self, feedback: AsyncFeedbackResource) -> None:
        self._feedback = feedback

        self.list = async_to_streamed_response_wrapper(
            feedback.list,
        )
