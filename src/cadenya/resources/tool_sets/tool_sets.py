# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .tools import (
    ToolsResource,
    AsyncToolsResource,
    ToolsResourceWithRawResponse,
    AsyncToolsResourceWithRawResponse,
    ToolsResourceWithStreamingResponse,
    AsyncToolsResourceWithStreamingResponse,
)
from ...types import (
    tool_set_list_params,
    tool_set_create_params,
    tool_set_update_params,
    tool_set_list_usage_params,
    tool_set_list_events_params,
)
from .secrets import (
    SecretsResource,
    AsyncSecretsResource,
    SecretsResourceWithRawResponse,
    AsyncSecretsResourceWithRawResponse,
    SecretsResourceWithStreamingResponse,
    AsyncSecretsResourceWithStreamingResponse,
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
from ...types.tool_set import ToolSet
from ...types.tool_set_event import ToolSetEvent
from ...types.tool_set_usage import ToolSetUsage
from ...types.tool_set_spec_param import ToolSetSpecParam
from ...types.tool_set_get_openapi_spec_response import ToolSetGetOpenAPISpecResponse
from ...types.shared_params.create_resource_metadata import CreateResourceMetadata
from ...types.shared_params.update_resource_metadata import UpdateResourceMetadata

__all__ = ["ToolSetsResource", "AsyncToolSetsResource"]


class ToolSetsResource(SyncAPIResource):
    """Manage tool sets and the tools they contain.

    Tool sets group related tools,
     and tools define specific capabilities available to agents.

     When a tool set is managed, only API key actors can modify its tools; human
     (profile) actors cannot.
    """

    @cached_property
    def tools(self) -> ToolsResource:
        """Manage tool sets and the tools they contain.

        Tool sets group related tools,
         and tools define specific capabilities available to agents.

         When a tool set is managed, only API key actors can modify its tools; human
         (profile) actors cannot.
        """
        return ToolsResource(self._client)

    @cached_property
    def secrets(self) -> SecretsResource:
        """Manage tool sets and the tools they contain.

        Tool sets group related tools,
         and tools define specific capabilities available to agents.

         When a tool set is managed, only API key actors can modify its tools; human
         (profile) actors cannot.
        """
        return SecretsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ToolSetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cadenya/cadenya-python#accessing-raw-response-data-eg-headers
        """
        return ToolSetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ToolSetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cadenya/cadenya-python#with_streaming_response
        """
        return ToolSetsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        workspace_id: str | None = None,
        metadata: CreateResourceMetadata,
        spec: ToolSetSpecParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolSet:
        """
        Creates a new tool set in the workspace

        Args:
          metadata: CreateResourceMetadata contains the user-provided fields for creating a
              workspace-scoped resource. Read-only fields (id, account_id, workspace_id,
              profile_id, created_at) are excluded since they are set by the server.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if workspace_id is None:
            workspace_id = self._client._get_workspace_id_path_param()
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return self._post(
            path_template("/v1/workspaces/{workspace_id}/tool_sets", workspace_id=workspace_id),
            body=maybe_transform(
                {
                    "metadata": metadata,
                    "spec": spec,
                },
                tool_set_create_params.ToolSetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolSet,
        )

    def retrieve(
        self,
        id: str,
        *,
        workspace_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolSet:
        """
        Retrieves a tool set by ID from the workspace

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if workspace_id is None:
            workspace_id = self._client._get_workspace_id_path_param()
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/v1/workspaces/{workspace_id}/tool_sets/{id}", workspace_id=workspace_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolSet,
        )

    def update(
        self,
        id: str,
        *,
        workspace_id: str | None = None,
        metadata: UpdateResourceMetadata | Omit = omit,
        spec: ToolSetSpecParam | Omit = omit,
        update_mask: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolSet:
        """
        Updates a tool set in the workspace

        Args:
          metadata: UpdateResourceMetadata contains the user-provided fields for updating a
              workspace-scoped resource. Read-only fields (id, account_id, workspace_id,
              profile_id, created_at) are excluded since they are set by the server.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if workspace_id is None:
            workspace_id = self._client._get_workspace_id_path_param()
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/v1/workspaces/{workspace_id}/tool_sets/{id}", workspace_id=workspace_id, id=id),
            body=maybe_transform(
                {
                    "metadata": metadata,
                    "spec": spec,
                    "update_mask": update_mask,
                },
                tool_set_update_params.ToolSetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolSet,
        )

    def list(
        self,
        *,
        workspace_id: str | None = None,
        cursor: str | Omit = omit,
        include_info: bool | Omit = omit,
        labels: str | Omit = omit,
        limit: int | Omit = omit,
        prefix: str | Omit = omit,
        query: str | Omit = omit,
        sort_order: str | Omit = omit,
        state: Literal["STATE_UNSPECIFIED", "STATE_ACTIVE", "STATE_ARCHIVED"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPagination[ToolSet]:
        """
        Lists all tool sets in the workspace

        Args:
          cursor: Pagination cursor from previous response

          include_info: When set to true you may use more of your alloted API rate-limit

          labels: Filters by metadata labels. Comma-separated key=value pairs, e.g.
              "env=prod,team=ai". A resource matches only if every pair matches exactly (AND
              semantics).

          limit: Maximum number of results to return

          prefix: Filter expression (query param: prefix)

          query: Free-form search query

          sort_order: Sort order for results (asc or desc by creation time)

          state: Filter by tool set lifecycle state. Defaults to STATE_ACTIVE when unspecified;
              pass STATE_ARCHIVED to list archived tool sets.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if workspace_id is None:
            workspace_id = self._client._get_workspace_id_path_param()
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return self._get_api_list(
            path_template("/v1/workspaces/{workspace_id}/tool_sets", workspace_id=workspace_id),
            page=SyncCursorPagination[ToolSet],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "include_info": include_info,
                        "labels": labels,
                        "limit": limit,
                        "prefix": prefix,
                        "query": query,
                        "sort_order": sort_order,
                        "state": state,
                    },
                    tool_set_list_params.ToolSetListParams,
                ),
            ),
            model=ToolSet,
        )

    def delete(
        self,
        id: str,
        *,
        workspace_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes a tool set in the workspace

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if workspace_id is None:
            workspace_id = self._client._get_workspace_id_path_param()
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v1/workspaces/{workspace_id}/tool_sets/{id}", workspace_id=workspace_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def archive(
        self,
        id: str,
        *,
        workspace_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolSet:
        """Transitions a tool set to STATE_ARCHIVED.

        Syncing stops, the tool set is hidden
        from list results, its tools are no longer offered to objectives, and new
        variation assignments are rejected. Existing assignments are retained, and
        history is preserved — unlike delete, archiving works while the tool set is
        still assigned to agent variations.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if workspace_id is None:
            workspace_id = self._client._get_workspace_id_path_param()
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/v1/workspaces/{workspace_id}/tool_sets/{id}:archive", workspace_id=workspace_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolSet,
        )

    def get_openapi_spec(
        self,
        tool_set_id: str,
        *,
        workspace_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolSetGetOpenAPISpecResponse:
        """
        Retrieves the current OpenAPI specification JSON that has been consumed by the
        tool set. Only applicable to tool sets using the OpenAPI adapter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if workspace_id is None:
            workspace_id = self._client._get_workspace_id_path_param()
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not tool_set_id:
            raise ValueError(f"Expected a non-empty value for `tool_set_id` but received {tool_set_id!r}")
        return self._get(
            path_template(
                "/v1/workspaces/{workspace_id}/tool_sets/{tool_set_id}/openapi_spec",
                workspace_id=workspace_id,
                tool_set_id=tool_set_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolSetGetOpenAPISpecResponse,
        )

    def list_events(
        self,
        tool_set_id: str,
        *,
        workspace_id: str | None = None,
        cursor: str | Omit = omit,
        include_info: bool | Omit = omit,
        labels: str | Omit = omit,
        limit: int | Omit = omit,
        sort_order: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPagination[ToolSetEvent]:
        """
        Lists all events (including sync status) for a tool set

        Args:
          cursor: Pagination cursor from previous response

          include_info: When set to true you may use more of your alloted API rate-limit

          labels: Filters by metadata labels. Comma-separated key=value pairs, e.g.
              "env=prod,team=ai". A resource matches only if every pair matches exactly (AND
              semantics).

          limit: Maximum number of results to return

          sort_order: Sort order for results (asc or desc by creation time)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if workspace_id is None:
            workspace_id = self._client._get_workspace_id_path_param()
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not tool_set_id:
            raise ValueError(f"Expected a non-empty value for `tool_set_id` but received {tool_set_id!r}")
        return self._get_api_list(
            path_template(
                "/v1/workspaces/{workspace_id}/tool_sets/{tool_set_id}/events",
                workspace_id=workspace_id,
                tool_set_id=tool_set_id,
            ),
            page=SyncCursorPagination[ToolSetEvent],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "include_info": include_info,
                        "labels": labels,
                        "limit": limit,
                        "sort_order": sort_order,
                    },
                    tool_set_list_events_params.ToolSetListEventsParams,
                ),
            ),
            model=ToolSetEvent,
        )

    def list_usage(
        self,
        tool_set_id: str,
        *,
        workspace_id: str | None = None,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        sort_order: str | Omit = omit,
        tool_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPagination[ToolSetUsage]:
        """
        Lists the agent variations (with their parent agent) that have the tool set
        assigned. Pass tool_id to instead list variations with a direct assignment of
        that individual tool; variations that receive the tool implicitly through a
        whole-set assignment are not included in that filtered view.

        Args:
          cursor: Pagination cursor from previous response

          limit: Maximum number of results to return

          sort_order: Sort order for results (asc or desc by assignment creation time)

          tool_id: When set, lists only variations with a direct assignment of this individual
              tool. When unset, lists variations assigned the whole tool set. The tool must
              belong to the tool set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if workspace_id is None:
            workspace_id = self._client._get_workspace_id_path_param()
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not tool_set_id:
            raise ValueError(f"Expected a non-empty value for `tool_set_id` but received {tool_set_id!r}")
        return self._get_api_list(
            path_template(
                "/v1/workspaces/{workspace_id}/tool_sets/{tool_set_id}/usage",
                workspace_id=workspace_id,
                tool_set_id=tool_set_id,
            ),
            page=SyncCursorPagination[ToolSetUsage],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "sort_order": sort_order,
                        "tool_id": tool_id,
                    },
                    tool_set_list_usage_params.ToolSetListUsageParams,
                ),
            ),
            model=ToolSetUsage,
        )

    def unarchive(
        self,
        id: str,
        *,
        workspace_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolSet:
        """Transitions an archived tool set back to STATE_ACTIVE.

        Managed tool sets resume
        syncing on their next cycle and their tools become available to objectives
        again.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if workspace_id is None:
            workspace_id = self._client._get_workspace_id_path_param()
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/v1/workspaces/{workspace_id}/tool_sets/{id}:unarchive", workspace_id=workspace_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolSet,
        )


class AsyncToolSetsResource(AsyncAPIResource):
    """Manage tool sets and the tools they contain.

    Tool sets group related tools,
     and tools define specific capabilities available to agents.

     When a tool set is managed, only API key actors can modify its tools; human
     (profile) actors cannot.
    """

    @cached_property
    def tools(self) -> AsyncToolsResource:
        """Manage tool sets and the tools they contain.

        Tool sets group related tools,
         and tools define specific capabilities available to agents.

         When a tool set is managed, only API key actors can modify its tools; human
         (profile) actors cannot.
        """
        return AsyncToolsResource(self._client)

    @cached_property
    def secrets(self) -> AsyncSecretsResource:
        """Manage tool sets and the tools they contain.

        Tool sets group related tools,
         and tools define specific capabilities available to agents.

         When a tool set is managed, only API key actors can modify its tools; human
         (profile) actors cannot.
        """
        return AsyncSecretsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncToolSetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cadenya/cadenya-python#accessing-raw-response-data-eg-headers
        """
        return AsyncToolSetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncToolSetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cadenya/cadenya-python#with_streaming_response
        """
        return AsyncToolSetsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        workspace_id: str | None = None,
        metadata: CreateResourceMetadata,
        spec: ToolSetSpecParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolSet:
        """
        Creates a new tool set in the workspace

        Args:
          metadata: CreateResourceMetadata contains the user-provided fields for creating a
              workspace-scoped resource. Read-only fields (id, account_id, workspace_id,
              profile_id, created_at) are excluded since they are set by the server.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if workspace_id is None:
            workspace_id = self._client._get_workspace_id_path_param()
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return await self._post(
            path_template("/v1/workspaces/{workspace_id}/tool_sets", workspace_id=workspace_id),
            body=await async_maybe_transform(
                {
                    "metadata": metadata,
                    "spec": spec,
                },
                tool_set_create_params.ToolSetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolSet,
        )

    async def retrieve(
        self,
        id: str,
        *,
        workspace_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolSet:
        """
        Retrieves a tool set by ID from the workspace

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if workspace_id is None:
            workspace_id = self._client._get_workspace_id_path_param()
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/v1/workspaces/{workspace_id}/tool_sets/{id}", workspace_id=workspace_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolSet,
        )

    async def update(
        self,
        id: str,
        *,
        workspace_id: str | None = None,
        metadata: UpdateResourceMetadata | Omit = omit,
        spec: ToolSetSpecParam | Omit = omit,
        update_mask: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolSet:
        """
        Updates a tool set in the workspace

        Args:
          metadata: UpdateResourceMetadata contains the user-provided fields for updating a
              workspace-scoped resource. Read-only fields (id, account_id, workspace_id,
              profile_id, created_at) are excluded since they are set by the server.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if workspace_id is None:
            workspace_id = self._client._get_workspace_id_path_param()
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/v1/workspaces/{workspace_id}/tool_sets/{id}", workspace_id=workspace_id, id=id),
            body=await async_maybe_transform(
                {
                    "metadata": metadata,
                    "spec": spec,
                    "update_mask": update_mask,
                },
                tool_set_update_params.ToolSetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolSet,
        )

    def list(
        self,
        *,
        workspace_id: str | None = None,
        cursor: str | Omit = omit,
        include_info: bool | Omit = omit,
        labels: str | Omit = omit,
        limit: int | Omit = omit,
        prefix: str | Omit = omit,
        query: str | Omit = omit,
        sort_order: str | Omit = omit,
        state: Literal["STATE_UNSPECIFIED", "STATE_ACTIVE", "STATE_ARCHIVED"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ToolSet, AsyncCursorPagination[ToolSet]]:
        """
        Lists all tool sets in the workspace

        Args:
          cursor: Pagination cursor from previous response

          include_info: When set to true you may use more of your alloted API rate-limit

          labels: Filters by metadata labels. Comma-separated key=value pairs, e.g.
              "env=prod,team=ai". A resource matches only if every pair matches exactly (AND
              semantics).

          limit: Maximum number of results to return

          prefix: Filter expression (query param: prefix)

          query: Free-form search query

          sort_order: Sort order for results (asc or desc by creation time)

          state: Filter by tool set lifecycle state. Defaults to STATE_ACTIVE when unspecified;
              pass STATE_ARCHIVED to list archived tool sets.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if workspace_id is None:
            workspace_id = self._client._get_workspace_id_path_param()
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return self._get_api_list(
            path_template("/v1/workspaces/{workspace_id}/tool_sets", workspace_id=workspace_id),
            page=AsyncCursorPagination[ToolSet],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "include_info": include_info,
                        "labels": labels,
                        "limit": limit,
                        "prefix": prefix,
                        "query": query,
                        "sort_order": sort_order,
                        "state": state,
                    },
                    tool_set_list_params.ToolSetListParams,
                ),
            ),
            model=ToolSet,
        )

    async def delete(
        self,
        id: str,
        *,
        workspace_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes a tool set in the workspace

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if workspace_id is None:
            workspace_id = self._client._get_workspace_id_path_param()
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/workspaces/{workspace_id}/tool_sets/{id}", workspace_id=workspace_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def archive(
        self,
        id: str,
        *,
        workspace_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolSet:
        """Transitions a tool set to STATE_ARCHIVED.

        Syncing stops, the tool set is hidden
        from list results, its tools are no longer offered to objectives, and new
        variation assignments are rejected. Existing assignments are retained, and
        history is preserved — unlike delete, archiving works while the tool set is
        still assigned to agent variations.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if workspace_id is None:
            workspace_id = self._client._get_workspace_id_path_param()
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/v1/workspaces/{workspace_id}/tool_sets/{id}:archive", workspace_id=workspace_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolSet,
        )

    async def get_openapi_spec(
        self,
        tool_set_id: str,
        *,
        workspace_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolSetGetOpenAPISpecResponse:
        """
        Retrieves the current OpenAPI specification JSON that has been consumed by the
        tool set. Only applicable to tool sets using the OpenAPI adapter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if workspace_id is None:
            workspace_id = self._client._get_workspace_id_path_param()
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not tool_set_id:
            raise ValueError(f"Expected a non-empty value for `tool_set_id` but received {tool_set_id!r}")
        return await self._get(
            path_template(
                "/v1/workspaces/{workspace_id}/tool_sets/{tool_set_id}/openapi_spec",
                workspace_id=workspace_id,
                tool_set_id=tool_set_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolSetGetOpenAPISpecResponse,
        )

    def list_events(
        self,
        tool_set_id: str,
        *,
        workspace_id: str | None = None,
        cursor: str | Omit = omit,
        include_info: bool | Omit = omit,
        labels: str | Omit = omit,
        limit: int | Omit = omit,
        sort_order: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ToolSetEvent, AsyncCursorPagination[ToolSetEvent]]:
        """
        Lists all events (including sync status) for a tool set

        Args:
          cursor: Pagination cursor from previous response

          include_info: When set to true you may use more of your alloted API rate-limit

          labels: Filters by metadata labels. Comma-separated key=value pairs, e.g.
              "env=prod,team=ai". A resource matches only if every pair matches exactly (AND
              semantics).

          limit: Maximum number of results to return

          sort_order: Sort order for results (asc or desc by creation time)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if workspace_id is None:
            workspace_id = self._client._get_workspace_id_path_param()
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not tool_set_id:
            raise ValueError(f"Expected a non-empty value for `tool_set_id` but received {tool_set_id!r}")
        return self._get_api_list(
            path_template(
                "/v1/workspaces/{workspace_id}/tool_sets/{tool_set_id}/events",
                workspace_id=workspace_id,
                tool_set_id=tool_set_id,
            ),
            page=AsyncCursorPagination[ToolSetEvent],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "include_info": include_info,
                        "labels": labels,
                        "limit": limit,
                        "sort_order": sort_order,
                    },
                    tool_set_list_events_params.ToolSetListEventsParams,
                ),
            ),
            model=ToolSetEvent,
        )

    def list_usage(
        self,
        tool_set_id: str,
        *,
        workspace_id: str | None = None,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        sort_order: str | Omit = omit,
        tool_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ToolSetUsage, AsyncCursorPagination[ToolSetUsage]]:
        """
        Lists the agent variations (with their parent agent) that have the tool set
        assigned. Pass tool_id to instead list variations with a direct assignment of
        that individual tool; variations that receive the tool implicitly through a
        whole-set assignment are not included in that filtered view.

        Args:
          cursor: Pagination cursor from previous response

          limit: Maximum number of results to return

          sort_order: Sort order for results (asc or desc by assignment creation time)

          tool_id: When set, lists only variations with a direct assignment of this individual
              tool. When unset, lists variations assigned the whole tool set. The tool must
              belong to the tool set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if workspace_id is None:
            workspace_id = self._client._get_workspace_id_path_param()
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not tool_set_id:
            raise ValueError(f"Expected a non-empty value for `tool_set_id` but received {tool_set_id!r}")
        return self._get_api_list(
            path_template(
                "/v1/workspaces/{workspace_id}/tool_sets/{tool_set_id}/usage",
                workspace_id=workspace_id,
                tool_set_id=tool_set_id,
            ),
            page=AsyncCursorPagination[ToolSetUsage],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "sort_order": sort_order,
                        "tool_id": tool_id,
                    },
                    tool_set_list_usage_params.ToolSetListUsageParams,
                ),
            ),
            model=ToolSetUsage,
        )

    async def unarchive(
        self,
        id: str,
        *,
        workspace_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolSet:
        """Transitions an archived tool set back to STATE_ACTIVE.

        Managed tool sets resume
        syncing on their next cycle and their tools become available to objectives
        again.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if workspace_id is None:
            workspace_id = self._client._get_workspace_id_path_param()
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/v1/workspaces/{workspace_id}/tool_sets/{id}:unarchive", workspace_id=workspace_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolSet,
        )


