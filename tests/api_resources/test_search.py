# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cadenya import Cadenya, AsyncCadenya
from tests.utils import assert_matches_type
from cadenya.types import SearchSearchToolsOrToolSetsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSearch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_tools_or_tool_sets(self, client: Cadenya) -> None:
        search = client.search.search_tools_or_tool_sets(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            query="query",
        )
        assert_matches_type(SearchSearchToolsOrToolSetsResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search_tools_or_tool_sets(self, client: Cadenya) -> None:
        response = client.search.with_raw_response.search_tools_or_tool_sets(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert_matches_type(SearchSearchToolsOrToolSetsResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_search_tools_or_tool_sets(self, client: Cadenya) -> None:
        with client.search.with_streaming_response.search_tools_or_tool_sets(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = response.parse()
            assert_matches_type(SearchSearchToolsOrToolSetsResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_search_tools_or_tool_sets(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.search.with_raw_response.search_tools_or_tool_sets(
                workspace_id="",
                query="query",
            )


class TestAsyncSearch:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_tools_or_tool_sets(self, async_client: AsyncCadenya) -> None:
        search = await async_client.search.search_tools_or_tool_sets(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            query="query",
        )
        assert_matches_type(SearchSearchToolsOrToolSetsResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search_tools_or_tool_sets(self, async_client: AsyncCadenya) -> None:
        response = await async_client.search.with_raw_response.search_tools_or_tool_sets(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = await response.parse()
        assert_matches_type(SearchSearchToolsOrToolSetsResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_search_tools_or_tool_sets(self, async_client: AsyncCadenya) -> None:
        async with async_client.search.with_streaming_response.search_tools_or_tool_sets(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = await response.parse()
            assert_matches_type(SearchSearchToolsOrToolSetsResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_search_tools_or_tool_sets(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.search.with_raw_response.search_tools_or_tool_sets(
                workspace_id="",
                query="query",
            )
