# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cadenya import Cadenya, AsyncCadenya
from tests.utils import assert_matches_type
from cadenya.pagination import SyncCursorPagination, AsyncCursorPagination
from cadenya.types.objectives import (
    ObjectiveFeedback,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFeedback:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Cadenya) -> None:
        feedback = client.objectives.feedback.create(
            objective_id="objectiveId",
            workspace_id="workspaceId",
            data={},
            metadata={},
        )
        assert_matches_type(ObjectiveFeedback, feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Cadenya) -> None:
        feedback = client.objectives.feedback.create(
            objective_id="objectiveId",
            workspace_id="workspaceId",
            data={
                "comment": "comment",
                "score": 0,
            },
            metadata={
                "external_id": "externalId",
                "labels": {"foo": "string"},
            },
        )
        assert_matches_type(ObjectiveFeedback, feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Cadenya) -> None:
        response = client.objectives.feedback.with_raw_response.create(
            objective_id="objectiveId",
            workspace_id="workspaceId",
            data={},
            metadata={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback = response.parse()
        assert_matches_type(ObjectiveFeedback, feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Cadenya) -> None:
        with client.objectives.feedback.with_streaming_response.create(
            objective_id="objectiveId",
            workspace_id="workspaceId",
            data={},
            metadata={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feedback = response.parse()
            assert_matches_type(ObjectiveFeedback, feedback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.objectives.feedback.with_raw_response.create(
                objective_id="objectiveId",
                workspace_id="",
                data={},
                metadata={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `objective_id` but received ''"):
            client.objectives.feedback.with_raw_response.create(
                objective_id="",
                workspace_id="workspaceId",
                data={},
                metadata={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Cadenya) -> None:
        feedback = client.objectives.feedback.list(
            objective_id="objectiveId",
            workspace_id="workspaceId",
        )
        assert_matches_type(SyncCursorPagination[ObjectiveFeedback], feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Cadenya) -> None:
        feedback = client.objectives.feedback.list(
            objective_id="objectiveId",
            workspace_id="workspaceId",
            cursor="cursor",
            labels="labels",
            limit=0,
        )
        assert_matches_type(SyncCursorPagination[ObjectiveFeedback], feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Cadenya) -> None:
        response = client.objectives.feedback.with_raw_response.list(
            objective_id="objectiveId",
            workspace_id="workspaceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback = response.parse()
        assert_matches_type(SyncCursorPagination[ObjectiveFeedback], feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Cadenya) -> None:
        with client.objectives.feedback.with_streaming_response.list(
            objective_id="objectiveId",
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
            client.objectives.feedback.with_raw_response.list(
                objective_id="objectiveId",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `objective_id` but received ''"):
            client.objectives.feedback.with_raw_response.list(
                objective_id="",
                workspace_id="workspaceId",
            )


class TestAsyncFeedback:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCadenya) -> None:
        feedback = await async_client.objectives.feedback.create(
            objective_id="objectiveId",
            workspace_id="workspaceId",
            data={},
            metadata={},
        )
        assert_matches_type(ObjectiveFeedback, feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCadenya) -> None:
        feedback = await async_client.objectives.feedback.create(
            objective_id="objectiveId",
            workspace_id="workspaceId",
            data={
                "comment": "comment",
                "score": 0,
            },
            metadata={
                "external_id": "externalId",
                "labels": {"foo": "string"},
            },
        )
        assert_matches_type(ObjectiveFeedback, feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCadenya) -> None:
        response = await async_client.objectives.feedback.with_raw_response.create(
            objective_id="objectiveId",
            workspace_id="workspaceId",
            data={},
            metadata={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback = await response.parse()
        assert_matches_type(ObjectiveFeedback, feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCadenya) -> None:
        async with async_client.objectives.feedback.with_streaming_response.create(
            objective_id="objectiveId",
            workspace_id="workspaceId",
            data={},
            metadata={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feedback = await response.parse()
            assert_matches_type(ObjectiveFeedback, feedback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.objectives.feedback.with_raw_response.create(
                objective_id="objectiveId",
                workspace_id="",
                data={},
                metadata={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `objective_id` but received ''"):
            await async_client.objectives.feedback.with_raw_response.create(
                objective_id="",
                workspace_id="workspaceId",
                data={},
                metadata={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCadenya) -> None:
        feedback = await async_client.objectives.feedback.list(
            objective_id="objectiveId",
            workspace_id="workspaceId",
        )
        assert_matches_type(AsyncCursorPagination[ObjectiveFeedback], feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCadenya) -> None:
        feedback = await async_client.objectives.feedback.list(
            objective_id="objectiveId",
            workspace_id="workspaceId",
            cursor="cursor",
            labels="labels",
            limit=0,
        )
        assert_matches_type(AsyncCursorPagination[ObjectiveFeedback], feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCadenya) -> None:
        response = await async_client.objectives.feedback.with_raw_response.list(
            objective_id="objectiveId",
            workspace_id="workspaceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback = await response.parse()
        assert_matches_type(AsyncCursorPagination[ObjectiveFeedback], feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCadenya) -> None:
        async with async_client.objectives.feedback.with_streaming_response.list(
            objective_id="objectiveId",
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
            await async_client.objectives.feedback.with_raw_response.list(
                objective_id="objectiveId",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `objective_id` but received ''"):
            await async_client.objectives.feedback.with_raw_response.list(
                objective_id="",
                workspace_id="workspaceId",
            )
