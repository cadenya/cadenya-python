# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
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
from ...types.objectives import feedback_list_params, feedback_create_params
from ...types.objectives.objective_feedback import ObjectiveFeedback
from ...types.shared_params.create_operation_metadata import CreateOperationMetadata
from ...types.objectives.objective_feedback_data_param import ObjectiveFeedbackDataParam

__all__ = ["FeedbackResource", "AsyncFeedbackResource"]


class FeedbackResource(SyncAPIResource):
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

    def create(
        self,
        objective_id: str,
        *,
        workspace_id: str,
        data: ObjectiveFeedbackDataParam,
        metadata: CreateOperationMetadata,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObjectiveFeedback:
        """Submits feedback for an objective's execution.

        Feedback scores are used by the
        agent variation scoring system to evaluate and rank variation performance.

        Args:
          metadata: CreateOperationMetadata contains the user-provided fields for creating an
              operation. Read-only fields (id, account_id, workspace_id, created_at,
              profile_id) are excluded since they are set by the server.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not objective_id:
            raise ValueError(f"Expected a non-empty value for `objective_id` but received {objective_id!r}")
        return self._post(
            path_template(
                "/v1/workspaces/{workspace_id}/objectives/{objective_id}/feedback",
                workspace_id=workspace_id,
                objective_id=objective_id,
            ),
            body=maybe_transform(
                {
                    "data": data,
                    "metadata": metadata,
                },
                feedback_create_params.FeedbackCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectiveFeedback,
        )

    def list(
        self,
        objective_id: str,
        *,
        workspace_id: str,
        cursor: str | Omit = omit,
        labels: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPagination[ObjectiveFeedback]:
        """
        Lists all feedback submitted for an objective

        Args:
          cursor: Pagination cursor from previous response

          labels: Filters by metadata labels. Comma-separated key=value pairs, e.g.
              "env=prod,team=ai". A resource matches only if every pair matches exactly (AND
              semantics).

          limit: Maximum number of results to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not objective_id:
            raise ValueError(f"Expected a non-empty value for `objective_id` but received {objective_id!r}")
        return self._get_api_list(
            path_template(
                "/v1/workspaces/{workspace_id}/objectives/{objective_id}/feedback",
                workspace_id=workspace_id,
                objective_id=objective_id,
            ),
            page=SyncCursorPagination[ObjectiveFeedback],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "labels": labels,
                        "limit": limit,
                    },
                    feedback_list_params.FeedbackListParams,
                ),
            ),
            model=ObjectiveFeedback,
        )


class AsyncFeedbackResource(AsyncAPIResource):
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

    async def create(
        self,
        objective_id: str,
        *,
        workspace_id: str,
        data: ObjectiveFeedbackDataParam,
        metadata: CreateOperationMetadata,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObjectiveFeedback:
        """Submits feedback for an objective's execution.

        Feedback scores are used by the
        agent variation scoring system to evaluate and rank variation performance.

        Args:
          metadata: CreateOperationMetadata contains the user-provided fields for creating an
              operation. Read-only fields (id, account_id, workspace_id, created_at,
              profile_id) are excluded since they are set by the server.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not objective_id:
            raise ValueError(f"Expected a non-empty value for `objective_id` but received {objective_id!r}")
        return await self._post(
            path_template(
                "/v1/workspaces/{workspace_id}/objectives/{objective_id}/feedback",
                workspace_id=workspace_id,
                objective_id=objective_id,
            ),
            body=await async_maybe_transform(
                {
                    "data": data,
                    "metadata": metadata,
                },
                feedback_create_params.FeedbackCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectiveFeedback,
        )

    def list(
        self,
        objective_id: str,
        *,
        workspace_id: str,
        cursor: str | Omit = omit,
        labels: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ObjectiveFeedback, AsyncCursorPagination[ObjectiveFeedback]]:
        """
        Lists all feedback submitted for an objective

        Args:
          cursor: Pagination cursor from previous response

          labels: Filters by metadata labels. Comma-separated key=value pairs, e.g.
              "env=prod,team=ai". A resource matches only if every pair matches exactly (AND
              semantics).

          limit: Maximum number of results to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not objective_id:
            raise ValueError(f"Expected a non-empty value for `objective_id` but received {objective_id!r}")
        return self._get_api_list(
            path_template(
                "/v1/workspaces/{workspace_id}/objectives/{objective_id}/feedback",
                workspace_id=workspace_id,
                objective_id=objective_id,
            ),
            page=AsyncCursorPagination[ObjectiveFeedback],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "labels": labels,
                        "limit": limit,
                    },
                    feedback_list_params.FeedbackListParams,
                ),
            ),
            model=ObjectiveFeedback,
        )


class FeedbackResourceWithRawResponse:
    def __init__(self, feedback: FeedbackResource) -> None:
        self._feedback = feedback

        self.create = to_raw_response_wrapper(
            feedback.create,
        )
        self.list = to_raw_response_wrapper(
            feedback.list,
        )


class AsyncFeedbackResourceWithRawResponse:
    def __init__(self, feedback: AsyncFeedbackResource) -> None:
        self._feedback = feedback

        self.create = async_to_raw_response_wrapper(
            feedback.create,
        )
        self.list = async_to_raw_response_wrapper(
            feedback.list,
        )


class FeedbackResourceWithStreamingResponse:
    def __init__(self, feedback: FeedbackResource) -> None:
        self._feedback = feedback

        self.create = to_streamed_response_wrapper(
            feedback.create,
        )
        self.list = to_streamed_response_wrapper(
            feedback.list,
        )


class AsyncFeedbackResourceWithStreamingResponse:
    def __init__(self, feedback: AsyncFeedbackResource) -> None:
        self._feedback = feedback

        self.create = async_to_streamed_response_wrapper(
            feedback.create,
        )
        self.list = async_to_streamed_response_wrapper(
            feedback.list,
        )
