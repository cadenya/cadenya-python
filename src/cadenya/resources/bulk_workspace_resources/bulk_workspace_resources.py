# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...types import bulk_workspace_resource_list_params, bulk_workspace_resource_apply_params
from .results import (
    ResultsResource,
    AsyncResultsResource,
    ResultsResourceWithRawResponse,
    AsyncResultsResourceWithRawResponse,
    ResultsResourceWithStreamingResponse,
    AsyncResultsResourceWithStreamingResponse,
)
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
from ...types.bulk_workspace_apply import BulkWorkspaceApply
from ...types.bulk_workspace_apply_data_param import BulkWorkspaceApplyDataParam

__all__ = ["BulkWorkspaceResourcesResource", "AsyncBulkWorkspaceResourcesResource"]


class BulkWorkspaceResourcesResource(SyncAPIResource):
    """
    Apply a declarative bundle of workspace resources — tool sets, memory
     layers, agents, variations, assignments, and schedules — in a single
     asynchronous operation.
    """

    @cached_property
    def results(self) -> ResultsResource:
        """
        Apply a declarative bundle of workspace resources — tool sets, memory
         layers, agents, variations, assignments, and schedules — in a single
         asynchronous operation.
        """
        return ResultsResource(self._client)

    @cached_property
    def with_raw_response(self) -> BulkWorkspaceResourcesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cadenya/cadenya-python#accessing-raw-response-data-eg-headers
        """
        return BulkWorkspaceResourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BulkWorkspaceResourcesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cadenya/cadenya-python#with_streaming_response
        """
        return BulkWorkspaceResourcesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        workspace_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BulkWorkspaceApply:
        """
        Retrieves a bulk workspace apply operation by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template(
                "/v1/workspaces/{workspace_id}/bulk_workspace_applies/{id}", workspace_id=workspace_id, id=id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkWorkspaceApply,
        )

    def list(
        self,
        workspace_id: str,
        *,
        bundle_key: str | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        sort_order: str | Omit = omit,
        state: Literal[
            "STATE_UNSPECIFIED",
            "STATE_PENDING",
            "STATE_VALIDATING",
            "STATE_RUNNING",
            "STATE_SUCCEEDED",
            "STATE_PARTIALLY_APPLIED",
            "STATE_FAILED",
            "STATE_CANCELLED",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPagination[BulkWorkspaceApply]:
        """
        Lists past and in-flight bulk workspace apply operations in the workspace.

        Args:
          bundle_key: Filter by bundle_key — list every apply for a given bundle.

          cursor: Pagination cursor from previous response

          limit: Maximum number of results to return

          sort_order: Sort order for results (asc or desc by creation time)

          state: Filter by lifecycle state.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return self._get_api_list(
            path_template("/v1/workspaces/{workspace_id}/bulk_workspace_applies", workspace_id=workspace_id),
            page=SyncCursorPagination[BulkWorkspaceApply],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "bundle_key": bundle_key,
                        "cursor": cursor,
                        "limit": limit,
                        "sort_order": sort_order,
                        "state": state,
                    },
                    bulk_workspace_resource_list_params.BulkWorkspaceResourceListParams,
                ),
            ),
            model=BulkWorkspaceApply,
        )

    def apply(
        self,
        workspace_id: str,
        *,
        data: BulkWorkspaceApplyDataParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BulkWorkspaceApply:
        """Asynchronously applies a declarative bundle of workspace resources.

        Returns the
        operation immediately in PENDING; clients poll Get to track progress.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return self._post(
            path_template("/v1/workspaces/{workspace_id}/bulk_workspace_applies", workspace_id=workspace_id),
            body=maybe_transform({"data": data}, bulk_workspace_resource_apply_params.BulkWorkspaceResourceApplyParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkWorkspaceApply,
        )


class AsyncBulkWorkspaceResourcesResource(AsyncAPIResource):
    """
    Apply a declarative bundle of workspace resources — tool sets, memory
     layers, agents, variations, assignments, and schedules — in a single
     asynchronous operation.
    """

    @cached_property
    def results(self) -> AsyncResultsResource:
        """
        Apply a declarative bundle of workspace resources — tool sets, memory
         layers, agents, variations, assignments, and schedules — in a single
         asynchronous operation.
        """
        return AsyncResultsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBulkWorkspaceResourcesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cadenya/cadenya-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBulkWorkspaceResourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBulkWorkspaceResourcesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cadenya/cadenya-python#with_streaming_response
        """
        return AsyncBulkWorkspaceResourcesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        workspace_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BulkWorkspaceApply:
        """
        Retrieves a bulk workspace apply operation by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template(
                "/v1/workspaces/{workspace_id}/bulk_workspace_applies/{id}", workspace_id=workspace_id, id=id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkWorkspaceApply,
        )

    def list(
        self,
        workspace_id: str,
        *,
        bundle_key: str | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        sort_order: str | Omit = omit,
        state: Literal[
            "STATE_UNSPECIFIED",
            "STATE_PENDING",
            "STATE_VALIDATING",
            "STATE_RUNNING",
            "STATE_SUCCEEDED",
            "STATE_PARTIALLY_APPLIED",
            "STATE_FAILED",
            "STATE_CANCELLED",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[BulkWorkspaceApply, AsyncCursorPagination[BulkWorkspaceApply]]:
        """
        Lists past and in-flight bulk workspace apply operations in the workspace.

        Args:
          bundle_key: Filter by bundle_key — list every apply for a given bundle.

          cursor: Pagination cursor from previous response

          limit: Maximum number of results to return

          sort_order: Sort order for results (asc or desc by creation time)

          state: Filter by lifecycle state.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return self._get_api_list(
            path_template("/v1/workspaces/{workspace_id}/bulk_workspace_applies", workspace_id=workspace_id),
            page=AsyncCursorPagination[BulkWorkspaceApply],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "bundle_key": bundle_key,
                        "cursor": cursor,
                        "limit": limit,
                        "sort_order": sort_order,
                        "state": state,
                    },
                    bulk_workspace_resource_list_params.BulkWorkspaceResourceListParams,
                ),
            ),
            model=BulkWorkspaceApply,
        )

    async def apply(
        self,
        workspace_id: str,
        *,
        data: BulkWorkspaceApplyDataParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BulkWorkspaceApply:
        """Asynchronously applies a declarative bundle of workspace resources.

        Returns the
        operation immediately in PENDING; clients poll Get to track progress.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return await self._post(
            path_template("/v1/workspaces/{workspace_id}/bulk_workspace_applies", workspace_id=workspace_id),
            body=await async_maybe_transform(
                {"data": data}, bulk_workspace_resource_apply_params.BulkWorkspaceResourceApplyParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkWorkspaceApply,
        )


class BulkWorkspaceResourcesResourceWithRawResponse:
    def __init__(self, bulk_workspace_resources: BulkWorkspaceResourcesResource) -> None:
        self._bulk_workspace_resources = bulk_workspace_resources

        self.retrieve = to_raw_response_wrapper(
            bulk_workspace_resources.retrieve,
        )
        self.list = to_raw_response_wrapper(
            bulk_workspace_resources.list,
        )
        self.apply = to_raw_response_wrapper(
            bulk_workspace_resources.apply,
        )

    @cached_property
    def results(self) -> ResultsResourceWithRawResponse:
        """
        Apply a declarative bundle of workspace resources — tool sets, memory
         layers, agents, variations, assignments, and schedules — in a single
         asynchronous operation.
        """
        return ResultsResourceWithRawResponse(self._bulk_workspace_resources.results)


class AsyncBulkWorkspaceResourcesResourceWithRawResponse:
    def __init__(self, bulk_workspace_resources: AsyncBulkWorkspaceResourcesResource) -> None:
        self._bulk_workspace_resources = bulk_workspace_resources

        self.retrieve = async_to_raw_response_wrapper(
            bulk_workspace_resources.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            bulk_workspace_resources.list,
        )
        self.apply = async_to_raw_response_wrapper(
            bulk_workspace_resources.apply,
        )

    @cached_property
    def results(self) -> AsyncResultsResourceWithRawResponse:
        """
        Apply a declarative bundle of workspace resources — tool sets, memory
         layers, agents, variations, assignments, and schedules — in a single
         asynchronous operation.
        """
        return AsyncResultsResourceWithRawResponse(self._bulk_workspace_resources.results)


class BulkWorkspaceResourcesResourceWithStreamingResponse:
    def __init__(self, bulk_workspace_resources: BulkWorkspaceResourcesResource) -> None:
        self._bulk_workspace_resources = bulk_workspace_resources

        self.retrieve = to_streamed_response_wrapper(
            bulk_workspace_resources.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            bulk_workspace_resources.list,
        )
        self.apply = to_streamed_response_wrapper(
            bulk_workspace_resources.apply,
        )

    @cached_property
    def results(self) -> ResultsResourceWithStreamingResponse:
        """
        Apply a declarative bundle of workspace resources — tool sets, memory
         layers, agents, variations, assignments, and schedules — in a single
         asynchronous operation.
        """
        return ResultsResourceWithStreamingResponse(self._bulk_workspace_resources.results)


class AsyncBulkWorkspaceResourcesResourceWithStreamingResponse:
    def __init__(self, bulk_workspace_resources: AsyncBulkWorkspaceResourcesResource) -> None:
        self._bulk_workspace_resources = bulk_workspace_resources

        self.retrieve = async_to_streamed_response_wrapper(
            bulk_workspace_resources.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            bulk_workspace_resources.list,
        )
        self.apply = async_to_streamed_response_wrapper(
            bulk_workspace_resources.apply,
        )

    @cached_property
    def results(self) -> AsyncResultsResourceWithStreamingResponse:
        """
        Apply a declarative bundle of workspace resources — tool sets, memory
         layers, agents, variations, assignments, and schedules — in a single
         asynchronous operation.
        """
        return AsyncResultsResourceWithStreamingResponse(self._bulk_workspace_resources.results)
