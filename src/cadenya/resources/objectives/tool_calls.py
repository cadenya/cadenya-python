# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

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
from ...types.objectives import tool_call_deny_params, tool_call_list_params
from ...types.objectives.objective_tool_call import ObjectiveToolCall
from ...types.objectives.objective_tool_call_with_result import ObjectiveToolCallWithResult

__all__ = ["ToolCallsResource", "AsyncToolCallsResource"]


class ToolCallsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ToolCallsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cadenya/cadenya-python#accessing-raw-response-data-eg-headers
        """
        return ToolCallsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ToolCallsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cadenya/cadenya-python#with_streaming_response
        """
        return ToolCallsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        tool_call_id: str,
        *,
        workspace_id: str,
        objective_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObjectiveToolCallWithResult:
        """Retrieves a single tool call, including the content the tool returned.

        Media
        content (images, audio) is served as short-lived signed URLs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not objective_id:
            raise ValueError(f"Expected a non-empty value for `objective_id` but received {objective_id!r}")
        if not tool_call_id:
            raise ValueError(f"Expected a non-empty value for `tool_call_id` but received {tool_call_id!r}")
        return self._get(
            path_template(
                "/v1/workspaces/{workspace_id}/objectives/{objective_id}/tool_calls/{tool_call_id}",
                workspace_id=workspace_id,
                objective_id=objective_id,
                tool_call_id=tool_call_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectiveToolCallWithResult,
        )

    def list(
        self,
        objective_id: str,
        *,
        workspace_id: str,
        cursor: str | Omit = omit,
        include_info: bool | Omit = omit,
        limit: int | Omit = omit,
        status: Literal[
            "TOOL_CALL_STATUS_UNSPECIFIED",
            "TOOL_CALL_STATUS_AUTO_APPROVED",
            "TOOL_CALL_STATUS_WAITING_FOR_APPROVAL",
            "TOOL_CALL_STATUS_APPROVED",
            "TOOL_CALL_STATUS_DENIED",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPagination[ObjectiveToolCall]:
        """
        Lists all tool calls for an objective

        Args:
          cursor: Pagination cursor from previous response

          include_info: When set to true you may use more of your alloted API rate-limit

          limit: Maximum number of results to return

          status: Filter by tool call status

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
                "/v1/workspaces/{workspace_id}/objectives/{objective_id}/tool_calls",
                workspace_id=workspace_id,
                objective_id=objective_id,
            ),
            page=SyncCursorPagination[ObjectiveToolCall],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "include_info": include_info,
                        "limit": limit,
                        "status": status,
                    },
                    tool_call_list_params.ToolCallListParams,
                ),
            ),
            model=ObjectiveToolCall,
        )

    def approve(
        self,
        tool_call_id: str,
        *,
        workspace_id: str,
        objective_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObjectiveToolCall:
        """
        When an agent attempts to use a tool that requires approval, use this endpoint
        to mark it as approved.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not objective_id:
            raise ValueError(f"Expected a non-empty value for `objective_id` but received {objective_id!r}")
        if not tool_call_id:
            raise ValueError(f"Expected a non-empty value for `tool_call_id` but received {tool_call_id!r}")
        return self._post(
            path_template(
                "/v1/workspaces/{workspace_id}/objectives/{objective_id}/tool_calls/{tool_call_id}:approve",
                workspace_id=workspace_id,
                objective_id=objective_id,
                tool_call_id=tool_call_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectiveToolCall,
        )

    def deny(
        self,
        tool_call_id: str,
        *,
        workspace_id: str,
        objective_id: str,
        memo: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObjectiveToolCall:
        """
        When an agent attempts to use a tool that requires approval, use this endpoint
        to mark it as denied. Use a memo to steer the LLM to a different decision or
        usage of the tool.

        Args:
          memo: A memo to associate to the tool call denial. Use a memo to steer the LLM to a
              different decision or usage of the tool.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not objective_id:
            raise ValueError(f"Expected a non-empty value for `objective_id` but received {objective_id!r}")
        if not tool_call_id:
            raise ValueError(f"Expected a non-empty value for `tool_call_id` but received {tool_call_id!r}")
        return self._post(
            path_template(
                "/v1/workspaces/{workspace_id}/objectives/{objective_id}/tool_calls/{tool_call_id}:deny",
                workspace_id=workspace_id,
                objective_id=objective_id,
                tool_call_id=tool_call_id,
            ),
            body=maybe_transform({"memo": memo}, tool_call_deny_params.ToolCallDenyParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectiveToolCall,
        )


class AsyncToolCallsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncToolCallsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cadenya/cadenya-python#accessing-raw-response-data-eg-headers
        """
        return AsyncToolCallsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncToolCallsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cadenya/cadenya-python#with_streaming_response
        """
        return AsyncToolCallsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        tool_call_id: str,
        *,
        workspace_id: str,
        objective_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObjectiveToolCallWithResult:
        """Retrieves a single tool call, including the content the tool returned.

        Media
        content (images, audio) is served as short-lived signed URLs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not objective_id:
            raise ValueError(f"Expected a non-empty value for `objective_id` but received {objective_id!r}")
        if not tool_call_id:
            raise ValueError(f"Expected a non-empty value for `tool_call_id` but received {tool_call_id!r}")
        return await self._get(
            path_template(
                "/v1/workspaces/{workspace_id}/objectives/{objective_id}/tool_calls/{tool_call_id}",
                workspace_id=workspace_id,
                objective_id=objective_id,
                tool_call_id=tool_call_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectiveToolCallWithResult,
        )

    def list(
        self,
        objective_id: str,
        *,
        workspace_id: str,
        cursor: str | Omit = omit,
        include_info: bool | Omit = omit,
        limit: int | Omit = omit,
        status: Literal[
            "TOOL_CALL_STATUS_UNSPECIFIED",
            "TOOL_CALL_STATUS_AUTO_APPROVED",
            "TOOL_CALL_STATUS_WAITING_FOR_APPROVAL",
            "TOOL_CALL_STATUS_APPROVED",
            "TOOL_CALL_STATUS_DENIED",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ObjectiveToolCall, AsyncCursorPagination[ObjectiveToolCall]]:
        """
        Lists all tool calls for an objective

        Args:
          cursor: Pagination cursor from previous response

          include_info: When set to true you may use more of your alloted API rate-limit

          limit: Maximum number of results to return

          status: Filter by tool call status

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
                "/v1/workspaces/{workspace_id}/objectives/{objective_id}/tool_calls",
                workspace_id=workspace_id,
                objective_id=objective_id,
            ),
            page=AsyncCursorPagination[ObjectiveToolCall],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "include_info": include_info,
                        "limit": limit,
                        "status": status,
                    },
                    tool_call_list_params.ToolCallListParams,
                ),
            ),
            model=ObjectiveToolCall,
        )

    async def approve(
        self,
        tool_call_id: str,
        *,
        workspace_id: str,
        objective_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObjectiveToolCall:
        """
        When an agent attempts to use a tool that requires approval, use this endpoint
        to mark it as approved.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not objective_id:
            raise ValueError(f"Expected a non-empty value for `objective_id` but received {objective_id!r}")
        if not tool_call_id:
            raise ValueError(f"Expected a non-empty value for `tool_call_id` but received {tool_call_id!r}")
        return await self._post(
            path_template(
                "/v1/workspaces/{workspace_id}/objectives/{objective_id}/tool_calls/{tool_call_id}:approve",
                workspace_id=workspace_id,
                objective_id=objective_id,
                tool_call_id=tool_call_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectiveToolCall,
        )

    async def deny(
        self,
        tool_call_id: str,
        *,
        workspace_id: str,
        objective_id: str,
        memo: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObjectiveToolCall:
        """
        When an agent attempts to use a tool that requires approval, use this endpoint
        to mark it as denied. Use a memo to steer the LLM to a different decision or
        usage of the tool.

        Args:
          memo: A memo to associate to the tool call denial. Use a memo to steer the LLM to a
              different decision or usage of the tool.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not objective_id:
            raise ValueError(f"Expected a non-empty value for `objective_id` but received {objective_id!r}")
        if not tool_call_id:
            raise ValueError(f"Expected a non-empty value for `tool_call_id` but received {tool_call_id!r}")
        return await self._post(
            path_template(
                "/v1/workspaces/{workspace_id}/objectives/{objective_id}/tool_calls/{tool_call_id}:deny",
                workspace_id=workspace_id,
                objective_id=objective_id,
                tool_call_id=tool_call_id,
            ),
            body=await async_maybe_transform({"memo": memo}, tool_call_deny_params.ToolCallDenyParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectiveToolCall,
        )


class ToolCallsResourceWithRawResponse:
    def __init__(self, tool_calls: ToolCallsResource) -> None:
        self._tool_calls = tool_calls

        self.retrieve = to_raw_response_wrapper(
            tool_calls.retrieve,
        )
        self.list = to_raw_response_wrapper(
            tool_calls.list,
        )
        self.approve = to_raw_response_wrapper(
            tool_calls.approve,
        )
        self.deny = to_raw_response_wrapper(
            tool_calls.deny,
        )


class AsyncToolCallsResourceWithRawResponse:
    def __init__(self, tool_calls: AsyncToolCallsResource) -> None:
        self._tool_calls = tool_calls

        self.retrieve = async_to_raw_response_wrapper(
            tool_calls.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            tool_calls.list,
        )
        self.approve = async_to_raw_response_wrapper(
            tool_calls.approve,
        )
        self.deny = async_to_raw_response_wrapper(
            tool_calls.deny,
        )


class ToolCallsResourceWithStreamingResponse:
    def __init__(self, tool_calls: ToolCallsResource) -> None:
        self._tool_calls = tool_calls

        self.retrieve = to_streamed_response_wrapper(
            tool_calls.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            tool_calls.list,
        )
        self.approve = to_streamed_response_wrapper(
            tool_calls.approve,
        )
        self.deny = to_streamed_response_wrapper(
            tool_calls.deny,
        )


class AsyncToolCallsResourceWithStreamingResponse:
    def __init__(self, tool_calls: AsyncToolCallsResource) -> None:
        self._tool_calls = tool_calls

        self.retrieve = async_to_streamed_response_wrapper(
            tool_calls.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            tool_calls.list,
        )
        self.approve = async_to_streamed_response_wrapper(
            tool_calls.approve,
        )
        self.deny = async_to_streamed_response_wrapper(
            tool_calls.deny,
        )
