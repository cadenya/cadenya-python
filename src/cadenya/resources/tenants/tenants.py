# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...types import tenant_list_params, tenant_retrieve_params
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from .subjects import (
    SubjectsResource,
    AsyncSubjectsResource,
    SubjectsResourceWithRawResponse,
    AsyncSubjectsResourceWithRawResponse,
    SubjectsResourceWithStreamingResponse,
    AsyncSubjectsResourceWithStreamingResponse,
)
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
from ...types.tenant import Tenant

__all__ = ["TenantsResource", "AsyncTenantsResource"]


class TenantsResource(SyncAPIResource):
    """Read and erase tenants and the subjects under them.

    Tenants and subjects are
     created by assertion — on objective creation or widget session mint — never
     directly, so this service has no create or update: it exists to enumerate what
     assertions have produced, and to destroy it on request.
    """

    @cached_property
    def subjects(self) -> SubjectsResource:
        """Read and erase tenants and the subjects under them.

        Tenants and subjects are
         created by assertion — on objective creation or widget session mint — never
         directly, so this service has no create or update: it exists to enumerate what
         assertions have produced, and to destroy it on request.
        """
        return SubjectsResource(self._client)

    @cached_property
    def with_raw_response(self) -> TenantsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cadenya/cadenya-python#accessing-raw-response-data-eg-headers
        """
        return TenantsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TenantsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cadenya/cadenya-python#with_streaming_response
        """
        return TenantsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        workspace_id: str | None = None,
        include_info: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Tenant:
        """
        Retrieves a tenant by its canonical id or by the `external_id:<value>` form the
        customer asserted it under.

        Args:
          include_info: When true, the `info` field is populated.

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
            path_template("/v1/workspaces/{workspace_id}/tenants/{id}", workspace_id=workspace_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"include_info": include_info}, tenant_retrieve_params.TenantRetrieveParams),
            ),
            cast_to=Tenant,
        )

    def list(
        self,
        *,
        workspace_id: str | None = None,
        cursor: str | Omit = omit,
        include_info: bool | Omit = omit,
        labels: str | Omit = omit,
        limit: int | Omit = omit,
        query: str | Omit = omit,
        sort_order: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPagination[Tenant]:
        """Lists the tenants asserted in a workspace, newest first.

        `query` matches against
        a tenant's name and its external_id, for type-ahead filters.

        Args:
          cursor: Pagination cursor from previous response.

          include_info: When true, the `info` field on each returned tenant is populated. This costs
              several count queries per tenant, so it is off by default.

          labels: Filters by metadata labels. Comma-separated key=value pairs, e.g.
              "env=prod,team=ai". A resource matches only if every pair matches exactly (AND
              semantics).

          limit: Maximum number of results to return.

          query: Substring match against the tenant's name and external_id. Built for type-ahead
              filter pickers, where the operator knows the customer's own identifier rather
              than Cadenya's.

          sort_order: Sort order for results (asc or desc by creation time).

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
            path_template("/v1/workspaces/{workspace_id}/tenants", workspace_id=workspace_id),
            page=SyncCursorPagination[Tenant],
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
                        "query": query,
                        "sort_order": sort_order,
                    },
                    tenant_list_params.TenantListParams,
                ),
            ),
            model=Tenant,
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
    ) -> Tenant:
        """
        Destroys the tenant, its subjects, every objective associated with it and
        everything reachable from those objectives, and its widget sessions. This is the
        full erasure hammer, wider than `DELETE /widget_sessions`, which removes only
        what widget sessions created. The work runs in the background: this returns the
        tenant in STATE_ERASING rather than a count of what was removed, since a large
        tenant's history cannot be destroyed inside a request. Poll the tenant to follow
        it — STATE_ERASING while it runs, NotFound once it finishes. Erasure is
        terminal; a tenant cannot be recovered once it starts.

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
        return self._delete(
            path_template("/v1/workspaces/{workspace_id}/tenants/{id}", workspace_id=workspace_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tenant,
        )


class AsyncTenantsResource(AsyncAPIResource):
    """Read and erase tenants and the subjects under them.

    Tenants and subjects are
     created by assertion — on objective creation or widget session mint — never
     directly, so this service has no create or update: it exists to enumerate what
     assertions have produced, and to destroy it on request.
    """

    @cached_property
    def subjects(self) -> AsyncSubjectsResource:
        """Read and erase tenants and the subjects under them.

        Tenants and subjects are
         created by assertion — on objective creation or widget session mint — never
         directly, so this service has no create or update: it exists to enumerate what
         assertions have produced, and to destroy it on request.
        """
        return AsyncSubjectsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTenantsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cadenya/cadenya-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTenantsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTenantsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cadenya/cadenya-python#with_streaming_response
        """
        return AsyncTenantsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        workspace_id: str | None = None,
        include_info: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Tenant:
        """
        Retrieves a tenant by its canonical id or by the `external_id:<value>` form the
        customer asserted it under.

        Args:
          include_info: When true, the `info` field is populated.

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
            path_template("/v1/workspaces/{workspace_id}/tenants/{id}", workspace_id=workspace_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"include_info": include_info}, tenant_retrieve_params.TenantRetrieveParams
                ),
            ),
            cast_to=Tenant,
        )

    def list(
        self,
        *,
        workspace_id: str | None = None,
        cursor: str | Omit = omit,
        include_info: bool | Omit = omit,
        labels: str | Omit = omit,
        limit: int | Omit = omit,
        query: str | Omit = omit,
        sort_order: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Tenant, AsyncCursorPagination[Tenant]]:
        """Lists the tenants asserted in a workspace, newest first.

        `query` matches against
        a tenant's name and its external_id, for type-ahead filters.

        Args:
          cursor: Pagination cursor from previous response.

          include_info: When true, the `info` field on each returned tenant is populated. This costs
              several count queries per tenant, so it is off by default.

          labels: Filters by metadata labels. Comma-separated key=value pairs, e.g.
              "env=prod,team=ai". A resource matches only if every pair matches exactly (AND
              semantics).

          limit: Maximum number of results to return.

          query: Substring match against the tenant's name and external_id. Built for type-ahead
              filter pickers, where the operator knows the customer's own identifier rather
              than Cadenya's.

          sort_order: Sort order for results (asc or desc by creation time).

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
            path_template("/v1/workspaces/{workspace_id}/tenants", workspace_id=workspace_id),
            page=AsyncCursorPagination[Tenant],
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
                        "query": query,
                        "sort_order": sort_order,
                    },
                    tenant_list_params.TenantListParams,
                ),
            ),
            model=Tenant,
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
    ) -> Tenant:
        """
        Destroys the tenant, its subjects, every objective associated with it and
        everything reachable from those objectives, and its widget sessions. This is the
        full erasure hammer, wider than `DELETE /widget_sessions`, which removes only
        what widget sessions created. The work runs in the background: this returns the
        tenant in STATE_ERASING rather than a count of what was removed, since a large
        tenant's history cannot be destroyed inside a request. Poll the tenant to follow
        it — STATE_ERASING while it runs, NotFound once it finishes. Erasure is
        terminal; a tenant cannot be recovered once it starts.

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
        return await self._delete(
            path_template("/v1/workspaces/{workspace_id}/tenants/{id}", workspace_id=workspace_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tenant,
        )


class TenantsResourceWithRawResponse:
    def __init__(self, tenants: TenantsResource) -> None:
        self._tenants = tenants

        self.retrieve = to_raw_response_wrapper(
            tenants.retrieve,
        )
        self.list = to_raw_response_wrapper(
            tenants.list,
        )
        self.delete = to_raw_response_wrapper(
            tenants.delete,
        )

    @cached_property
    def subjects(self) -> SubjectsResourceWithRawResponse:
        """Read and erase tenants and the subjects under them.

        Tenants and subjects are
         created by assertion — on objective creation or widget session mint — never
         directly, so this service has no create or update: it exists to enumerate what
         assertions have produced, and to destroy it on request.
        """
        return SubjectsResourceWithRawResponse(self._tenants.subjects)


class AsyncTenantsResourceWithRawResponse:
    def __init__(self, tenants: AsyncTenantsResource) -> None:
        self._tenants = tenants

        self.retrieve = async_to_raw_response_wrapper(
            tenants.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            tenants.list,
        )
        self.delete = async_to_raw_response_wrapper(
            tenants.delete,
        )

    @cached_property
    def subjects(self) -> AsyncSubjectsResourceWithRawResponse:
        """Read and erase tenants and the subjects under them.

        Tenants and subjects are
         created by assertion — on objective creation or widget session mint — never
         directly, so this service has no create or update: it exists to enumerate what
         assertions have produced, and to destroy it on request.
        """
        return AsyncSubjectsResourceWithRawResponse(self._tenants.subjects)


class TenantsResourceWithStreamingResponse:
    def __init__(self, tenants: TenantsResource) -> None:
        self._tenants = tenants

        self.retrieve = to_streamed_response_wrapper(
            tenants.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            tenants.list,
        )
        self.delete = to_streamed_response_wrapper(
            tenants.delete,
        )

    @cached_property
    def subjects(self) -> SubjectsResourceWithStreamingResponse:
        """Read and erase tenants and the subjects under them.

        Tenants and subjects are
         created by assertion — on objective creation or widget session mint — never
         directly, so this service has no create or update: it exists to enumerate what
         assertions have produced, and to destroy it on request.
        """
        return SubjectsResourceWithStreamingResponse(self._tenants.subjects)


class AsyncTenantsResourceWithStreamingResponse:
    def __init__(self, tenants: AsyncTenantsResource) -> None:
        self._tenants = tenants

        self.retrieve = async_to_streamed_response_wrapper(
            tenants.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            tenants.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            tenants.delete,
        )

    @cached_property
    def subjects(self) -> AsyncSubjectsResourceWithStreamingResponse:
        """Read and erase tenants and the subjects under them.

        Tenants and subjects are
         created by assertion — on objective creation or widget session mint — never
         directly, so this service has no create or update: it exists to enumerate what
         assertions have produced, and to destroy it on request.
        """
        return AsyncSubjectsResourceWithStreamingResponse(self._tenants.subjects)
