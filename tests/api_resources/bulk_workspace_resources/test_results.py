# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cadenya import Cadenya, AsyncCadenya
from tests.utils import assert_matches_type
from cadenya.pagination import SyncCursorPagination, AsyncCursorPagination
from cadenya.types.bulk_workspace_resources import BulkWorkspaceApplyResult

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestResults:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Cadenya) -> None:
        result = client.bulk_workspace_resources.results.list(
            bulk_workspace_apply_id="bulkWorkspaceApplyId",
            workspace_id="workspaceId",
        )
        assert_matches_type(SyncCursorPagination[BulkWorkspaceApplyResult], result, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Cadenya) -> None:
        result = client.bulk_workspace_resources.results.list(
            bulk_workspace_apply_id="bulkWorkspaceApplyId",
            workspace_id="workspaceId",
            action="ACTION_UNSPECIFIED",
            cursor="cursor",
            limit=0,
            sort_order="sortOrder",
            type="type",
        )
        assert_matches_type(SyncCursorPagination[BulkWorkspaceApplyResult], result, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Cadenya) -> None:
        response = client.bulk_workspace_resources.results.with_raw_response.list(
            bulk_workspace_apply_id="bulkWorkspaceApplyId",
            workspace_id="workspaceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        result = response.parse()
        assert_matches_type(SyncCursorPagination[BulkWorkspaceApplyResult], result, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Cadenya) -> None:
        with client.bulk_workspace_resources.results.with_streaming_response.list(
            bulk_workspace_apply_id="bulkWorkspaceApplyId",
            workspace_id="workspaceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            result = response.parse()
            assert_matches_type(SyncCursorPagination[BulkWorkspaceApplyResult], result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.bulk_workspace_resources.results.with_raw_response.list(
                bulk_workspace_apply_id="bulkWorkspaceApplyId",
                workspace_id="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `bulk_workspace_apply_id` but received ''"
        ):
            client.bulk_workspace_resources.results.with_raw_response.list(
                bulk_workspace_apply_id="",
                workspace_id="workspaceId",
            )


class TestAsyncResults:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCadenya) -> None:
        result = await async_client.bulk_workspace_resources.results.list(
            bulk_workspace_apply_id="bulkWorkspaceApplyId",
            workspace_id="workspaceId",
        )
        assert_matches_type(AsyncCursorPagination[BulkWorkspaceApplyResult], result, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCadenya) -> None:
        result = await async_client.bulk_workspace_resources.results.list(
            bulk_workspace_apply_id="bulkWorkspaceApplyId",
            workspace_id="workspaceId",
            action="ACTION_UNSPECIFIED",
            cursor="cursor",
            limit=0,
            sort_order="sortOrder",
            type="type",
        )
        assert_matches_type(AsyncCursorPagination[BulkWorkspaceApplyResult], result, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCadenya) -> None:
        response = await async_client.bulk_workspace_resources.results.with_raw_response.list(
            bulk_workspace_apply_id="bulkWorkspaceApplyId",
            workspace_id="workspaceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        result = await response.parse()
        assert_matches_type(AsyncCursorPagination[BulkWorkspaceApplyResult], result, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCadenya) -> None:
        async with async_client.bulk_workspace_resources.results.with_streaming_response.list(
            bulk_workspace_apply_id="bulkWorkspaceApplyId",
            workspace_id="workspaceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            result = await response.parse()
            assert_matches_type(AsyncCursorPagination[BulkWorkspaceApplyResult], result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.bulk_workspace_resources.results.with_raw_response.list(
                bulk_workspace_apply_id="bulkWorkspaceApplyId",
                workspace_id="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `bulk_workspace_apply_id` but received ''"
        ):
            await async_client.bulk_workspace_resources.results.with_raw_response.list(
                bulk_workspace_apply_id="",
                workspace_id="workspaceId",
            )
