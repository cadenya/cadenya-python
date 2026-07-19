# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast
from typing_extensions import Literal, overload

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, required_args, maybe_transform, async_maybe_transform
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
from ...types.agents import (
    variation_list_params,
    variation_create_params,
    variation_update_params,
    variation_add_assignment_params,
    variation_add_memory_layer_params,
    variation_update_memory_layer_params,
)
from ...types.agents.agent_variation import AgentVariation
from ...types.agents.variation_assignment import VariationAssignment
from ...types.agents.agent_variation_spec_param import AgentVariationSpecParam
from ...types.shared_params.create_resource_metadata import CreateResourceMetadata
from ...types.shared_params.update_resource_metadata import UpdateResourceMetadata
from ...types.agents.variation_memory_layer_assignment import VariationMemoryLayerAssignment

__all__ = ["VariationsResource", "AsyncVariationsResource"]


class VariationsResource(SyncAPIResource):
    """
    Manage variations of an agent and their tool, sub-agent, and memory layer assignments.
    """

    @cached_property
    def with_raw_response(self) -> VariationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cadenya/cadenya-python#accessing-raw-response-data-eg-headers
        """
        return VariationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VariationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cadenya/cadenya-python#with_streaming_response
        """
        return VariationsResourceWithStreamingResponse(self)

    def create(
        self,
        agent_id: str,
        *,
        workspace_id: str | None = None,
        metadata: CreateResourceMetadata,
        spec: AgentVariationSpecParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentVariation:
        """
        Creates a new variation for an agent

        Args:
          metadata: CreateResourceMetadata contains the user-provided fields for creating a
              workspace-scoped resource. Read-only fields (id, account_id, workspace_id,
              profile_id, created_at) are excluded since they are set by the server.

          spec: AgentVariationSpec defines the operational configuration for a variation

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
        return self._post(
            path_template(
                "/v1/workspaces/{workspace_id}/agents/{agent_id}/variations",
                workspace_id=workspace_id,
                agent_id=agent_id,
            ),
            body=maybe_transform(
                {
                    "metadata": metadata,
                    "spec": spec,
                },
                variation_create_params.VariationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentVariation,
        )

    def retrieve(
        self,
        agent_id: str,
        id: str,
        *,
        workspace_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentVariation:
        """
        Retrieves a variation by ID from an agent

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
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template(
                "/v1/workspaces/{workspace_id}/agents/{agent_id}/variations/{id}",
                workspace_id=workspace_id,
                agent_id=agent_id,
                id=id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentVariation,
        )

    def update(
        self,
        agent_id: str,
        id: str,
        *,
        workspace_id: str | None = None,
        metadata: UpdateResourceMetadata | Omit = omit,
        spec: AgentVariationSpecParam | Omit = omit,
        update_mask: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentVariation:
        """
        Updates a variation for an agent

        Args:
          metadata: UpdateResourceMetadata contains the user-provided fields for updating a
              workspace-scoped resource. Read-only fields (id, account_id, workspace_id,
              profile_id, created_at) are excluded since they are set by the server.

          spec: AgentVariationSpec defines the operational configuration for a variation

          update_mask: Fields to update

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
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template(
                "/v1/workspaces/{workspace_id}/agents/{agent_id}/variations/{id}",
                workspace_id=workspace_id,
                agent_id=agent_id,
                id=id,
            ),
            body=maybe_transform(
                {
                    "metadata": metadata,
                    "spec": spec,
                    "update_mask": update_mask,
                },
                variation_update_params.VariationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentVariation,
        )

    def list(
        self,
        agent_id: str,
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
    ) -> SyncCursorPagination[AgentVariation]:
        """
        Lists all variations for an agent

        Args:
          cursor: Pagination cursor from previous response

          include_info: When true, the `info` field on each returned variation is populated. Requests
              with this flag count more against your rate limit.

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
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get_api_list(
            path_template(
                "/v1/workspaces/{workspace_id}/agents/{agent_id}/variations",
                workspace_id=workspace_id,
                agent_id=agent_id,
            ),
            page=SyncCursorPagination[AgentVariation],
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
                    variation_list_params.VariationListParams,
                ),
            ),
            model=AgentVariation,
        )

    def delete(
        self,
        agent_id: str,
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
        Deletes a variation from an agent

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
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/v1/workspaces/{workspace_id}/agents/{agent_id}/variations/{id}",
                workspace_id=workspace_id,
                agent_id=agent_id,
                id=id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    @overload
    def add_assignment(
        self,
        agent_id: str,
        variation_id: str,
        *,
        workspace_id: str | None = None,
        tool_id: str,
        type: Literal["toolId"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VariationAssignment:
        """Assigns a tool, tool set, or sub-agent to a variation.

        Exactly one target ID
        must be set.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def add_assignment(
        self,
        agent_id: str,
        variation_id: str,
        *,
        workspace_id: str | None = None,
        tool_set_id: str,
        type: Literal["toolSetId"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VariationAssignment:
        """Assigns a tool, tool set, or sub-agent to a variation.

        Exactly one target ID
        must be set.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def add_assignment(
        self,
        agent_id: str,
        variation_id: str,
        *,
        workspace_id: str | None = None,
        sub_agent_id: str,
        type: Literal["subAgentId"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VariationAssignment:
        """Assigns a tool, tool set, or sub-agent to a variation.

        Exactly one target ID
        must be set.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["tool_id", "type"], ["tool_set_id", "type"], ["sub_agent_id", "type"])
    def add_assignment(
        self,
        agent_id: str,
        variation_id: str,
        *,
        workspace_id: str | None = None,
        tool_id: str | Omit = omit,
        type: Literal["toolId"] | Literal["toolSetId"] | Literal["subAgentId"],
        tool_set_id: str | Omit = omit,
        sub_agent_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VariationAssignment:
        if workspace_id is None:
            workspace_id = self._client._get_workspace_id_path_param()
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not variation_id:
            raise ValueError(f"Expected a non-empty value for `variation_id` but received {variation_id!r}")
        return cast(
            VariationAssignment,
            self._post(
                path_template(
                    "/v1/workspaces/{workspace_id}/agents/{agent_id}/variations/{variation_id}/assignments",
                    workspace_id=workspace_id,
                    agent_id=agent_id,
                    variation_id=variation_id,
                ),
                body=maybe_transform(
                    {
                        "tool_id": tool_id,
                        "type": type,
                        "tool_set_id": tool_set_id,
                        "sub_agent_id": sub_agent_id,
                    },
                    variation_add_assignment_params.VariationAddAssignmentParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, VariationAssignment
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def add_memory_layer(
        self,
        agent_id: str,
        variation_id: str,
        *,
        workspace_id: str | None = None,
        memory_layer_id: str,
        position: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VariationMemoryLayerAssignment:
        """
        Attaches a memory layer to a variation at a given position in the variation's
        baseline memory cascade.

        Args:
          memory_layer_id: Layer to attach. Accepts the canonical `memlyr_…` form or the
              `external_id:<value>` form.

          position: Position in the baseline cascade (lower = more specific). If omitted, the server
              appends at the most general end (max existing position + 1).

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
        if not variation_id:
            raise ValueError(f"Expected a non-empty value for `variation_id` but received {variation_id!r}")
        return self._post(
            path_template(
                "/v1/workspaces/{workspace_id}/agents/{agent_id}/variations/{variation_id}/memory_layer_assignments",
                workspace_id=workspace_id,
                agent_id=agent_id,
                variation_id=variation_id,
            ),
            body=maybe_transform(
                {
                    "memory_layer_id": memory_layer_id,
                    "position": position,
                },
                variation_add_memory_layer_params.VariationAddMemoryLayerParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VariationMemoryLayerAssignment,
        )

    def remove_assignment(
        self,
        agent_id: str,
        variation_id: str,
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
        Detaches an assignment from a variation, identified by the assignment ID
        returned when it was added.

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
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not variation_id:
            raise ValueError(f"Expected a non-empty value for `variation_id` but received {variation_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/v1/workspaces/{workspace_id}/agents/{agent_id}/variations/{variation_id}/assignments/{id}",
                workspace_id=workspace_id,
                agent_id=agent_id,
                variation_id=variation_id,
                id=id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def remove_memory_layer(
        self,
        agent_id: str,
        variation_id: str,
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
        Detaches a memory layer assignment from a variation, identified by the
        assignment id.

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
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not variation_id:
            raise ValueError(f"Expected a non-empty value for `variation_id` but received {variation_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/v1/workspaces/{workspace_id}/agents/{agent_id}/variations/{variation_id}/memory_layer_assignments/{id}",
                workspace_id=workspace_id,
                agent_id=agent_id,
                variation_id=variation_id,
                id=id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def update_memory_layer(
        self,
        agent_id: str,
        variation_id: str,
        id: str,
        *,
        workspace_id: str | None = None,
        position: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VariationMemoryLayerAssignment:
        """
        Updates the position of a memory layer assignment on a variation.

        Args:
          position: New position. Only field currently updatable on an assignment.

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
        if not variation_id:
            raise ValueError(f"Expected a non-empty value for `variation_id` but received {variation_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template(
                "/v1/workspaces/{workspace_id}/agents/{agent_id}/variations/{variation_id}/memory_layer_assignments/{id}",
                workspace_id=workspace_id,
                agent_id=agent_id,
                variation_id=variation_id,
                id=id,
            ),
            body=maybe_transform(
                {"position": position}, variation_update_memory_layer_params.VariationUpdateMemoryLayerParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VariationMemoryLayerAssignment,
        )


class AsyncVariationsResource(AsyncAPIResource):
    """
    Manage variations of an agent and their tool, sub-agent, and memory layer assignments.
    """

    @cached_property
    def with_raw_response(self) -> AsyncVariationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cadenya/cadenya-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVariationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVariationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cadenya/cadenya-python#with_streaming_response
        """
        return AsyncVariationsResourceWithStreamingResponse(self)

    async def create(
        self,
        agent_id: str,
        *,
        workspace_id: str | None = None,
        metadata: CreateResourceMetadata,
        spec: AgentVariationSpecParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentVariation:
        """
        Creates a new variation for an agent

        Args:
          metadata: CreateResourceMetadata contains the user-provided fields for creating a
              workspace-scoped resource. Read-only fields (id, account_id, workspace_id,
              profile_id, created_at) are excluded since they are set by the server.

          spec: AgentVariationSpec defines the operational configuration for a variation

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
        return await self._post(
            path_template(
                "/v1/workspaces/{workspace_id}/agents/{agent_id}/variations",
                workspace_id=workspace_id,
                agent_id=agent_id,
            ),
            body=await async_maybe_transform(
                {
                    "metadata": metadata,
                    "spec": spec,
                },
                variation_create_params.VariationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentVariation,
        )

    async def retrieve(
        self,
        agent_id: str,
        id: str,
        *,
        workspace_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentVariation:
        """
        Retrieves a variation by ID from an agent

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
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template(
                "/v1/workspaces/{workspace_id}/agents/{agent_id}/variations/{id}",
                workspace_id=workspace_id,
                agent_id=agent_id,
                id=id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentVariation,
        )

    async def update(
        self,
        agent_id: str,
        id: str,
        *,
        workspace_id: str | None = None,
        metadata: UpdateResourceMetadata | Omit = omit,
        spec: AgentVariationSpecParam | Omit = omit,
        update_mask: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentVariation:
        """
        Updates a variation for an agent

        Args:
          metadata: UpdateResourceMetadata contains the user-provided fields for updating a
              workspace-scoped resource. Read-only fields (id, account_id, workspace_id,
              profile_id, created_at) are excluded since they are set by the server.

          spec: AgentVariationSpec defines the operational configuration for a variation

          update_mask: Fields to update

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
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template(
                "/v1/workspaces/{workspace_id}/agents/{agent_id}/variations/{id}",
                workspace_id=workspace_id,
                agent_id=agent_id,
                id=id,
            ),
            body=await async_maybe_transform(
                {
                    "metadata": metadata,
                    "spec": spec,
                    "update_mask": update_mask,
                },
                variation_update_params.VariationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentVariation,
        )

    def list(
        self,
        agent_id: str,
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
    ) -> AsyncPaginator[AgentVariation, AsyncCursorPagination[AgentVariation]]:
        """
        Lists all variations for an agent

        Args:
          cursor: Pagination cursor from previous response

          include_info: When true, the `info` field on each returned variation is populated. Requests
              with this flag count more against your rate limit.

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
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get_api_list(
            path_template(
                "/v1/workspaces/{workspace_id}/agents/{agent_id}/variations",
                workspace_id=workspace_id,
                agent_id=agent_id,
            ),
            page=AsyncCursorPagination[AgentVariation],
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
                    variation_list_params.VariationListParams,
                ),
            ),
            model=AgentVariation,
        )

    async def delete(
        self,
        agent_id: str,
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
        Deletes a variation from an agent

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
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/v1/workspaces/{workspace_id}/agents/{agent_id}/variations/{id}",
                workspace_id=workspace_id,
                agent_id=agent_id,
                id=id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    @overload
    async def add_assignment(
        self,
        agent_id: str,
        variation_id: str,
        *,
        workspace_id: str | None = None,
        tool_id: str,
        type: Literal["toolId"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VariationAssignment:
        """Assigns a tool, tool set, or sub-agent to a variation.

        Exactly one target ID
        must be set.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def add_assignment(
        self,
        agent_id: str,
        variation_id: str,
        *,
        workspace_id: str | None = None,
        tool_set_id: str,
        type: Literal["toolSetId"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VariationAssignment:
        """Assigns a tool, tool set, or sub-agent to a variation.

        Exactly one target ID
        must be set.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def add_assignment(
        self,
        agent_id: str,
        variation_id: str,
        *,
        workspace_id: str | None = None,
        sub_agent_id: str,
        type: Literal["subAgentId"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VariationAssignment:
        """Assigns a tool, tool set, or sub-agent to a variation.

        Exactly one target ID
        must be set.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["tool_id", "type"], ["tool_set_id", "type"], ["sub_agent_id", "type"])
    async def add_assignment(
        self,
        agent_id: str,
        variation_id: str,
        *,
        workspace_id: str | None = None,
        tool_id: str | Omit = omit,
        type: Literal["toolId"] | Literal["toolSetId"] | Literal["subAgentId"],
        tool_set_id: str | Omit = omit,
        sub_agent_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VariationAssignment:
        if workspace_id is None:
            workspace_id = self._client._get_workspace_id_path_param()
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not variation_id:
            raise ValueError(f"Expected a non-empty value for `variation_id` but received {variation_id!r}")
        return cast(
            VariationAssignment,
            await self._post(
                path_template(
                    "/v1/workspaces/{workspace_id}/agents/{agent_id}/variations/{variation_id}/assignments",
                    workspace_id=workspace_id,
                    agent_id=agent_id,
                    variation_id=variation_id,
                ),
                body=await async_maybe_transform(
                    {
                        "tool_id": tool_id,
                        "type": type,
                        "tool_set_id": tool_set_id,
                        "sub_agent_id": sub_agent_id,
                    },
                    variation_add_assignment_params.VariationAddAssignmentParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, VariationAssignment
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def add_memory_layer(
        self,
        agent_id: str,
        variation_id: str,
        *,
        workspace_id: str | None = None,
        memory_layer_id: str,
        position: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VariationMemoryLayerAssignment:
        """
        Attaches a memory layer to a variation at a given position in the variation's
        baseline memory cascade.

        Args:
          memory_layer_id: Layer to attach. Accepts the canonical `memlyr_…` form or the
              `external_id:<value>` form.

          position: Position in the baseline cascade (lower = more specific). If omitted, the server
              appends at the most general end (max existing position + 1).

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
        if not variation_id:
            raise ValueError(f"Expected a non-empty value for `variation_id` but received {variation_id!r}")
        return await self._post(
            path_template(
                "/v1/workspaces/{workspace_id}/agents/{agent_id}/variations/{variation_id}/memory_layer_assignments",
                workspace_id=workspace_id,
                agent_id=agent_id,
                variation_id=variation_id,
            ),
            body=await async_maybe_transform(
                {
                    "memory_layer_id": memory_layer_id,
                    "position": position,
                },
                variation_add_memory_layer_params.VariationAddMemoryLayerParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VariationMemoryLayerAssignment,
        )

    async def remove_assignment(
        self,
        agent_id: str,
        variation_id: str,
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
        Detaches an assignment from a variation, identified by the assignment ID
        returned when it was added.

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
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not variation_id:
            raise ValueError(f"Expected a non-empty value for `variation_id` but received {variation_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/v1/workspaces/{workspace_id}/agents/{agent_id}/variations/{variation_id}/assignments/{id}",
                workspace_id=workspace_id,
                agent_id=agent_id,
                variation_id=variation_id,
                id=id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def remove_memory_layer(
        self,
        agent_id: str,
        variation_id: str,
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
        Detaches a memory layer assignment from a variation, identified by the
        assignment id.

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
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not variation_id:
            raise ValueError(f"Expected a non-empty value for `variation_id` but received {variation_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/v1/workspaces/{workspace_id}/agents/{agent_id}/variations/{variation_id}/memory_layer_assignments/{id}",
                workspace_id=workspace_id,
                agent_id=agent_id,
                variation_id=variation_id,
                id=id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def update_memory_layer(
        self,
        agent_id: str,
        variation_id: str,
        id: str,
        *,
        workspace_id: str | None = None,
        position: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VariationMemoryLayerAssignment:
        """
        Updates the position of a memory layer assignment on a variation.

        Args:
          position: New position. Only field currently updatable on an assignment.

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
        if not variation_id:
            raise ValueError(f"Expected a non-empty value for `variation_id` but received {variation_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template(
                "/v1/workspaces/{workspace_id}/agents/{agent_id}/variations/{variation_id}/memory_layer_assignments/{id}",
                workspace_id=workspace_id,
                agent_id=agent_id,
                variation_id=variation_id,
                id=id,
            ),
            body=await async_maybe_transform(
                {"position": position}, variation_update_memory_layer_params.VariationUpdateMemoryLayerParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VariationMemoryLayerAssignment,
        )


class VariationsResourceWithRawResponse:
    def __init__(self, variations: VariationsResource) -> None:
        self._variations = variations

        self.create = to_raw_response_wrapper(
            variations.create,
        )
        self.retrieve = to_raw_response_wrapper(
            variations.retrieve,
        )
        self.update = to_raw_response_wrapper(
            variations.update,
        )
        self.list = to_raw_response_wrapper(
            variations.list,
        )
        self.delete = to_raw_response_wrapper(
            variations.delete,
        )
        self.add_assignment = to_raw_response_wrapper(
            variations.add_assignment,
        )
        self.add_memory_layer = to_raw_response_wrapper(
            variations.add_memory_layer,
        )
        self.remove_assignment = to_raw_response_wrapper(
            variations.remove_assignment,
        )
        self.remove_memory_layer = to_raw_response_wrapper(
            variations.remove_memory_layer,
        )
        self.update_memory_layer = to_raw_response_wrapper(
            variations.update_memory_layer,
        )


class AsyncVariationsResourceWithRawResponse:
    def __init__(self, variations: AsyncVariationsResource) -> None:
        self._variations = variations

        self.create = async_to_raw_response_wrapper(
            variations.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            variations.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            variations.update,
        )
        self.list = async_to_raw_response_wrapper(
            variations.list,
        )
        self.delete = async_to_raw_response_wrapper(
            variations.delete,
        )
        self.add_assignment = async_to_raw_response_wrapper(
            variations.add_assignment,
        )
        self.add_memory_layer = async_to_raw_response_wrapper(
            variations.add_memory_layer,
        )
        self.remove_assignment = async_to_raw_response_wrapper(
            variations.remove_assignment,
        )
        self.remove_memory_layer = async_to_raw_response_wrapper(
            variations.remove_memory_layer,
        )
        self.update_memory_layer = async_to_raw_response_wrapper(
            variations.update_memory_layer,
        )


class VariationsResourceWithStreamingResponse:
    def __init__(self, variations: VariationsResource) -> None:
        self._variations = variations

        self.create = to_streamed_response_wrapper(
            variations.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            variations.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            variations.update,
        )
        self.list = to_streamed_response_wrapper(
            variations.list,
        )
        self.delete = to_streamed_response_wrapper(
            variations.delete,
        )
        self.add_assignment = to_streamed_response_wrapper(
            variations.add_assignment,
        )
        self.add_memory_layer = to_streamed_response_wrapper(
            variations.add_memory_layer,
        )
        self.remove_assignment = to_streamed_response_wrapper(
            variations.remove_assignment,
        )
        self.remove_memory_layer = to_streamed_response_wrapper(
            variations.remove_memory_layer,
        )
        self.update_memory_layer = to_streamed_response_wrapper(
            variations.update_memory_layer,
        )


class AsyncVariationsResourceWithStreamingResponse:
    def __init__(self, variations: AsyncVariationsResource) -> None:
        self._variations = variations

        self.create = async_to_streamed_response_wrapper(
            variations.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            variations.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            variations.update,
        )
        self.list = async_to_streamed_response_wrapper(
            variations.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            variations.delete,
        )
        self.add_assignment = async_to_streamed_response_wrapper(
            variations.add_assignment,
        )
        self.add_memory_layer = async_to_streamed_response_wrapper(
            variations.add_memory_layer,
        )
        self.remove_assignment = async_to_streamed_response_wrapper(
            variations.remove_assignment,
        )
        self.remove_memory_layer = async_to_streamed_response_wrapper(
            variations.remove_memory_layer,
        )
        self.update_memory_layer = async_to_streamed_response_wrapper(
            variations.update_memory_layer,
        )