class ToolSetsResourceWithRawResponse:
    def __init__(self, tool_sets: ToolSetsResource) -> None:
        self._tool_sets = tool_sets

        self.create = to_raw_response_wrapper(
            tool_sets.create,
        )
        self.retrieve = to_raw_response_wrapper(
            tool_sets.retrieve,
        )
        self.update = to_raw_response_wrapper(
            tool_sets.update,
        )
        self.list = to_raw_response_wrapper(
            tool_sets.list,
        )
        self.delete = to_raw_response_wrapper(
            tool_sets.delete,
        )
        self.archive = to_raw_response_wrapper(
            tool_sets.archive,
        )
        self.get_openapi_spec = to_raw_response_wrapper(
            tool_sets.get_openapi_spec,
        )
        self.list_events = to_raw_response_wrapper(
            tool_sets.list_events,
        )
        self.list_usage = to_raw_response_wrapper(
            tool_sets.list_usage,
        )
        self.unarchive = to_raw_response_wrapper(
            tool_sets.unarchive,
        )

    @cached_property
    def tools(self) -> ToolsResourceWithRawResponse:
        """Manage tool sets and the tools they contain.

        Tool sets group related tools,
         and tools define specific capabilities available to agents.

         When a tool set is managed, only API key actors can modify its tools; human
         (profile) actors cannot.
        """
        return ToolsResourceWithRawResponse(self._tool_sets.tools)

    @cached_property
    def secrets(self) -> SecretsResourceWithRawResponse:
        """Manage tool sets and the tools they contain.

        Tool sets group related tools,
         and tools define specific capabilities available to agents.

         When a tool set is managed, only API key actors can modify its tools; human
         (profile) actors cannot.
        """
        return SecretsResourceWithRawResponse(self._tool_sets.secrets)


