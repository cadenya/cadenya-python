# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cadenya import Cadenya, AsyncCadenya
from tests.utils import assert_matches_type
from cadenya.pagination import SyncCursorPagination, AsyncCursorPagination
from cadenya.types.memory_layers import (
    MemoryEntry,
    MemoryEntryDetail,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEntries:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Cadenya) -> None:
        entry = client.memory_layers.entries.create(
            memory_layer_id="memoryLayerId",
            workspace_id="workspaceId",
            metadata={"name": "name"},
            spec={"key": "key"},
        )
        assert_matches_type(MemoryEntryDetail, entry, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Cadenya) -> None:
        entry = client.memory_layers.entries.create(
            memory_layer_id="memoryLayerId",
            workspace_id="workspaceId",
            metadata={
                "name": "name",
                "external_id": "externalId",
                "labels": {"foo": "string"},
            },
            spec={
                "key": "key",
                "content": "content",
                "description": "description",
                "upload_id": "uploadId",
            },
        )
        assert_matches_type(MemoryEntryDetail, entry, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Cadenya) -> None:
        response = client.memory_layers.entries.with_raw_response.create(
            memory_layer_id="memoryLayerId",
            workspace_id="workspaceId",
            metadata={"name": "name"},
            spec={"key": "key"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entry = response.parse()
        assert_matches_type(MemoryEntryDetail, entry, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Cadenya) -> None:
        with client.memory_layers.entries.with_streaming_response.create(
            memory_layer_id="memoryLayerId",
            workspace_id="workspaceId",
            metadata={"name": "name"},
            spec={"key": "key"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entry = response.parse()
            assert_matches_type(MemoryEntryDetail, entry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.memory_layers.entries.with_raw_response.create(
                memory_layer_id="memoryLayerId",
                workspace_id="",
                metadata={"name": "name"},
                spec={"key": "key"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `memory_layer_id` but received ''"):
            client.memory_layers.entries.with_raw_response.create(
                memory_layer_id="",
                workspace_id="workspaceId",
                metadata={"name": "name"},
                spec={"key": "key"},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Cadenya) -> None:
        entry = client.memory_layers.entries.retrieve(
            id="id",
            workspace_id="workspaceId",
            memory_layer_id="memoryLayerId",
        )
        assert_matches_type(MemoryEntryDetail, entry, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Cadenya) -> None:
        response = client.memory_layers.entries.with_raw_response.retrieve(
            id="id",
            workspace_id="workspaceId",
            memory_layer_id="memoryLayerId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entry = response.parse()
        assert_matches_type(MemoryEntryDetail, entry, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Cadenya) -> None:
        with client.memory_layers.entries.with_streaming_response.retrieve(
            id="id",
            workspace_id="workspaceId",
            memory_layer_id="memoryLayerId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entry = response.parse()
            assert_matches_type(MemoryEntryDetail, entry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.memory_layers.entries.with_raw_response.retrieve(
                id="id",
                workspace_id="",
                memory_layer_id="memoryLayerId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `memory_layer_id` but received ''"):
            client.memory_layers.entries.with_raw_response.retrieve(
                id="id",
                workspace_id="workspaceId",
                memory_layer_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.memory_layers.entries.with_raw_response.retrieve(
                id="",
                workspace_id="workspaceId",
                memory_layer_id="memoryLayerId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Cadenya) -> None:
        entry = client.memory_layers.entries.update(
            id="id",
            workspace_id="workspaceId",
            memory_layer_id="memoryLayerId",
        )
        assert_matches_type(MemoryEntryDetail, entry, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Cadenya) -> None:
        entry = client.memory_layers.entries.update(
            id="id",
            workspace_id="workspaceId",
            memory_layer_id="memoryLayerId",
            metadata={
                "name": "name",
                "external_id": "externalId",
                "labels": {"foo": "string"},
            },
            spec={
                "content": "content",
                "description": "description",
                "key": "key",
                "upload_id": "uploadId",
            },
            update_mask="updateMask",
        )
        assert_matches_type(MemoryEntryDetail, entry, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Cadenya) -> None:
        response = client.memory_layers.entries.with_raw_response.update(
            id="id",
            workspace_id="workspaceId",
            memory_layer_id="memoryLayerId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entry = response.parse()
        assert_matches_type(MemoryEntryDetail, entry, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Cadenya) -> None:
        with client.memory_layers.entries.with_streaming_response.update(
            id="id",
            workspace_id="workspaceId",
            memory_layer_id="memoryLayerId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entry = response.parse()
            assert_matches_type(MemoryEntryDetail, entry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.memory_layers.entries.with_raw_response.update(
                id="id",
                workspace_id="",
                memory_layer_id="memoryLayerId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `memory_layer_id` but received ''"):
            client.memory_layers.entries.with_raw_response.update(
                id="id",
                workspace_id="workspaceId",
                memory_layer_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.memory_layers.entries.with_raw_response.update(
                id="",
                workspace_id="workspaceId",
                memory_layer_id="memoryLayerId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Cadenya) -> None:
        entry = client.memory_layers.entries.list(
            memory_layer_id="memoryLayerId",
            workspace_id="workspaceId",
        )
        assert_matches_type(SyncCursorPagination[MemoryEntry], entry, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Cadenya) -> None:
        entry = client.memory_layers.entries.list(
            memory_layer_id="memoryLayerId",
            workspace_id="workspaceId",
            cursor="cursor",
            include_info=True,
            limit=0,
            prefix="prefix",
            query="query",
            sort_order="sortOrder",
        )
        assert_matches_type(SyncCursorPagination[MemoryEntry], entry, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Cadenya) -> None:
        response = client.memory_layers.entries.with_raw_response.list(
            memory_layer_id="memoryLayerId",
            workspace_id="workspaceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entry = response.parse()
        assert_matches_type(SyncCursorPagination[MemoryEntry], entry, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Cadenya) -> None:
        with client.memory_layers.entries.with_streaming_response.list(
            memory_layer_id="memoryLayerId",
            workspace_id="workspaceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entry = response.parse()
            assert_matches_type(SyncCursorPagination[MemoryEntry], entry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.memory_layers.entries.with_raw_response.list(
                memory_layer_id="memoryLayerId",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `memory_layer_id` but received ''"):
            client.memory_layers.entries.with_raw_response.list(
                memory_layer_id="",
                workspace_id="workspaceId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Cadenya) -> None:
        entry = client.memory_layers.entries.delete(
            id="id",
            workspace_id="workspaceId",
            memory_layer_id="memoryLayerId",
        )
        assert entry is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Cadenya) -> None:
        response = client.memory_layers.entries.with_raw_response.delete(
            id="id",
            workspace_id="workspaceId",
            memory_layer_id="memoryLayerId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entry = response.parse()
        assert entry is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Cadenya) -> None:
        with client.memory_layers.entries.with_streaming_response.delete(
            id="id",
            workspace_id="workspaceId",
            memory_layer_id="memoryLayerId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entry = response.parse()
            assert entry is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.memory_layers.entries.with_raw_response.delete(
                id="id",
                workspace_id="",
                memory_layer_id="memoryLayerId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `memory_layer_id` but received ''"):
            client.memory_layers.entries.with_raw_response.delete(
                id="id",
                workspace_id="workspaceId",
                memory_layer_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.memory_layers.entries.with_raw_response.delete(
                id="",
                workspace_id="workspaceId",
                memory_layer_id="memoryLayerId",
            )


class TestAsyncEntries:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCadenya) -> None:
        entry = await async_client.memory_layers.entries.create(
            memory_layer_id="memoryLayerId",
            workspace_id="workspaceId",
            metadata={"name": "name"},
            spec={"key": "key"},
        )
        assert_matches_type(MemoryEntryDetail, entry, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCadenya) -> None:
        entry = await async_client.memory_layers.entries.create(
            memory_layer_id="memoryLayerId",
            workspace_id="workspaceId",
            metadata={
                "name": "name",
                "external_id": "externalId",
                "labels": {"foo": "string"},
            },
            spec={
                "key": "key",
                "content": "content",
                "description": "description",
                "upload_id": "uploadId",
            },
        )
        assert_matches_type(MemoryEntryDetail, entry, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCadenya) -> None:
        response = await async_client.memory_layers.entries.with_raw_response.create(
            memory_layer_id="memoryLayerId",
            workspace_id="workspaceId",
            metadata={"name": "name"},
            spec={"key": "key"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entry = await response.parse()
        assert_matches_type(MemoryEntryDetail, entry, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCadenya) -> None:
        async with async_client.memory_layers.entries.with_streaming_response.create(
            memory_layer_id="memoryLayerId",
            workspace_id="workspaceId",
            metadata={"name": "name"},
            spec={"key": "key"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entry = await response.parse()
            assert_matches_type(MemoryEntryDetail, entry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.memory_layers.entries.with_raw_response.create(
                memory_layer_id="memoryLayerId",
                workspace_id="",
                metadata={"name": "name"},
                spec={"key": "key"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `memory_layer_id` but received ''"):
            await async_client.memory_layers.entries.with_raw_response.create(
                memory_layer_id="",
                workspace_id="workspaceId",
                metadata={"name": "name"},
                spec={"key": "key"},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCadenya) -> None:
        entry = await async_client.memory_layers.entries.retrieve(
            id="id",
            workspace_id="workspaceId",
            memory_layer_id="memoryLayerId",
        )
        assert_matches_type(MemoryEntryDetail, entry, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCadenya) -> None:
        response = await async_client.memory_layers.entries.with_raw_response.retrieve(
            id="id",
            workspace_id="workspaceId",
            memory_layer_id="memoryLayerId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entry = await response.parse()
        assert_matches_type(MemoryEntryDetail, entry, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCadenya) -> None:
        async with async_client.memory_layers.entries.with_streaming_response.retrieve(
            id="id",
            workspace_id="workspaceId",
            memory_layer_id="memoryLayerId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entry = await response.parse()
            assert_matches_type(MemoryEntryDetail, entry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.memory_layers.entries.with_raw_response.retrieve(
                id="id",
                workspace_id="",
                memory_layer_id="memoryLayerId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `memory_layer_id` but received ''"):
            await async_client.memory_layers.entries.with_raw_response.retrieve(
                id="id",
                workspace_id="workspaceId",
                memory_layer_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.memory_layers.entries.with_raw_response.retrieve(
                id="",
                workspace_id="workspaceId",
                memory_layer_id="memoryLayerId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncCadenya) -> None:
        entry = await async_client.memory_layers.entries.update(
            id="id",
            workspace_id="workspaceId",
            memory_layer_id="memoryLayerId",
        )
        assert_matches_type(MemoryEntryDetail, entry, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCadenya) -> None:
        entry = await async_client.memory_layers.entries.update(
            id="id",
            workspace_id="workspaceId",
            memory_layer_id="memoryLayerId",
            metadata={
                "name": "name",
                "external_id": "externalId",
                "labels": {"foo": "string"},
            },
            spec={
                "content": "content",
                "description": "description",
                "key": "key",
                "upload_id": "uploadId",
            },
            update_mask="updateMask",
        )
        assert_matches_type(MemoryEntryDetail, entry, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCadenya) -> None:
        response = await async_client.memory_layers.entries.with_raw_response.update(
            id="id",
            workspace_id="workspaceId",
            memory_layer_id="memoryLayerId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entry = await response.parse()
        assert_matches_type(MemoryEntryDetail, entry, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCadenya) -> None:
        async with async_client.memory_layers.entries.with_streaming_response.update(
            id="id",
            workspace_id="workspaceId",
            memory_layer_id="memoryLayerId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entry = await response.parse()
            assert_matches_type(MemoryEntryDetail, entry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.memory_layers.entries.with_raw_response.update(
                id="id",
                workspace_id="",
                memory_layer_id="memoryLayerId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `memory_layer_id` but received ''"):
            await async_client.memory_layers.entries.with_raw_response.update(
                id="id",
                workspace_id="workspaceId",
                memory_layer_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.memory_layers.entries.with_raw_response.update(
                id="",
                workspace_id="workspaceId",
                memory_layer_id="memoryLayerId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCadenya) -> None:
        entry = await async_client.memory_layers.entries.list(
            memory_layer_id="memoryLayerId",
            workspace_id="workspaceId",
        )
        assert_matches_type(AsyncCursorPagination[MemoryEntry], entry, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCadenya) -> None:
        entry = await async_client.memory_layers.entries.list(
            memory_layer_id="memoryLayerId",
            workspace_id="workspaceId",
            cursor="cursor",
            include_info=True,
            limit=0,
            prefix="prefix",
            query="query",
            sort_order="sortOrder",
        )
        assert_matches_type(AsyncCursorPagination[MemoryEntry], entry, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCadenya) -> None:
        response = await async_client.memory_layers.entries.with_raw_response.list(
            memory_layer_id="memoryLayerId",
            workspace_id="workspaceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entry = await response.parse()
        assert_matches_type(AsyncCursorPagination[MemoryEntry], entry, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCadenya) -> None:
        async with async_client.memory_layers.entries.with_streaming_response.list(
            memory_layer_id="memoryLayerId",
            workspace_id="workspaceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entry = await response.parse()
            assert_matches_type(AsyncCursorPagination[MemoryEntry], entry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.memory_layers.entries.with_raw_response.list(
                memory_layer_id="memoryLayerId",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `memory_layer_id` but received ''"):
            await async_client.memory_layers.entries.with_raw_response.list(
                memory_layer_id="",
                workspace_id="workspaceId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCadenya) -> None:
        entry = await async_client.memory_layers.entries.delete(
            id="id",
            workspace_id="workspaceId",
            memory_layer_id="memoryLayerId",
        )
        assert entry is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCadenya) -> None:
        response = await async_client.memory_layers.entries.with_raw_response.delete(
            id="id",
            workspace_id="workspaceId",
            memory_layer_id="memoryLayerId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entry = await response.parse()
        assert entry is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCadenya) -> None:
        async with async_client.memory_layers.entries.with_streaming_response.delete(
            id="id",
            workspace_id="workspaceId",
            memory_layer_id="memoryLayerId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entry = await response.parse()
            assert entry is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.memory_layers.entries.with_raw_response.delete(
                id="id",
                workspace_id="",
                memory_layer_id="memoryLayerId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `memory_layer_id` but received ''"):
            await async_client.memory_layers.entries.with_raw_response.delete(
                id="id",
                workspace_id="workspaceId",
                memory_layer_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.memory_layers.entries.with_raw_response.delete(
                id="",
                workspace_id="workspaceId",
                memory_layer_id="memoryLayerId",
            )
