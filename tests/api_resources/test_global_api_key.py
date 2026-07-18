# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cadenya import Cadenya, AsyncCadenya
from tests.utils import assert_matches_type
from cadenya.types import APIKey

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGlobalAPIKey:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Cadenya) -> None:
        global_api_key = client.global_api_key.retrieve()
        assert_matches_type(APIKey, global_api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Cadenya) -> None:
        response = client.global_api_key.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        global_api_key = response.parse()
        assert_matches_type(APIKey, global_api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Cadenya) -> None:
        with client.global_api_key.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            global_api_key = response.parse()
            assert_matches_type(APIKey, global_api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_disable(self, client: Cadenya) -> None:
        global_api_key = client.global_api_key.disable()
        assert_matches_type(APIKey, global_api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_disable(self, client: Cadenya) -> None:
        response = client.global_api_key.with_raw_response.disable()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        global_api_key = response.parse()
        assert_matches_type(APIKey, global_api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_disable(self, client: Cadenya) -> None:
        with client.global_api_key.with_streaming_response.disable() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            global_api_key = response.parse()
            assert_matches_type(APIKey, global_api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_enable(self, client: Cadenya) -> None:
        global_api_key = client.global_api_key.enable()
        assert_matches_type(APIKey, global_api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_enable(self, client: Cadenya) -> None:
        response = client.global_api_key.with_raw_response.enable()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        global_api_key = response.parse()
        assert_matches_type(APIKey, global_api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_enable(self, client: Cadenya) -> None:
        with client.global_api_key.with_streaming_response.enable() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            global_api_key = response.parse()
            assert_matches_type(APIKey, global_api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rotate(self, client: Cadenya) -> None:
        global_api_key = client.global_api_key.rotate()
        assert_matches_type(APIKey, global_api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_rotate(self, client: Cadenya) -> None:
        response = client.global_api_key.with_raw_response.rotate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        global_api_key = response.parse()
        assert_matches_type(APIKey, global_api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_rotate(self, client: Cadenya) -> None:
        with client.global_api_key.with_streaming_response.rotate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            global_api_key = response.parse()
            assert_matches_type(APIKey, global_api_key, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncGlobalAPIKey:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCadenya) -> None:
        global_api_key = await async_client.global_api_key.retrieve()
        assert_matches_type(APIKey, global_api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCadenya) -> None:
        response = await async_client.global_api_key.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        global_api_key = await response.parse()
        assert_matches_type(APIKey, global_api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCadenya) -> None:
        async with async_client.global_api_key.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            global_api_key = await response.parse()
            assert_matches_type(APIKey, global_api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_disable(self, async_client: AsyncCadenya) -> None:
        global_api_key = await async_client.global_api_key.disable()
        assert_matches_type(APIKey, global_api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_disable(self, async_client: AsyncCadenya) -> None:
        response = await async_client.global_api_key.with_raw_response.disable()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        global_api_key = await response.parse()
        assert_matches_type(APIKey, global_api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_disable(self, async_client: AsyncCadenya) -> None:
        async with async_client.global_api_key.with_streaming_response.disable() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            global_api_key = await response.parse()
            assert_matches_type(APIKey, global_api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_enable(self, async_client: AsyncCadenya) -> None:
        global_api_key = await async_client.global_api_key.enable()
        assert_matches_type(APIKey, global_api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_enable(self, async_client: AsyncCadenya) -> None:
        response = await async_client.global_api_key.with_raw_response.enable()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        global_api_key = await response.parse()
        assert_matches_type(APIKey, global_api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_enable(self, async_client: AsyncCadenya) -> None:
        async with async_client.global_api_key.with_streaming_response.enable() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            global_api_key = await response.parse()
            assert_matches_type(APIKey, global_api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rotate(self, async_client: AsyncCadenya) -> None:
        global_api_key = await async_client.global_api_key.rotate()
        assert_matches_type(APIKey, global_api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_rotate(self, async_client: AsyncCadenya) -> None:
        response = await async_client.global_api_key.with_raw_response.rotate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        global_api_key = await response.parse()
        assert_matches_type(APIKey, global_api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_rotate(self, async_client: AsyncCadenya) -> None:
        async with async_client.global_api_key.with_streaming_response.rotate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            global_api_key = await response.parse()
            assert_matches_type(APIKey, global_api_key, path=["response"])

        assert cast(Any, response.is_closed) is True
