# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform
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
from ...types.agents import webhook_delivery_list_params
from ...types.agents.webhook_delivery import WebhookDelivery

__all__ = ["WebhookDeliveriesResource", "AsyncWebhookDeliveriesResource"]


class WebhookDeliveriesResource(SyncAPIResource):
    """Manage AI agents within a workspace. Agents define AI behavior and tool access."""

    @cached_property
    def with_raw_response(self) -> WebhookDeliveriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cadenya/cadenya-python#accessing-raw-response-data-eg-headers
        """
        return WebhookDeliveriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WebhookDeliveriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cadenya/cadenya-python#with_streaming_response
        """
        return WebhookDeliveriesResourceWithStreamingResponse(self)

    def list(
        self,
        agent_id: str,
        *,
        workspace_id: str | None = None,
        cursor: str | Omit = omit,
        event_type: Literal[
            "OBJECTIVE_EVENT_TYPE_UNSPECIFIED",
            "OBJECTIVE_EVENT_TYPE_USER_MESSAGE",
            "OBJECTIVE_EVENT_TYPE_TOOL_APPROVAL_REQUESTED",
            "OBJECTIVE_EVENT_TYPE_TOOL_APPROVED",
            "OBJECTIVE_EVENT_TYPE_TOOL_DENIED",
            "OBJECTIVE_EVENT_TYPE_TOOL_CALLED",
            "OBJECTIVE_EVENT_TYPE_ERROR",
            "OBJECTIVE_EVENT_TYPE_ASSISTANT_MESSAGE",
            "OBJECTIVE_EVENT_TYPE_TOOL_RESULT",
            "OBJECTIVE_EVENT_TYPE_TOOL_ERROR",
            "OBJECTIVE_EVENT_TYPE_CONTEXT_WINDOW_COMPACTED",
            "OBJECTIVE_EVENT_TYPE_MEMORY_READ",
            "OBJECTIVE_EVENT_TYPE_CANCELLED",
            "OBJECTIVE_EVENT_TYPE_SUB_AGENT_SPAWNED",
            "OBJECTIVE_EVENT_TYPE_SUB_AGENT_UPDATED",
            "OBJECTIVE_EVENT_TYPE_FINALIZED",
            "OBJECTIVE_EVENT_TYPE_NOTICE",
            "OBJECTIVE_EVENT_TYPE_TIMED_OUT",
        ]
        | Omit = omit,
        labels: str | Omit = omit,
        limit: int | Omit = omit,
        objective_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPagination[WebhookDelivery]:
        """
        Lists all webhook deliveries for an agent

        Args:
          cursor: Pagination cursor from previous response

          event_type: Optional filter by event type

          labels: Filters by metadata labels. Comma-separated key=value pairs, e.g.
              "env=prod,team=ai". A resource matches only if every pair matches exactly (AND
              semantics).

          limit: Maximum number of results to return

          objective_id: Optional filter by objective ID

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
                "/v1/workspaces/{workspace_id}/agents/{agent_id}/webhook_deliveries",
                workspace_id=workspace_id,
                agent_id=agent_id,
            ),
            page=SyncCursorPagination[WebhookDelivery],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "event_type": event_type,
                        "labels": labels,
                        "limit": limit,
                        "objective_id": objective_id,
                    },
                    webhook_delivery_list_params.WebhookDeliveryListParams,
                ),
            ),
            model=WebhookDelivery,
        )


class AsyncWebhookDeliveriesResource(AsyncAPIResource):
    """Manage AI agents within a workspace. Agents define AI behavior and tool access."""

    @cached_property
    def with_raw_response(self) -> AsyncWebhookDeliveriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cadenya/cadenya-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWebhookDeliveriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWebhookDeliveriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cadenya/cadenya-python#with_streaming_response
        """
        return AsyncWebhookDeliveriesResourceWithStreamingResponse(self)

    def list(
        self,
        agent_id: str,
        *,
        workspace_id: str | None = None,
        cursor: str | Omit = omit,
        event_type: Literal[
            "OBJECTIVE_EVENT_TYPE_UNSPECIFIED",
            "OBJECTIVE_EVENT_TYPE_USER_MESSAGE",
            "OBJECTIVE_EVENT_TYPE_TOOL_APPROVAL_REQUESTED",
            "OBJECTIVE_EVENT_TYPE_TOOL_APPROVED",
            "OBJECTIVE_EVENT_TYPE_TOOL_DENIED",
            "OBJECTIVE_EVENT_TYPE_TOOL_CALLED",
            "OBJECTIVE_EVENT_TYPE_ERROR",
            "OBJECTIVE_EVENT_TYPE_ASSISTANT_MESSAGE",
            "OBJECTIVE_EVENT_TYPE_TOOL_RESULT",
            "OBJECTIVE_EVENT_TYPE_TOOL_ERROR",
            "OBJECTIVE_EVENT_TYPE_CONTEXT_WINDOW_COMPACTED",
            "OBJECTIVE_EVENT_TYPE_MEMORY_READ",
            "OBJECTIVE_EVENT_TYPE_CANCELLED",
            "OBJECTIVE_EVENT_TYPE_SUB_AGENT_SPAWNED",
            "OBJECTIVE_EVENT_TYPE_SUB_AGENT_UPDATED",
            "OBJECTIVE_EVENT_TYPE_FINALIZED",
            "OBJECTIVE_EVENT_TYPE_NOTICE",
            "OBJECTIVE_EVENT_TYPE_TIMED_OUT",
        ]
        | Omit = omit,
        labels: str | Omit = omit,
        limit: int | Omit = omit,
        objective_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[WebhookDelivery, AsyncCursorPagination[WebhookDelivery]]:
        """
        Lists all webhook deliveries for an agent

        Args:
          cursor: Pagination cursor from previous response

          event_type: Optional filter by event type

          labels: Filters by metadata labels. Comma-separated key=value pairs, e.g.
              "env=prod,team=ai". A resource matches only if every pair matches exactly (AND
              semantics).

          limit: Maximum number of results to return

          objective_id: Optional filter by objective ID

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
                "/v1/workspaces/{workspace_id}/agents/{agent_id}/webhook_deliveries",
                workspace_id=workspace_id,
                agent_id=agent_id,
            ),
            page=AsyncCursorPagination[WebhookDelivery],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "event_type": event_type,
                        "labels": labels,
                        "limit": limit,
                        "objective_id": objective_id,
                    },
                    webhook_delivery_list_params.WebhookDeliveryListParams,
                ),
            ),
            model=WebhookDelivery,
        )


class WebhookDeliveriesResourceWithRawResponse:
    def __init__(self, webhook_deliveries: WebhookDeliveriesResource) -> None:
        self._webhook_deliveries = webhook_deliveries

        self.list = to_raw_response_wrapper(
            webhook_deliveries.list,
        )


class AsyncWebhookDeliveriesResourceWithRawResponse:
    def __init__(self, webhook_deliveries: AsyncWebhookDeliveriesResource) -> None:
        self._webhook_deliveries = webhook_deliveries

        self.list = async_to_raw_response_wrapper(
            webhook_deliveries.list,
        )


class WebhookDeliveriesResourceWithStreamingResponse:
    def __init__(self, webhook_deliveries: WebhookDeliveriesResource) -> None:
        self._webhook_deliveries = webhook_deliveries

        self.list = to_streamed_response_wrapper(
            webhook_deliveries.list,
        )


class AsyncWebhookDeliveriesResourceWithStreamingResponse:
    def __init__(self, webhook_deliveries: AsyncWebhookDeliveriesResource) -> None:
        self._webhook_deliveries = webhook_deliveries

        self.list = async_to_streamed_response_wrapper(
            webhook_deliveries.list,
        )
