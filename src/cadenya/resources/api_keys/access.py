# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ...types.api_key import APIKey
from ...types.api_keys import access_add_params, access_list_params
from ...types.workspace import Workspace

__all__ = ["AccessResource", "AsyncAccessResource"]


class AccessResource(SyncAPIResource):
    """
    Issue, rotate, and revoke API keys for the account, and grant or revoke
     each key's access to individual workspaces.
    """

    @cached_property
    def with_raw_response(self) -> AccessResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cadenya/cadenya-python#accessing-raw-response-data-eg-headers
        """
        return AccessResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccessResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cadenya/cadenya-python#with_streaming_response
        """
        return AccessResourceWithStreamingResponse(self)

    def list(
        self,
        id: str,
        *,
        cursor: str | Omit = omit,
        labels: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPagination[Workspace]:
        """Lists the workspaces this API key has access to.

        Cursor-paginated.

        Args:
          cursor: Pagination cursor from previous response.

          labels: Filters by metadata labels. Comma-separated key=value pairs, e.g.
              "env=prod,team=ai". A resource matches only if every pair matches exactly (AND
              semantics).

          limit: Maximum number of results to return.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get_api_list(
            path_template("/v1/account/api_keys/{id}/workspaces", id=id),
            page=SyncCursorPagination[Workspace],
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
                    access_list_params.AccessListParams,
                ),
            ),
            model=Workspace,
        )

    def add(
        self,
        id: str,
        *,
        workspace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKey:
        """Grants this API key access to the specified workspace.

        Idempotent — adding an
        already-associated workspace is a no-op. Returns the updated API key with
        refreshed workspace preview and total.

        Args:
          workspace_id: The workspace to grant access to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/v1/account/api_keys/{id}/workspaces", id=id),
            body=maybe_transform({"workspace_id": workspace_id}, access_add_params.AccessAddParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKey,
        )

    def remove(
        self,
        workspace_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Revokes this API key's access to the specified workspace.

        Idempotent. A key may
        have zero workspaces and remains valid.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v1/account/api_keys/{id}/workspaces/{workspace_id}", id=id, workspace_id=workspace_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncAccessResource(AsyncAPIResource):
    """
    Issue, rotate, and revoke API keys for the account, and grant or revoke
     each key's access to individual workspaces.
    """

    @cached_property
    def with_raw_response(self) -> AsyncAccessResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cadenya/cadenya-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAccessResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccessResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cadenya/cadenya-python#with_streaming_response
        """
        return AsyncAccessResourceWithStreamingResponse(self)

    def list(
        self,
        id: str,
        *,
        cursor: str | Omit = omit,
        labels: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Workspace, AsyncCursorPagination[Workspace]]:
        """Lists the workspaces this API key has access to.

        Cursor-paginated.

        Args:
          cursor: Pagination cursor from previous response.

          labels: Filters by metadata labels. Comma-separated key=value pairs, e.g.
              "env=prod,team=ai". A resource matches only if every pair matches exactly (AND
              semantics).

          limit: Maximum number of results to return.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get_api_list(
            path_template("/v1/account/api_keys/{id}/workspaces", id=id),
            page=AsyncCursorPagination[Workspace],
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
                    access_list_params.AccessListParams,
                ),
            ),
            model=Workspace,
        )

    async def add(
        self,
        id: str,
        *,
        workspace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKey:
        """Grants this API key access to the specified workspace.

        Idempotent — adding an
        already-associated workspace is a no-op. Returns the updated API key with
        refreshed workspace preview and total.

        Args:
          workspace_id: The workspace to grant access to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/v1/account/api_keys/{id}/workspaces", id=id),
            body=await async_maybe_transform({"workspace_id": workspace_id}, access_add_params.AccessAddParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKey,
        )

    async def remove(
        self,
        workspace_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Revokes this API key's access to the specified workspace.

        Idempotent. A key may
        have zero workspaces and remains valid.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/account/api_keys/{id}/workspaces/{workspace_id}", id=id, workspace_id=workspace_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AccessResourceWithRawResponse:
    def __init__(self, access: AccessResource) -> None:
        self._access = access

        self.list = to_raw_response_wrapper(
            access.list,
        )
        self.add = to_raw_response_wrapper(
            access.add,
        )
        self.remove = to_raw_response_wrapper(
            access.remove,
        )


class AsyncAccessResourceWithRawResponse:
    def __init__(self, access: AsyncAccessResource) -> None:
        self._access = access

        self.list = async_to_raw_response_wrapper(
            access.list,
        )
        self.add = async_to_raw_response_wrapper(
            access.add,
        )
        self.remove = async_to_raw_response_wrapper(
            access.remove,
        )


class AccessResourceWithStreamingResponse:
    def __init__(self, access: AccessResource) -> None:
        self._access = access

        self.list = to_streamed_response_wrapper(
            access.list,
        )
        self.add = to_streamed_response_wrapper(
            access.add,
        )
        self.remove = to_streamed_response_wrapper(
            access.remove,
        )


class AsyncAccessResourceWithStreamingResponse:
    def __init__(self, access: AsyncAccessResource) -> None:
        self._access = access

        self.list = async_to_streamed_response_wrapper(
            access.list,
        )
        self.add = async_to_streamed_response_wrapper(
            access.add,
        )
        self.remove = async_to_streamed_response_wrapper(
            access.remove,
        )
