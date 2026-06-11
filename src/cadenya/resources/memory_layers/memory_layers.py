# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...types import (
    memory_layer_list_params,
    memory_layer_create_params,
    memory_layer_update_params,
)
from .entries import (
    EntriesResource,
    AsyncEntriesResource,
    EntriesResourceWithRawResponse,
    AsyncEntriesResourceWithRawResponse,
    EntriesResourceWithStreamingResponse,
    AsyncEntriesResourceWithStreamingResponse,
)
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
from ...types.memory_layer import MemoryLayer
from ...types.memory_layer_spec_param import MemoryLayerSpecParam
from ...types.shared_params.create_resource_metadata import CreateResourceMetadata
from ...types.shared_params.update_resource_metadata import UpdateResourceMetadata

__all__ = ["MemoryLayersResource", "AsyncMemoryLayersResource"]


class MemoryLayersResource(SyncAPIResource):
    """Manage memory layers and their entries.

    Layers are named containers that can
     be composed into an objective's memory cascade; entries are the keyed values
     within a layer. System-managed layers (e.g., episodic layers created by the
     runtime) cannot be mutated through this API.
    """

    @cached_property
    def entries(self) -> EntriesResource:
        """Manage memory layers and their entries.

        Layers are named containers that can
         be composed into an objective's memory cascade; entries are the keyed values
         within a layer. System-managed layers (e.g., episodic layers created by the
         runtime) cannot be mutated through this API.
        """
        return EntriesResource(self._client)

    @cached_property
    def with_raw_response(self) -> MemoryLayersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cadenya/cadenya-python#accessing-raw-response-data-eg-headers
        """
        return MemoryLayersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MemoryLayersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cadenya/cadenya-python#with_streaming_response
        """
        return MemoryLayersResourceWithStreamingResponse(self)

    def create(
        self,
        workspace_id: str,
        *,
        metadata: CreateResourceMetadata,
        spec: MemoryLayerSpecParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryLayer:
        """
        Creates a new memory layer in the workspace

        Args:
          metadata: CreateResourceMetadata contains the user-provided fields for creating a
              workspace-scoped resource. Read-only fields (id, account_id, workspace_id,
              profile_id, created_at) are excluded since they are set by the server.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return self._post(
            path_template("/v1/workspaces/{workspace_id}/memory_layers", workspace_id=workspace_id),
            body=maybe_transform(
                {
                    "metadata": metadata,
                    "spec": spec,
                },
                memory_layer_create_params.MemoryLayerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryLayer,
        )

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
    ) -> MemoryLayer:
        """
        Retrieves a memory layer by ID from the workspace

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
            path_template("/v1/workspaces/{workspace_id}/memory_layers/{id}", workspace_id=workspace_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryLayer,
        )

    def update(
        self,
        id: str,
        *,
        workspace_id: str,
        metadata: UpdateResourceMetadata | Omit = omit,
        spec: MemoryLayerSpecParam | Omit = omit,
        update_mask: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryLayer:
        """
        Updates a memory layer in the workspace

        Args:
          metadata: UpdateResourceMetadata contains the user-provided fields for updating a
              workspace-scoped resource. Read-only fields (id, account_id, workspace_id,
              profile_id, created_at) are excluded since they are set by the server.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/v1/workspaces/{workspace_id}/memory_layers/{id}", workspace_id=workspace_id, id=id),
            body=maybe_transform(
                {
                    "metadata": metadata,
                    "spec": spec,
                    "update_mask": update_mask,
                },
                memory_layer_update_params.MemoryLayerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryLayer,
        )

    def list(
        self,
        workspace_id: str,
        *,
        agent_id: str | Omit = omit,
        bundle_key: str | Omit = omit,
        cursor: str | Omit = omit,
        episodic_key_prefix: str | Omit = omit,
        include_info: bool | Omit = omit,
        limit: int | Omit = omit,
        prefix: str | Omit = omit,
        query: str | Omit = omit,
        sort_order: str | Omit = omit,
        type: Literal["MEMORY_LAYER_TYPE_UNSPECIFIED", "MEMORY_LAYER_TYPE_EPISODIC", "MEMORY_LAYER_TYPE_SKILLS"]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPagination[MemoryLayer]:
        """
        Lists all memory layers in the workspace

        Args:
          agent_id: Filter to episodic layers belonging to this agent.

          bundle_key: Filter by bundle_key — return only resources owned by this bundle.

          cursor: Pagination cursor from previous response

          episodic_key_prefix: Filter to episodic layers whose episodic key starts with this prefix (e.g.
              "customer/" matches "customer/42" and "customer/43"). Useful for namespaced
              keys, similar to a redis key scan.

          include_info: When set to true you may use more of your alloted API rate-limit

          limit: Maximum number of results to return

          prefix: Filter expression (query param: prefix)

          query: Free-form search query

          sort_order: Sort order for results (asc or desc by creation time)

          type: Filter by layer type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return self._get_api_list(
            path_template("/v1/workspaces/{workspace_id}/memory_layers", workspace_id=workspace_id),
            page=SyncCursorPagination[MemoryLayer],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "agent_id": agent_id,
                        "bundle_key": bundle_key,
                        "cursor": cursor,
                        "episodic_key_prefix": episodic_key_prefix,
                        "include_info": include_info,
                        "limit": limit,
                        "prefix": prefix,
                        "query": query,
                        "sort_order": sort_order,
                        "type": type,
                    },
                    memory_layer_list_params.MemoryLayerListParams,
                ),
            ),
            model=MemoryLayer,
        )

    def delete(
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
    ) -> None:
        """
        Deletes a memory layer from the workspace

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v1/workspaces/{workspace_id}/memory_layers/{id}", workspace_id=workspace_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncMemoryLayersResource(AsyncAPIResource):
    """Manage memory layers and their entries.

    Layers are named containers that can
     be composed into an objective's memory cascade; entries are the keyed values
     within a layer. System-managed layers (e.g., episodic layers created by the
     runtime) cannot be mutated through this API.
    """

    @cached_property
    def entries(self) -> AsyncEntriesResource:
        """Manage memory layers and their entries.

        Layers are named containers that can
         be composed into an objective's memory cascade; entries are the keyed values
         within a layer. System-managed layers (e.g., episodic layers created by the
         runtime) cannot be mutated through this API.
        """
        return AsyncEntriesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMemoryLayersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cadenya/cadenya-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMemoryLayersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMemoryLayersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cadenya/cadenya-python#with_streaming_response
        """
        return AsyncMemoryLayersResourceWithStreamingResponse(self)

    async def create(
        self,
        workspace_id: str,
        *,
        metadata: CreateResourceMetadata,
        spec: MemoryLayerSpecParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryLayer:
        """
        Creates a new memory layer in the workspace

        Args:
          metadata: CreateResourceMetadata contains the user-provided fields for creating a
              workspace-scoped resource. Read-only fields (id, account_id, workspace_id,
              profile_id, created_at) are excluded since they are set by the server.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return await self._post(
            path_template("/v1/workspaces/{workspace_id}/memory_layers", workspace_id=workspace_id),
            body=await async_maybe_transform(
                {
                    "metadata": metadata,
                    "spec": spec,
                },
                memory_layer_create_params.MemoryLayerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryLayer,
        )

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
    ) -> MemoryLayer:
        """
        Retrieves a memory layer by ID from the workspace

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
            path_template("/v1/workspaces/{workspace_id}/memory_layers/{id}", workspace_id=workspace_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryLayer,
        )

    async def update(
        self,
        id: str,
        *,
        workspace_id: str,
        metadata: UpdateResourceMetadata | Omit = omit,
        spec: MemoryLayerSpecParam | Omit = omit,
        update_mask: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryLayer:
        """
        Updates a memory layer in the workspace

        Args:
          metadata: UpdateResourceMetadata contains the user-provided fields for updating a
              workspace-scoped resource. Read-only fields (id, account_id, workspace_id,
              profile_id, created_at) are excluded since they are set by the server.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/v1/workspaces/{workspace_id}/memory_layers/{id}", workspace_id=workspace_id, id=id),
            body=await async_maybe_transform(
                {
                    "metadata": metadata,
                    "spec": spec,
                    "update_mask": update_mask,
                },
                memory_layer_update_params.MemoryLayerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryLayer,
        )

    def list(
        self,
        workspace_id: str,
        *,
        agent_id: str | Omit = omit,
        bundle_key: str | Omit = omit,
        cursor: str | Omit = omit,
        episodic_key_prefix: str | Omit = omit,
        include_info: bool | Omit = omit,
        limit: int | Omit = omit,
        prefix: str | Omit = omit,
        query: str | Omit = omit,
        sort_order: str | Omit = omit,
        type: Literal["MEMORY_LAYER_TYPE_UNSPECIFIED", "MEMORY_LAYER_TYPE_EPISODIC", "MEMORY_LAYER_TYPE_SKILLS"]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[MemoryLayer, AsyncCursorPagination[MemoryLayer]]:
        """
        Lists all memory layers in the workspace

        Args:
          agent_id: Filter to episodic layers belonging to this agent.

          bundle_key: Filter by bundle_key — return only resources owned by this bundle.

          cursor: Pagination cursor from previous response

          episodic_key_prefix: Filter to episodic layers whose episodic key starts with this prefix (e.g.
              "customer/" matches "customer/42" and "customer/43"). Useful for namespaced
              keys, similar to a redis key scan.

          include_info: When set to true you may use more of your alloted API rate-limit

          limit: Maximum number of results to return

          prefix: Filter expression (query param: prefix)

          query: Free-form search query

          sort_order: Sort order for results (asc or desc by creation time)

          type: Filter by layer type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return self._get_api_list(
            path_template("/v1/workspaces/{workspace_id}/memory_layers", workspace_id=workspace_id),
            page=AsyncCursorPagination[MemoryLayer],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "agent_id": agent_id,
                        "bundle_key": bundle_key,
                        "cursor": cursor,
                        "episodic_key_prefix": episodic_key_prefix,
                        "include_info": include_info,
                        "limit": limit,
                        "prefix": prefix,
                        "query": query,
                        "sort_order": sort_order,
                        "type": type,
                    },
                    memory_layer_list_params.MemoryLayerListParams,
                ),
            ),
            model=MemoryLayer,
        )

    async def delete(
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
    ) -> None:
        """
        Deletes a memory layer from the workspace

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/workspaces/{workspace_id}/memory_layers/{id}", workspace_id=workspace_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class MemoryLayersResourceWithRawResponse:
    def __init__(self, memory_layers: MemoryLayersResource) -> None:
        self._memory_layers = memory_layers

        self.create = to_raw_response_wrapper(
            memory_layers.create,
        )
        self.retrieve = to_raw_response_wrapper(
            memory_layers.retrieve,
        )
        self.update = to_raw_response_wrapper(
            memory_layers.update,
        )
        self.list = to_raw_response_wrapper(
            memory_layers.list,
        )
        self.delete = to_raw_response_wrapper(
            memory_layers.delete,
        )

    @cached_property
    def entries(self) -> EntriesResourceWithRawResponse:
        """Manage memory layers and their entries.

        Layers are named containers that can
         be composed into an objective's memory cascade; entries are the keyed values
         within a layer. System-managed layers (e.g., episodic layers created by the
         runtime) cannot be mutated through this API.
        """
        return EntriesResourceWithRawResponse(self._memory_layers.entries)


class AsyncMemoryLayersResourceWithRawResponse:
    def __init__(self, memory_layers: AsyncMemoryLayersResource) -> None:
        self._memory_layers = memory_layers

        self.create = async_to_raw_response_wrapper(
            memory_layers.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            memory_layers.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            memory_layers.update,
        )
        self.list = async_to_raw_response_wrapper(
            memory_layers.list,
        )
        self.delete = async_to_raw_response_wrapper(
            memory_layers.delete,
        )

    @cached_property
    def entries(self) -> AsyncEntriesResourceWithRawResponse:
        """Manage memory layers and their entries.

        Layers are named containers that can
         be composed into an objective's memory cascade; entries are the keyed values
         within a layer. System-managed layers (e.g., episodic layers created by the
         runtime) cannot be mutated through this API.
        """
        return AsyncEntriesResourceWithRawResponse(self._memory_layers.entries)


class MemoryLayersResourceWithStreamingResponse:
    def __init__(self, memory_layers: MemoryLayersResource) -> None:
        self._memory_layers = memory_layers

        self.create = to_streamed_response_wrapper(
            memory_layers.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            memory_layers.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            memory_layers.update,
        )
        self.list = to_streamed_response_wrapper(
            memory_layers.list,
        )
        self.delete = to_streamed_response_wrapper(
            memory_layers.delete,
        )

    @cached_property
    def entries(self) -> EntriesResourceWithStreamingResponse:
        """Manage memory layers and their entries.

        Layers are named containers that can
         be composed into an objective's memory cascade; entries are the keyed values
         within a layer. System-managed layers (e.g., episodic layers created by the
         runtime) cannot be mutated through this API.
        """
        return EntriesResourceWithStreamingResponse(self._memory_layers.entries)


class AsyncMemoryLayersResourceWithStreamingResponse:
    def __init__(self, memory_layers: AsyncMemoryLayersResource) -> None:
        self._memory_layers = memory_layers

        self.create = async_to_streamed_response_wrapper(
            memory_layers.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            memory_layers.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            memory_layers.update,
        )
        self.list = async_to_streamed_response_wrapper(
            memory_layers.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            memory_layers.delete,
        )

    @cached_property
    def entries(self) -> AsyncEntriesResourceWithStreamingResponse:
        """Manage memory layers and their entries.

        Layers are named containers that can
         be composed into an objective's memory cascade; entries are the keyed values
         within a layer. System-managed layers (e.g., episodic layers created by the
         runtime) cannot be mutated through this API.
        """
        return AsyncEntriesResourceWithStreamingResponse(self._memory_layers.entries)
