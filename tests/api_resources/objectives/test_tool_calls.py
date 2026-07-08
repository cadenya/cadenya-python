# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cadenya import Cadenya, AsyncCadenya
from tests.utils import assert_matches_type
from cadenya.pagination import SyncCursorPagination, AsyncCursorPagination
from cadenya.types.objectives import (
    ObjectiveToolCall,
    ObjectiveToolCallWithResult,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestToolCalls:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Cadenya) -> None:
        tool_call = client.objectives.tool_calls.retrieve(
            tool_call_id="toolCallId",
            workspace_id="workspaceId",
            objective_id="objectiveId",
        )
        assert_matches_type(ObjectiveToolCallWithResult, tool_call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Cadenya) -> None:
        response = client.objectives.tool_calls.with_raw_response.retrieve(
            tool_call_id="toolCallId",
            workspace_id="workspaceId",
            objective_id="objectiveId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool_call = response.parse()
        assert_matches_type(ObjectiveToolCallWithResult, tool_call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Cadenya) -> None:
        with client.objectives.tool_calls.with_streaming_response.retrieve(
            tool_call_id="toolCallId",
            workspace_id="workspaceId",
            objective_id="objectiveId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool_call = response.parse()
            assert_matches_type(ObjectiveToolCallWithResult, tool_call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.objectives.tool_calls.with_raw_response.retrieve(
                tool_call_id="toolCallId",
                workspace_id="",
                objective_id="objectiveId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `objective_id` but received ''"):
            client.objectives.tool_calls.with_raw_response.retrieve(
                tool_call_id="toolCallId",
                workspace_id="workspaceId",
                objective_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_call_id` but received ''"):
            client.objectives.tool_calls.with_raw_response.retrieve(
                tool_call_id="",
                workspace_id="workspaceId",
                objective_id="objectiveId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Cadenya) -> None:
        tool_call = client.objectives.tool_calls.list(
            objective_id="objectiveId",
            workspace_id="workspaceId",
        )
        assert_matches_type(SyncCursorPagination[ObjectiveToolCall], tool_call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Cadenya) -> None:
        tool_call = client.objectives.tool_calls.list(
            objective_id="objectiveId",
            workspace_id="workspaceId",
            cursor="cursor",
            execution_status="TOOL_CALL_EXECUTION_STATUS_UNSPECIFIED",
            include_info=True,
            labels="labels",
            limit=0,
            status="TOOL_CALL_STATUS_UNSPECIFIED",
        )
        assert_matches_type(SyncCursorPagination[ObjectiveToolCall], tool_call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Cadenya) -> None:
        response = client.objectives.tool_calls.with_raw_response.list(
            objective_id="objectiveId",
            workspace_id="workspaceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool_call = response.parse()
        assert_matches_type(SyncCursorPagination[ObjectiveToolCall], tool_call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Cadenya) -> None:
        with client.objectives.tool_calls.with_streaming_response.list(
            objective_id="objectiveId",
            workspace_id="workspaceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool_call = response.parse()
            assert_matches_type(SyncCursorPagination[ObjectiveToolCall], tool_call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.objectives.tool_calls.with_raw_response.list(
                objective_id="objectiveId",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `objective_id` but received ''"):
            client.objectives.tool_calls.with_raw_response.list(
                objective_id="",
                workspace_id="workspaceId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_approve(self, client: Cadenya) -> None:
        tool_call = client.objectives.tool_calls.approve(
            tool_call_id="toolCallId",
            workspace_id="workspaceId",
            objective_id="objectiveId",
        )
        assert_matches_type(ObjectiveToolCall, tool_call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_approve(self, client: Cadenya) -> None:
        response = client.objectives.tool_calls.with_raw_response.approve(
            tool_call_id="toolCallId",
            workspace_id="workspaceId",
            objective_id="objectiveId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool_call = response.parse()
        assert_matches_type(ObjectiveToolCall, tool_call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_approve(self, client: Cadenya) -> None:
        with client.objectives.tool_calls.with_streaming_response.approve(
            tool_call_id="toolCallId",
            workspace_id="workspaceId",
            objective_id="objectiveId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool_call = response.parse()
            assert_matches_type(ObjectiveToolCall, tool_call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_approve(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.objectives.tool_calls.with_raw_response.approve(
                tool_call_id="toolCallId",
                workspace_id="",
                objective_id="objectiveId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `objective_id` but received ''"):
            client.objectives.tool_calls.with_raw_response.approve(
                tool_call_id="toolCallId",
                workspace_id="workspaceId",
                objective_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_call_id` but received ''"):
            client.objectives.tool_calls.with_raw_response.approve(
                tool_call_id="",
                workspace_id="workspaceId",
                objective_id="objectiveId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_deny(self, client: Cadenya) -> None:
        tool_call = client.objectives.tool_calls.deny(
            tool_call_id="toolCallId",
            workspace_id="workspaceId",
            objective_id="objectiveId",
        )
        assert_matches_type(ObjectiveToolCall, tool_call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_deny_with_all_params(self, client: Cadenya) -> None:
        tool_call = client.objectives.tool_calls.deny(
            tool_call_id="toolCallId",
            workspace_id="workspaceId",
            objective_id="objectiveId",
            memo="memo",
        )
        assert_matches_type(ObjectiveToolCall, tool_call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_deny(self, client: Cadenya) -> None:
        response = client.objectives.tool_calls.with_raw_response.deny(
            tool_call_id="toolCallId",
            workspace_id="workspaceId",
            objective_id="objectiveId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool_call = response.parse()
        assert_matches_type(ObjectiveToolCall, tool_call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_deny(self, client: Cadenya) -> None:
        with client.objectives.tool_calls.with_streaming_response.deny(
            tool_call_id="toolCallId",
            workspace_id="workspaceId",
            objective_id="objectiveId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool_call = response.parse()
            assert_matches_type(ObjectiveToolCall, tool_call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_deny(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.objectives.tool_calls.with_raw_response.deny(
                tool_call_id="toolCallId",
                workspace_id="",
                objective_id="objectiveId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `objective_id` but received ''"):
            client.objectives.tool_calls.with_raw_response.deny(
                tool_call_id="toolCallId",
                workspace_id="workspaceId",
                objective_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_call_id` but received ''"):
            client.objectives.tool_calls.with_raw_response.deny(
                tool_call_id="",
                workspace_id="workspaceId",
                objective_id="objectiveId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_set_content(self, client: Cadenya) -> None:
        tool_call = client.objectives.tool_calls.set_content(
            tool_call_id="toolCallId",
            workspace_id="workspaceId",
            objective_id="objectiveId",
            content=[{}],
        )
        assert_matches_type(ObjectiveToolCall, tool_call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_set_content(self, client: Cadenya) -> None:
        response = client.objectives.tool_calls.with_raw_response.set_content(
            tool_call_id="toolCallId",
            workspace_id="workspaceId",
            objective_id="objectiveId",
            content=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool_call = response.parse()
        assert_matches_type(ObjectiveToolCall, tool_call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_set_content(self, client: Cadenya) -> None:
        with client.objectives.tool_calls.with_streaming_response.set_content(
            tool_call_id="toolCallId",
            workspace_id="workspaceId",
            objective_id="objectiveId",
            content=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool_call = response.parse()
            assert_matches_type(ObjectiveToolCall, tool_call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_set_content(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.objectives.tool_calls.with_raw_response.set_content(
                tool_call_id="toolCallId",
                workspace_id="",
                objective_id="objectiveId",
                content=[{}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `objective_id` but received ''"):
            client.objectives.tool_calls.with_raw_response.set_content(
                tool_call_id="toolCallId",
                workspace_id="workspaceId",
                objective_id="",
                content=[{}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_call_id` but received ''"):
            client.objectives.tool_calls.with_raw_response.set_content(
                tool_call_id="",
                workspace_id="workspaceId",
                objective_id="objectiveId",
                content=[{}],
            )


class TestAsyncToolCalls:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCadenya) -> None:
        tool_call = await async_client.objectives.tool_calls.retrieve(
            tool_call_id="toolCallId",
            workspace_id="workspaceId",
            objective_id="objectiveId",
        )
        assert_matches_type(ObjectiveToolCallWithResult, tool_call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCadenya) -> None:
        response = await async_client.objectives.tool_calls.with_raw_response.retrieve(
            tool_call_id="toolCallId",
            workspace_id="workspaceId",
            objective_id="objectiveId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool_call = await response.parse()
        assert_matches_type(ObjectiveToolCallWithResult, tool_call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCadenya) -> None:
        async with async_client.objectives.tool_calls.with_streaming_response.retrieve(
            tool_call_id="toolCallId",
            workspace_id="workspaceId",
            objective_id="objectiveId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool_call = await response.parse()
            assert_matches_type(ObjectiveToolCallWithResult, tool_call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.objectives.tool_calls.with_raw_response.retrieve(
                tool_call_id="toolCallId",
                workspace_id="",
                objective_id="objectiveId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `objective_id` but received ''"):
            await async_client.objectives.tool_calls.with_raw_response.retrieve(
                tool_call_id="toolCallId",
                workspace_id="workspaceId",
                objective_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_call_id` but received ''"):
            await async_client.objectives.tool_calls.with_raw_response.retrieve(
                tool_call_id="",
                workspace_id="workspaceId",
                objective_id="objectiveId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCadenya) -> None:
        tool_call = await async_client.objectives.tool_calls.list(
            objective_id="objectiveId",
            workspace_id="workspaceId",
        )
        assert_matches_type(AsyncCursorPagination[ObjectiveToolCall], tool_call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCadenya) -> None:
        tool_call = await async_client.objectives.tool_calls.list(
            objective_id="objectiveId",
            workspace_id="workspaceId",
            cursor="cursor",
            execution_status="TOOL_CALL_EXECUTION_STATUS_UNSPECIFIED",
            include_info=True,
            labels="labels",
            limit=0,
            status="TOOL_CALL_STATUS_UNSPECIFIED",
        )
        assert_matches_type(AsyncCursorPagination[ObjectiveToolCall], tool_call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCadenya) -> None:
        response = await async_client.objectives.tool_calls.with_raw_response.list(
            objective_id="objectiveId",
            workspace_id="workspaceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool_call = await response.parse()
        assert_matches_type(AsyncCursorPagination[ObjectiveToolCall], tool_call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCadenya) -> None:
        async with async_client.objectives.tool_calls.with_streaming_response.list(
            objective_id="objectiveId",
            workspace_id="workspaceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool_call = await response.parse()
            assert_matches_type(AsyncCursorPagination[ObjectiveToolCall], tool_call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.objectives.tool_calls.with_raw_response.list(
                objective_id="objectiveId",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `objective_id` but received ''"):
            await async_client.objectives.tool_calls.with_raw_response.list(
                objective_id="",
                workspace_id="workspaceId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_approve(self, async_client: AsyncCadenya) -> None:
        tool_call = await async_client.objectives.tool_calls.approve(
            tool_call_id="toolCallId",
            workspace_id="workspaceId",
            objective_id="objectiveId",
        )
        assert_matches_type(ObjectiveToolCall, tool_call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_approve(self, async_client: AsyncCadenya) -> None:
        response = await async_client.objectives.tool_calls.with_raw_response.approve(
            tool_call_id="toolCallId",
            workspace_id="workspaceId",
            objective_id="objectiveId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool_call = await response.parse()
        assert_matches_type(ObjectiveToolCall, tool_call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_approve(self, async_client: AsyncCadenya) -> None:
        async with async_client.objectives.tool_calls.with_streaming_response.approve(
            tool_call_id="toolCallId",
            workspace_id="workspaceId",
            objective_id="objectiveId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool_call = await response.parse()
            assert_matches_type(ObjectiveToolCall, tool_call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_approve(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.objectives.tool_calls.with_raw_response.approve(
                tool_call_id="toolCallId",
                workspace_id="",
                objective_id="objectiveId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `objective_id` but received ''"):
            await async_client.objectives.tool_calls.with_raw_response.approve(
                tool_call_id="toolCallId",
                workspace_id="workspaceId",
                objective_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_call_id` but received ''"):
            await async_client.objectives.tool_calls.with_raw_response.approve(
                tool_call_id="",
                workspace_id="workspaceId",
                objective_id="objectiveId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_deny(self, async_client: AsyncCadenya) -> None:
        tool_call = await async_client.objectives.tool_calls.deny(
            tool_call_id="toolCallId",
            workspace_id="workspaceId",
            objective_id="objectiveId",
        )
        assert_matches_type(ObjectiveToolCall, tool_call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_deny_with_all_params(self, async_client: AsyncCadenya) -> None:
        tool_call = await async_client.objectives.tool_calls.deny(
            tool_call_id="toolCallId",
            workspace_id="workspaceId",
            objective_id="objectiveId",
            memo="memo",
        )
        assert_matches_type(ObjectiveToolCall, tool_call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_deny(self, async_client: AsyncCadenya) -> None:
        response = await async_client.objectives.tool_calls.with_raw_response.deny(
            tool_call_id="toolCallId",
            workspace_id="workspaceId",
            objective_id="objectiveId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool_call = await response.parse()
        assert_matches_type(ObjectiveToolCall, tool_call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_deny(self, async_client: AsyncCadenya) -> None:
        async with async_client.objectives.tool_calls.with_streaming_response.deny(
            tool_call_id="toolCallId",
            workspace_id="workspaceId",
            objective_id="objectiveId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool_call = await response.parse()
            assert_matches_type(ObjectiveToolCall, tool_call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_deny(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.objectives.tool_calls.with_raw_response.deny(
                tool_call_id="toolCallId",
                workspace_id="",
                objective_id="objectiveId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `objective_id` but received ''"):
            await async_client.objectives.tool_calls.with_raw_response.deny(
                tool_call_id="toolCallId",
                workspace_id="workspaceId",
                objective_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_call_id` but received ''"):
            await async_client.objectives.tool_calls.with_raw_response.deny(
                tool_call_id="",
                workspace_id="workspaceId",
                objective_id="objectiveId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_set_content(self, async_client: AsyncCadenya) -> None:
        tool_call = await async_client.objectives.tool_calls.set_content(
            tool_call_id="toolCallId",
            workspace_id="workspaceId",
            objective_id="objectiveId",
            content=[{}],
        )
        assert_matches_type(ObjectiveToolCall, tool_call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_set_content(self, async_client: AsyncCadenya) -> None:
        response = await async_client.objectives.tool_calls.with_raw_response.set_content(
            tool_call_id="toolCallId",
            workspace_id="workspaceId",
            objective_id="objectiveId",
            content=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool_call = await response.parse()
        assert_matches_type(ObjectiveToolCall, tool_call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_set_content(self, async_client: AsyncCadenya) -> None:
        async with async_client.objectives.tool_calls.with_streaming_response.set_content(
            tool_call_id="toolCallId",
            workspace_id="workspaceId",
            objective_id="objectiveId",
            content=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool_call = await response.parse()
            assert_matches_type(ObjectiveToolCall, tool_call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_set_content(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.objectives.tool_calls.with_raw_response.set_content(
                tool_call_id="toolCallId",
                workspace_id="",
                objective_id="objectiveId",
                content=[{}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `objective_id` but received ''"):
            await async_client.objectives.tool_calls.with_raw_response.set_content(
                tool_call_id="toolCallId",
                workspace_id="workspaceId",
                objective_id="",
                content=[{}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_call_id` but received ''"):
            await async_client.objectives.tool_calls.with_raw_response.set_content(
                tool_call_id="",
                workspace_id="workspaceId",
                objective_id="objectiveId",
                content=[{}],
            )
