# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...types import (
    workspace_admin_list_params,
    workspace_admin_create_params,
    workspace_admin_update_params,
)
from .members import (
    MembersResource,
    AsyncMembersResource,
    MembersResourceWithRawResponse,
    AsyncMembersResourceWithRawResponse,
    MembersResourceWithStreamingResponse,
    AsyncMembersResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from .profiles import (
    ProfilesResource,
    AsyncProfilesResource,
    ProfilesResourceWithRawResponse,
    AsyncProfilesResourceWithRawResponse,
    ProfilesResourceWithStreamingResponse,
    AsyncProfilesResourceWithStreamingResponse,
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
from ...types.workspace import Workspace
from ...types.workspace_spec_param import WorkspaceSpecParam

__all__ = ["WorkspaceAdminResource", "AsyncWorkspaceAdminResource"]


class WorkspaceAdminResource(SyncAPIResource):
    """
    Administer workspaces across the account: create and archive workspaces and
     manage their membership. These operations are account-scoped and require the
     admin role (a token whose profile holds the WorkOS admin role); they live
     under /v1/account/workspaces rather than the workspace-scoped /v1/workspaces
     tree so an admin can manage any workspace in the account, including ones they
     are not themselves a member of.
    """

    @cached_property
    def members(self) -> MembersResource:
        """
        Administer workspaces across the account: create and archive workspaces and
         manage their membership. These operations are account-scoped and require the
         admin role (a token whose profile holds the WorkOS admin role); they live
         under /v1/account/workspaces rather than the workspace-scoped /v1/workspaces
         tree so an admin can manage any workspace in the account, including ones they
         are not themselves a member of.
        """
        return MembersResource(self._client)

    @cached_property
    def profiles(self) -> ProfilesResource:
        """
        Administer workspaces across the account: create and archive workspaces and
         manage their membership. These operations are account-scoped and require the
         admin role (a token whose profile holds the WorkOS admin role); they live
         under /v1/account/workspaces rather than the workspace-scoped /v1/workspaces
         tree so an admin can manage any workspace in the account, including ones they
         are not themselves a member of.
        """
        return ProfilesResource(self._client)

    @cached_property
    def with_raw_response(self) -> WorkspaceAdminResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cadenya/cadenya-python#accessing-raw-response-data-eg-headers
        """
        return WorkspaceAdminResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WorkspaceAdminResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cadenya/cadenya-python#with_streaming_response
        """
        return WorkspaceAdminResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        metadata: workspace_admin_create_params.Metadata,
        spec: WorkspaceSpecParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Workspace:
        """Creates a new workspace in the account.

        Admin only.

        Args:
          metadata: CreateAccountResourceMetadata contains the user-provided fields for creating an
              account-scoped resource. Read-only fields (id, account_id, profile_id) are
              excluded since they are set by the server.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/account/workspaces",
            body=maybe_transform(
                {
                    "metadata": metadata,
                    "spec": spec,
                },
                workspace_admin_create_params.WorkspaceAdminCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Workspace,
        )

    def retrieve(
        self,
        workspace_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Workspace:
        """Retrieves a workspace in the account by ID.

        Admin only.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return self._get(
            path_template("/v1/account/workspaces/{workspace_id}", workspace_id=workspace_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Workspace,
        )

    def update(
        self,
        workspace_id: str,
        *,
        metadata: workspace_admin_update_params.Metadata | Omit = omit,
        spec: WorkspaceSpecParam | Omit = omit,
        update_mask: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Workspace:
        """Updates a workspace's metadata (e.g.

        name) and spec. Admin only.

        Args:
          metadata: UpdateAccountResourceMetadata contains the user-provided fields for updating an
              account-scoped resource. Read-only fields (id, account_id, profile_id) are
              excluded since they are set by the server.

          update_mask: Fields to update.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return self._patch(
            path_template("/v1/account/workspaces/{workspace_id}", workspace_id=workspace_id),
            body=maybe_transform(
                {
                    "metadata": metadata,
                    "spec": spec,
                    "update_mask": update_mask,
                },
                workspace_admin_update_params.WorkspaceAdminUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Workspace,
        )

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        include_archived: bool | Omit = omit,
        labels: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPagination[Workspace]:
        """Lists every workspace in the account, optionally including archived ones.

        Admin
        only.

        Args:
          cursor: Pagination cursor from previous response

          include_archived: When true, archived workspaces are included in the results. Defaults to false
              (active workspaces only).

          labels: Filters by metadata labels. Comma-separated key=value pairs, e.g.
              "env=prod,team=ai". A resource matches only if every pair matches exactly (AND
              semantics).

          limit: Maximum number of results to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/account/workspaces",
            page=SyncCursorPagination[Workspace],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "include_archived": include_archived,
                        "labels": labels,
                        "limit": limit,
                    },
                    workspace_admin_list_params.WorkspaceAdminListParams,
                ),
            ),
            model=Workspace,
        )

    def archive(
        self,
        workspace_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Archives a workspace (soft delete).

        The workspace is retained, but any
        subsequent request scoped to it returns a permission error. Archiving the
        account's last active (non-archived) workspace is not allowed and returns
        FailedPrecondition. Admin only.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v1/account/workspaces/{workspace_id}", workspace_id=workspace_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncWorkspaceAdminResource(AsyncAPIResource):
    """
    Administer workspaces across the account: create and archive workspaces and
     manage their membership. These operations are account-scoped and require the
     admin role (a token whose profile holds the WorkOS admin role); they live
     under /v1/account/workspaces rather than the workspace-scoped /v1/workspaces
     tree so an admin can manage any workspace in the account, including ones they
     are not themselves a member of.
    """

    @cached_property
    def members(self) -> AsyncMembersResource:
        """
        Administer workspaces across the account: create and archive workspaces and
         manage their membership. These operations are account-scoped and require the
         admin role (a token whose profile holds the WorkOS admin role); they live
         under /v1/account/workspaces rather than the workspace-scoped /v1/workspaces
         tree so an admin can manage any workspace in the account, including ones they
         are not themselves a member of.
        """
        return AsyncMembersResource(self._client)

    @cached_property
    def profiles(self) -> AsyncProfilesResource:
        """
        Administer workspaces across the account: create and archive workspaces and
         manage their membership. These operations are account-scoped and require the
         admin role (a token whose profile holds the WorkOS admin role); they live
         under /v1/account/workspaces rather than the workspace-scoped /v1/workspaces
         tree so an admin can manage any workspace in the account, including ones they
         are not themselves a member of.
        """
        return AsyncProfilesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncWorkspaceAdminResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cadenya/cadenya-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWorkspaceAdminResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWorkspaceAdminResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cadenya/cadenya-python#with_streaming_response
        """
        return AsyncWorkspaceAdminResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        metadata: workspace_admin_create_params.Metadata,
        spec: WorkspaceSpecParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Workspace:
        """Creates a new workspace in the account.

        Admin only.

        Args:
          metadata: CreateAccountResourceMetadata contains the user-provided fields for creating an
              account-scoped resource. Read-only fields (id, account_id, profile_id) are
              excluded since they are set by the server.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/account/workspaces",
            body=await async_maybe_transform(
                {
                    "metadata": metadata,
                    "spec": spec,
                },
                workspace_admin_create_params.WorkspaceAdminCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Workspace,
        )

    async def retrieve(
        self,
        workspace_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Workspace:
        """Retrieves a workspace in the account by ID.

        Admin only.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return await self._get(
            path_template("/v1/account/workspaces/{workspace_id}", workspace_id=workspace_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Workspace,
        )

    async def update(
        self,
        workspace_id: str,
        *,
        metadata: workspace_admin_update_params.Metadata | Omit = omit,
        spec: WorkspaceSpecParam | Omit = omit,
        update_mask: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Workspace:
        """Updates a workspace's metadata (e.g.

        name) and spec. Admin only.

        Args:
          metadata: UpdateAccountResourceMetadata contains the user-provided fields for updating an
              account-scoped resource. Read-only fields (id, account_id, profile_id) are
              excluded since they are set by the server.

          update_mask: Fields to update.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return await self._patch(
            path_template("/v1/account/workspaces/{workspace_id}", workspace_id=workspace_id),
            body=await async_maybe_transform(
                {
                    "metadata": metadata,
                    "spec": spec,
                    "update_mask": update_mask,
                },
                workspace_admin_update_params.WorkspaceAdminUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Workspace,
        )

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        include_archived: bool | Omit = omit,
        labels: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Workspace, AsyncCursorPagination[Workspace]]:
        """Lists every workspace in the account, optionally including archived ones.

        Admin
        only.

        Args:
          cursor: Pagination cursor from previous response

          include_archived: When true, archived workspaces are included in the results. Defaults to false
              (active workspaces only).

          labels: Filters by metadata labels. Comma-separated key=value pairs, e.g.
              "env=prod,team=ai". A resource matches only if every pair matches exactly (AND
              semantics).

          limit: Maximum number of results to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/account/workspaces",
            page=AsyncCursorPagination[Workspace],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "include_archived": include_archived,
                        "labels": labels,
                        "limit": limit,
                    },
                    workspace_admin_list_params.WorkspaceAdminListParams,
                ),
            ),
            model=Workspace,
        )

    async def archive(
        self,
        workspace_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Archives a workspace (soft delete).

        The workspace is retained, but any
        subsequent request scoped to it returns a permission error. Archiving the
        account's last active (non-archived) workspace is not allowed and returns
        FailedPrecondition. Admin only.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/account/workspaces/{workspace_id}", workspace_id=workspace_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class WorkspaceAdminResourceWithRawResponse:
    def __init__(self, workspace_admin: WorkspaceAdminResource) -> None:
        self._workspace_admin = workspace_admin

        self.create = to_raw_response_wrapper(
            workspace_admin.create,
        )
        self.retrieve = to_raw_response_wrapper(
            workspace_admin.retrieve,
        )
        self.update = to_raw_response_wrapper(
            workspace_admin.update,
        )
        self.list = to_raw_response_wrapper(
            workspace_admin.list,
        )
        self.archive = to_raw_response_wrapper(
            workspace_admin.archive,
        )

    @cached_property
    def members(self) -> MembersResourceWithRawResponse:
        """
        Administer workspaces across the account: create and archive workspaces and
         manage their membership. These operations are account-scoped and require the
         admin role (a token whose profile holds the WorkOS admin role); they live
         under /v1/account/workspaces rather than the workspace-scoped /v1/workspaces
         tree so an admin can manage any workspace in the account, including ones they
         are not themselves a member of.
        """
        return MembersResourceWithRawResponse(self._workspace_admin.members)

    @cached_property
    def profiles(self) -> ProfilesResourceWithRawResponse:
        """
        Administer workspaces across the account: create and archive workspaces and
         manage their membership. These operations are account-scoped and require the
         admin role (a token whose profile holds the WorkOS admin role); they live
         under /v1/account/workspaces rather than the workspace-scoped /v1/workspaces
         tree so an admin can manage any workspace in the account, including ones they
         are not themselves a member of.
        """
        return ProfilesResourceWithRawResponse(self._workspace_admin.profiles)


class AsyncWorkspaceAdminResourceWithRawResponse:
    def __init__(self, workspace_admin: AsyncWorkspaceAdminResource) -> None:
        self._workspace_admin = workspace_admin

        self.create = async_to_raw_response_wrapper(
            workspace_admin.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            workspace_admin.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            workspace_admin.update,
        )
        self.list = async_to_raw_response_wrapper(
            workspace_admin.list,
        )
        self.archive = async_to_raw_response_wrapper(
            workspace_admin.archive,
        )

    @cached_property
    def members(self) -> AsyncMembersResourceWithRawResponse:
        """
        Administer workspaces across the account: create and archive workspaces and
         manage their membership. These operations are account-scoped and require the
         admin role (a token whose profile holds the WorkOS admin role); they live
         under /v1/account/workspaces rather than the workspace-scoped /v1/workspaces
         tree so an admin can manage any workspace in the account, including ones they
         are not themselves a member of.
        """
        return AsyncMembersResourceWithRawResponse(self._workspace_admin.members)

    @cached_property
    def profiles(self) -> AsyncProfilesResourceWithRawResponse:
        """
        Administer workspaces across the account: create and archive workspaces and
         manage their membership. These operations are account-scoped and require the
         admin role (a token whose profile holds the WorkOS admin role); they live
         under /v1/account/workspaces rather than the workspace-scoped /v1/workspaces
         tree so an admin can manage any workspace in the account, including ones they
         are not themselves a member of.
        """
        return AsyncProfilesResourceWithRawResponse(self._workspace_admin.profiles)


class WorkspaceAdminResourceWithStreamingResponse:
    def __init__(self, workspace_admin: WorkspaceAdminResource) -> None:
        self._workspace_admin = workspace_admin

        self.create = to_streamed_response_wrapper(
            workspace_admin.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            workspace_admin.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            workspace_admin.update,
        )
        self.list = to_streamed_response_wrapper(
            workspace_admin.list,
        )
        self.archive = to_streamed_response_wrapper(
            workspace_admin.archive,
        )

    @cached_property
    def members(self) -> MembersResourceWithStreamingResponse:
        """
        Administer workspaces across the account: create and archive workspaces and
         manage their membership. These operations are account-scoped and require the
         admin role (a token whose profile holds the WorkOS admin role); they live
         under /v1/account/workspaces rather than the workspace-scoped /v1/workspaces
         tree so an admin can manage any workspace in the account, including ones they
         are not themselves a member of.
        """
        return MembersResourceWithStreamingResponse(self._workspace_admin.members)

    @cached_property
    def profiles(self) -> ProfilesResourceWithStreamingResponse:
        """
        Administer workspaces across the account: create and archive workspaces and
         manage their membership. These operations are account-scoped and require the
         admin role (a token whose profile holds the WorkOS admin role); they live
         under /v1/account/workspaces rather than the workspace-scoped /v1/workspaces
         tree so an admin can manage any workspace in the account, including ones they
         are not themselves a member of.
        """
        return ProfilesResourceWithStreamingResponse(self._workspace_admin.profiles)


class AsyncWorkspaceAdminResourceWithStreamingResponse:
    def __init__(self, workspace_admin: AsyncWorkspaceAdminResource) -> None:
        self._workspace_admin = workspace_admin

        self.create = async_to_streamed_response_wrapper(
            workspace_admin.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            workspace_admin.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            workspace_admin.update,
        )
        self.list = async_to_streamed_response_wrapper(
            workspace_admin.list,
        )
        self.archive = async_to_streamed_response_wrapper(
            workspace_admin.archive,
        )

    @cached_property
    def members(self) -> AsyncMembersResourceWithStreamingResponse:
        """
        Administer workspaces across the account: create and archive workspaces and
         manage their membership. These operations are account-scoped and require the
         admin role (a token whose profile holds the WorkOS admin role); they live
         under /v1/account/workspaces rather than the workspace-scoped /v1/workspaces
         tree so an admin can manage any workspace in the account, including ones they
         are not themselves a member of.
        """
        return AsyncMembersResourceWithStreamingResponse(self._workspace_admin.members)

    @cached_property
    def profiles(self) -> AsyncProfilesResourceWithStreamingResponse:
        """
        Administer workspaces across the account: create and archive workspaces and
         manage their membership. These operations are account-scoped and require the
         admin role (a token whose profile holds the WorkOS admin role); they live
         under /v1/account/workspaces rather than the workspace-scoped /v1/workspaces
         tree so an admin can manage any workspace in the account, including ones they
         are not themselves a member of.
        """
        return AsyncProfilesResourceWithStreamingResponse(self._workspace_admin.profiles)
