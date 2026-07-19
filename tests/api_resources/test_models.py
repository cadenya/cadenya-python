# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cadenya import Cadenya, AsyncCadenya
from tests.utils import assert_matches_type
from cadenya.types import Model
from cadenya.pagination import SyncCursorPagination, AsyncCursorPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestModels:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Cadenya) -> None:
        model = client.models.retrieve(
            id="model_01HXKD2E5NQM3T9AYWCFKJ4GED",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert_matches_type(Model, model, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Cadenya) -> None:
        response = client.models.with_raw_response.retrieve(
            id="model_01HXKD2E5NQM3T9AYWCFKJ4GED",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert_matches_type(Model, model, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Cadenya) -> None:
        with client.models.with_streaming_response.retrieve(
            id="model_01HXKD2E5NQM3T9AYWCFKJ4GED",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = response.parse()
            assert_matches_type(Model, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.models.with_raw_response.retrieve(
                id="model_01HXKD2E5NQM3T9AYWCFKJ4GED",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.models.with_raw_response.retrieve(
                id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Cadenya) -> None:
        model = client.models.list(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert_matches_type(SyncCursorPagination[Model], model, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Cadenya) -> None:
        model = client.models.list(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            ai_provider_key_id="aiProviderKeyId",
            cursor="cursor",
            include_info=True,
            is_assigned=True,
            labels="labels",
            limit=0,
            prefix="prefix",
            query="query",
            sort_order="sortOrder",
            state="STATE_UNSPECIFIED",
        )
        assert_matches_type(SyncCursorPagination[Model], model, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Cadenya) -> None:
        response = client.models.with_raw_response.list(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert_matches_type(SyncCursorPagination[Model], model, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Cadenya) -> None:
        with client.models.with_streaming_response.list(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = response.parse()
            assert_matches_type(SyncCursorPagination[Model], model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.models.with_raw_response.list(
                workspace_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_disable(self, client: Cadenya) -> None:
        model = client.models.disable(
            id="model_01HXKD2E5NQM3T9AYWCFKJ4GED",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert_matches_type(Model, model, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_disable(self, client: Cadenya) -> None:
        response = client.models.with_raw_response.disable(
            id="model_01HXKD2E5NQM3T9AYWCFKJ4GED",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert_matches_type(Model, model, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_disable(self, client: Cadenya) -> None:
        with client.models.with_streaming_response.disable(
            id="model_01HXKD2E5NQM3T9AYWCFKJ4GED",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = response.parse()
            assert_matches_type(Model, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_disable(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.models.with_raw_response.disable(
                id="model_01HXKD2E5NQM3T9AYWCFKJ4GED",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.models.with_raw_response.disable(
                id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_enable(self, client: Cadenya) -> None:
        model = client.models.enable(
            id="model_01HXKD2E5NQM3T9AYWCFKJ4GED",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert_matches_type(Model, model, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_enable(self, client: Cadenya) -> None:
        response = client.models.with_raw_response.enable(
            id="model_01HXKD2E5NQM3T9AYWCFKJ4GED",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert_matches_type(Model, model, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_enable(self, client: Cadenya) -> None:
        with client.models.with_streaming_response.enable(
            id="model_01HXKD2E5NQM3T9AYWCFKJ4GED",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = response.parse()
            assert_matches_type(Model, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_enable(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.models.with_raw_response.enable(
                id="model_01HXKD2E5NQM3T9AYWCFKJ4GED",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.models.with_raw_response.enable(
                id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_swap(self, client: Cadenya) -> None:
        model = client.models.swap(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert_matches_type(object, model, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_swap_with_all_params(self, client: Cadenya) -> None:
        model = client.models.swap(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            model_swaps=[
                {
                    "current_model_id": "model_01HXKD2E5NQM3T9AYWCFKJ4GED",
                    "disable_current_after_swap": True,
                    "next_model_id": "model_01HXKD2E5NQM3T9AYWCFKJ4GED",
                }
            ],
        )
        assert_matches_type(object, model, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_swap(self, client: Cadenya) -> None:
        response = client.models.with_raw_response.swap(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert_matches_type(object, model, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_swap(self, client: Cadenya) -> None:
        with client.models.with_streaming_response.swap(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = response.parse()
            assert_matches_type(object, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_swap(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.models.with_raw_response.swap(
                workspace_id="",
            )


class TestAsyncModels:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCadenya) -> None:
        model = await async_client.models.retrieve(
            id="model_01HXKD2E5NQM3T9AYWCFKJ4GED",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert_matches_type(Model, model, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCadenya) -> None:
        response = await async_client.models.with_raw_response.retrieve(
            id="model_01HXKD2E5NQM3T9AYWCFKJ4GED",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = await response.parse()
        assert_matches_type(Model, model, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCadenya) -> None:
        async with async_client.models.with_streaming_response.retrieve(
            id="model_01HXKD2E5NQM3T9AYWCFKJ4GED",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = await response.parse()
            assert_matches_type(Model, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.models.with_raw_response.retrieve(
                id="model_01HXKD2E5NQM3T9AYWCFKJ4GED",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.models.with_raw_response.retrieve(
                id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCadenya) -> None:
        model = await async_client.models.list(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert_matches_type(AsyncCursorPagination[Model], model, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCadenya) -> None:
        model = await async_client.models.list(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            ai_provider_key_id="aiProviderKeyId",
            cursor="cursor",
            include_info=True,
            is_assigned=True,
            labels="labels",
            limit=0,
            prefix="prefix",
            query="query",
            sort_order="sortOrder",
            state="STATE_UNSPECIFIED",
        )
        assert_matches_type(AsyncCursorPagination[Model], model, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCadenya) -> None:
        response = await async_client.models.with_raw_response.list(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = await response.parse()
        assert_matches_type(AsyncCursorPagination[Model], model, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCadenya) -> None:
        async with async_client.models.with_streaming_response.list(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = await response.parse()
            assert_matches_type(AsyncCursorPagination[Model], model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.models.with_raw_response.list(
                workspace_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_disable(self, async_client: AsyncCadenya) -> None:
        model = await async_client.models.disable(
            id="model_01HXKD2E5NQM3T9AYWCFKJ4GED",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert_matches_type(Model, model, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_disable(self, async_client: AsyncCadenya) -> None:
        response = await async_client.models.with_raw_response.disable(
            id="model_01HXKD2E5NQM3T9AYWCFKJ4GED",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = await response.parse()
        assert_matches_type(Model, model, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_disable(self, async_client: AsyncCadenya) -> None:
        async with async_client.models.with_streaming_response.disable(
            id="model_01HXKD2E5NQM3T9AYWCFKJ4GED",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = await response.parse()
            assert_matches_type(Model, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_disable(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.models.with_raw_response.disable(
                id="model_01HXKD2E5NQM3T9AYWCFKJ4GED",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.models.with_raw_response.disable(
                id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_enable(self, async_client: AsyncCadenya) -> None:
        model = await async_client.models.enable(
            id="model_01HXKD2E5NQM3T9AYWCFKJ4GED",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert_matches_type(Model, model, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_enable(self, async_client: AsyncCadenya) -> None:
        response = await async_client.models.with_raw_response.enable(
            id="model_01HXKD2E5NQM3T9AYWCFKJ4GED",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = await response.parse()
        assert_matches_type(Model, model, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_enable(self, async_client: AsyncCadenya) -> None:
        async with async_client.models.with_streaming_response.enable(
            id="model_01HXKD2E5NQM3T9AYWCFKJ4GED",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = await response.parse()
            assert_matches_type(Model, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_enable(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.models.with_raw_response.enable(
                id="model_01HXKD2E5NQM3T9AYWCFKJ4GED",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.models.with_raw_response.enable(
                id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_swap(self, async_client: AsyncCadenya) -> None:
        model = await async_client.models.swap(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert_matches_type(object, model, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_swap_with_all_params(self, async_client: AsyncCadenya) -> None:
        model = await async_client.models.swap(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            model_swaps=[
                {
                    "current_model_id": "model_01HXKD2E5NQM3T9AYWCFKJ4GED",
                    "disable_current_after_swap": True,
                    "next_model_id": "model_01HXKD2E5NQM3T9AYWCFKJ4GED",
                }
            ],
        )
        assert_matches_type(object, model, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_swap(self, async_client: AsyncCadenya) -> None:
        response = await async_client.models.with_raw_response.swap(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = await response.parse()
        assert_matches_type(object, model, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_swap(self, async_client: AsyncCadenya) -> None:
        async with async_client.models.with_streaming_response.swap(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = await response.parse()
            assert_matches_type(object, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_swap(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.models.with_raw_response.swap(
                workspace_id="",
            )
