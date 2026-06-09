# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...types import agent_list_params, agent_create_params, agent_update_params
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from .feedback import (
    FeedbackResource,
    AsyncFeedbackResource,
    FeedbackResourceWithRawResponse,
    AsyncFeedbackResourceWithRawResponse,
    FeedbackResourceWithStreamingResponse,
    AsyncFeedbackResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .schedules import (
    SchedulesResource,
    AsyncSchedulesResource,
    SchedulesResourceWithRawResponse,
    AsyncSchedulesResourceWithRawResponse,
    SchedulesResourceWithStreamingResponse,
    AsyncSchedulesResourceWithStreamingResponse,
)
from .variations import (
    VariationsResource,
    AsyncVariationsResource,
    VariationsResourceWithRawResponse,
    AsyncVariationsResourceWithRawResponse,
    VariationsResourceWithStreamingResponse,
    AsyncVariationsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncCursorPagination, AsyncCursorPagination
from ...types.agent import Agent
from ..._base_client import AsyncPaginator, make_request_options
from .webhook_deliveries import (
    WebhookDeliveriesResource,
    AsyncWebhookDeliveriesResource,
    WebhookDeliveriesResourceWithRawResponse,
    AsyncWebhookDeliveriesResourceWithRawResponse,
    WebhookDeliveriesResourceWithStreamingResponse,
    AsyncWebhookDeliveriesResourceWithStreamingResponse,
)
from ...types.agent_spec_param import AgentSpecParam
from ...types.shared_params.create_resource_metadata import CreateResourceMetadata
from ...types.shared_params.update_resource_metadata import UpdateResourceMetadata

__all__ = ["AgentsResource", "AsyncAgentsResource"]


class AgentsResource(SyncAPIResource):
    """Manage AI agents within a workspace. Agents define AI behavior and tool access."""

    @cached_property
    def feedback(self) -> FeedbackResource:
        """Manage AI agents within a workspace. Agents define AI behavior and tool access."""
        return FeedbackResource(self._client)

    @cached_property
    def webhook_deliveries(self) -> WebhookDeliveriesResource:
        """Manage AI agents within a workspace. Agents define AI behavior and tool access."""
        return WebhookDeliveriesResource(self._client)

    @cached_property
    def variations(self) -> VariationsResource:
        """
        Manage variations of an agent and their tool, sub-agent, and memory layer assignments.
        """
        return VariationsResource(self._client)

    @cached_property
    def schedules(self) -> SchedulesResource:
        """Manage recurring schedules attached to agents.

        Schedules trigger objectives
         on a cadence defined by AgentScheduleSpec.Schedule.
        """
        return SchedulesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cadenya/cadenya-python#accessing-raw-response-data-eg-headers
        """
        return AgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cadenya/cadenya-python#with_streaming_response
        """
        return AgentsResourceWithStreamingResponse(self)

    def create(
        self,
        workspace_id: str,
        *,
        metadata: CreateResourceMetadata,
        spec: AgentSpecParam,
        default_variation: agent_create_params.DefaultVariation | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Agent:
        """
        Creates a new agent in the workspace

        Args:
          metadata: CreateResourceMetadata contains the user-provided fields for creating a
              workspace-scoped resource. Read-only fields (id, account_id, workspace_id,
              profile_id, created_at) are excluded since they are set by the server.

          spec: Agent specification (user-provided configuration)

          default_variation: Create agent variation request

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return self._post(
            path_template("/v1/workspaces/{workspace_id}/agents", workspace_id=workspace_id),
            body=maybe_transform(
                {
                    "metadata": metadata,
                    "spec": spec,
                    "default_variation": default_variation,
                },
                agent_create_params.AgentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Agent,
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
    ) -> Agent:
        """
        Retrieves an agent by ID from the workspace

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
            path_template("/v1/workspaces/{workspace_id}/agents/{id}", workspace_id=workspace_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Agent,
        )

    def update(
        self,
        id: str,
        *,
        workspace_id: str,
        metadata: UpdateResourceMetadata | Omit = omit,
        spec: AgentSpecParam | Omit = omit,
        update_mask: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Agent:
        """
        Updates an agent in the workspace

        Args:
          metadata: UpdateResourceMetadata contains the user-provided fields for updating a
              workspace-scoped resource. Read-only fields (id, account_id, workspace_id,
              profile_id, created_at) are excluded since they are set by the server.

          spec: Agent specification (user-provided configuration)

          update_mask: Fields to update

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
            path_template("/v1/workspaces/{workspace_id}/agents/{id}", workspace_id=workspace_id, id=id),
            body=maybe_transform(
                {
                    "metadata": metadata,
                    "spec": spec,
                    "update_mask": update_mask,
                },
                agent_update_params.AgentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Agent,
        )

    def list(
        self,
        workspace_id: str,
        *,
        bundle_key: str | Omit = omit,
        cursor: str | Omit = omit,
        include_info: bool | Omit = omit,
        limit: int | Omit = omit,
        prefix: str | Omit = omit,
        query: str | Omit = omit,
        sort_order: str | Omit = omit,
        state: Literal["STATE_UNSPECIFIED", "STATE_DRAFT", "STATE_PUBLISHED", "STATE_ARCHIVED"] | Omit = omit,
        variation_selection_mode: Literal[
            "VARIATION_SELECTION_MODE_UNSPECIFIED",
            "VARIATION_SELECTION_MODE_RANDOM",
            "VARIATION_SELECTION_MODE_WEIGHTED",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPagination[Agent]:
        """
        Lists all agents in the workspace

        Args:
          bundle_key: Filter by bundle_key — return only resources owned by this bundle.

          cursor: Pagination cursor from previous response

          include_info: When true, the `info` field on each returned agent is populated. Requests with
              this flag count more against your rate limit.

          limit: Maximum number of results to return

          prefix: Filter expression (query param: prefix)

          query: Free-form search query

          sort_order: Sort order for results (asc or desc by creation time)

          state: Filter by agent lifecycle state

          variation_selection_mode: Filter by variation selection mode

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return self._get_api_list(
            path_template("/v1/workspaces/{workspace_id}/agents", workspace_id=workspace_id),
            page=SyncCursorPagination[Agent],
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
                        "state": state,
                        "variation_selection_mode": variation_selection_mode,
                    },
                    agent_list_params.AgentListParams,
                ),
            ),
            model=Agent,
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
        Deletes an agent from the workspace

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
            path_template("/v1/workspaces/{workspace_id}/agents/{id}", workspace_id=workspace_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def archive(
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
    ) -> Agent:
        """Transitions an agent to STATE_ARCHIVED.

        Archived agents are hidden from list
        results and cannot be used for objectives; active schedules are paused.

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
        return self._post(
            path_template("/v1/workspaces/{workspace_id}/agents/{id}:archive", workspace_id=workspace_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Agent,
        )

    def publish(
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
    ) -> Agent:
        """Transitions an agent to STATE_PUBLISHED, making it available for objectives.

        The
        agent must have at least one variation.

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
        return self._post(
            path_template("/v1/workspaces/{workspace_id}/agents/{id}:publish", workspace_id=workspace_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Agent,
        )

    def unarchive(
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
    ) -> Agent:
        """Transitions an archived agent back to STATE_DRAFT.

        Publish the agent again to
        make it available for objectives.

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
        return self._post(
            path_template("/v1/workspaces/{workspace_id}/agents/{id}:unarchive", workspace_id=workspace_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Agent,
        )

    def unpublish(
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
    ) -> Agent:
        """Transitions a published agent back to STATE_DRAFT.

        Active schedules for the
        agent are paused until it is published again.

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
        return self._post(
            path_template("/v1/workspaces/{workspace_id}/agents/{id}:unpublish", workspace_id=workspace_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Agent,
        )


class AsyncAgentsResource(AsyncAPIResource):
    """Manage AI agents within a workspace. Agents define AI behavior and tool access."""

    @cached_property
    def feedback(self) -> AsyncFeedbackResource:
        """Manage AI agents within a workspace. Agents define AI behavior and tool access."""
        return AsyncFeedbackResource(self._client)

    @cached_property
    def webhook_deliveries(self) -> AsyncWebhookDeliveriesResource:
        """Manage AI agents within a workspace. Agents define AI behavior and tool access."""
        return AsyncWebhookDeliveriesResource(self._client)

    @cached_property
    def variations(self) -> AsyncVariationsResource:
        """
        Manage variations of an agent and their tool, sub-agent, and memory layer assignments.
        """
        return AsyncVariationsResource(self._client)

    @cached_property
    def schedules(self) -> AsyncSchedulesResource:
        """Manage recurring schedules attached to agents.

        Schedules trigger objectives
         on a cadence defined by AgentScheduleSpec.Schedule.
        """
        return AsyncSchedulesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cadenya/cadenya-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cadenya/cadenya-python#with_streaming_response
        """
        return AsyncAgentsResourceWithStreamingResponse(self)

    async def create(
        self,
        workspace_id: str,
        *,
        metadata: CreateResourceMetadata,
        spec: AgentSpecParam,
        default_variation: agent_create_params.DefaultVariation | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Agent:
        """
        Creates a new agent in the workspace

        Args:
          metadata: CreateResourceMetadata contains the user-provided fields for creating a
              workspace-scoped resource. Read-only fields (id, account_id, workspace_id,
              profile_id, created_at) are excluded since they are set by the server.

          spec: Agent specification (user-provided configuration)

          default_variation: Create agent variation request

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return await self._post(
            path_template("/v1/workspaces/{workspace_id}/agents", workspace_id=workspace_id),
            body=await async_maybe_transform(
                {
                    "metadata": metadata,
                    "spec": spec,
                    "default_variation": default_variation,
                },
                agent_create_params.AgentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Agent,
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
    ) -> Agent:
        """
        Retrieves an agent by ID from the workspace

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
            path_template("/v1/workspaces/{workspace_id}/agents/{id}", workspace_id=workspace_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Agent,
        )

    async def update(
        self,
        id: str,
        *,
        workspace_id: str,
        metadata: UpdateResourceMetadata | Omit = omit,
        spec: AgentSpecParam | Omit = omit,
        update_mask: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Agent:
        """
        Updates an agent in the workspace

        Args:
          metadata: UpdateResourceMetadata contains the user-provided fields for updating a
              workspace-scoped resource. Read-only fields (id, account_id, workspace_id,
              profile_id, created_at) are excluded since they are set by the server.

          spec: Agent specification (user-provided configuration)

          update_mask: Fields to update

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
            path_template("/v1/workspaces/{workspace_id}/agents/{id}", workspace_id=workspace_id, id=id),
            body=await async_maybe_transform(
                {
                    "metadata": metadata,
                    "spec": spec,
                    "update_mask": update_mask,
                },
                agent_update_params.AgentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Agent,
        )

    def list(
        self,
        workspace_id: str,
        *,
        bundle_key: str | Omit = omit,
        cursor: str | Omit = omit,
        include_info: bool | Omit = omit,
        limit: int | Omit = omit,
        prefix: str | Omit = omit,
        query: str | Omit = omit,
        sort_order: str | Omit = omit,
        state: Literal["STATE_UNSPECIFIED", "STATE_DRAFT", "STATE_PUBLISHED", "STATE_ARCHIVED"] | Omit = omit,
        variation_selection_mode: Literal[
            "VARIATION_SELECTION_MODE_UNSPECIFIED",
            "VARIATION_SELECTION_MODE_RANDOM",
            "VARIATION_SELECTION_MODE_WEIGHTED",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Agent, AsyncCursorPagination[Agent]]:
        """
        Lists all agents in the workspace

        Args:
          bundle_key: Filter by bundle_key — return only resources owned by this bundle.

          cursor: Pagination cursor from previous response

          include_info: When true, the `info` field on each returned agent is populated. Requests with
              this flag count more against your rate limit.

          limit: Maximum number of results to return

          prefix: Filter expression (query param: prefix)

          query: Free-form search query

          sort_order: Sort order for results (asc or desc by creation time)

          state: Filter by agent lifecycle state

          variation_selection_mode: Filter by variation selection mode

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return self._get_api_list(
            path_template("/v1/workspaces/{workspace_id}/agents", workspace_id=workspace_id),
            page=AsyncCursorPagination[Agent],
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
                        "state": state,
                        "variation_selection_mode": variation_selection_mode,
                    },
                    agent_list_params.AgentListParams,
                ),
            ),
            model=Agent,
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
        Deletes an agent from the workspace

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
            path_template("/v1/workspaces/{workspace_id}/agents/{id}", workspace_id=workspace_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def archive(
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
    ) -> Agent:
        """Transitions an agent to STATE_ARCHIVED.

        Archived agents are hidden from list
        results and cannot be used for objectives; active schedules are paused.

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
        return await self._post(
            path_template("/v1/workspaces/{workspace_id}/agents/{id}:archive", workspace_id=workspace_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Agent,
        )

    async def publish(
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
    ) -> Agent:
        """Transitions an agent to STATE_PUBLISHED, making it available for objectives.

        The
        agent must have at least one variation.

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
        return await self._post(
            path_template("/v1/workspaces/{workspace_id}/agents/{id}:publish", workspace_id=workspace_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Agent,
        )

    async def unarchive(
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
    ) -> Agent:
        """Transitions an archived agent back to STATE_DRAFT.

        Publish the agent again to
        make it available for objectives.

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
        return await self._post(
            path_template("/v1/workspaces/{workspace_id}/agents/{id}:unarchive", workspace_id=workspace_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Agent,
        )

    async def unpublish(
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
    ) -> Agent:
        """Transitions a published agent back to STATE_DRAFT.

        Active schedules for the
        agent are paused until it is published again.

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
        return await self._post(
            path_template("/v1/workspaces/{workspace_id}/agents/{id}:unpublish", workspace_id=workspace_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Agent,
        )


class AgentsResourceWithRawResponse:
    def __init__(self, agents: AgentsResource) -> None:
        self._agents = agents

        self.create = to_raw_response_wrapper(
            agents.create,
        )
        self.retrieve = to_raw_response_wrapper(
            agents.retrieve,
        )
        self.update = to_raw_response_wrapper(
            agents.update,
        )
        self.list = to_raw_response_wrapper(
            agents.list,
        )
        self.delete = to_raw_response_wrapper(
            agents.delete,
        )
        self.archive = to_raw_response_wrapper(
            agents.archive,
        )
        self.publish = to_raw_response_wrapper(
            agents.publish,
        )
        self.unarchive = to_raw_response_wrapper(
            agents.unarchive,
        )
        self.unpublish = to_raw_response_wrapper(
            agents.unpublish,
        )

    @cached_property
    def feedback(self) -> FeedbackResourceWithRawResponse:
        """Manage AI agents within a workspace. Agents define AI behavior and tool access."""
        return FeedbackResourceWithRawResponse(self._agents.feedback)

    @cached_property
    def webhook_deliveries(self) -> WebhookDeliveriesResourceWithRawResponse:
        """Manage AI agents within a workspace. Agents define AI behavior and tool access."""
        return WebhookDeliveriesResourceWithRawResponse(self._agents.webhook_deliveries)

    @cached_property
    def variations(self) -> VariationsResourceWithRawResponse:
        """
        Manage variations of an agent and their tool, sub-agent, and memory layer assignments.
        """
        return VariationsResourceWithRawResponse(self._agents.variations)

    @cached_property
    def schedules(self) -> SchedulesResourceWithRawResponse:
        """Manage recurring schedules attached to agents.

        Schedules trigger objectives
         on a cadence defined by AgentScheduleSpec.Schedule.
        """
        return SchedulesResourceWithRawResponse(self._agents.schedules)


class AsyncAgentsResourceWithRawResponse:
    def __init__(self, agents: AsyncAgentsResource) -> None:
        self._agents = agents

        self.create = async_to_raw_response_wrapper(
            agents.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            agents.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            agents.update,
        )
        self.list = async_to_raw_response_wrapper(
            agents.list,
        )
        self.delete = async_to_raw_response_wrapper(
            agents.delete,
        )
        self.archive = async_to_raw_response_wrapper(
            agents.archive,
        )
        self.publish = async_to_raw_response_wrapper(
            agents.publish,
        )
        self.unarchive = async_to_raw_response_wrapper(
            agents.unarchive,
        )
        self.unpublish = async_to_raw_response_wrapper(
            agents.unpublish,
        )

    @cached_property
    def feedback(self) -> AsyncFeedbackResourceWithRawResponse:
        """Manage AI agents within a workspace. Agents define AI behavior and tool access."""
        return AsyncFeedbackResourceWithRawResponse(self._agents.feedback)

    @cached_property
    def webhook_deliveries(self) -> AsyncWebhookDeliveriesResourceWithRawResponse:
        """Manage AI agents within a workspace. Agents define AI behavior and tool access."""
        return AsyncWebhookDeliveriesResourceWithRawResponse(self._agents.webhook_deliveries)

    @cached_property
    def variations(self) -> AsyncVariationsResourceWithRawResponse:
        """
        Manage variations of an agent and their tool, sub-agent, and memory layer assignments.
        """
        return AsyncVariationsResourceWithRawResponse(self._agents.variations)

    @cached_property
    def schedules(self) -> AsyncSchedulesResourceWithRawResponse:
        """Manage recurring schedules attached to agents.

        Schedules trigger objectives
         on a cadence defined by AgentScheduleSpec.Schedule.
        """
        return AsyncSchedulesResourceWithRawResponse(self._agents.schedules)


class AgentsResourceWithStreamingResponse:
    def __init__(self, agents: AgentsResource) -> None:
        self._agents = agents

        self.create = to_streamed_response_wrapper(
            agents.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            agents.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            agents.update,
        )
        self.list = to_streamed_response_wrapper(
            agents.list,
        )
        self.delete = to_streamed_response_wrapper(
            agents.delete,
        )
        self.archive = to_streamed_response_wrapper(
            agents.archive,
        )
        self.publish = to_streamed_response_wrapper(
            agents.publish,
        )
        self.unarchive = to_streamed_response_wrapper(
            agents.unarchive,
        )
        self.unpublish = to_streamed_response_wrapper(
            agents.unpublish,
        )

    @cached_property
    def feedback(self) -> FeedbackResourceWithStreamingResponse:
        """Manage AI agents within a workspace. Agents define AI behavior and tool access."""
        return FeedbackResourceWithStreamingResponse(self._agents.feedback)

    @cached_property
    def webhook_deliveries(self) -> WebhookDeliveriesResourceWithStreamingResponse:
        """Manage AI agents within a workspace. Agents define AI behavior and tool access."""
        return WebhookDeliveriesResourceWithStreamingResponse(self._agents.webhook_deliveries)

    @cached_property
    def variations(self) -> VariationsResourceWithStreamingResponse:
        """
        Manage variations of an agent and their tool, sub-agent, and memory layer assignments.
        """
        return VariationsResourceWithStreamingResponse(self._agents.variations)

    @cached_property
    def schedules(self) -> SchedulesResourceWithStreamingResponse:
        """Manage recurring schedules attached to agents.

        Schedules trigger objectives
         on a cadence defined by AgentScheduleSpec.Schedule.
        """
        return SchedulesResourceWithStreamingResponse(self._agents.schedules)


class AsyncAgentsResourceWithStreamingResponse:
    def __init__(self, agents: AsyncAgentsResource) -> None:
        self._agents = agents

        self.create = async_to_streamed_response_wrapper(
            agents.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            agents.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            agents.update,
        )
        self.list = async_to_streamed_response_wrapper(
            agents.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            agents.delete,
        )
        self.archive = async_to_streamed_response_wrapper(
            agents.archive,
        )
        self.publish = async_to_streamed_response_wrapper(
            agents.publish,
        )
        self.unarchive = async_to_streamed_response_wrapper(
            agents.unarchive,
        )
        self.unpublish = async_to_streamed_response_wrapper(
            agents.unpublish,
        )

    @cached_property
    def feedback(self) -> AsyncFeedbackResourceWithStreamingResponse:
        """Manage AI agents within a workspace. Agents define AI behavior and tool access."""
        return AsyncFeedbackResourceWithStreamingResponse(self._agents.feedback)

    @cached_property
    def webhook_deliveries(self) -> AsyncWebhookDeliveriesResourceWithStreamingResponse:
        """Manage AI agents within a workspace. Agents define AI behavior and tool access."""
        return AsyncWebhookDeliveriesResourceWithStreamingResponse(self._agents.webhook_deliveries)

    @cached_property
    def variations(self) -> AsyncVariationsResourceWithStreamingResponse:
        """
        Manage variations of an agent and their tool, sub-agent, and memory layer assignments.
        """
        return AsyncVariationsResourceWithStreamingResponse(self._agents.variations)

    @cached_property
    def schedules(self) -> AsyncSchedulesResourceWithStreamingResponse:
        """Manage recurring schedules attached to agents.

        Schedules trigger objectives
         on a cadence defined by AgentScheduleSpec.Schedule.
        """
        return AsyncSchedulesResourceWithStreamingResponse(self._agents.schedules)
