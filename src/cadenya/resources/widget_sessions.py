# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ..types import (
    widget_session_list_params,
    widget_session_create_params,
    widget_session_delete_tenant_params,
)
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncCursorPagination, AsyncCursorPagination
from .._base_client import AsyncPaginator, make_request_options
from ..types.widget_session import WidgetSession
from ..types.widget_session_spec_param import WidgetSessionSpecParam
from ..types.widget_session_delete_tenant_response import WidgetSessionDeleteTenantResponse
from ..types.shared_params.create_operation_metadata import CreateOperationMetadata

__all__ = ["WidgetSessionsResource", "AsyncWidgetSessionsResource"]


class WidgetSessionsResource(SyncAPIResource):
    """Mint and manage widget sessions.

    Session creation is server-to-server only:
     the customer's backend authenticates its visitor, asserts tenant/subject
     context, attaches any per-visitor secrets, and receives a short-lived
     bearer token the browser uses against the widget host.
    """

    @cached_property
    def with_raw_response(self) -> WidgetSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cadenya/cadenya-python#accessing-raw-response-data-eg-headers
        """
        return WidgetSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WidgetSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cadenya/cadenya-python#with_streaming_response
        """
        return WidgetSessionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        workspace_id: str | None = None,
        spec: WidgetSessionSpecParam,
        metadata: CreateOperationMetadata | Omit = omit,
        secrets: Iterable[widget_session_create_params.Secret] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WidgetSession:
        """
        Mints a session against a widget and returns the session bearer token
        (`spec.token`, returned only on creation) plus the authoritative widget hostname
        (`info.host`). Asserting a tenant upserts the tenant record; attached secrets
        flow to every conversation the session creates.

        Args:
          spec: WidgetSessionSpec is the configuration of a session, fixed at mint.

          metadata: CreateOperationMetadata contains the user-provided fields for creating an
              operation. Read-only fields (id, account_id, workspace_id, created_at,
              profile_id) are excluded since they are set by the server.

          secrets: Secrets to attach to the session.

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
            path_template("/v1/workspaces/{workspace_id}/widget_sessions", workspace_id=workspace_id),
            body=maybe_transform(
                {
                    "spec": spec,
                    "metadata": metadata,
                    "secrets": secrets,
                },
                widget_session_create_params.WidgetSessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WidgetSession,
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
    ) -> WidgetSession:
        """Retrieves a widget session.

        The bearer token is never returned on reads.

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
            path_template("/v1/workspaces/{workspace_id}/widget_sessions/{id}", workspace_id=workspace_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WidgetSession,
        )

    def list(
        self,
        *,
        workspace_id: str | None = None,
        cursor: str | Omit = omit,
        include_info: bool | Omit = omit,
        labels: str | Omit = omit,
        limit: int | Omit = omit,
        sort_order: str | Omit = omit,
        state: Literal["STATE_UNSPECIFIED", "STATE_ACTIVE", "STATE_EXPIRED", "STATE_REVOKED", "STATE_EXHAUSTED"]
        | Omit = omit,
        subject_id: str | Omit = omit,
        tenant_id: str | Omit = omit,
        widget_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPagination[WidgetSession]:
        """
        Lists widget sessions in a workspace, filterable by widget, tenant, subject, and
        state

        Args:
          cursor: Pagination cursor from previous response.

          include_info: When true, the `info` field on each returned session is populated. Requests with
              this flag count more against your rate limit.

          labels: Filters by metadata labels. Comma-separated key=value pairs, e.g.
              "env=prod,team=ai". A resource matches only if every pair matches exactly (AND
              semantics).

          limit: Maximum number of results to return.

          sort_order: Sort order for results (asc or desc by creation time).

          state: Filter by state.

          subject_id: Filter to sessions asserted for a subject. Accepts the canonical `subj_…` form
              or the `external_id:<value>` form; the external_id form is scoped within a
              tenant and requires `tenant_id` to also be set.

          tenant_id: Filter to sessions belonging to a tenant. Accepts the canonical `tenant_…` form
              or the `external_id:<value>` form.

          widget_id: Filter to sessions on a specific widget. Accepts the canonical `wgt_…` form or
              the `external_id:<value>` form.

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
            path_template("/v1/workspaces/{workspace_id}/widget_sessions", workspace_id=workspace_id),
            page=SyncCursorPagination[WidgetSession],
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
                        "state": state,
                        "subject_id": subject_id,
                        "tenant_id": tenant_id,
                        "widget_id": widget_id,
                    },
                    widget_session_list_params.WidgetSessionListParams,
                ),
            ),
            model=WidgetSession,
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
        """Deletes a session and its secrets.

        The session's conversations are
        disassociated, not deleted; use the tenant-level delete for full erasure.

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
            path_template("/v1/workspaces/{workspace_id}/widget_sessions/{id}", workspace_id=workspace_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def delete_tenant(
        self,
        *,
        workspace_id: str | None = None,
        tenant_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WidgetSessionDeleteTenantResponse:
        """
        Deletes every session belonging to a tenant across all widgets in the workspace,
        along with the conversations those sessions created — built for GDPR erasure
        requests. The tenant is required; an empty value is rejected rather than
        matching everything.

        Args:
          tenant_id: Tenant whose sessions to delete. Required — an empty value is rejected rather
              than matching everything. Accepts the canonical `tenant_…` form or the
              `external_id:<value>` form.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if workspace_id is None:
            workspace_id = self._client._get_workspace_id_path_param()
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return self._delete(
            path_template("/v1/workspaces/{workspace_id}/widget_sessions", workspace_id=workspace_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"tenant_id": tenant_id}, widget_session_delete_tenant_params.WidgetSessionDeleteTenantParams
                ),
            ),
            cast_to=WidgetSessionDeleteTenantResponse,
        )

    def revoke(
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
    ) -> WidgetSession:
        """Transitions a session to STATE_REVOKED.

        Outstanding tokens stop working
        immediately, open event streams close within seconds, and the session's secrets
        are deleted. Terminal.

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
            path_template(
                "/v1/workspaces/{workspace_id}/widget_sessions/{id}:revoke", workspace_id=workspace_id, id=id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WidgetSession,
        )


class AsyncWidgetSessionsResource(AsyncAPIResource):
    """Mint and manage widget sessions.

    Session creation is server-to-server only:
     the customer's backend authenticates its visitor, asserts tenant/subject
     context, attaches any per-visitor secrets, and receives a short-lived
     bearer token the browser uses against the widget host.
    """

    @cached_property
    def with_raw_response(self) -> AsyncWidgetSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cadenya/cadenya-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWidgetSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWidgetSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cadenya/cadenya-python#with_streaming_response
        """
        return AsyncWidgetSessionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        workspace_id: str | None = None,
        spec: WidgetSessionSpecParam,
        metadata: CreateOperationMetadata | Omit = omit,
        secrets: Iterable[widget_session_create_params.Secret] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WidgetSession:
        """
        Mints a session against a widget and returns the session bearer token
        (`spec.token`, returned only on creation) plus the authoritative widget hostname
        (`info.host`). Asserting a tenant upserts the tenant record; attached secrets
        flow to every conversation the session creates.

        Args:
          spec: WidgetSessionSpec is the configuration of a session, fixed at mint.

          metadata: CreateOperationMetadata contains the user-provided fields for creating an
              operation. Read-only fields (id, account_id, workspace_id, created_at,
              profile_id) are excluded since they are set by the server.

          secrets: Secrets to attach to the session.

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
            path_template("/v1/workspaces/{workspace_id}/widget_sessions", workspace_id=workspace_id),
            body=await async_maybe_transform(
                {
                    "spec": spec,
                    "metadata": metadata,
                    "secrets": secrets,
                },
                widget_session_create_params.WidgetSessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WidgetSession,
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
    ) -> WidgetSession:
        """Retrieves a widget session.

        The bearer token is never returned on reads.

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
            path_template("/v1/workspaces/{workspace_id}/widget_sessions/{id}", workspace_id=workspace_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WidgetSession,
        )

    def list(
        self,
        *,
        workspace_id: str | None = None,
        cursor: str | Omit = omit,
        include_info: bool | Omit = omit,
        labels: str | Omit = omit,
        limit: int | Omit = omit,
        sort_order: str | Omit = omit,
        state: Literal["STATE_UNSPECIFIED", "STATE_ACTIVE", "STATE_EXPIRED", "STATE_REVOKED", "STATE_EXHAUSTED"]
        | Omit = omit,
        subject_id: str | Omit = omit,
        tenant_id: str | Omit = omit,
        widget_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[WidgetSession, AsyncCursorPagination[WidgetSession]]:
        """
        Lists widget sessions in a workspace, filterable by widget, tenant, subject, and
        state

        Args:
          cursor: Pagination cursor from previous response.

          include_info: When true, the `info` field on each returned session is populated. Requests with
              this flag count more against your rate limit.

          labels: Filters by metadata labels. Comma-separated key=value pairs, e.g.
              "env=prod,team=ai". A resource matches only if every pair matches exactly (AND
              semantics).

          limit: Maximum number of results to return.

          sort_order: Sort order for results (asc or desc by creation time).

          state: Filter by state.

          subject_id: Filter to sessions asserted for a subject. Accepts the canonical `subj_…` form
              or the `external_id:<value>` form; the external_id form is scoped within a
              tenant and requires `tenant_id` to also be set.

          tenant_id: Filter to sessions belonging to a tenant. Accepts the canonical `tenant_…` form
              or the `external_id:<value>` form.

          widget_id: Filter to sessions on a specific widget. Accepts the canonical `wgt_…` form or
              the `external_id:<value>` form.

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
            path_template("/v1/workspaces/{workspace_id}/widget_sessions", workspace_id=workspace_id),
            page=AsyncCursorPagination[WidgetSession],
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
                        "state": state,
                        "subject_id": subject_id,
                        "tenant_id": tenant_id,
                        "widget_id": widget_id,
                    },
                    widget_session_list_params.WidgetSessionListParams,
                ),
            ),
            model=WidgetSession,
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
        """Deletes a session and its secrets.

        The session's conversations are
        disassociated, not deleted; use the tenant-level delete for full erasure.

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
            path_template("/v1/workspaces/{workspace_id}/widget_sessions/{id}", workspace_id=workspace_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def delete_tenant(
        self,
        *,
        workspace_id: str | None = None,
        tenant_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WidgetSessionDeleteTenantResponse:
        """
        Deletes every session belonging to a tenant across all widgets in the workspace,
        along with the conversations those sessions created — built for GDPR erasure
        requests. The tenant is required; an empty value is rejected rather than
        matching everything.

        Args:
          tenant_id: Tenant whose sessions to delete. Required — an empty value is rejected rather
              than matching everything. Accepts the canonical `tenant_…` form or the
              `external_id:<value>` form.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if workspace_id is None:
            workspace_id = self._client._get_workspace_id_path_param()
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return await self._delete(
            path_template("/v1/workspaces/{workspace_id}/widget_sessions", workspace_id=workspace_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"tenant_id": tenant_id}, widget_session_delete_tenant_params.WidgetSessionDeleteTenantParams
                ),
            ),
            cast_to=WidgetSessionDeleteTenantResponse,
        )

    async def revoke(
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
    ) -> WidgetSession:
        """Transitions a session to STATE_REVOKED.

        Outstanding tokens stop working
        immediately, open event streams close within seconds, and the session's secrets
        are deleted. Terminal.

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
            path_template(
                "/v1/workspaces/{workspace_id}/widget_sessions/{id}:revoke", workspace_id=workspace_id, id=id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WidgetSession,
        )


class WidgetSessionsResourceWithRawResponse:
    def __init__(self, widget_sessions: WidgetSessionsResource) -> None:
        self._widget_sessions = widget_sessions

        self.create = to_raw_response_wrapper(
            widget_sessions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            widget_sessions.retrieve,
        )
        self.list = to_raw_response_wrapper(
            widget_sessions.list,
        )
        self.delete = to_raw_response_wrapper(
            widget_sessions.delete,
        )
        self.delete_tenant = to_raw_response_wrapper(
            widget_sessions.delete_tenant,
        )
        self.revoke = to_raw_response_wrapper(
            widget_sessions.revoke,
        )


class AsyncWidgetSessionsResourceWithRawResponse:
    def __init__(self, widget_sessions: AsyncWidgetSessionsResource) -> None:
        self._widget_sessions = widget_sessions

        self.create = async_to_raw_response_wrapper(
            widget_sessions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            widget_sessions.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            widget_sessions.list,
        )
        self.delete = async_to_raw_response_wrapper(
            widget_sessions.delete,
        )
        self.delete_tenant = async_to_raw_response_wrapper(
            widget_sessions.delete_tenant,
        )
        self.revoke = async_to_raw_response_wrapper(
            widget_sessions.revoke,
        )


class WidgetSessionsResourceWithStreamingResponse:
    def __init__(self, widget_sessions: WidgetSessionsResource) -> None:
        self._widget_sessions = widget_sessions

        self.create = to_streamed_response_wrapper(
            widget_sessions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            widget_sessions.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            widget_sessions.list,
        )
        self.delete = to_streamed_response_wrapper(
            widget_sessions.delete,
        )
        self.delete_tenant = to_streamed_response_wrapper(
            widget_sessions.delete_tenant,
        )
        self.revoke = to_streamed_response_wrapper(
            widget_sessions.revoke,
        )


class AsyncWidgetSessionsResourceWithStreamingResponse:
    def __init__(self, widget_sessions: AsyncWidgetSessionsResource) -> None:
        self._widget_sessions = widget_sessions

        self.create = async_to_streamed_response_wrapper(
            widget_sessions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            widget_sessions.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            widget_sessions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            widget_sessions.delete,
        )
        self.delete_tenant = async_to_streamed_response_wrapper(
            widget_sessions.delete_tenant,
        )
        self.revoke = async_to_streamed_response_wrapper(
            widget_sessions.revoke,
        )
