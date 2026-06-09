# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .access import (
    AccessResource,
    AsyncAccessResource,
    AccessResourceWithRawResponse,
    AsyncAccessResourceWithRawResponse,
    AccessResourceWithStreamingResponse,
    AsyncAccessResourceWithStreamingResponse,
)
from ...types import api_key_list_params, api_key_create_params, api_key_update_params
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
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
from ...types.api_key_spec_param import APIKeySpecParam

__all__ = ["APIKeysResource", "AsyncAPIKeysResource"]


class APIKeysResource(SyncAPIResource):
    """
    Issue, rotate, and revoke API keys for the account, and grant or revoke
     each key's access to individual workspaces.
    """

    @cached_property
    def access(self) -> AccessResource:
        """
        Issue, rotate, and revoke API keys for the account, and grant or revoke
         each key's access to individual workspaces.
        """
        return AccessResource(self._client)

    @cached_property
    def with_raw_response(self) -> APIKeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cadenya/cadenya-python#accessing-raw-response-data-eg-headers
        """
        return APIKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> APIKeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cadenya/cadenya-python#with_streaming_response
        """
        return APIKeysResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        metadata: api_key_create_params.Metadata,
        spec: APIKeySpecParam,
        initial_workspace_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKey:
        """Creates a new API key on the account.

        Optionally grants the key access to one or
        more workspaces via initial_workspace_ids.

        Args:
          metadata: CreateAccountResourceMetadata contains the user-provided fields for creating an
              account-scoped resource. Read-only fields (id, account_id, profile_id) are
              excluded since they are set by the server.

          spec: Configuration for an API key.

          initial_workspace_ids: Workspaces this API key will have access to on creation. Optional — a key can be
              created with no workspace access and granted later via AddAPIKeyWorkspace.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/account/api_keys",
            body=maybe_transform(
                {
                    "metadata": metadata,
                    "spec": spec,
                    "initial_workspace_ids": initial_workspace_ids,
                },
                api_key_create_params.APIKeyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKey,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKey:
        """
        Retrieves an API key by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/v1/account/api_keys/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKey,
        )

    def update(
        self,
        id: str,
        *,
        metadata: api_key_update_params.Metadata | Omit = omit,
        spec: APIKeySpecParam | Omit = omit,
        update_mask: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKey:
        """
        Updates an API key.

        Args:
          metadata: UpdateAccountResourceMetadata contains the user-provided fields for updating an
              account-scoped resource. Read-only fields (id, account_id, profile_id) are
              excluded since they are set by the server.

          spec: Configuration for an API key.

          update_mask: Fields to update.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/v1/account/api_keys/{id}", id=id),
            body=maybe_transform(
                {
                    "metadata": metadata,
                    "spec": spec,
                    "update_mask": update_mask,
                },
                api_key_update_params.APIKeyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKey,
        )

    def list(
        self,
        *,
        bundle_key: str | Omit = omit,
        cursor: str | Omit = omit,
        include_info: bool | Omit = omit,
        limit: int | Omit = omit,
        prefix: str | Omit = omit,
        query: str | Omit = omit,
        sort_order: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPagination[APIKey]:
        """
        Lists all API keys on the account.

        Args:
          bundle_key: Filter by bundle_key — return only resources owned by this bundle.

          cursor: Pagination cursor from previous response.

          include_info: When true, included info fields are populated. Requests with this flag count
              more against your rate limit.

          limit: Maximum number of results to return.

          prefix: Filter by ID prefix.

          query: Free-form search query.

          sort_order: Sort order for results (asc or desc by creation time).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/account/api_keys",
            page=SyncCursorPagination[APIKey],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "bundle_key": bundle_key,
                        "cursor": cursor,
                        "include_info": include_info,
                        "limit": limit,
                        "prefix": prefix,
                        "query": query,
                        "sort_order": sort_order,
                    },
                    api_key_list_params.APIKeyListParams,
                ),
            ),
            model=APIKey,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes an API key.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v1/account/api_keys/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def rotate(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKey:
        """Rotates an API key and returns a new token.

        All previous tokens for this key are
        invalidated.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/v1/account/api_keys/{id}:rotate", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKey,
        )


class AsyncAPIKeysResource(AsyncAPIResource):
    """
    Issue, rotate, and revoke API keys for the account, and grant or revoke
     each key's access to individual workspaces.
    """

    @cached_property
    def access(self) -> AsyncAccessResource:
        """
        Issue, rotate, and revoke API keys for the account, and grant or revoke
         each key's access to individual workspaces.
        """
        return AsyncAccessResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAPIKeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cadenya/cadenya-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAPIKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAPIKeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cadenya/cadenya-python#with_streaming_response
        """
        return AsyncAPIKeysResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        metadata: api_key_create_params.Metadata,
        spec: APIKeySpecParam,
        initial_workspace_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKey:
        """Creates a new API key on the account.

        Optionally grants the key access to one or
        more workspaces via initial_workspace_ids.

        Args:
          metadata: CreateAccountResourceMetadata contains the user-provided fields for creating an
              account-scoped resource. Read-only fields (id, account_id, profile_id) are
              excluded since they are set by the server.

          spec: Configuration for an API key.

          initial_workspace_ids: Workspaces this API key will have access to on creation. Optional — a key can be
              created with no workspace access and granted later via AddAPIKeyWorkspace.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/account/api_keys",
            body=await async_maybe_transform(
                {
                    "metadata": metadata,
                    "spec": spec,
                    "initial_workspace_ids": initial_workspace_ids,
                },
                api_key_create_params.APIKeyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKey,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKey:
        """
        Retrieves an API key by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/v1/account/api_keys/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKey,
        )

    async def update(
        self,
        id: str,
        *,
        metadata: api_key_update_params.Metadata | Omit = omit,
        spec: APIKeySpecParam | Omit = omit,
        update_mask: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKey:
        """
        Updates an API key.

        Args:
          metadata: UpdateAccountResourceMetadata contains the user-provided fields for updating an
              account-scoped resource. Read-only fields (id, account_id, profile_id) are
              excluded since they are set by the server.

          spec: Configuration for an API key.

          update_mask: Fields to update.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/v1/account/api_keys/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "metadata": metadata,
                    "spec": spec,
                    "update_mask": update_mask,
                },
                api_key_update_params.APIKeyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKey,
        )

    def list(
        self,
        *,
        bundle_key: str | Omit = omit,
        cursor: str | Omit = omit,
        include_info: bool | Omit = omit,
        limit: int | Omit = omit,
        prefix: str | Omit = omit,
        query: str | Omit = omit,
        sort_order: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[APIKey, AsyncCursorPagination[APIKey]]:
        """
        Lists all API keys on the account.

        Args:
          bundle_key: Filter by bundle_key — return only resources owned by this bundle.

          cursor: Pagination cursor from previous response.

          include_info: When true, included info fields are populated. Requests with this flag count
              more against your rate limit.

          limit: Maximum number of results to return.

          prefix: Filter by ID prefix.

          query: Free-form search query.

          sort_order: Sort order for results (asc or desc by creation time).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/account/api_keys",
            page=AsyncCursorPagination[APIKey],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "bundle_key": bundle_key,
                        "cursor": cursor,
                        "include_info": include_info,
                        "limit": limit,
                        "prefix": prefix,
                        "query": query,
                        "sort_order": sort_order,
                    },
                    api_key_list_params.APIKeyListParams,
                ),
            ),
            model=APIKey,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes an API key.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/account/api_keys/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def rotate(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKey:
        """Rotates an API key and returns a new token.

        All previous tokens for this key are
        invalidated.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/v1/account/api_keys/{id}:rotate", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKey,
        )


class APIKeysResourceWithRawResponse:
    def __init__(self, api_keys: APIKeysResource) -> None:
        self._api_keys = api_keys

        self.create = to_raw_response_wrapper(
            api_keys.create,
        )
        self.retrieve = to_raw_response_wrapper(
            api_keys.retrieve,
        )
        self.update = to_raw_response_wrapper(
            api_keys.update,
        )
        self.list = to_raw_response_wrapper(
            api_keys.list,
        )
        self.delete = to_raw_response_wrapper(
            api_keys.delete,
        )
        self.rotate = to_raw_response_wrapper(
            api_keys.rotate,
        )

    @cached_property
    def access(self) -> AccessResourceWithRawResponse:
        """
        Issue, rotate, and revoke API keys for the account, and grant or revoke
         each key's access to individual workspaces.
        """
        return AccessResourceWithRawResponse(self._api_keys.access)


class AsyncAPIKeysResourceWithRawResponse:
    def __init__(self, api_keys: AsyncAPIKeysResource) -> None:
        self._api_keys = api_keys

        self.create = async_to_raw_response_wrapper(
            api_keys.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            api_keys.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            api_keys.update,
        )
        self.list = async_to_raw_response_wrapper(
            api_keys.list,
        )
        self.delete = async_to_raw_response_wrapper(
            api_keys.delete,
        )
        self.rotate = async_to_raw_response_wrapper(
            api_keys.rotate,
        )

    @cached_property
    def access(self) -> AsyncAccessResourceWithRawResponse:
        """
        Issue, rotate, and revoke API keys for the account, and grant or revoke
         each key's access to individual workspaces.
        """
        return AsyncAccessResourceWithRawResponse(self._api_keys.access)


class APIKeysResourceWithStreamingResponse:
    def __init__(self, api_keys: APIKeysResource) -> None:
        self._api_keys = api_keys

        self.create = to_streamed_response_wrapper(
            api_keys.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            api_keys.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            api_keys.update,
        )
        self.list = to_streamed_response_wrapper(
            api_keys.list,
        )
        self.delete = to_streamed_response_wrapper(
            api_keys.delete,
        )
        self.rotate = to_streamed_response_wrapper(
            api_keys.rotate,
        )

    @cached_property
    def access(self) -> AccessResourceWithStreamingResponse:
        """
        Issue, rotate, and revoke API keys for the account, and grant or revoke
         each key's access to individual workspaces.
        """
        return AccessResourceWithStreamingResponse(self._api_keys.access)


class AsyncAPIKeysResourceWithStreamingResponse:
    def __init__(self, api_keys: AsyncAPIKeysResource) -> None:
        self._api_keys = api_keys

        self.create = async_to_streamed_response_wrapper(
            api_keys.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            api_keys.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            api_keys.update,
        )
        self.list = async_to_streamed_response_wrapper(
            api_keys.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            api_keys.delete,
        )
        self.rotate = async_to_streamed_response_wrapper(
            api_keys.rotate,
        )

    @cached_property
    def access(self) -> AsyncAccessResourceWithStreamingResponse:
        """
        Issue, rotate, and revoke API keys for the account, and grant or revoke
         each key's access to individual workspaces.
        """
        return AsyncAccessResourceWithStreamingResponse(self._api_keys.access)
