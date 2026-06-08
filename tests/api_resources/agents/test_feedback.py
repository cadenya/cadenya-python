# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cadenya import Cadenya, AsyncCadenya
from tests.utils import assert_matches_type
from cadenya._utils import parse_datetime
from cadenya.pagination import SyncCursorPagination, AsyncCursorPagination
from cadenya.types.objectives import ObjectiveFeedback

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFeedback:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Cadenya) -> None:
        feedback = client.agents.feedback.list(
            agent_id="agentId",
            workspace_id="workspaceId",
        )
        assert_matches_type(SyncCursorPagination[ObjectiveFeedback], feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Cadenya) -> None:
        feedback = client.agents.feedback.list(
            agent_id="agentId",
            workspace_id="workspaceId",
            agent_variation_id="agentVariationId",
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            cursor="cursor",
            include_info=True,
            limit=0,
            query="query",
            sentiment="FEEDBACK_SENTIMENT_UNSPECIFIED",
        )
        assert_matches_type(SyncCursorPagination[ObjectiveFeedback], feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Cadenya) -> None:
        response = client.agents.feedback.with_raw_response.list(
            agent_id="agentId",
            workspace_id="workspaceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback = response.parse()
        assert_matches_type(SyncCursorPagination[ObjectiveFeedback], feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Cadenya) -> None:
        with client.agents.feedback.with_streaming_response.list(
            agent_id="agentId",
            workspace_id="workspaceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feedback = response.parse()
            assert_matches_type(SyncCursorPagination[ObjectiveFeedback], feedback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.agents.feedback.with_raw_response.list(
                agent_id="agentId",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.feedback.with_raw_response.list(
                agent_id="",
                workspace_id="workspaceId",
            )


class TestAsyncFeedback:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCadenya) -> None:
        feedback = await async_client.agents.feedback.list(
            agent_id="agentId",
            workspace_id="workspaceId",
        )
        assert_matches_type(AsyncCursorPagination[ObjectiveFeedback], feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCadenya) -> None:
        feedback = await async_client.agents.feedback.list(
            agent_id="agentId",
            workspace_id="workspaceId",
            agent_variation_id="agentVariationId",
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            cursor="cursor",
            include_info=True,
            limit=0,
            query="query",
            sentiment="FEEDBACK_SENTIMENT_UNSPECIFIED",
        )
        assert_matches_type(AsyncCursorPagination[ObjectiveFeedback], feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCadenya) -> None:
        response = await async_client.agents.feedback.with_raw_response.list(
            agent_id="agentId",
            workspace_id="workspaceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback = await response.parse()
        assert_matches_type(AsyncCursorPagination[ObjectiveFeedback], feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCadenya) -> None:
        async with async_client.agents.feedback.with_streaming_response.list(
            agent_id="agentId",
            workspace_id="workspaceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feedback = await response.parse()
            assert_matches_type(AsyncCursorPagination[ObjectiveFeedback], feedback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.agents.feedback.with_raw_response.list(
                agent_id="agentId",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.feedback.with_raw_response.list(
                agent_id="",
                workspace_id="workspaceId",
            )
