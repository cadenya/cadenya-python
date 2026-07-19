# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cadenya import Cadenya, AsyncCadenya
from tests.utils import assert_matches_type
from cadenya.pagination import SyncCursorPagination, AsyncCursorPagination
from cadenya.types.objectives import ObjectiveTask

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTasks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Cadenya) -> None:
        task = client.objectives.tasks.retrieve(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            id="id",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert_matches_type(ObjectiveTask, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Cadenya) -> None:
        response = client.objectives.tasks.with_raw_response.retrieve(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            id="id",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(ObjectiveTask, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Cadenya) -> None:
        with client.objectives.tasks.with_streaming_response.retrieve(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            id="id",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(ObjectiveTask, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.objectives.tasks.with_raw_response.retrieve(
                objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
                id="id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `objective_id` but received ''"):
            client.objectives.tasks.with_raw_response.retrieve(
                objective_id="",
                id="id",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.objectives.tasks.with_raw_response.retrieve(
                objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
                id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Cadenya) -> None:
        task = client.objectives.tasks.list(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert_matches_type(SyncCursorPagination[ObjectiveTask], task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Cadenya) -> None:
        task = client.objectives.tasks.list(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            cursor="cursor",
            limit=0,
            sort_order="sortOrder",
        )
        assert_matches_type(SyncCursorPagination[ObjectiveTask], task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Cadenya) -> None:
        response = client.objectives.tasks.with_raw_response.list(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(SyncCursorPagination[ObjectiveTask], task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Cadenya) -> None:
        with client.objectives.tasks.with_streaming_response.list(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(SyncCursorPagination[ObjectiveTask], task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.objectives.tasks.with_raw_response.list(
                objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `objective_id` but received ''"):
            client.objectives.tasks.with_raw_response.list(
                objective_id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )


class TestAsyncTasks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCadenya) -> None:
        task = await async_client.objectives.tasks.retrieve(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            id="id",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert_matches_type(ObjectiveTask, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCadenya) -> None:
        response = await async_client.objectives.tasks.with_raw_response.retrieve(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            id="id",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(ObjectiveTask, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCadenya) -> None:
        async with async_client.objectives.tasks.with_streaming_response.retrieve(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            id="id",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(ObjectiveTask, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.objectives.tasks.with_raw_response.retrieve(
                objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
                id="id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `objective_id` but received ''"):
            await async_client.objectives.tasks.with_raw_response.retrieve(
                objective_id="",
                id="id",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.objectives.tasks.with_raw_response.retrieve(
                objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
                id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCadenya) -> None:
        task = await async_client.objectives.tasks.list(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert_matches_type(AsyncCursorPagination[ObjectiveTask], task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCadenya) -> None:
        task = await async_client.objectives.tasks.list(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            cursor="cursor",
            limit=0,
            sort_order="sortOrder",
        )
        assert_matches_type(AsyncCursorPagination[ObjectiveTask], task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCadenya) -> None:
        response = await async_client.objectives.tasks.with_raw_response.list(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(AsyncCursorPagination[ObjectiveTask], task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCadenya) -> None:
        async with async_client.objectives.tasks.with_streaming_response.list(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(AsyncCursorPagination[ObjectiveTask], task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.objectives.tasks.with_raw_response.list(
                objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `objective_id` but received ''"):
            await async_client.objectives.tasks.with_raw_response.list(
                objective_id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )
