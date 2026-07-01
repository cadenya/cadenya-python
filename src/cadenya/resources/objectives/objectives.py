# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal

import httpx

from .tasks import (
    TasksResource,
    AsyncTasksResource,
    TasksResourceWithRawResponse,
    AsyncTasksResourceWithRawResponse,
    TasksResourceWithStreamingResponse,
    AsyncTasksResourceWithStreamingResponse,
)
from .tools import (
    ToolsResource,
    AsyncToolsResource,
    ToolsResourceWithRawResponse,
    AsyncToolsResourceWithRawResponse,
    ToolsResourceWithStreamingResponse,
    AsyncToolsResourceWithStreamingResponse,
)
from ...types import (
    objective_list_params,
    objective_cancel_params,
    objective_create_params,
    objective_compact_params,
    objective_continue_params,
    objective_list_events_params,
    objective_list_context_windows_params,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from .tool_calls import (
    ToolCallsResource,
    AsyncToolCallsResource,
    ToolCallsResourceWithRawResponse,
    AsyncToolCallsResourceWithRawResponse,
    ToolCallsResourceWithStreamingResponse,
    AsyncToolCallsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._streaming import Stream, AsyncStream
from ...pagination import SyncCursorPagination, AsyncCursorPagination
from ..._base_client import AsyncPaginator, make_request_options
from ...types.objective import Objective
from ...types.objective_event import ObjectiveEvent
from ...types.memory_reference_param import MemoryReferenceParam
from ...types.objective_context_window import ObjectiveContextWindow
from ...types.objective_compact_response import ObjectiveCompactResponse
from ...types.shared_params.create_operation_metadata import CreateOperationMetadata
from ...types.agents.agent_variation_spec_compaction_config_param import AgentVariationSpecCompactionConfigParam

__all__ = ["ObjectivesResource", "AsyncObjectivesResource"]


class ObjectivesResource(SyncAPIResource):
    @cached_property
    def tools(self) -> ToolsResource:
        return ToolsResource(self._client)

    @cached_property
    def tool_calls(self) -> ToolCallsResource:
        return ToolCallsResource(self._client)

    @cached_property
    def tasks(self) -> TasksResource:
        return TasksResource(self._client)

    @cached_property
    def feedback(self) -> FeedbackResource:
        return FeedbackResource(self._client)

    @cached_property
    def with_raw_response(self) -> ObjectivesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cadenya/cadenya-python#accessing-raw-response-data-eg-headers
        """
        return ObjectivesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ObjectivesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cadenya/cadenya-python#with_streaming_response
        """
        return ObjectivesResourceWithStreamingResponse(self)

    def create(
        self,
        workspace_id: str,
        *,
        agent_id: str,
        data: Dict[str, object],
        episodic_memory: objective_create_params.EpisodicMemory | Omit = omit,
        initial_message: str | Omit = omit,
        memory_cascade: Iterable[MemoryReferenceParam] | Omit = omit,
        metadata: CreateOperationMetadata | Omit = omit,
        secrets: Iterable[objective_create_params.Secret] | Omit = omit,
        user_data: Dict[str, object] | Omit = omit,
        variation_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Objective:
        """
        Creates a new objective in the workspace

        Args:
          data: Arbitrary data for the objective. May be used in liquid templates for prompts
              configured on the agent variation

          episodic_memory: Episodic is used to configure the episodic memory for the objective

          initial_message: Optional override for the initial message sent to the agent. This becomes the
              first user message in the LLM chat history. When not set, the selected
              variation's user_message_template is rendered with user_data instead. If neither
              this field nor a user_message_template is present, the request is rejected with
              InvalidArgument.

          memory_cascade: Memory layers/entries layered over the baseline cascade inherited from the
              selected variation — element-level rules over inherited styles, in CSS terms.

              Array order is resolution order: EARLIER elements are more specific and are
              consulted first. Entries pinned via memory_entry_id behave as single-entry
              layers at their position.

              System-managed layers (e.g., episodic) cannot be referenced here; they attach
              themselves automatically based on the episodic key.

              Size cap: the TOTAL effective cascade (this field + the variation's memory layer
              assignments) must not exceed 10 entries. A request that would produce a larger
              cascade is rejected with InvalidArgument.

          metadata: CreateOperationMetadata contains the user-provided fields for creating an
              operation. Read-only fields (id, account_id, workspace_id, created_at,
              profile_id) are excluded since they are set by the server.

          secrets: Secrets that can be used in the headers for tool calls using the secret
              interpolation format.

          user_data: Arbitrary data rendered into the selected variation's user_message_template
              (liquid) to produce the initial user message. Separate from `data`, which
              renders the system prompt template.

          variation_id: Optional explicit variation selection. Overrides the agent's
              variation_selection_mode.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return self._post(
            path_template("/v1/workspaces/{workspace_id}/objectives", workspace_id=workspace_id),
            body=maybe_transform(
                {
                    "agent_id": agent_id,
                    "data": data,
                    "episodic_memory": episodic_memory,
                    "initial_message": initial_message,
                    "memory_cascade": memory_cascade,
                    "metadata": metadata,
                    "secrets": secrets,
                    "user_data": user_data,
                    "variation_id": variation_id,
                },
                objective_create_params.ObjectiveCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Objective,
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
    ) -> Objective:
        """
        Retrieves an objective by ID from the workspace

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
            path_template("/v1/workspaces/{workspace_id}/objectives/{id}", workspace_id=workspace_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Objective,
        )

    def list(
        self,
        workspace_id: str,
        *,
        agent_id: str | Omit = omit,
        agent_schedule_id: str | Omit = omit,
        cursor: str | Omit = omit,
        include_info: bool | Omit = omit,
        limit: int | Omit = omit,
        parent_objective_id: str | Omit = omit,
        profile_id: str | Omit = omit,
        sort_order: str | Omit = omit,
        state: Literal[
            "STATE_UNSPECIFIED",
            "STATE_PENDING",
            "STATE_RUNNING",
            "STATE_WAITING",
            "STATE_FAILED",
            "STATE_CANCELLED",
            "STATE_FINALIZED",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPagination[Objective]:
        """
        Lists all objectives in the workspace

        Args:
          agent_id: Agent ID for filtering

          agent_schedule_id: Filter to objectives produced by a specific AgentSchedule. Accepts canonical
              as\\__… form or external_id:<value> form.

          cursor: Pagination cursor from previous response

          include_info: When set to true you may use more of your alloted API rate-limit

          limit: Maximum number of results to return

          parent_objective_id: Optional filters

          sort_order: Sort order for results (asc or desc by creation time)

          state: Filter by state

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return self._get_api_list(
            path_template("/v1/workspaces/{workspace_id}/objectives", workspace_id=workspace_id),
            page=SyncCursorPagination[Objective],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "agent_id": agent_id,
                        "agent_schedule_id": agent_schedule_id,
                        "cursor": cursor,
                        "include_info": include_info,
                        "limit": limit,
                        "parent_objective_id": parent_objective_id,
                        "profile_id": profile_id,
                        "sort_order": sort_order,
                        "state": state,
                    },
                    objective_list_params.ObjectiveListParams,
                ),
            ),
            model=Objective,
        )

    def cancel(
        self,
        objective_id: str,
        *,
        workspace_id: str,
        reason: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Objective:
        """Cancels a running or pending objective.

        The objective's state will be set to
        STATE_CANCELLED.

        Args:
          reason: Optional reason for cancellation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not objective_id:
            raise ValueError(f"Expected a non-empty value for `objective_id` but received {objective_id!r}")
        return self._post(
            path_template(
                "/v1/workspaces/{workspace_id}/objectives/{objective_id}:cancel",
                workspace_id=workspace_id,
                objective_id=objective_id,
            ),
            body=maybe_transform({"reason": reason}, objective_cancel_params.ObjectiveCancelParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Objective,
        )

    def compact(
        self,
        objective_id: str,
        *,
        workspace_id: str,
        compaction_config: AgentVariationSpecCompactionConfigParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObjectiveCompactResponse:
        """Triggers compaction on a running objective.

        Optionally override the variation's
        compaction config.

        Args:
          compaction_config: CompactionConfig defines how context window compaction behaves for objectives
              using this variation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not objective_id:
            raise ValueError(f"Expected a non-empty value for `objective_id` but received {objective_id!r}")
        return self._post(
            path_template(
                "/v1/workspaces/{workspace_id}/objectives/{objective_id}:compact",
                workspace_id=workspace_id,
                objective_id=objective_id,
            ),
            body=maybe_transform(
                {"compaction_config": compaction_config}, objective_compact_params.ObjectiveCompactParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectiveCompactResponse,
        )

    def continue_(
        self,
        objective_id: str,
        *,
        workspace_id: str,
        enqueue: bool | Omit = omit,
        message: str | Omit = omit,
        secrets: Iterable[objective_continue_params.Secret] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObjectiveEvent:
        """
        Continues an objective that has completed

        Args:
          enqueue: When set to true, the message will be enqueued for when the agent loop is
              available to process it.

          message: The message to continue an objective that has completed (or you are enqueing)

          secrets: Secrets that should be included with the message. Helpful for when you need to
              update secrets on the objective (IE: A secret expires and needs to be refreshed)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not objective_id:
            raise ValueError(f"Expected a non-empty value for `objective_id` but received {objective_id!r}")
        return self._post(
            path_template(
                "/v1/workspaces/{workspace_id}/objectives/{objective_id}:continue",
                workspace_id=workspace_id,
                objective_id=objective_id,
            ),
            body=maybe_transform(
                {
                    "enqueue": enqueue,
                    "message": message,
                    "secrets": secrets,
                },
                objective_continue_params.ObjectiveContinueParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectiveEvent,
        )

    def list_context_windows(
        self,
        objective_id: str,
        *,
        workspace_id: str,
        cursor: str | Omit = omit,
        include_info: bool | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPagination[ObjectiveContextWindow]:
        """
        Read-only list of the last five windows of execution for this objective, ordered
        by most recent first

        Args:
          cursor: Pagination cursor from previous response

          include_info: When set to true you may use more of your alloted API rate-limit

          limit: Maximum number of results to return

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
                "/v1/workspaces/{workspace_id}/objectives/{objective_id}/context_windows",
                workspace_id=workspace_id,
                objective_id=objective_id,
            ),
            page=SyncCursorPagination[ObjectiveContextWindow],
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
                    },
                    objective_list_context_windows_params.ObjectiveListContextWindowsParams,
                ),
            ),
            model=ObjectiveContextWindow,
        )

    def list_events(
        self,
        objective_id: str,
        *,
        workspace_id: str,
        cursor: str | Omit = omit,
        include_info: bool | Omit = omit,
        limit: int | Omit = omit,
        since_event_id: str | Omit = omit,
        sort_order: str | Omit = omit,
        window_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPagination[ObjectiveEvent]:
        """
        Lists all events for an objective

        Args:
          cursor: Pagination cursor from previous response

          include_info: When set to true you may use more of your alloted API rate-limit

          limit: Maximum number of results to return

          since_event_id: Optional string to fetch events since an ID

          sort_order: Sort order for results (asc or desc by creation time)

          window_id: Optional context window ID to filter events by

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
                "/v1/workspaces/{workspace_id}/objectives/{objective_id}/events",
                workspace_id=workspace_id,
                objective_id=objective_id,
            ),
            page=SyncCursorPagination[ObjectiveEvent],
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
                        "since_event_id": since_event_id,
                        "sort_order": sort_order,
                        "window_id": window_id,
                    },
                    objective_list_events_params.ObjectiveListEventsParams,
                ),
            ),
            model=ObjectiveEvent,
        )

    def stream_events(
        self,
        objective_id: str,
        *,
        workspace_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[ObjectiveEvent]:
        """
        Streams events for an objective in real-time using server-sent events (SSE)

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
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._get(
            path_template(
                "/v1/workspaces/{workspace_id}/objectives/{objective_id}/events:stream",
                workspace_id=workspace_id,
                objective_id=objective_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectiveEvent,
            stream=True,
            stream_cls=Stream[ObjectiveEvent],
        )


class AsyncObjectivesResource(AsyncAPIResource):
    @cached_property
    def tools(self) -> AsyncToolsResource:
        return AsyncToolsResource(self._client)

    @cached_property
    def tool_calls(self) -> AsyncToolCallsResource:
        return AsyncToolCallsResource(self._client)

    @cached_property
    def tasks(self) -> AsyncTasksResource:
        return AsyncTasksResource(self._client)

    @cached_property
    def feedback(self) -> AsyncFeedbackResource:
        return AsyncFeedbackResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncObjectivesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cadenya/cadenya-python#accessing-raw-response-data-eg-headers
        """
        return AsyncObjectivesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncObjectivesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cadenya/cadenya-python#with_streaming_response
        """
        return AsyncObjectivesResourceWithStreamingResponse(self)

    async def create(
        self,
        workspace_id: str,
        *,
        agent_id: str,
        data: Dict[str, object],
        episodic_memory: objective_create_params.EpisodicMemory | Omit = omit,
        initial_message: str | Omit = omit,
        memory_cascade: Iterable[MemoryReferenceParam] | Omit = omit,
        metadata: CreateOperationMetadata | Omit = omit,
        secrets: Iterable[objective_create_params.Secret] | Omit = omit,
        user_data: Dict[str, object] | Omit = omit,
        variation_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Objective:
        """
        Creates a new objective in the workspace

        Args:
          data: Arbitrary data for the objective. May be used in liquid templates for prompts
              configured on the agent variation

          episodic_memory: Episodic is used to configure the episodic memory for the objective

          initial_message: Optional override for the initial message sent to the agent. This becomes the
              first user message in the LLM chat history. When not set, the selected
              variation's user_message_template is rendered with user_data instead. If neither
              this field nor a user_message_template is present, the request is rejected with
              InvalidArgument.

          memory_cascade: Memory layers/entries layered over the baseline cascade inherited from the
              selected variation — element-level rules over inherited styles, in CSS terms.

              Array order is resolution order: EARLIER elements are more specific and are
              consulted first. Entries pinned via memory_entry_id behave as single-entry
              layers at their position.

              System-managed layers (e.g., episodic) cannot be referenced here; they attach
              themselves automatically based on the episodic key.

              Size cap: the TOTAL effective cascade (this field + the variation's memory layer
              assignments) must not exceed 10 entries. A request that would produce a larger
              cascade is rejected with InvalidArgument.

          metadata: CreateOperationMetadata contains the user-provided fields for creating an
              operation. Read-only fields (id, account_id, workspace_id, created_at,
              profile_id) are excluded since they are set by the server.

          secrets: Secrets that can be used in the headers for tool calls using the secret
              interpolation format.

          user_data: Arbitrary data rendered into the selected variation's user_message_template
              (liquid) to produce the initial user message. Separate from `data`, which
              renders the system prompt template.

          variation_id: Optional explicit variation selection. Overrides the agent's
              variation_selection_mode.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return await self._post(
            path_template("/v1/workspaces/{workspace_id}/objectives", workspace_id=workspace_id),
            body=await async_maybe_transform(
                {
                    "agent_id": agent_id,
                    "data": data,
                    "episodic_memory": episodic_memory,
                    "initial_message": initial_message,
                    "memory_cascade": memory_cascade,
                    "metadata": metadata,
                    "secrets": secrets,
                    "user_data": user_data,
                    "variation_id": variation_id,
                },
                objective_create_params.ObjectiveCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Objective,
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
    ) -> Objective:
        """
        Retrieves an objective by ID from the workspace

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
            path_template("/v1/workspaces/{workspace_id}/objectives/{id}", workspace_id=workspace_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Objective,
        )

    def list(
        self,
        workspace_id: str,
        *,
        agent_id: str | Omit = omit,
        agent_schedule_id: str | Omit = omit,
        cursor: str | Omit = omit,
        include_info: bool | Omit = omit,
        limit: int | Omit = omit,
        parent_objective_id: str | Omit = omit,
        profile_id: str | Omit = omit,
        sort_order: str | Omit = omit,
        state: Literal[
            "STATE_UNSPECIFIED",
            "STATE_PENDING",
            "STATE_RUNNING",
            "STATE_WAITING",
            "STATE_FAILED",
            "STATE_CANCELLED",
            "STATE_FINALIZED",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Objective, AsyncCursorPagination[Objective]]:
        """
        Lists all objectives in the workspace

        Args:
          agent_id: Agent ID for filtering

          agent_schedule_id: Filter to objectives produced by a specific AgentSchedule. Accepts canonical
              as\\__… form or external_id:<value> form.

          cursor: Pagination cursor from previous response

          include_info: When set to true you may use more of your alloted API rate-limit

          limit: Maximum number of results to return

          parent_objective_id: Optional filters

          sort_order: Sort order for results (asc or desc by creation time)

          state: Filter by state

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return self._get_api_list(
            path_template("/v1/workspaces/{workspace_id}/objectives", workspace_id=workspace_id),
            page=AsyncCursorPagination[Objective],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "agent_id": agent_id,
                        "agent_schedule_id": agent_schedule_id,
                        "cursor": cursor,
                        "include_info": include_info,
                        "limit": limit,
                        "parent_objective_id": parent_objective_id,
                        "profile_id": profile_id,
                        "sort_order": sort_order,
                        "state": state,
                    },
                    objective_list_params.ObjectiveListParams,
                ),
            ),
            model=Objective,
        )

    async def cancel(
        self,
        objective_id: str,
        *,
        workspace_id: str,
        reason: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Objective:
        """Cancels a running or pending objective.

        The objective's state will be set to
        STATE_CANCELLED.

        Args:
          reason: Optional reason for cancellation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not objective_id:
            raise ValueError(f"Expected a non-empty value for `objective_id` but received {objective_id!r}")
        return await self._post(
            path_template(
                "/v1/workspaces/{workspace_id}/objectives/{objective_id}:cancel",
                workspace_id=workspace_id,
                objective_id=objective_id,
            ),
            body=await async_maybe_transform({"reason": reason}, objective_cancel_params.ObjectiveCancelParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Objective,
        )

    async def compact(
        self,
        objective_id: str,
        *,
        workspace_id: str,
        compaction_config: AgentVariationSpecCompactionConfigParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObjectiveCompactResponse:
        """Triggers compaction on a running objective.

        Optionally override the variation's
        compaction config.

        Args:
          compaction_config: CompactionConfig defines how context window compaction behaves for objectives
              using this variation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not objective_id:
            raise ValueError(f"Expected a non-empty value for `objective_id` but received {objective_id!r}")
        return await self._post(
            path_template(
                "/v1/workspaces/{workspace_id}/objectives/{objective_id}:compact",
                workspace_id=workspace_id,
                objective_id=objective_id,
            ),
            body=await async_maybe_transform(
                {"compaction_config": compaction_config}, objective_compact_params.ObjectiveCompactParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectiveCompactResponse,
        )

    async def continue_(
        self,
        objective_id: str,
        *,
        workspace_id: str,
        enqueue: bool | Omit = omit,
        message: str | Omit = omit,
        secrets: Iterable[objective_continue_params.Secret] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ObjectiveEvent:
        """
        Continues an objective that has completed

        Args:
          enqueue: When set to true, the message will be enqueued for when the agent loop is
              available to process it.

          message: The message to continue an objective that has completed (or you are enqueing)

          secrets: Secrets that should be included with the message. Helpful for when you need to
              update secrets on the objective (IE: A secret expires and needs to be refreshed)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not objective_id:
            raise ValueError(f"Expected a non-empty value for `objective_id` but received {objective_id!r}")
        return await self._post(
            path_template(
                "/v1/workspaces/{workspace_id}/objectives/{objective_id}:continue",
                workspace_id=workspace_id,
                objective_id=objective_id,
            ),
            body=await async_maybe_transform(
                {
                    "enqueue": enqueue,
                    "message": message,
                    "secrets": secrets,
                },
                objective_continue_params.ObjectiveContinueParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectiveEvent,
        )

    def list_context_windows(
        self,
        objective_id: str,
        *,
        workspace_id: str,
        cursor: str | Omit = omit,
        include_info: bool | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ObjectiveContextWindow, AsyncCursorPagination[ObjectiveContextWindow]]:
        """
        Read-only list of the last five windows of execution for this objective, ordered
        by most recent first

        Args:
          cursor: Pagination cursor from previous response

          include_info: When set to true you may use more of your alloted API rate-limit

          limit: Maximum number of results to return

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
                "/v1/workspaces/{workspace_id}/objectives/{objective_id}/context_windows",
                workspace_id=workspace_id,
                objective_id=objective_id,
            ),
            page=AsyncCursorPagination[ObjectiveContextWindow],
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
                    },
                    objective_list_context_windows_params.ObjectiveListContextWindowsParams,
                ),
            ),
            model=ObjectiveContextWindow,
        )

    def list_events(
        self,
        objective_id: str,
        *,
        workspace_id: str,
        cursor: str | Omit = omit,
        include_info: bool | Omit = omit,
        limit: int | Omit = omit,
        since_event_id: str | Omit = omit,
        sort_order: str | Omit = omit,
        window_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ObjectiveEvent, AsyncCursorPagination[ObjectiveEvent]]:
        """
        Lists all events for an objective

        Args:
          cursor: Pagination cursor from previous response

          include_info: When set to true you may use more of your alloted API rate-limit

          limit: Maximum number of results to return

          since_event_id: Optional string to fetch events since an ID

          sort_order: Sort order for results (asc or desc by creation time)

          window_id: Optional context window ID to filter events by

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
                "/v1/workspaces/{workspace_id}/objectives/{objective_id}/events",
                workspace_id=workspace_id,
                objective_id=objective_id,
            ),
            page=AsyncCursorPagination[ObjectiveEvent],
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
                        "since_event_id": since_event_id,
                        "sort_order": sort_order,
                        "window_id": window_id,
                    },
                    objective_list_events_params.ObjectiveListEventsParams,
                ),
            ),
            model=ObjectiveEvent,
        )

    async def stream_events(
        self,
        objective_id: str,
        *,
        workspace_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[ObjectiveEvent]:
        """
        Streams events for an objective in real-time using server-sent events (SSE)

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
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._get(
            path_template(
                "/v1/workspaces/{workspace_id}/objectives/{objective_id}/events:stream",
                workspace_id=workspace_id,
                objective_id=objective_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectiveEvent,
            stream=True,
            stream_cls=AsyncStream[ObjectiveEvent],
        )


class ObjectivesResourceWithRawResponse:
    def __init__(self, objectives: ObjectivesResource) -> None:
        self._objectives = objectives

        self.create = to_raw_response_wrapper(
            objectives.create,
        )
        self.retrieve = to_raw_response_wrapper(
            objectives.retrieve,
        )
        self.list = to_raw_response_wrapper(
            objectives.list,
        )
        self.cancel = to_raw_response_wrapper(
            objectives.cancel,
        )
        self.compact = to_raw_response_wrapper(
            objectives.compact,
        )
        self.continue_ = to_raw_response_wrapper(
            objectives.continue_,
        )
        self.list_context_windows = to_raw_response_wrapper(
            objectives.list_context_windows,
        )
        self.list_events = to_raw_response_wrapper(
            objectives.list_events,
        )
        self.stream_events = to_raw_response_wrapper(
            objectives.stream_events,
        )

    @cached_property
    def tools(self) -> ToolsResourceWithRawResponse:
        return ToolsResourceWithRawResponse(self._objectives.tools)

    @cached_property
    def tool_calls(self) -> ToolCallsResourceWithRawResponse:
        return ToolCallsResourceWithRawResponse(self._objectives.tool_calls)

    @cached_property
    def tasks(self) -> TasksResourceWithRawResponse:
        return TasksResourceWithRawResponse(self._objectives.tasks)

    @cached_property
    def feedback(self) -> FeedbackResourceWithRawResponse:
        return FeedbackResourceWithRawResponse(self._objectives.feedback)


class AsyncObjectivesResourceWithRawResponse:
    def __init__(self, objectives: AsyncObjectivesResource) -> None:
        self._objectives = objectives

        self.create = async_to_raw_response_wrapper(
            objectives.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            objectives.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            objectives.list,
        )
        self.cancel = async_to_raw_response_wrapper(
            objectives.cancel,
        )
        self.compact = async_to_raw_response_wrapper(
            objectives.compact,
        )
        self.continue_ = async_to_raw_response_wrapper(
            objectives.continue_,
        )
        self.list_context_windows = async_to_raw_response_wrapper(
            objectives.list_context_windows,
        )
        self.list_events = async_to_raw_response_wrapper(
            objectives.list_events,
        )
        self.stream_events = async_to_raw_response_wrapper(
            objectives.stream_events,
        )

    @cached_property
    def tools(self) -> AsyncToolsResourceWithRawResponse:
        return AsyncToolsResourceWithRawResponse(self._objectives.tools)

    @cached_property
    def tool_calls(self) -> AsyncToolCallsResourceWithRawResponse:
        return AsyncToolCallsResourceWithRawResponse(self._objectives.tool_calls)

    @cached_property
    def tasks(self) -> AsyncTasksResourceWithRawResponse:
        return AsyncTasksResourceWithRawResponse(self._objectives.tasks)

    @cached_property
    def feedback(self) -> AsyncFeedbackResourceWithRawResponse:
        return AsyncFeedbackResourceWithRawResponse(self._objectives.feedback)


class ObjectivesResourceWithStreamingResponse:
    def __init__(self, objectives: ObjectivesResource) -> None:
        self._objectives = objectives

        self.create = to_streamed_response_wrapper(
            objectives.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            objectives.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            objectives.list,
        )
        self.cancel = to_streamed_response_wrapper(
            objectives.cancel,
        )
        self.compact = to_streamed_response_wrapper(
            objectives.compact,
        )
        self.continue_ = to_streamed_response_wrapper(
            objectives.continue_,
        )
        self.list_context_windows = to_streamed_response_wrapper(
            objectives.list_context_windows,
        )
        self.list_events = to_streamed_response_wrapper(
            objectives.list_events,
        )
        self.stream_events = to_streamed_response_wrapper(
            objectives.stream_events,
        )

    @cached_property
    def tools(self) -> ToolsResourceWithStreamingResponse:
        return ToolsResourceWithStreamingResponse(self._objectives.tools)

    @cached_property
    def tool_calls(self) -> ToolCallsResourceWithStreamingResponse:
        return ToolCallsResourceWithStreamingResponse(self._objectives.tool_calls)

    @cached_property
    def tasks(self) -> TasksResourceWithStreamingResponse:
        return TasksResourceWithStreamingResponse(self._objectives.tasks)

    @cached_property
    def feedback(self) -> FeedbackResourceWithStreamingResponse:
        return FeedbackResourceWithStreamingResponse(self._objectives.feedback)


class AsyncObjectivesResourceWithStreamingResponse:
    def __init__(self, objectives: AsyncObjectivesResource) -> None:
        self._objectives = objectives

        self.create = async_to_streamed_response_wrapper(
            objectives.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            objectives.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            objectives.list,
        )
        self.cancel = async_to_streamed_response_wrapper(
            objectives.cancel,
        )
        self.compact = async_to_streamed_response_wrapper(
            objectives.compact,
        )
        self.continue_ = async_to_streamed_response_wrapper(
            objectives.continue_,
        )
        self.list_context_windows = async_to_streamed_response_wrapper(
            objectives.list_context_windows,
        )
        self.list_events = async_to_streamed_response_wrapper(
            objectives.list_events,
        )
        self.stream_events = async_to_streamed_response_wrapper(
            objectives.stream_events,
        )

    @cached_property
    def tools(self) -> AsyncToolsResourceWithStreamingResponse:
        return AsyncToolsResourceWithStreamingResponse(self._objectives.tools)

    @cached_property
    def tool_calls(self) -> AsyncToolCallsResourceWithStreamingResponse:
        return AsyncToolCallsResourceWithStreamingResponse(self._objectives.tool_calls)

    @cached_property
    def tasks(self) -> AsyncTasksResourceWithStreamingResponse:
        return AsyncTasksResourceWithStreamingResponse(self._objectives.tasks)

    @cached_property
    def feedback(self) -> AsyncFeedbackResourceWithStreamingResponse:
        return AsyncFeedbackResourceWithStreamingResponse(self._objectives.feedback)
