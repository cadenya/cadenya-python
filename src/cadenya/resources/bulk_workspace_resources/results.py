# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...types.bulk_workspace_resources import result_list_params
from ...types.bulk_workspace_resources.bulk_workspace_apply_result import BulkWorkspaceApplyResult

__all__ = ["ResultsResource", "AsyncResultsResource"]


class ResultsResource(SyncAPIResource):
    """
    Apply a declarative bundle of workspace resources — tool sets, memory
     layers, agents, variations, assignments, and schedules — in a single
     asynchronous operation.
    """

    @cached_property
    def with_raw_response(self) -> ResultsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cadenya/cadenya-python#accessing-raw-response-data-eg-headers
        """
        return ResultsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResultsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cadenya/cadenya-python#with_streaming_response
        """
        return ResultsResourceWithStreamingResponse(self)

    def list(
        self,
        bulk_workspace_apply_id: str,
        *,
        workspace_id: str,
        action: Literal[
            "ACTION_UNSPECIFIED",
            "ACTION_CREATED",
            "ACTION_UPDATED",
            "ACTION_UNCHANGED",
            "ACTION_DELETED",
            "ACTION_FAILED",
        ]
        | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        sort_order: str | Omit = omit,
        type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPagination[BulkWorkspaceApplyResult]:
        """
        Lists each resource action recorded by a bulk workspace apply operation.

        Args:
          action: Filter by action.

          cursor: Pagination cursor from previous response

          limit: Maximum number of results to return

          sort_order: Sort order for results (asc or desc by creation time)

          type: Filter by data.type discriminator (e.g., "toolSet", "memoryEntry").

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not bulk_workspace_apply_id:
            raise ValueError(
                f"Expected a non-empty value for `bulk_workspace_apply_id` but received {bulk_workspace_apply_id!r}"
            )
        return self._get_api_list(
            path_template(
                "/v1/workspaces/{workspace_id}/bulk_workspace_applies/{bulk_workspace_apply_id}/results",
                workspace_id=workspace_id,
                bulk_workspace_apply_id=bulk_workspace_apply_id,
            ),
            page=SyncCursorPagination[BulkWorkspaceApplyResult],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "action": action,
                        "cursor": cursor,
                        "limit": limit,
                        "sort_order": sort_order,
                        "type": type,
                    },
                    result_list_params.ResultListParams,
                ),
            ),
            model=BulkWorkspaceApplyResult,
        )


class AsyncResultsResource(AsyncAPIResource):
    """
    Apply a declarative bundle of workspace resources — tool sets, memory
     layers, agents, variations, assignments, and schedules — in a single
     asynchronous operation.
    """

    @cached_property
    def with_raw_response(self) -> AsyncResultsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cadenya/cadenya-python#accessing-raw-response-data-eg-headers
        """
        return AsyncResultsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResultsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cadenya/cadenya-python#with_streaming_response
        """
        return AsyncResultsResourceWithStreamingResponse(self)

    def list(
        self,
        bulk_workspace_apply_id: str,
        *,
        workspace_id: str,
        action: Literal[
            "ACTION_UNSPECIFIED",
            "ACTION_CREATED",
            "ACTION_UPDATED",
            "ACTION_UNCHANGED",
            "ACTION_DELETED",
            "ACTION_FAILED",
        ]
        | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        sort_order: str | Omit = omit,
        type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[BulkWorkspaceApplyResult, AsyncCursorPagination[BulkWorkspaceApplyResult]]:
        """
        Lists each resource action recorded by a bulk workspace apply operation.

        Args:
          action: Filter by action.

          cursor: Pagination cursor from previous response

          limit: Maximum number of results to return

          sort_order: Sort order for results (asc or desc by creation time)

          type: Filter by data.type discriminator (e.g., "toolSet", "memoryEntry").

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not bulk_workspace_apply_id:
            raise ValueError(
                f"Expected a non-empty value for `bulk_workspace_apply_id` but received {bulk_workspace_apply_id!r}"
            )
        return self._get_api_list(
            path_template(
                "/v1/workspaces/{workspace_id}/bulk_workspace_applies/{bulk_workspace_apply_id}/results",
                workspace_id=workspace_id,
                bulk_workspace_apply_id=bulk_workspace_apply_id,
            ),
            page=AsyncCursorPagination[BulkWorkspaceApplyResult],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "action": action,
                        "cursor": cursor,
                        "limit": limit,
                        "sort_order": sort_order,
                        "type": type,
                    },
                    result_list_params.ResultListParams,
                ),
            ),
            model=BulkWorkspaceApplyResult,
        )


class ResultsResourceWithRawResponse:
    def __init__(self, results: ResultsResource) -> None:
        self._results = results

        self.list = to_raw_response_wrapper(
            results.list,
        )


class AsyncResultsResourceWithRawResponse:
    def __init__(self, results: AsyncResultsResource) -> None:
        self._results = results

        self.list = async_to_raw_response_wrapper(
            results.list,
        )


class ResultsResourceWithStreamingResponse:
    def __init__(self, results: ResultsResource) -> None:
        self._results = results

        self.list = to_streamed_response_wrapper(
            results.list,
        )


class AsyncResultsResourceWithStreamingResponse:
    def __init__(self, results: AsyncResultsResource) -> None:
        self._results = results

        self.list = async_to_streamed_response_wrapper(
            results.list,
        )