class AsyncToolSetsResourceWithRawResponse:
    def __init__(self, tool_sets: AsyncToolSetsResource) -> None:
        self._tool_sets = tool_sets

        self.create = async_to_raw_response_wrapper(
            tool_sets.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            tool_sets.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            tool_sets.update,
        )
        self.list = async_to_raw_response_wrapper(
            tool_sets.list,
        )
        self.delete = async_to_raw_response_wrapper(
            tool_sets.delete,
        )
        self.archive = async_to_raw_response_wrapper(
            tool_sets.archive,
        )
        self.get_openapi_spec = async_to_raw_response_wrapper(
            tool_sets.get_openapi_spec,
        )
        self.list_events = async_to_raw_response_wrapper(
            tool_sets.list_events,
        )
        self.list_usage = async_to_raw_response_wrapper(
            tool_sets.list_usage,
        )
        self.unarchive = async_to_raw_response_wrapper(
            tool_sets.unarchive,
        )

    @cached_property
    def tools(self) -> AsyncToolsResourceWithRawResponse:
        """Manage tool sets and the tools they contain.

        Tool sets group related tools,
         and tools define specific capabilities available to agents.

         When a tool set is managed, only API key actors can modify its tools; human
         (profile) actors cannot.
        """
        return AsyncToolsResourceWithRawResponse(self._tool_sets.tools)

    @cached_property
    def secrets(self) -> AsyncSecretsResourceWithRawResponse:
        """Manage tool sets and the tools they contain.

        Tool sets group related tools,
         and tools define specific capabilities available to agents.

         When a tool set is managed, only API key actors can modify its tools; human
         (profile) actors cannot.
        """
        return AsyncSecretsResourceWithRawResponse(self._tool_sets.secrets)


class ToolSetsResourceWithStreamingResponse:
    def __init__(self, tool_sets: ToolSetsResource) -> None:
        self._tool_sets = tool_sets

        self.create = to_streamed_response_wrapper(
            tool_sets.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            tool_sets.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            tool_sets.update,
        )
        self.list = to_streamed_response_wrapper(
            tool_sets.list,
        )
        self.delete = to_streamed_response_wrapper(
            tool_sets.delete,
        )
        self.archive = to_streamed_response_wrapper(
            tool_sets.archive,
        )
        self.get_openapi_spec = to_streamed_response_wrapper(
            tool_sets.get_openapi_spec,
        )
        self.list_events = to_streamed_response_wrapper(
            tool_sets.list_events,
        )
        self.list_usage = to_streamed_response_wrapper(
            tool_sets.list_usage,
        )
        self.unarchive = to_streamed_response_wrapper(
            tool_sets.unarchive,
        )

    @cached_property
    def tools(self) -> ToolsResourceWithStreamingResponse:
        """Manage tool sets and the tools they contain.

        Tool sets group related tools,
         and tools define specific capabilities available to agents.

         When a tool set is managed, only API key actors can modify its tools; human
         (profile) actors cannot.
        """
        return ToolsResourceWithStreamingResponse(self._tool_sets.tools)

    @cached_property
    def secrets(self) -> SecretsResourceWithStreamingResponse:
        """Manage tool sets and the tools they contain.

        Tool sets group related tools,
         and tools define specific capabilities available to agents.

         When a tool set is managed, only API key actors can modify its tools; human
         (profile) actors cannot.
        """
        return SecretsResourceWithStreamingResponse(self._tool_sets.secrets)


