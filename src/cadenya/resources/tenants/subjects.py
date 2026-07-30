# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...types.subject import Subject
from ...types.tenants import subject_list_params

__all__ = ["SubjectsResource", "AsyncSubjectsResource"]


class SubjectsResource(SyncAPIResource):
    """Read and erase tenants and the subjects under them.

    Tenants and subjects are
     created by assertion — on objective creation or widget session mint — never
     directly, so this service has no create or update: it exists to enumerate what
     assertions have produced, and to destroy it on request.
    """

    @cached_property
    def with_raw_response(self) -> SubjectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cadenya/cadenya-python#accessing-raw-response-data-eg-headers
        """
        return SubjectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubjectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cadenya/cadenya-python#with_streaming_response
        """
        return SubjectsResourceWithStreamingResponse(self)

    def list(
        self,
        tenant_id: str,
        *,
        workspace_id: str | None = None,
        cursor: str | Omit = omit,
        include_info: bool | Omit = omit,
        limit: int | Omit = omit,
        query: str | Omit = omit,
        sort_order: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPagination[Subject]:
        """Lists the subjects asserted under a tenant.

        Subjects are only listable through
        their tenant: a subject's external_id is unique within its tenant, not across
        the workspace, so the same key can name different people under different
        tenants.

        Args:
          cursor: Pagination cursor from previous response.

          include_info: When true, the `info` field on each returned subject is populated.

          limit: Maximum number of results to return.

          query: Substring match against the subject's name and external_id.

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
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        return self._get_api_list(
            path_template(
                "/v1/workspaces/{workspace_id}/tenants/{tenant_id}/subjects",
                workspace_id=workspace_id,
                tenant_id=tenant_id,
            ),
            page=SyncCursorPagination[Subject],
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
                        "query": query,
                        "sort_order": sort_order,
                    },
                    subject_list_params.SubjectListParams,
                ),
            ),
            model=Subject,
        )


class AsyncSubjectsResource(AsyncAPIResource):
    """Read and erase tenants and the subjects under them.

    Tenants and subjects are
     created by assertion — on objective creation or widget session mint — never
     directly, so this service has no create or update: it exists to enumerate what
     assertions have produced, and to destroy it on request.
    """

    @cached_property
    def with_raw_response(self) -> AsyncSubjectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cadenya/cadenya-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSubjectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubjectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cadenya/cadenya-python#with_streaming_response
        """
        return AsyncSubjectsResourceWithStreamingResponse(self)

    def list(
        self,
        tenant_id: str,
        *,
        workspace_id: str | None = None,
        cursor: str | Omit = omit,
        include_info: bool | Omit = omit,
        limit: int | Omit = omit,
        query: str | Omit = omit,
        sort_order: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Subject, AsyncCursorPagination[Subject]]:
        """Lists the subjects asserted under a tenant.

        Subjects are only listable through
        their tenant: a subject's external_id is unique within its tenant, not across
        the workspace, so the same key can name different people under different
        tenants.

        Args:
          cursor: Pagination cursor from previous response.

          include_info: When true, the `info` field on each returned subject is populated.

          limit: Maximum number of results to return.

          query: Substring match against the subject's name and external_id.

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
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        return self._get_api_list(
            path_template(
                "/v1/workspaces/{workspace_id}/tenants/{tenant_id}/subjects",
                workspace_id=workspace_id,
                tenant_id=tenant_id,
            ),
            page=AsyncCursorPagination[Subject],
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
                        "query": query,
                        "sort_order": sort_order,
                    },
                    subject_list_params.SubjectListParams,
                ),
            ),
            model=Subject,
        )


class SubjectsResourceWithRawResponse:
    def __init__(self, subjects: SubjectsResource) -> None:
        self._subjects = subjects

        self.list = to_raw_response_wrapper(
            subjects.list,
        )


class AsyncSubjectsResourceWithRawResponse:
    def __init__(self, subjects: AsyncSubjectsResource) -> None:
        self._subjects = subjects

        self.list = async_to_raw_response_wrapper(
            subjects.list,
        )


class SubjectsResourceWithStreamingResponse:
    def __init__(self, subjects: SubjectsResource) -> None:
        self._subjects = subjects

        self.list = to_streamed_response_wrapper(
            subjects.list,
        )


class AsyncSubjectsResourceWithStreamingResponse:
    def __init__(self, subjects: AsyncSubjectsResource) -> None:
        self._subjects = subjects

        self.list = async_to_streamed_response_wrapper(
            subjects.list,
        )
