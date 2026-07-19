# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cadenya import Cadenya, AsyncCadenya
from tests.utils import assert_matches_type
from cadenya.types import (
    MemoryLayer,
)
from cadenya.pagination import SyncCursorPagination, AsyncCursorPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMemoryLayers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Cadenya) -> None:
        memory_layer = client.memory_layers.create(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            metadata={"name": "name"},
            spec={"type": "MEMORY_LAYER_TYPE_UNSPECIFIED"},
        )
        assert_matches_type(MemoryLayer, memory_layer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Cadenya) -> None:
        memory_layer = client.memory_layers.create(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            metadata={
                "name": "name",
                "external_id": "externalId",
                "labels": {"foo": "string"},
            },
            spec={
                "type": "MEMORY_LAYER_TYPE_UNSPECIFIED",
                "description": "description",
            },
        )
        assert_matches_type(MemoryLayer, memory_layer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Cadenya) -> None:
        response = client.memory_layers.with_raw_response.create(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            metadata={"name": "name"},
            spec={"type": "MEMORY_LAYER_TYPE_UNSPECIFIED"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory_layer = response.parse()
        assert_matches_type(MemoryLayer, memory_layer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Cadenya) -> None:
        with client.memory_layers.with_streaming_response.create(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            metadata={"name": "name"},
            spec={"type": "MEMORY_LAYER_TYPE_UNSPECIFIED"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory_layer = response.parse()
            assert_matches_type(MemoryLayer, memory_layer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.memory_layers.with_raw_response.create(
                workspace_id="",
                metadata={"name": "name"},
                spec={"type": "MEMORY_LAYER_TYPE_UNSPECIFIED"},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Cadenya) -> None:
        memory_layer = client.memory_layers.retrieve(
            id="memlyr_01HXKD2E5NQM3T9AYWCFFFBMJH",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert_matches_type(MemoryLayer, memory_layer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Cadenya) -> None:
        response = client.memory_layers.with_raw_response.retrieve(
            id="memlyr_01HXKD2E5NQM3T9AYWCFFFBMJH",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory_layer = response.parse()
        assert_matches_type(MemoryLayer, memory_layer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Cadenya) -> None:
        with client.memory_layers.with_streaming_response.retrieve(
            id="memlyr_01HXKD2E5NQM3T9AYWCFFFBMJH",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory_layer = response.parse()
            assert_matches_type(MemoryLayer, memory_layer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.memory_layers.with_raw_response.retrieve(
                id="memlyr_01HXKD2E5NQM3T9AYWCFFFBMJH",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.memory_layers.with_raw_response.retrieve(
                id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Cadenya) -> None:
        memory_layer = client.memory_layers.update(
            id="memlyr_01HXKD2E5NQM3T9AYWCFFFBMJH",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert_matches_type(MemoryLayer, memory_layer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Cadenya) -> None:
        memory_layer = client.memory_layers.update(
            id="memlyr_01HXKD2E5NQM3T9AYWCFFFBMJH",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            metadata={
                "name": "name",
                "external_id": "externalId",
                "labels": {"foo": "string"},
            },
            spec={
                "type": "MEMORY_LAYER_TYPE_UNSPECIFIED",
                "description": "description",
            },
            update_mask="updateMask",
        )
        assert_matches_type(MemoryLayer, memory_layer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Cadenya) -> None:
        response = client.memory_layers.with_raw_response.update(
            id="memlyr_01HXKD2E5NQM3T9AYWCFFFBMJH",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory_layer = response.parse()
        assert_matches_type(MemoryLayer, memory_layer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Cadenya) -> None:
        with client.memory_layers.with_streaming_response.update(
            id="memlyr_01HXKD2E5NQM3T9AYWCFFFBMJH",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory_layer = response.parse()
            assert_matches_type(MemoryLayer, memory_layer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.memory_layers.with_raw_response.update(
                id="memlyr_01HXKD2E5NQM3T9AYWCFFFBMJH",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.memory_layers.with_raw_response.update(
                id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Cadenya) -> None:
        memory_layer = client.memory_layers.list(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert_matches_type(SyncCursorPagination[MemoryLayer], memory_layer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Cadenya) -> None:
        memory_layer = client.memory_layers.list(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            cursor="cursor",
            episodic_key_prefix="episodicKeyPrefix",
            include_info=True,
            labels="labels",
            limit=0,
            prefix="prefix",
            query="query",
            sort_order="sortOrder",
            type="MEMORY_LAYER_TYPE_UNSPECIFIED",
        )
        assert_matches_type(SyncCursorPagination[MemoryLayer], memory_layer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Cadenya) -> None:
        response = client.memory_layers.with_raw_response.list(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory_layer = response.parse()
        assert_matches_type(SyncCursorPagination[MemoryLayer], memory_layer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Cadenya) -> None:
        with client.memory_layers.with_streaming_response.list(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory_layer = response.parse()
            assert_matches_type(SyncCursorPagination[MemoryLayer], memory_layer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.memory_layers.with_raw_response.list(
                workspace_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Cadenya) -> None:
        memory_layer = client.memory_layers.delete(
            id="memlyr_01HXKD2E5NQM3T9AYWCFFFBMJH",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert memory_layer is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Cadenya) -> None:
        response = client.memory_layers.with_raw_response.delete(
            id="memlyr_01HXKD2E5NQM3T9AYWCFFFBMJH",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory_layer = response.parse()
        assert memory_layer is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Cadenya) -> None:
        with client.memory_layers.with_streaming_response.delete(
            id="memlyr_01HXKD2E5NQM3T9AYWCFFFBMJH",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory_layer = response.parse()
            assert memory_layer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.memory_layers.with_raw_response.delete(
                id="memlyr_01HXKD2E5NQM3T9AYWCFFFBMJH",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.memory_layers.with_raw_response.delete(
                id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )


class TestAsyncMemoryLayers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCadenya) -> None:
        memory_layer = await async_client.memory_layers.create(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            metadata={"name": "name"},
            spec={"type": "MEMORY_LAYER_TYPE_UNSPECIFIED"},
        )
        assert_matches_type(MemoryLayer, memory_layer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCadenya) -> None:
        memory_layer = await async_client.memory_layers.create(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            metadata={
                "name": "name",
                "external_id": "externalId",
                "labels": {"foo": "string"},
            },
            spec={
                "type": "MEMORY_LAYER_TYPE_UNSPECIFIED",
                "description": "description",
            },
        )
        assert_matches_type(MemoryLayer, memory_layer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCadenya) -> None:
        response = await async_client.memory_layers.with_raw_response.create(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            metadata={"name": "name"},
            spec={"type": "MEMORY_LAYER_TYPE_UNSPECIFIED"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory_layer = await response.parse()
        assert_matches_type(MemoryLayer, memory_layer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCadenya) -> None:
        async with async_client.memory_layers.with_streaming_response.create(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            metadata={"name": "name"},
            spec={"type": "MEMORY_LAYER_TYPE_UNSPECIFIED"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory_layer = await response.parse()
            assert_matches_type(MemoryLayer, memory_layer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.memory_layers.with_raw_response.create(
                workspace_id="",
                metadata={"name": "name"},
                spec={"type": "MEMORY_LAYER_TYPE_UNSPECIFIED"},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCadenya) -> None:
        memory_layer = await async_client.memory_layers.retrieve(
            id="memlyr_01HXKD2E5NQM3T9AYWCFFFBMJH",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert_matches_type(MemoryLayer, memory_layer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCadenya) -> None:
        response = await async_client.memory_layers.with_raw_response.retrieve(
            id="memlyr_01HXKD2E5NQM3T9AYWCFFFBMJH",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory_layer = await response.parse()
        assert_matches_type(MemoryLayer, memory_layer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCadenya) -> None:
        async with async_client.memory_layers.with_streaming_response.retrieve(
            id="memlyr_01HXKD2E5NQM3T9AYWCFFFBMJH",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory_layer = await response.parse()
            assert_matches_type(MemoryLayer, memory_layer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.memory_layers.with_raw_response.retrieve(
                id="memlyr_01HXKD2E5NQM3T9AYWCFFFBMJH",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.memory_layers.with_raw_response.retrieve(
                id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncCadenya) -> None:
        memory_layer = await async_client.memory_layers.update(
            id="memlyr_01HXKD2E5NQM3T9AYWCFFFBMJH",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert_matches_type(MemoryLayer, memory_layer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCadenya) -> None:
        memory_layer = await async_client.memory_layers.update(
            id="memlyr_01HXKD2E5NQM3T9AYWCFFFBMJH",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            metadata={
                "name": "name",
                "external_id": "externalId",
                "labels": {"foo": "string"},
            },
            spec={
                "type": "MEMORY_LAYER_TYPE_UNSPECIFIED",
                "description": "description",
            },
            update_mask="updateMask",
        )
        assert_matches_type(MemoryLayer, memory_layer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCadenya) -> None:
        response = await async_client.memory_layers.with_raw_response.update(
            id="memlyr_01HXKD2E5NQM3T9AYWCFFFBMJH",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory_layer = await response.parse()
        assert_matches_type(MemoryLayer, memory_layer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCadenya) -> None:
        async with async_client.memory_layers.with_streaming_response.update(
            id="memlyr_01HXKD2E5NQM3T9AYWCFFFBMJH",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory_layer = await response.parse()
            assert_matches_type(MemoryLayer, memory_layer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.memory_layers.with_raw_response.update(
                id="memlyr_01HXKD2E5NQM3T9AYWCFFFBMJH",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.memory_layers.with_raw_response.update(
                id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCadenya) -> None:
        memory_layer = await async_client.memory_layers.list(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert_matches_type(AsyncCursorPagination[MemoryLayer], memory_layer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCadenya) -> None:
        memory_layer = await async_client.memory_layers.list(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            cursor="cursor",
            episodic_key_prefix="episodicKeyPrefix",
            include_info=True,
            labels="labels",
            limit=0,
            prefix="prefix",
            query="query",
            sort_order="sortOrder",
            type="MEMORY_LAYER_TYPE_UNSPECIFIED",
        )
        assert_matches_type(AsyncCursorPagination[MemoryLayer], memory_layer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCadenya) -> None:
        response = await async_client.memory_layers.with_raw_response.list(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory_layer = await response.parse()
        assert_matches_type(AsyncCursorPagination[MemoryLayer], memory_layer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCadenya) -> None:
        async with async_client.memory_layers.with_streaming_response.list(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory_layer = await response.parse()
            assert_matches_type(AsyncCursorPagination[MemoryLayer], memory_layer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.memory_layers.with_raw_response.list(
                workspace_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCadenya) -> None:
        memory_layer = await async_client.memory_layers.delete(
            id="memlyr_01HXKD2E5NQM3T9AYWCFFFBMJH",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert memory_layer is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCadenya) -> None:
        response = await async_client.memory_layers.with_raw_response.delete(
            id="memlyr_01HXKD2E5NQM3T9AYWCFFFBMJH",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory_layer = await response.parse()
        assert memory_layer is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCadenya) -> None:
        async with async_client.memory_layers.with_streaming_response.delete(
            id="memlyr_01HXKD2E5NQM3T9AYWCFFFBMJH",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory_layer = await response.parse()
            assert memory_layer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.memory_layers.with_raw_response.delete(
                id="memlyr_01HXKD2E5NQM3T9AYWCFFFBMJH",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.memory_layers.with_raw_response.delete(
                id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )
