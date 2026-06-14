# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cadenya import Cadenya, AsyncCadenya
from tests.utils import assert_matches_type
from cadenya.pagination import SyncCursorPagination, AsyncCursorPagination
from cadenya.types.tool_sets import (
    ToolSetSecret,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSecrets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Cadenya) -> None:
        secret = client.tool_sets.secrets.create(
            tool_set_id="toolSetId",
            workspace_id="workspaceId",
            metadata={"name": "name"},
            spec={},
        )
        assert_matches_type(ToolSetSecret, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Cadenya) -> None:
        secret = client.tool_sets.secrets.create(
            tool_set_id="toolSetId",
            workspace_id="workspaceId",
            metadata={
                "name": "name",
                "bundle_key": "bundleKey",
                "external_id": "externalId",
                "labels": {"foo": "string"},
            },
            spec={"value": "value"},
        )
        assert_matches_type(ToolSetSecret, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Cadenya) -> None:
        response = client.tool_sets.secrets.with_raw_response.create(
            tool_set_id="toolSetId",
            workspace_id="workspaceId",
            metadata={"name": "name"},
            spec={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(ToolSetSecret, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Cadenya) -> None:
        with client.tool_sets.secrets.with_streaming_response.create(
            tool_set_id="toolSetId",
            workspace_id="workspaceId",
            metadata={"name": "name"},
            spec={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(ToolSetSecret, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.tool_sets.secrets.with_raw_response.create(
                tool_set_id="toolSetId",
                workspace_id="",
                metadata={"name": "name"},
                spec={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_set_id` but received ''"):
            client.tool_sets.secrets.with_raw_response.create(
                tool_set_id="",
                workspace_id="workspaceId",
                metadata={"name": "name"},
                spec={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Cadenya) -> None:
        secret = client.tool_sets.secrets.retrieve(
            id="id",
            workspace_id="workspaceId",
            tool_set_id="toolSetId",
        )
        assert_matches_type(ToolSetSecret, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Cadenya) -> None:
        response = client.tool_sets.secrets.with_raw_response.retrieve(
            id="id",
            workspace_id="workspaceId",
            tool_set_id="toolSetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(ToolSetSecret, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Cadenya) -> None:
        with client.tool_sets.secrets.with_streaming_response.retrieve(
            id="id",
            workspace_id="workspaceId",
            tool_set_id="toolSetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(ToolSetSecret, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.tool_sets.secrets.with_raw_response.retrieve(
                id="id",
                workspace_id="",
                tool_set_id="toolSetId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_set_id` but received ''"):
            client.tool_sets.secrets.with_raw_response.retrieve(
                id="id",
                workspace_id="workspaceId",
                tool_set_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tool_sets.secrets.with_raw_response.retrieve(
                id="",
                workspace_id="workspaceId",
                tool_set_id="toolSetId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Cadenya) -> None:
        secret = client.tool_sets.secrets.update(
            id="id",
            workspace_id="workspaceId",
            tool_set_id="toolSetId",
        )
        assert_matches_type(ToolSetSecret, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Cadenya) -> None:
        secret = client.tool_sets.secrets.update(
            id="id",
            workspace_id="workspaceId",
            tool_set_id="toolSetId",
            metadata={
                "name": "name",
                "bundle_key": "bundleKey",
                "external_id": "externalId",
                "labels": {"foo": "string"},
            },
            spec={"value": "value"},
            update_mask="updateMask",
        )
        assert_matches_type(ToolSetSecret, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Cadenya) -> None:
        response = client.tool_sets.secrets.with_raw_response.update(
            id="id",
            workspace_id="workspaceId",
            tool_set_id="toolSetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(ToolSetSecret, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Cadenya) -> None:
        with client.tool_sets.secrets.with_streaming_response.update(
            id="id",
            workspace_id="workspaceId",
            tool_set_id="toolSetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(ToolSetSecret, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.tool_sets.secrets.with_raw_response.update(
                id="id",
                workspace_id="",
                tool_set_id="toolSetId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_set_id` but received ''"):
            client.tool_sets.secrets.with_raw_response.update(
                id="id",
                workspace_id="workspaceId",
                tool_set_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tool_sets.secrets.with_raw_response.update(
                id="",
                workspace_id="workspaceId",
                tool_set_id="toolSetId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Cadenya) -> None:
        secret = client.tool_sets.secrets.list(
            tool_set_id="toolSetId",
            workspace_id="workspaceId",
        )
        assert_matches_type(SyncCursorPagination[ToolSetSecret], secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Cadenya) -> None:
        secret = client.tool_sets.secrets.list(
            tool_set_id="toolSetId",
            workspace_id="workspaceId",
            bundle_key="bundleKey",
            cursor="cursor",
            include_info=True,
            limit=0,
            prefix="prefix",
            query="query",
            sort_order="sortOrder",
        )
        assert_matches_type(SyncCursorPagination[ToolSetSecret], secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Cadenya) -> None:
        response = client.tool_sets.secrets.with_raw_response.list(
            tool_set_id="toolSetId",
            workspace_id="workspaceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(SyncCursorPagination[ToolSetSecret], secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Cadenya) -> None:
        with client.tool_sets.secrets.with_streaming_response.list(
            tool_set_id="toolSetId",
            workspace_id="workspaceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(SyncCursorPagination[ToolSetSecret], secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.tool_sets.secrets.with_raw_response.list(
                tool_set_id="toolSetId",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_set_id` but received ''"):
            client.tool_sets.secrets.with_raw_response.list(
                tool_set_id="",
                workspace_id="workspaceId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Cadenya) -> None:
        secret = client.tool_sets.secrets.delete(
            id="id",
            workspace_id="workspaceId",
            tool_set_id="toolSetId",
        )
        assert secret is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Cadenya) -> None:
        response = client.tool_sets.secrets.with_raw_response.delete(
            id="id",
            workspace_id="workspaceId",
            tool_set_id="toolSetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert secret is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Cadenya) -> None:
        with client.tool_sets.secrets.with_streaming_response.delete(
            id="id",
            workspace_id="workspaceId",
            tool_set_id="toolSetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert secret is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.tool_sets.secrets.with_raw_response.delete(
                id="id",
                workspace_id="",
                tool_set_id="toolSetId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_set_id` but received ''"):
            client.tool_sets.secrets.with_raw_response.delete(
                id="id",
                workspace_id="workspaceId",
                tool_set_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tool_sets.secrets.with_raw_response.delete(
                id="",
                workspace_id="workspaceId",
                tool_set_id="toolSetId",
            )


class TestAsyncSecrets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCadenya) -> None:
        secret = await async_client.tool_sets.secrets.create(
            tool_set_id="toolSetId",
            workspace_id="workspaceId",
            metadata={"name": "name"},
            spec={},
        )
        assert_matches_type(ToolSetSecret, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCadenya) -> None:
        secret = await async_client.tool_sets.secrets.create(
            tool_set_id="toolSetId",
            workspace_id="workspaceId",
            metadata={
                "name": "name",
                "bundle_key": "bundleKey",
                "external_id": "externalId",
                "labels": {"foo": "string"},
            },
            spec={"value": "value"},
        )
        assert_matches_type(ToolSetSecret, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCadenya) -> None:
        response = await async_client.tool_sets.secrets.with_raw_response.create(
            tool_set_id="toolSetId",
            workspace_id="workspaceId",
            metadata={"name": "name"},
            spec={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(ToolSetSecret, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCadenya) -> None:
        async with async_client.tool_sets.secrets.with_streaming_response.create(
            tool_set_id="toolSetId",
            workspace_id="workspaceId",
            metadata={"name": "name"},
            spec={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(ToolSetSecret, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.tool_sets.secrets.with_raw_response.create(
                tool_set_id="toolSetId",
                workspace_id="",
                metadata={"name": "name"},
                spec={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_set_id` but received ''"):
            await async_client.tool_sets.secrets.with_raw_response.create(
                tool_set_id="",
                workspace_id="workspaceId",
                metadata={"name": "name"},
                spec={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCadenya) -> None:
        secret = await async_client.tool_sets.secrets.retrieve(
            id="id",
            workspace_id="workspaceId",
            tool_set_id="toolSetId",
        )
        assert_matches_type(ToolSetSecret, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCadenya) -> None:
        response = await async_client.tool_sets.secrets.with_raw_response.retrieve(
            id="id",
            workspace_id="workspaceId",
            tool_set_id="toolSetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(ToolSetSecret, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCadenya) -> None:
        async with async_client.tool_sets.secrets.with_streaming_response.retrieve(
            id="id",
            workspace_id="workspaceId",
            tool_set_id="toolSetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(ToolSetSecret, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.tool_sets.secrets.with_raw_response.retrieve(
                id="id",
                workspace_id="",
                tool_set_id="toolSetId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_set_id` but received ''"):
            await async_client.tool_sets.secrets.with_raw_response.retrieve(
                id="id",
                workspace_id="workspaceId",
                tool_set_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tool_sets.secrets.with_raw_response.retrieve(
                id="",
                workspace_id="workspaceId",
                tool_set_id="toolSetId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncCadenya) -> None:
        secret = await async_client.tool_sets.secrets.update(
            id="id",
            workspace_id="workspaceId",
            tool_set_id="toolSetId",
        )
        assert_matches_type(ToolSetSecret, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCadenya) -> None:
        secret = await async_client.tool_sets.secrets.update(
            id="id",
            workspace_id="workspaceId",
            tool_set_id="toolSetId",
            metadata={
                "name": "name",
                "bundle_key": "bundleKey",
                "external_id": "externalId",
                "labels": {"foo": "string"},
            },
            spec={"value": "value"},
            update_mask="updateMask",
        )
        assert_matches_type(ToolSetSecret, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCadenya) -> None:
        response = await async_client.tool_sets.secrets.with_raw_response.update(
            id="id",
            workspace_id="workspaceId",
            tool_set_id="toolSetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(ToolSetSecret, secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCadenya) -> None:
        async with async_client.tool_sets.secrets.with_streaming_response.update(
            id="id",
            workspace_id="workspaceId",
            tool_set_id="toolSetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(ToolSetSecret, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.tool_sets.secrets.with_raw_response.update(
                id="id",
                workspace_id="",
                tool_set_id="toolSetId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_set_id` but received ''"):
            await async_client.tool_sets.secrets.with_raw_response.update(
                id="id",
                workspace_id="workspaceId",
                tool_set_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tool_sets.secrets.with_raw_response.update(
                id="",
                workspace_id="workspaceId",
                tool_set_id="toolSetId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCadenya) -> None:
        secret = await async_client.tool_sets.secrets.list(
            tool_set_id="toolSetId",
            workspace_id="workspaceId",
        )
        assert_matches_type(AsyncCursorPagination[ToolSetSecret], secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCadenya) -> None:
        secret = await async_client.tool_sets.secrets.list(
            tool_set_id="toolSetId",
            workspace_id="workspaceId",
            bundle_key="bundleKey",
            cursor="cursor",
            include_info=True,
            limit=0,
            prefix="prefix",
            query="query",
            sort_order="sortOrder",
        )
        assert_matches_type(AsyncCursorPagination[ToolSetSecret], secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCadenya) -> None:
        response = await async_client.tool_sets.secrets.with_raw_response.list(
            tool_set_id="toolSetId",
            workspace_id="workspaceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(AsyncCursorPagination[ToolSetSecret], secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCadenya) -> None:
        async with async_client.tool_sets.secrets.with_streaming_response.list(
            tool_set_id="toolSetId",
            workspace_id="workspaceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(AsyncCursorPagination[ToolSetSecret], secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.tool_sets.secrets.with_raw_response.list(
                tool_set_id="toolSetId",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_set_id` but received ''"):
            await async_client.tool_sets.secrets.with_raw_response.list(
                tool_set_id="",
                workspace_id="workspaceId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCadenya) -> None:
        secret = await async_client.tool_sets.secrets.delete(
            id="id",
            workspace_id="workspaceId",
            tool_set_id="toolSetId",
        )
        assert secret is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCadenya) -> None:
        response = await async_client.tool_sets.secrets.with_raw_response.delete(
            id="id",
            workspace_id="workspaceId",
            tool_set_id="toolSetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert secret is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCadenya) -> None:
        async with async_client.tool_sets.secrets.with_streaming_response.delete(
            id="id",
            workspace_id="workspaceId",
            tool_set_id="toolSetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert secret is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.tool_sets.secrets.with_raw_response.delete(
                id="id",
                workspace_id="",
                tool_set_id="toolSetId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_set_id` but received ''"):
            await async_client.tool_sets.secrets.with_raw_response.delete(
                id="id",
                workspace_id="workspaceId",
                tool_set_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tool_sets.secrets.with_raw_response.delete(
                id="",
                workspace_id="workspaceId",
                tool_set_id="toolSetId",
            )
