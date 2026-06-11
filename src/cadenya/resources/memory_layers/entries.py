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
from ...types.memory_layers import (
    entry_list_params,
    entry_create_params,
    entry_update_params,
)
from ...types.memory_layers.memory_entry import MemoryEntry
from ...types.memory_layers.memory_entry_detail import MemoryEntryDetail
from ...types.shared_params.create_resource_metadata import CreateResourceMetadata
from ...types.shared_params.update_resource_metadata import UpdateResourceMetadata
from ...types.memory_layers.memory_entry_create_spec_param import MemoryEntryCreateSpecParam
from ...types.memory_layers.memory_entry_update_spec_param import MemoryEntryUpdateSpecParam

__all__ = ["EntriesResource", "AsyncEntriesResource"]


class EntriesResource(SyncAPIResource):
    """Manage memory layers and their entries.

    Layers are named containers that can
     be composed into an objective's memory cascade; entries are the keyed values
     within a layer. System-managed layers (e.g., episodic layers created by the
     runtime) cannot be mutated through this API.
    """

    @cached_property
    def with_raw_response(self) -> EntriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cadenya/cadenya-python#accessing-raw-response-data-eg-headers
        """
        return EntriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EntriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cadenya/cadenya-python#with_streaming_response
        """
        return EntriesResourceWithStreamingResponse(self)

    def create(
        self,
        memory_layer_id: str,
        *,
        workspace_id: str,
        metadata: CreateResourceMetadata,
        spec: MemoryEntryCreateSpecParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryEntryDetail:
        """Creates a new entry in a memory layer.

        Returns the detail view, including the
        resolved content body.

        Args:
          metadata: CreateResourceMetadata contains the user-provided fields for creating a
              workspace-scoped resource. Read-only fields (id, account_id, workspace_id,
              profile_id, created_at) are excluded since they are set by the server.

          spec: MemoryEntryCreateSpec is the input shape for CreateMemoryEntry. It accepts
              either inline content or a reference to a completed Upload; exactly one of the
              two must be set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not memory_layer_id:
            raise ValueError(f"Expected a non-empty value for `memory_layer_id` but received {memory_layer_id!r}")
        return self._post(
            path_template(
                "/v1/workspaces/{workspace_id}/memory_layers/{memory_layer_id}/entries",
                workspace_id=workspace_id,
                memory_layer_id=memory_layer_id,
            ),
            body=maybe_transform(
                {
                    "metadata": metadata,
                    "spec": spec,
                },
                entry_create_params.EntryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryEntryDetail,
        )

    def retrieve(
        self,
        id: str,
        *,
        workspace_id: str,
        memory_layer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryEntryDetail:
        """Retrieves a memory entry by ID from a memory layer.

        Returns the detail view,
        including the content body.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not memory_layer_id:
            raise ValueError(f"Expected a non-empty value for `memory_layer_id` but received {memory_layer_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template(
                "/v1/workspaces/{workspace_id}/memory_layers/{memory_layer_id}/entries/{id}",
                workspace_id=workspace_id,
                memory_layer_id=memory_layer_id,
                id=id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryEntryDetail,
        )

    def update(
        self,
        id: str,
        *,
        workspace_id: str,
        memory_layer_id: str,
        metadata: UpdateResourceMetadata | Omit = omit,
        spec: MemoryEntryUpdateSpecParam | Omit = omit,
        update_mask: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryEntryDetail:
        """Updates a memory entry in a memory layer.

        Returns the detail view, including the
        resolved content body.

        Args:
          metadata: UpdateResourceMetadata contains the user-provided fields for updating a
              workspace-scoped resource. Read-only fields (id, account_id, workspace_id,
              profile_id, created_at) are excluded since they are set by the server.

          spec: MemoryEntryUpdateSpec is the input shape for UpdateMemoryEntry. Fields present
              in the request's update_mask are applied; unset fields are left alone. The
              source oneof is optional for updates — omit it to leave the body untouched, or
              set exactly one branch to replace it.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not memory_layer_id:
            raise ValueError(f"Expected a non-empty value for `memory_layer_id` but received {memory_layer_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template(
                "/v1/workspaces/{workspace_id}/memory_layers/{memory_layer_id}/entries/{id}",
                workspace_id=workspace_id,
                memory_layer_id=memory_layer_id,
                id=id,
            ),
            body=maybe_transform(
                {
                    "metadata": metadata,
                    "spec": spec,
                    "update_mask": update_mask,
                },
                entry_update_params.EntryUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryEntryDetail,
        )

    def list(
        self,
        memory_layer_id: str,
        *,
        workspace_id: str,
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
    ) -> SyncCursorPagination[MemoryEntry]:
        """
        Lists all entries in a memory layer

        Args:
          bundle_key: Filter by bundle_key — return only resources owned by this bundle.

          cursor: Pagination cursor from previous response

          include_info: When set to true you may use more of your alloted API rate-limit

          limit: Maximum number of results to return

          prefix: Filter by key prefix (e.g., "skills/postmortem/" to list all entries under that
              hierarchy). Matches against the entry's key, not its name.

          query: Free-form search query

          sort_order: Sort order for results (asc or desc by creation time)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not memory_layer_id:
            raise ValueError(f"Expected a non-empty value for `memory_layer_id` but received {memory_layer_id!r}")
        return self._get_api_list(
            path_template(
                "/v1/workspaces/{workspace_id}/memory_layers/{memory_layer_id}/entries",
                workspace_id=workspace_id,
                memory_layer_id=memory_layer_id,
            ),
            page=SyncCursorPagination[MemoryEntry],
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
                    entry_list_params.EntryListParams,
                ),
            ),
            model=MemoryEntry,
        )

    def delete(
        self,
        id: str,
        *,
        workspace_id: str,
        memory_layer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes a memory entry from a memory layer

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not memory_layer_id:
            raise ValueError(f"Expected a non-empty value for `memory_layer_id` but received {memory_layer_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/v1/workspaces/{workspace_id}/memory_layers/{memory_layer_id}/entries/{id}",
                workspace_id=workspace_id,
                memory_layer_id=memory_layer_id,
                id=id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncEntriesResource(AsyncAPIResource):
    """Manage memory layers and their entries.

    Layers are named containers that can
     be composed into an objective's memory cascade; entries are the keyed values
     within a layer. System-managed layers (e.g., episodic layers created by the
     runtime) cannot be mutated through this API.
    """

    @cached_property
    def with_raw_response(self) -> AsyncEntriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cadenya/cadenya-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEntriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEntriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cadenya/cadenya-python#with_streaming_response
        """
        return AsyncEntriesResourceWithStreamingResponse(self)

    async def create(
        self,
        memory_layer_id: str,
        *,
        workspace_id: str,
        metadata: CreateResourceMetadata,
        spec: MemoryEntryCreateSpecParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryEntryDetail:
        """Creates a new entry in a memory layer.

        Returns the detail view, including the
        resolved content body.

        Args:
          metadata: CreateResourceMetadata contains the user-provided fields for creating a
              workspace-scoped resource. Read-only fields (id, account_id, workspace_id,
              profile_id, created_at) are excluded since they are set by the server.

          spec: MemoryEntryCreateSpec is the input shape for CreateMemoryEntry. It accepts
              either inline content or a reference to a completed Upload; exactly one of the
              two must be set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not memory_layer_id:
            raise ValueError(f"Expected a non-empty value for `memory_layer_id` but received {memory_layer_id!r}")
        return await self._post(
            path_template(
                "/v1/workspaces/{workspace_id}/memory_layers/{memory_layer_id}/entries",
                workspace_id=workspace_id,
                memory_layer_id=memory_layer_id,
            ),
            body=await async_maybe_transform(
                {
                    "metadata": metadata,
                    "spec": spec,
                },
                entry_create_params.EntryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryEntryDetail,
        )

    async def retrieve(
        self,
        id: str,
        *,
        workspace_id: str,
        memory_layer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryEntryDetail:
        """Retrieves a memory entry by ID from a memory layer.

        Returns the detail view,
        including the content body.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not memory_layer_id:
            raise ValueError(f"Expected a non-empty value for `memory_layer_id` but received {memory_layer_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template(
                "/v1/workspaces/{workspace_id}/memory_layers/{memory_layer_id}/entries/{id}",
                workspace_id=workspace_id,
                memory_layer_id=memory_layer_id,
                id=id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryEntryDetail,
        )

    async def update(
        self,
        id: str,
        *,
        workspace_id: str,
        memory_layer_id: str,
        metadata: UpdateResourceMetadata | Omit = omit,
        spec: MemoryEntryUpdateSpecParam | Omit = omit,
        update_mask: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryEntryDetail:
        """Updates a memory entry in a memory layer.

        Returns the detail view, including the
        resolved content body.

        Args:
          metadata: UpdateResourceMetadata contains the user-provided fields for updating a
              workspace-scoped resource. Read-only fields (id, account_id, workspace_id,
              profile_id, created_at) are excluded since they are set by the server.

          spec: MemoryEntryUpdateSpec is the input shape for UpdateMemoryEntry. Fields present
              in the request's update_mask are applied; unset fields are left alone. The
              source oneof is optional for updates — omit it to leave the body untouched, or
              set exactly one branch to replace it.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not memory_layer_id:
            raise ValueError(f"Expected a non-empty value for `memory_layer_id` but received {memory_layer_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template(
                "/v1/workspaces/{workspace_id}/memory_layers/{memory_layer_id}/entries/{id}",
                workspace_id=workspace_id,
                memory_layer_id=memory_layer_id,
                id=id,
            ),
            body=await async_maybe_transform(
                {
                    "metadata": metadata,
                    "spec": spec,
                    "update_mask": update_mask,
                },
                entry_update_params.EntryUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryEntryDetail,
        )

    def list(
        self,
        memory_layer_id: str,
        *,
        workspace_id: str,
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
    ) -> AsyncPaginator[MemoryEntry, AsyncCursorPagination[MemoryEntry]]:
        """
        Lists all entries in a memory layer

        Args:
          bundle_key: Filter by bundle_key — return only resources owned by this bundle.

          cursor: Pagination cursor from previous response

          include_info: When set to true you may use more of your alloted API rate-limit

          limit: Maximum number of results to return

          prefix: Filter by key prefix (e.g., "skills/postmortem/" to list all entries under that
              hierarchy). Matches against the entry's key, not its name.

          query: Free-form search query

          sort_order: Sort order for results (asc or desc by creation time)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not memory_layer_id:
            raise ValueError(f"Expected a non-empty value for `memory_layer_id` but received {memory_layer_id!r}")
        return self._get_api_list(
            path_template(
                "/v1/workspaces/{workspace_id}/memory_layers/{memory_layer_id}/entries",
                workspace_id=workspace_id,
                memory_layer_id=memory_layer_id,
            ),
            page=AsyncCursorPagination[MemoryEntry],
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
                    entry_list_params.EntryListParams,
                ),
            ),
            model=MemoryEntry,
        )

    async def delete(
        self,
        id: str,
        *,
        workspace_id: str,
        memory_layer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes a memory entry from a memory layer

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not memory_layer_id:
            raise ValueError(f"Expected a non-empty value for `memory_layer_id` but received {memory_layer_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/v1/workspaces/{workspace_id}/memory_layers/{memory_layer_id}/entries/{id}",
                workspace_id=workspace_id,
                memory_layer_id=memory_layer_id,
                id=id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class EntriesResourceWithRawResponse:
    def __init__(self, entries: EntriesResource) -> None:
        self._entries = entries

        self.create = to_raw_response_wrapper(
            entries.create,
        )
        self.retrieve = to_raw_response_wrapper(
            entries.retrieve,
        )
        self.update = to_raw_response_wrapper(
            entries.update,
        )
        self.list = to_raw_response_wrapper(
            entries.list,
        )
        self.delete = to_raw_response_wrapper(
            entries.delete,
        )


class AsyncEntriesResourceWithRawResponse:
    def __init__(self, entries: AsyncEntriesResource) -> None:
        self._entries = entries

        self.create = async_to_raw_response_wrapper(
            entries.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            entries.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            entries.update,
        )
        self.list = async_to_raw_response_wrapper(
            entries.list,
        )
        self.delete = async_to_raw_response_wrapper(
            entries.delete,
        )


class EntriesResourceWithStreamingResponse:
    def __init__(self, entries: EntriesResource) -> None:
        self._entries = entries

        self.create = to_streamed_response_wrapper(
            entries.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            entries.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            entries.update,
        )
        self.list = to_streamed_response_wrapper(
            entries.list,
        )
        self.delete = to_streamed_response_wrapper(
            entries.delete,
        )


class AsyncEntriesResourceWithStreamingResponse:
    def __init__(self, entries: AsyncEntriesResource) -> None:
        self._entries = entries

        self.create = async_to_streamed_response_wrapper(
            entries.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            entries.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            entries.update,
        )
        self.list = async_to_streamed_response_wrapper(
            entries.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            entries.delete,
        )