class AsyncToolSetsResourceWithStreamingResponse:
    def __init__(self, tool_sets: AsyncToolSetsResource) -> None:
        self._tool_sets = tool_sets

        self.create = async_to_streamed_response_wrapper(
            tool_sets.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            tool_sets.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            tool_sets.update,
        )
        self.list = async_to_streamed_response_wrapper(
            tool_sets.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            tool_sets.delete,
        )
        self.archive = async_to_streamed_response_wrapper(
            tool_sets.archive,
        )
        self.get_openapi_spec = async_to_streamed_response_wrapper(
            tool_sets.get_openapi_spec,
        )
        self.list_events = async_to_streamed_response_wrapper(
            tool_sets.list_events,
        )
        self.list_usage = async_to_streamed_response_wrapper(
            tool_sets.list_usage,
        )
        self.unarchive = async_to_streamed_response_wrapper(
            tool_sets.unarchive,
        )

    @cached_property
    def tools(self) -> AsyncToolsResourceWithStreamingResponse:
        """Manage tool sets and the tools they contain.

        Tool sets group related tools,
         and tools define specific capabilities available to agents.

         When a tool set is managed, only API key actors can modify its tools; human
         (profile) actors cannot.
        """
        return AsyncToolsResourceWithStreamingResponse(self._tool_sets.tools)

    @cached_property
    def secrets(self) -> AsyncSecretsResourceWithStreamingResponse:
        """Manage tool sets and the tools they contain.

        Tool sets group related tools,
         and tools define specific capabilities available to agents.

         When a tool set is managed, only API key actors can modify its tools; human
         (profile) actors cannot.
        """
        return AsyncSecretsResourceWithStreamingResponse(self._tool_sets.secrets)
