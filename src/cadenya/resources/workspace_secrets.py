# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import (
    workspace_secret_list_params,
    workspace_secret_create_params,
    workspace_secret_update_params,
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
from ..types.workspace_secret import WorkspaceSecret
from ..types.workspace_secret_spec_param import WorkspaceSecretSpecParam
from ..types.shared_params.create_resource_metadata import CreateResourceMetadata
from ..types.shared_params.update_resource_metadata import UpdateResourceMetadata

__all__ = ["WorkspaceSecretsResource", "AsyncWorkspaceSecretsResource"]


class WorkspaceSecretsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WorkspaceSecretsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/cadenya-python#accessing-raw-response-data-eg-headers
        """
        return WorkspaceSecretsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WorkspaceSecretsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/cadenya-python#with_streaming_response
        """
        return WorkspaceSecretsResourceWithStreamingResponse(self)

    def create(
        self,
        workspace_id: str,
        *,
        metadata: CreateResourceMetadata,
        spec: WorkspaceSecretSpecParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkspaceSecret:
        """
        Creates a new workspace secret in the workspace

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
            path_template("/v1/workspaces/{workspace_id}/workspace_secrets", workspace_id=workspace_id),
            body=maybe_transform(
                {
                    "metadata": metadata,
                    "spec": spec,
                },
                workspace_secret_create_params.WorkspaceSecretCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkspaceSecret,
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
    ) -> WorkspaceSecret:
        """
        Retrieves a workspace secret by ID from the workspace

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
            path_template("/v1/workspaces/{workspace_id}/workspace_secrets/{id}", workspace_id=workspace_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkspaceSecret,
        )

    def update(
        self,
        id: str,
        *,
        workspace_id: str,
        metadata: UpdateResourceMetadata | Omit = omit,
        spec: WorkspaceSecretSpecParam | Omit = omit,
        update_mask: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkspaceSecret:
        """
        Updates a workspace secret in the workspace

        Args:
          metadata: UpdateResourceMetadata contains the user-provided fields for updating a
              workspace-scoped resource. Read-only fields (id, account_id, workspace_id,
              profile_id, created_at) are excluded since they are set by the server.

          update_mask: Fields to update.

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
            path_template("/v1/workspaces/{workspace_id}/workspace_secrets/{id}", workspace_id=workspace_id, id=id),
            body=maybe_transform(
                {
                    "metadata": metadata,
                    "spec": spec,
                    "update_mask": update_mask,
                },
                workspace_secret_update_params.WorkspaceSecretUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkspaceSecret,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPagination[WorkspaceSecret]:
        """
        Lists all workspace secrets in the workspace

        Args:
          bundle_key: Filter by bundle_key — return only resources owned by this bundle.

          cursor: Pagination cursor from previous response

          include_info: When set to true you may use more of your alloted API rate-limit

          limit: Maximum number of results to return

          prefix: Filter expression (query param: prefix)

          query: Free-form search query

          sort_order: Sort order for results (asc or desc by creation time)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return self._get_api_list(
            path_template("/v1/workspaces/{workspace_id}/workspace_secrets", workspace_id=workspace_id),
            page=SyncCursorPagination[WorkspaceSecret],
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
                    workspace_secret_list_params.WorkspaceSecretListParams,
                ),
            ),
            model=WorkspaceSecret,
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
        Deletes a workspace secret from the workspace

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
            path_template("/v1/workspaces/{workspace_id}/workspace_secrets/{id}", workspace_id=workspace_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncWorkspaceSecretsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWorkspaceSecretsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/cadenya-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWorkspaceSecretsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWorkspaceSecretsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/cadenya-python#with_streaming_response
        """
        return AsyncWorkspaceSecretsResourceWithStreamingResponse(self)

    async def create(
        self,
        workspace_id: str,
        *,
        metadata: CreateResourceMetadata,
        spec: WorkspaceSecretSpecParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkspaceSecret:
        """
        Creates a new workspace secret in the workspace

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
            path_template("/v1/workspaces/{workspace_id}/workspace_secrets", workspace_id=workspace_id),
            body=await async_maybe_transform(
                {
                    "metadata": metadata,
                    "spec": spec,
                },
                workspace_secret_create_params.WorkspaceSecretCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkspaceSecret,
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
    ) -> WorkspaceSecret:
        """
        Retrieves a workspace secret by ID from the workspace

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
            path_template("/v1/workspaces/{workspace_id}/workspace_secrets/{id}", workspace_id=workspace_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkspaceSecret,
        )

    async def update(
        self,
        id: str,
        *,
        workspace_id: str,
        metadata: UpdateResourceMetadata | Omit = omit,
        spec: WorkspaceSecretSpecParam | Omit = omit,
        update_mask: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkspaceSecret:
        """
        Updates a workspace secret in the workspace

        Args:
          metadata: UpdateResourceMetadata contains the user-provided fields for updating a
              workspace-scoped resource. Read-only fields (id, account_id, workspace_id,
              profile_id, created_at) are excluded since they are set by the server.

          update_mask: Fields to update.

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
            path_template("/v1/workspaces/{workspace_id}/workspace_secrets/{id}", workspace_id=workspace_id, id=id),
            body=await async_maybe_transform(
                {
                    "metadata": metadata,
                    "spec": spec,
                    "update_mask": update_mask,
                },
                workspace_secret_update_params.WorkspaceSecretUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkspaceSecret,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[WorkspaceSecret, AsyncCursorPagination[WorkspaceSecret]]:
        """
        Lists all workspace secrets in the workspace

        Args:
          bundle_key: Filter by bundle_key — return only resources owned by this bundle.

          cursor: Pagination cursor from previous response

          include_info: When set to true you may use more of your alloted API rate-limit

          limit: Maximum number of results to return

          prefix: Filter expression (query param: prefix)

          query: Free-form search query

          sort_order: Sort order for results (asc or desc by creation time)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return self._get_api_list(
            path_template("/v1/workspaces/{workspace_id}/workspace_secrets", workspace_id=workspace_id),
            page=AsyncCursorPagination[WorkspaceSecret],
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
                    workspace_secret_list_params.WorkspaceSecretListParams,
                ),
            ),
            model=WorkspaceSecret,
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
        Deletes a workspace secret from the workspace

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
            path_template("/v1/workspaces/{workspace_id}/workspace_secrets/{id}", workspace_id=workspace_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class WorkspaceSecretsResourceWithRawResponse:
    def __init__(self, workspace_secrets: WorkspaceSecretsResource) -> None:
        self._workspace_secrets = workspace_secrets

        self.create = to_raw_response_wrapper(
            workspace_secrets.create,
        )
        self.retrieve = to_raw_response_wrapper(
            workspace_secrets.retrieve,
        )
        self.update = to_raw_response_wrapper(
            workspace_secrets.update,
        )
        self.list = to_raw_response_wrapper(
            workspace_secrets.list,
        )
        self.delete = to_raw_response_wrapper(
            workspace_secrets.delete,
        )


class AsyncWorkspaceSecretsResourceWithRawResponse:
    def __init__(self, workspace_secrets: AsyncWorkspaceSecretsResource) -> None:
        self._workspace_secrets = workspace_secrets

        self.create = async_to_raw_response_wrapper(
            workspace_secrets.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            workspace_secrets.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            workspace_secrets.update,
        )
        self.list = async_to_raw_response_wrapper(
            workspace_secrets.list,
        )
        self.delete = async_to_raw_response_wrapper(
            workspace_secrets.delete,
        )


class WorkspaceSecretsResourceWithStreamingResponse:
    def __init__(self, workspace_secrets: WorkspaceSecretsResource) -> None:
        self._workspace_secrets = workspace_secrets

        self.create = to_streamed_response_wrapper(
            workspace_secrets.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            workspace_secrets.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            workspace_secrets.update,
        )
        self.list = to_streamed_response_wrapper(
            workspace_secrets.list,
        )
        self.delete = to_streamed_response_wrapper(
            workspace_secrets.delete,
        )


class AsyncWorkspaceSecretsResourceWithStreamingResponse:
    def __init__(self, workspace_secrets: AsyncWorkspaceSecretsResource) -> None:
        self._workspace_secrets = workspace_secrets

        self.create = async_to_streamed_response_wrapper(
            workspace_secrets.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            workspace_secrets.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            workspace_secrets.update,
        )
        self.list = async_to_streamed_response_wrapper(
            workspace_secrets.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            workspace_secrets.delete,
        )
