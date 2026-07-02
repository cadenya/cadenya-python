# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cadenya import Cadenya, AsyncCadenya
from tests.utils import assert_matches_type
from cadenya.pagination import SyncCursorPagination, AsyncCursorPagination
from cadenya.types.tool_sets import Tool

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTools:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Cadenya) -> None:
        tool = client.tool_sets.tools.create(
            tool_set_id="toolSetId",
            workspace_id="workspaceId",
            metadata={"name": "name"},
            spec={
                "config": {},
                "description": "description",
                "parameters": {"foo": "bar"},
                "requires_approval": True,
            },
        )
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Cadenya) -> None:
        tool = client.tool_sets.tools.create(
            tool_set_id="toolSetId",
            workspace_id="workspaceId",
            metadata={
                "name": "name",
                "external_id": "externalId",
                "labels": {"foo": "string"},
            },
            spec={
                "config": {
                    "http": {
                        "request_method": "HTTP_METHOD_UNSPECIFIED",
                        "headers": {"foo": "string"},
                        "path": "path",
                        "query": "query",
                        "request_body_content_type": "requestBodyContentType",
                        "request_body_template": "requestBodyTemplate",
                    },
                    "mcp": {
                        "annotations": {
                            "destructive_hint": True,
                            "idempotent_hint": True,
                            "open_world_hint": True,
                            "read_only_hint": True,
                            "title": "title",
                        }
                    },
                    "openapi": {
                        "method": "method",
                        "path": "path",
                    },
                },
                "description": "description",
                "parameters": {"foo": "bar"},
                "requires_approval": True,
                "llm_tool_name": "llmToolName",
            },
        )
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Cadenya) -> None:
        response = client.tool_sets.tools.with_raw_response.create(
            tool_set_id="toolSetId",
            workspace_id="workspaceId",
            metadata={"name": "name"},
            spec={
                "config": {},
                "description": "description",
                "parameters": {"foo": "bar"},
                "requires_approval": True,
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Cadenya) -> None:
        with client.tool_sets.tools.with_streaming_response.create(
            tool_set_id="toolSetId",
            workspace_id="workspaceId",
            metadata={"name": "name"},
            spec={
                "config": {},
                "description": "description",
                "parameters": {"foo": "bar"},
                "requires_approval": True,
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(Tool, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.tool_sets.tools.with_raw_response.create(
                tool_set_id="toolSetId",
                workspace_id="",
                metadata={"name": "name"},
                spec={
                    "config": {},
                    "description": "description",
                    "parameters": {"foo": "bar"},
                    "requires_approval": True,
                },
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_set_id` but received ''"):
            client.tool_sets.tools.with_raw_response.create(
                tool_set_id="",
                workspace_id="workspaceId",
                metadata={"name": "name"},
                spec={
                    "config": {},
                    "description": "description",
                    "parameters": {"foo": "bar"},
                    "requires_approval": True,
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Cadenya) -> None:
        tool = client.tool_sets.tools.retrieve(
            id="id",
            workspace_id="workspaceId",
            tool_set_id="toolSetId",
        )
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Cadenya) -> None:
        response = client.tool_sets.tools.with_raw_response.retrieve(
            id="id",
            workspace_id="workspaceId",
            tool_set_id="toolSetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Cadenya) -> None:
        with client.tool_sets.tools.with_streaming_response.retrieve(
            id="id",
            workspace_id="workspaceId",
            tool_set_id="toolSetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(Tool, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.tool_sets.tools.with_raw_response.retrieve(
                id="id",
                workspace_id="",
                tool_set_id="toolSetId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_set_id` but received ''"):
            client.tool_sets.tools.with_raw_response.retrieve(
                id="id",
                workspace_id="workspaceId",
                tool_set_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tool_sets.tools.with_raw_response.retrieve(
                id="",
                workspace_id="workspaceId",
                tool_set_id="toolSetId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Cadenya) -> None:
        tool = client.tool_sets.tools.update(
            id="id",
            workspace_id="workspaceId",
            tool_set_id="toolSetId",
        )
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Cadenya) -> None:
        tool = client.tool_sets.tools.update(
            id="id",
            workspace_id="workspaceId",
            tool_set_id="toolSetId",
            metadata={
                "name": "name",
                "external_id": "externalId",
                "labels": {"foo": "string"},
            },
            spec={
                "config": {
                    "http": {
                        "request_method": "HTTP_METHOD_UNSPECIFIED",
                        "headers": {"foo": "string"},
                        "path": "path",
                        "query": "query",
                        "request_body_content_type": "requestBodyContentType",
                        "request_body_template": "requestBodyTemplate",
                    },
                    "mcp": {
                        "annotations": {
                            "destructive_hint": True,
                            "idempotent_hint": True,
                            "open_world_hint": True,
                            "read_only_hint": True,
                            "title": "title",
                        }
                    },
                    "openapi": {
                        "method": "method",
                        "path": "path",
                    },
                },
                "description": "description",
                "parameters": {"foo": "bar"},
                "requires_approval": True,
                "llm_tool_name": "llmToolName",
            },
            update_mask="updateMask",
        )
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Cadenya) -> None:
        response = client.tool_sets.tools.with_raw_response.update(
            id="id",
            workspace_id="workspaceId",
            tool_set_id="toolSetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Cadenya) -> None:
        with client.tool_sets.tools.with_streaming_response.update(
            id="id",
            workspace_id="workspaceId",
            tool_set_id="toolSetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(Tool, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.tool_sets.tools.with_raw_response.update(
                id="id",
                workspace_id="",
                tool_set_id="toolSetId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_set_id` but received ''"):
            client.tool_sets.tools.with_raw_response.update(
                id="id",
                workspace_id="workspaceId",
                tool_set_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tool_sets.tools.with_raw_response.update(
                id="",
                workspace_id="workspaceId",
                tool_set_id="toolSetId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Cadenya) -> None:
        tool = client.tool_sets.tools.list(
            tool_set_id="toolSetId",
            workspace_id="workspaceId",
        )
        assert_matches_type(SyncCursorPagination[Tool], tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Cadenya) -> None:
        tool = client.tool_sets.tools.list(
            tool_set_id="toolSetId",
            workspace_id="workspaceId",
            cursor="cursor",
            include_info=True,
            limit=0,
            names=["string"],
            prefix="prefix",
            query="query",
            requires_approval=True,
            sort_order="sortOrder",
            states=["STATE_UNSPECIFIED"],
        )
        assert_matches_type(SyncCursorPagination[Tool], tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Cadenya) -> None:
        response = client.tool_sets.tools.with_raw_response.list(
            tool_set_id="toolSetId",
            workspace_id="workspaceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(SyncCursorPagination[Tool], tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Cadenya) -> None:
        with client.tool_sets.tools.with_streaming_response.list(
            tool_set_id="toolSetId",
            workspace_id="workspaceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(SyncCursorPagination[Tool], tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.tool_sets.tools.with_raw_response.list(
                tool_set_id="toolSetId",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_set_id` but received ''"):
            client.tool_sets.tools.with_raw_response.list(
                tool_set_id="",
                workspace_id="workspaceId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Cadenya) -> None:
        tool = client.tool_sets.tools.delete(
            id="id",
            workspace_id="workspaceId",
            tool_set_id="toolSetId",
        )
        assert tool is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Cadenya) -> None:
        response = client.tool_sets.tools.with_raw_response.delete(
            id="id",
            workspace_id="workspaceId",
            tool_set_id="toolSetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert tool is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Cadenya) -> None:
        with client.tool_sets.tools.with_streaming_response.delete(
            id="id",
            workspace_id="workspaceId",
            tool_set_id="toolSetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert tool is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.tool_sets.tools.with_raw_response.delete(
                id="id",
                workspace_id="",
                tool_set_id="toolSetId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_set_id` but received ''"):
            client.tool_sets.tools.with_raw_response.delete(
                id="id",
                workspace_id="workspaceId",
                tool_set_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tool_sets.tools.with_raw_response.delete(
                id="",
                workspace_id="workspaceId",
                tool_set_id="toolSetId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_omit(self, client: Cadenya) -> None:
        tool = client.tool_sets.tools.omit(
            id="id",
            workspace_id="workspaceId",
            tool_set_id="toolSetId",
        )
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_omit(self, client: Cadenya) -> None:
        response = client.tool_sets.tools.with_raw_response.omit(
            id="id",
            workspace_id="workspaceId",
            tool_set_id="toolSetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_omit(self, client: Cadenya) -> None:
        with client.tool_sets.tools.with_streaming_response.omit(
            id="id",
            workspace_id="workspaceId",
            tool_set_id="toolSetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(Tool, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_omit(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.tool_sets.tools.with_raw_response.omit(
                id="id",
                workspace_id="",
                tool_set_id="toolSetId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_set_id` but received ''"):
            client.tool_sets.tools.with_raw_response.omit(
                id="id",
                workspace_id="workspaceId",
                tool_set_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tool_sets.tools.with_raw_response.omit(
                id="",
                workspace_id="workspaceId",
                tool_set_id="toolSetId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_restore(self, client: Cadenya) -> None:
        tool = client.tool_sets.tools.restore(
            id="id",
            workspace_id="workspaceId",
            tool_set_id="toolSetId",
        )
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_restore(self, client: Cadenya) -> None:
        response = client.tool_sets.tools.with_raw_response.restore(
            id="id",
            workspace_id="workspaceId",
            tool_set_id="toolSetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_restore(self, client: Cadenya) -> None:
        with client.tool_sets.tools.with_streaming_response.restore(
            id="id",
            workspace_id="workspaceId",
            tool_set_id="toolSetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(Tool, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_restore(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.tool_sets.tools.with_raw_response.restore(
                id="id",
                workspace_id="",
                tool_set_id="toolSetId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_set_id` but received ''"):
            client.tool_sets.tools.with_raw_response.restore(
                id="id",
                workspace_id="workspaceId",
                tool_set_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tool_sets.tools.with_raw_response.restore(
                id="",
                workspace_id="workspaceId",
                tool_set_id="toolSetId",
            )


class TestAsyncTools:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCadenya) -> None:
        tool = await async_client.tool_sets.tools.create(
            tool_set_id="toolSetId",
            workspace_id="workspaceId",
            metadata={"name": "name"},
            spec={
                "config": {},
                "description": "description",
                "parameters": {"foo": "bar"},
                "requires_approval": True,
            },
        )
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCadenya) -> None:
        tool = await async_client.tool_sets.tools.create(
            tool_set_id="toolSetId",
            workspace_id="workspaceId",
            metadata={
                "name": "name",
                "external_id": "externalId",
                "labels": {"foo": "string"},
            },
            spec={
                "config": {
                    "http": {
                        "request_method": "HTTP_METHOD_UNSPECIFIED",
                        "headers": {"foo": "string"},
                        "path": "path",
                        "query": "query",
                        "request_body_content_type": "requestBodyContentType",
                        "request_body_template": "requestBodyTemplate",
                    },
                    "mcp": {
                        "annotations": {
                            "destructive_hint": True,
                            "idempotent_hint": True,
                            "open_world_hint": True,
                            "read_only_hint": True,
                            "title": "title",
                        }
                    },
                    "openapi": {
                        "method": "method",
                        "path": "path",
                    },
                },
                "description": "description",
                "parameters": {"foo": "bar"},
                "requires_approval": True,
                "llm_tool_name": "llmToolName",
            },
        )
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCadenya) -> None:
        response = await async_client.tool_sets.tools.with_raw_response.create(
            tool_set_id="toolSetId",
            workspace_id="workspaceId",
            metadata={"name": "name"},
            spec={
                "config": {},
                "description": "description",
                "parameters": {"foo": "bar"},
                "requires_approval": True,
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCadenya) -> None:
        async with async_client.tool_sets.tools.with_streaming_response.create(
            tool_set_id="toolSetId",
            workspace_id="workspaceId",
            metadata={"name": "name"},
            spec={
                "config": {},
                "description": "description",
                "parameters": {"foo": "bar"},
                "requires_approval": True,
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(Tool, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.tool_sets.tools.with_raw_response.create(
                tool_set_id="toolSetId",
                workspace_id="",
                metadata={"name": "name"},
                spec={
                    "config": {},
                    "description": "description",
                    "parameters": {"foo": "bar"},
                    "requires_approval": True,
                },
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_set_id` but received ''"):
            await async_client.tool_sets.tools.with_raw_response.create(
                tool_set_id="",
                workspace_id="workspaceId",
                metadata={"name": "name"},
                spec={
                    "config": {},
                    "description": "description",
                    "parameters": {"foo": "bar"},
                    "requires_approval": True,
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCadenya) -> None:
        tool = await async_client.tool_sets.tools.retrieve(
            id="id",
            workspace_id="workspaceId",
            tool_set_id="toolSetId",
        )
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCadenya) -> None:
        response = await async_client.tool_sets.tools.with_raw_response.retrieve(
            id="id",
            workspace_id="workspaceId",
            tool_set_id="toolSetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCadenya) -> None:
        async with async_client.tool_sets.tools.with_streaming_response.retrieve(
            id="id",
            workspace_id="workspaceId",
            tool_set_id="toolSetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(Tool, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.tool_sets.tools.with_raw_response.retrieve(
                id="id",
                workspace_id="",
                tool_set_id="toolSetId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_set_id` but received ''"):
            await async_client.tool_sets.tools.with_raw_response.retrieve(
                id="id",
                workspace_id="workspaceId",
                tool_set_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tool_sets.tools.with_raw_response.retrieve(
                id="",
                workspace_id="workspaceId",
                tool_set_id="toolSetId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncCadenya) -> None:
        tool = await async_client.tool_sets.tools.update(
            id="id",
            workspace_id="workspaceId",
            tool_set_id="toolSetId",
        )
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCadenya) -> None:
        tool = await async_client.tool_sets.tools.update(
            id="id",
            workspace_id="workspaceId",
            tool_set_id="toolSetId",
            metadata={
                "name": "name",
                "external_id": "externalId",
                "labels": {"foo": "string"},
            },
            spec={
                "config": {
                    "http": {
                        "request_method": "HTTP_METHOD_UNSPECIFIED",
                        "headers": {"foo": "string"},
                        "path": "path",
                        "query": "query",
                        "request_body_content_type": "requestBodyContentType",
                        "request_body_template": "requestBodyTemplate",
                    },
                    "mcp": {
                        "annotations": {
                            "destructive_hint": True,
                            "idempotent_hint": True,
                            "open_world_hint": True,
                            "read_only_hint": True,
                            "title": "title",
                        }
                    },
                    "openapi": {
                        "method": "method",
                        "path": "path",
                    },
                },
                "description": "description",
                "parameters": {"foo": "bar"},
                "requires_approval": True,
                "llm_tool_name": "llmToolName",
            },
            update_mask="updateMask",
        )
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCadenya) -> None:
        response = await async_client.tool_sets.tools.with_raw_response.update(
            id="id",
            workspace_id="workspaceId",
            tool_set_id="toolSetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCadenya) -> None:
        async with async_client.tool_sets.tools.with_streaming_response.update(
            id="id",
            workspace_id="workspaceId",
            tool_set_id="toolSetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(Tool, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.tool_sets.tools.with_raw_response.update(
                id="id",
                workspace_id="",
                tool_set_id="toolSetId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_set_id` but received ''"):
            await async_client.tool_sets.tools.with_raw_response.update(
                id="id",
                workspace_id="workspaceId",
                tool_set_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tool_sets.tools.with_raw_response.update(
                id="",
                workspace_id="workspaceId",
                tool_set_id="toolSetId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCadenya) -> None:
        tool = await async_client.tool_sets.tools.list(
            tool_set_id="toolSetId",
            workspace_id="workspaceId",
        )
        assert_matches_type(AsyncCursorPagination[Tool], tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCadenya) -> None:
        tool = await async_client.tool_sets.tools.list(
            tool_set_id="toolSetId",
            workspace_id="workspaceId",
            cursor="cursor",
            include_info=True,
            limit=0,
            names=["string"],
            prefix="prefix",
            query="query",
            requires_approval=True,
            sort_order="sortOrder",
            states=["STATE_UNSPECIFIED"],
        )
        assert_matches_type(AsyncCursorPagination[Tool], tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCadenya) -> None:
        response = await async_client.tool_sets.tools.with_raw_response.list(
            tool_set_id="toolSetId",
            workspace_id="workspaceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(AsyncCursorPagination[Tool], tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCadenya) -> None:
        async with async_client.tool_sets.tools.with_streaming_response.list(
            tool_set_id="toolSetId",
            workspace_id="workspaceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(AsyncCursorPagination[Tool], tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.tool_sets.tools.with_raw_response.list(
                tool_set_id="toolSetId",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_set_id` but received ''"):
            await async_client.tool_sets.tools.with_raw_response.list(
                tool_set_id="",
                workspace_id="workspaceId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCadenya) -> None:
        tool = await async_client.tool_sets.tools.delete(
            id="id",
            workspace_id="workspaceId",
            tool_set_id="toolSetId",
        )
        assert tool is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCadenya) -> None:
        response = await async_client.tool_sets.tools.with_raw_response.delete(
            id="id",
            workspace_id="workspaceId",
            tool_set_id="toolSetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert tool is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCadenya) -> None:
        async with async_client.tool_sets.tools.with_streaming_response.delete(
            id="id",
            workspace_id="workspaceId",
            tool_set_id="toolSetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert tool is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.tool_sets.tools.with_raw_response.delete(
                id="id",
                workspace_id="",
                tool_set_id="toolSetId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_set_id` but received ''"):
            await async_client.tool_sets.tools.with_raw_response.delete(
                id="id",
                workspace_id="workspaceId",
                tool_set_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tool_sets.tools.with_raw_response.delete(
                id="",
                workspace_id="workspaceId",
                tool_set_id="toolSetId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_omit(self, async_client: AsyncCadenya) -> None:
        tool = await async_client.tool_sets.tools.omit(
            id="id",
            workspace_id="workspaceId",
            tool_set_id="toolSetId",
        )
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_omit(self, async_client: AsyncCadenya) -> None:
        response = await async_client.tool_sets.tools.with_raw_response.omit(
            id="id",
            workspace_id="workspaceId",
            tool_set_id="toolSetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_omit(self, async_client: AsyncCadenya) -> None:
        async with async_client.tool_sets.tools.with_streaming_response.omit(
            id="id",
            workspace_id="workspaceId",
            tool_set_id="toolSetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(Tool, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_omit(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.tool_sets.tools.with_raw_response.omit(
                id="id",
                workspace_id="",
                tool_set_id="toolSetId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_set_id` but received ''"):
            await async_client.tool_sets.tools.with_raw_response.omit(
                id="id",
                workspace_id="workspaceId",
                tool_set_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tool_sets.tools.with_raw_response.omit(
                id="",
                workspace_id="workspaceId",
                tool_set_id="toolSetId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_restore(self, async_client: AsyncCadenya) -> None:
        tool = await async_client.tool_sets.tools.restore(
            id="id",
            workspace_id="workspaceId",
            tool_set_id="toolSetId",
        )
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_restore(self, async_client: AsyncCadenya) -> None:
        response = await async_client.tool_sets.tools.with_raw_response.restore(
            id="id",
            workspace_id="workspaceId",
            tool_set_id="toolSetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_restore(self, async_client: AsyncCadenya) -> None:
        async with async_client.tool_sets.tools.with_streaming_response.restore(
            id="id",
            workspace_id="workspaceId",
            tool_set_id="toolSetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(Tool, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_restore(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.tool_sets.tools.with_raw_response.restore(
                id="id",
                workspace_id="",
                tool_set_id="toolSetId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_set_id` but received ''"):
            await async_client.tool_sets.tools.with_raw_response.restore(
                id="id",
                workspace_id="workspaceId",
                tool_set_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tool_sets.tools.with_raw_response.restore(
                id="",
                workspace_id="workspaceId",
                tool_set_id="toolSetId",
            )
