# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cadenya import Cadenya, AsyncCadenya
from tests.utils import assert_matches_type
from cadenya.types import (
    BulkWorkspaceApply,
)
from cadenya.pagination import SyncCursorPagination, AsyncCursorPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBulkWorkspaceResources:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Cadenya) -> None:
        bulk_workspace_resource = client.bulk_workspace_resources.retrieve(
            id="id",
            workspace_id="workspaceId",
        )
        assert_matches_type(BulkWorkspaceApply, bulk_workspace_resource, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Cadenya) -> None:
        response = client.bulk_workspace_resources.with_raw_response.retrieve(
            id="id",
            workspace_id="workspaceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk_workspace_resource = response.parse()
        assert_matches_type(BulkWorkspaceApply, bulk_workspace_resource, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Cadenya) -> None:
        with client.bulk_workspace_resources.with_streaming_response.retrieve(
            id="id",
            workspace_id="workspaceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk_workspace_resource = response.parse()
            assert_matches_type(BulkWorkspaceApply, bulk_workspace_resource, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.bulk_workspace_resources.with_raw_response.retrieve(
                id="id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.bulk_workspace_resources.with_raw_response.retrieve(
                id="",
                workspace_id="workspaceId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Cadenya) -> None:
        bulk_workspace_resource = client.bulk_workspace_resources.list(
            workspace_id="workspaceId",
        )
        assert_matches_type(SyncCursorPagination[BulkWorkspaceApply], bulk_workspace_resource, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Cadenya) -> None:
        bulk_workspace_resource = client.bulk_workspace_resources.list(
            workspace_id="workspaceId",
            bundle_key="bundleKey",
            cursor="cursor",
            limit=0,
            sort_order="sortOrder",
            state="STATE_UNSPECIFIED",
        )
        assert_matches_type(SyncCursorPagination[BulkWorkspaceApply], bulk_workspace_resource, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Cadenya) -> None:
        response = client.bulk_workspace_resources.with_raw_response.list(
            workspace_id="workspaceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk_workspace_resource = response.parse()
        assert_matches_type(SyncCursorPagination[BulkWorkspaceApply], bulk_workspace_resource, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Cadenya) -> None:
        with client.bulk_workspace_resources.with_streaming_response.list(
            workspace_id="workspaceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk_workspace_resource = response.parse()
            assert_matches_type(SyncCursorPagination[BulkWorkspaceApply], bulk_workspace_resource, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.bulk_workspace_resources.with_raw_response.list(
                workspace_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_apply(self, client: Cadenya) -> None:
        bulk_workspace_resource = client.bulk_workspace_resources.apply(
            workspace_id="workspaceId",
            data={"bundle_key": "bundleKey"},
        )
        assert_matches_type(BulkWorkspaceApply, bulk_workspace_resource, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_apply_with_all_params(self, client: Cadenya) -> None:
        bulk_workspace_resource = client.bulk_workspace_resources.apply(
            workspace_id="workspaceId",
            data={
                "bundle_key": "bundleKey",
                "agents": {
                    "foo": {
                        "name": "name",
                        "spec": {
                            "variation_selection_mode": "VARIATION_SELECTION_MODE_UNSPECIFIED",
                            "description": "description",
                            "enable_episodic_memory": True,
                            "episodic_memory_ttl": 0,
                            "input_data_schema": {"foo": "bar"},
                            "output_definition": {"foo": "bar"},
                            "webhook_events_url": "webhookEventsUrl",
                        },
                        "labels": {"foo": "string"},
                        "schedules": {
                            "foo": {
                                "name": "name",
                                "spec": {
                                    "schedule": {
                                        "calendars": [
                                            {
                                                "comment": "comment",
                                                "day_of_month": [
                                                    {
                                                        "end": 0,
                                                        "start": 0,
                                                        "step": 0,
                                                    }
                                                ],
                                                "day_of_week": [
                                                    {
                                                        "end": 0,
                                                        "start": 0,
                                                        "step": 0,
                                                    }
                                                ],
                                                "hour": [
                                                    {
                                                        "end": 0,
                                                        "start": 0,
                                                        "step": 0,
                                                    }
                                                ],
                                                "minute": [
                                                    {
                                                        "end": 0,
                                                        "start": 0,
                                                        "step": 0,
                                                    }
                                                ],
                                                "month": [
                                                    {
                                                        "end": 0,
                                                        "start": 0,
                                                        "step": 0,
                                                    }
                                                ],
                                                "second": [
                                                    {
                                                        "end": 0,
                                                        "start": 0,
                                                        "step": 0,
                                                    }
                                                ],
                                            }
                                        ],
                                        "intervals": [
                                            {
                                                "every": "-160513s",
                                                "offset": "-160513s",
                                            }
                                        ],
                                        "timezone": "timezone",
                                    },
                                    "data": {},
                                    "initial_message": "initialMessage",
                                    "overlap_policy": "OVERLAP_POLICY_UNSPECIFIED",
                                    "user_data": {},
                                    "variation_id": "variationId",
                                },
                                "labels": {"foo": "string"},
                                "state": "STATE_UNSPECIFIED",
                            }
                        },
                        "state": "STATE_UNSPECIFIED",
                        "variations": {
                            "foo": {
                                "name": "name",
                                "spec": {
                                    "compaction_config": {
                                        "summarization": {"instructions": "instructions"},
                                        "tool_result_clearing": {"preserve_recent_results": 0},
                                        "trigger_threshold": 0,
                                    },
                                    "constraints": {
                                        "max_sub_objectives": 0,
                                        "max_tool_calls": 0,
                                    },
                                    "description": "description",
                                    "model_config": {
                                        "model_id": "modelId",
                                        "temperature": 0,
                                    },
                                    "progressive_discovery": {
                                        "hints": ["string"],
                                        "max_tools": 0,
                                        "rerank_threshold": 0,
                                    },
                                    "system_prompt_template": "systemPromptTemplate",
                                    "user_message_template": "userMessageTemplate",
                                    "weight": 0,
                                },
                                "assignments": [
                                    {
                                        "sub_agent_id": "subAgentId",
                                        "tool_id": "toolId",
                                        "tool_set_id": "toolSetId",
                                    }
                                ],
                                "labels": {"foo": "string"},
                                "memory_layers": [
                                    {
                                        "memory_layer_id": "memoryLayerId",
                                        "position": 0,
                                    }
                                ],
                            }
                        },
                    }
                },
                "automatically_publish_agents": True,
                "memory_layers": {
                    "foo": {
                        "name": "name",
                        "spec": {
                            "type": "MEMORY_LAYER_TYPE_UNSPECIFIED",
                            "description": "description",
                        },
                        "entries": {
                            "foo": {
                                "key": "key",
                                "content": "content",
                                "description": "description",
                                "upload_id": "uploadId",
                            }
                        },
                        "labels": {"foo": "string"},
                    }
                },
                "source_url": "sourceUrl",
                "tool_sets": {
                    "foo": {
                        "name": "name",
                        "spec": {
                            "adapter": {
                                "http": {
                                    "base_url": "baseUrl",
                                    "headers": {"foo": "string"},
                                },
                                "mcp": {
                                    "exclude_tools": {
                                        "operator": "OPERATOR_UNSPECIFIED",
                                        "filters": [
                                            {
                                                "attribute": "ATTRIBUTE_UNSPECIFIED",
                                                "matcher": {
                                                    "case_sensitive": True,
                                                    "contains": "contains",
                                                    "ends_with": "endsWith",
                                                    "exact": "exact",
                                                    "regex": "regex",
                                                    "starts_with": "startsWith",
                                                },
                                            }
                                        ],
                                    },
                                    "headers": {"foo": "string"},
                                    "include_tools": {
                                        "operator": "OPERATOR_UNSPECIFIED",
                                        "filters": [
                                            {
                                                "attribute": "ATTRIBUTE_UNSPECIFIED",
                                                "matcher": {
                                                    "case_sensitive": True,
                                                    "contains": "contains",
                                                    "ends_with": "endsWith",
                                                    "exact": "exact",
                                                    "regex": "regex",
                                                    "starts_with": "startsWith",
                                                },
                                            }
                                        ],
                                    },
                                    "tool_approvals": {
                                        "always": True,
                                        "only": {
                                            "operator": "OPERATOR_UNSPECIFIED",
                                            "filters": [
                                                {
                                                    "attribute": "ATTRIBUTE_UNSPECIFIED",
                                                    "matcher": {
                                                        "case_sensitive": True,
                                                        "contains": "contains",
                                                        "ends_with": "endsWith",
                                                        "exact": "exact",
                                                        "regex": "regex",
                                                        "starts_with": "startsWith",
                                                    },
                                                }
                                            ],
                                        },
                                    },
                                    "url": "url",
                                },
                                "openapi": {
                                    "base_url": "baseUrl",
                                    "exclude_tools": {
                                        "operator": "OPERATOR_UNSPECIFIED",
                                        "filters": [
                                            {
                                                "attribute": "ATTRIBUTE_UNSPECIFIED",
                                                "matcher": {
                                                    "case_sensitive": True,
                                                    "contains": "contains",
                                                    "ends_with": "endsWith",
                                                    "exact": "exact",
                                                    "regex": "regex",
                                                    "starts_with": "startsWith",
                                                },
                                            }
                                        ],
                                    },
                                    "headers": {"foo": "string"},
                                    "include_tools": {
                                        "operator": "OPERATOR_UNSPECIFIED",
                                        "filters": [
                                            {
                                                "attribute": "ATTRIBUTE_UNSPECIFIED",
                                                "matcher": {
                                                    "case_sensitive": True,
                                                    "contains": "contains",
                                                    "ends_with": "endsWith",
                                                    "exact": "exact",
                                                    "regex": "regex",
                                                    "starts_with": "startsWith",
                                                },
                                            }
                                        ],
                                    },
                                    "server_name": "serverName",
                                    "tool_approvals": {
                                        "always": True,
                                        "only": {
                                            "operator": "OPERATOR_UNSPECIFIED",
                                            "filters": [
                                                {
                                                    "attribute": "ATTRIBUTE_UNSPECIFIED",
                                                    "matcher": {
                                                        "case_sensitive": True,
                                                        "contains": "contains",
                                                        "ends_with": "endsWith",
                                                        "exact": "exact",
                                                        "regex": "regex",
                                                        "starts_with": "startsWith",
                                                    },
                                                }
                                            ],
                                        },
                                    },
                                    "upload_id": "uploadId",
                                    "url": "url",
                                },
                            },
                            "description": "description",
                        },
                        "labels": {"foo": "string"},
                        "tools": {
                            "foo": {
                                "name": "name",
                                "spec": {
                                    "config": {
                                        "http": {
                                            "request_method": "HTTP_METHOD_UNSPECIFIED",
                                            "headers": {"foo": "string"},
                                            "path": "path",
                                            "query": "query",
                                            "request_body_content_type": "requestBodyContentType",
                                            "request_body_template": "requestBodyTemplate",
                                            "tool_name": "toolName",
                                        },
                                        "mcp": {
                                            "tool_description": "toolDescription",
                                            "tool_name": "toolName",
                                            "tool_title": "toolTitle",
                                        },
                                        "openapi": {
                                            "method": "method",
                                            "operation_id": "operationId",
                                            "path": "path",
                                        },
                                    },
                                    "description": "description",
                                    "parameters": {"foo": "bar"},
                                    "requires_approval": True,
                                },
                                "labels": {"foo": "string"},
                                "state": "STATE_UNSPECIFIED",
                            }
                        },
                    }
                },
            },
        )
        assert_matches_type(BulkWorkspaceApply, bulk_workspace_resource, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_apply(self, client: Cadenya) -> None:
        response = client.bulk_workspace_resources.with_raw_response.apply(
            workspace_id="workspaceId",
            data={"bundle_key": "bundleKey"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk_workspace_resource = response.parse()
        assert_matches_type(BulkWorkspaceApply, bulk_workspace_resource, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_apply(self, client: Cadenya) -> None:
        with client.bulk_workspace_resources.with_streaming_response.apply(
            workspace_id="workspaceId",
            data={"bundle_key": "bundleKey"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk_workspace_resource = response.parse()
            assert_matches_type(BulkWorkspaceApply, bulk_workspace_resource, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_apply(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.bulk_workspace_resources.with_raw_response.apply(
                workspace_id="",
                data={"bundle_key": "bundleKey"},
            )


class TestAsyncBulkWorkspaceResources:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCadenya) -> None:
        bulk_workspace_resource = await async_client.bulk_workspace_resources.retrieve(
            id="id",
            workspace_id="workspaceId",
        )
        assert_matches_type(BulkWorkspaceApply, bulk_workspace_resource, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCadenya) -> None:
        response = await async_client.bulk_workspace_resources.with_raw_response.retrieve(
            id="id",
            workspace_id="workspaceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk_workspace_resource = await response.parse()
        assert_matches_type(BulkWorkspaceApply, bulk_workspace_resource, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCadenya) -> None:
        async with async_client.bulk_workspace_resources.with_streaming_response.retrieve(
            id="id",
            workspace_id="workspaceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk_workspace_resource = await response.parse()
            assert_matches_type(BulkWorkspaceApply, bulk_workspace_resource, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.bulk_workspace_resources.with_raw_response.retrieve(
                id="id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.bulk_workspace_resources.with_raw_response.retrieve(
                id="",
                workspace_id="workspaceId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCadenya) -> None:
        bulk_workspace_resource = await async_client.bulk_workspace_resources.list(
            workspace_id="workspaceId",
        )
        assert_matches_type(AsyncCursorPagination[BulkWorkspaceApply], bulk_workspace_resource, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCadenya) -> None:
        bulk_workspace_resource = await async_client.bulk_workspace_resources.list(
            workspace_id="workspaceId",
            bundle_key="bundleKey",
            cursor="cursor",
            limit=0,
            sort_order="sortOrder",
            state="STATE_UNSPECIFIED",
        )
        assert_matches_type(AsyncCursorPagination[BulkWorkspaceApply], bulk_workspace_resource, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCadenya) -> None:
        response = await async_client.bulk_workspace_resources.with_raw_response.list(
            workspace_id="workspaceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk_workspace_resource = await response.parse()
        assert_matches_type(AsyncCursorPagination[BulkWorkspaceApply], bulk_workspace_resource, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCadenya) -> None:
        async with async_client.bulk_workspace_resources.with_streaming_response.list(
            workspace_id="workspaceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk_workspace_resource = await response.parse()
            assert_matches_type(AsyncCursorPagination[BulkWorkspaceApply], bulk_workspace_resource, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.bulk_workspace_resources.with_raw_response.list(
                workspace_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_apply(self, async_client: AsyncCadenya) -> None:
        bulk_workspace_resource = await async_client.bulk_workspace_resources.apply(
            workspace_id="workspaceId",
            data={"bundle_key": "bundleKey"},
        )
        assert_matches_type(BulkWorkspaceApply, bulk_workspace_resource, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_apply_with_all_params(self, async_client: AsyncCadenya) -> None:
        bulk_workspace_resource = await async_client.bulk_workspace_resources.apply(
            workspace_id="workspaceId",
            data={
                "bundle_key": "bundleKey",
                "agents": {
                    "foo": {
                        "name": "name",
                        "spec": {
                            "variation_selection_mode": "VARIATION_SELECTION_MODE_UNSPECIFIED",
                            "description": "description",
                            "enable_episodic_memory": True,
                            "episodic_memory_ttl": 0,
                            "input_data_schema": {"foo": "bar"},
                            "output_definition": {"foo": "bar"},
                            "webhook_events_url": "webhookEventsUrl",
                        },
                        "labels": {"foo": "string"},
                        "schedules": {
                            "foo": {
                                "name": "name",
                                "spec": {
                                    "schedule": {
                                        "calendars": [
                                            {
                                                "comment": "comment",
                                                "day_of_month": [
                                                    {
                                                        "end": 0,
                                                        "start": 0,
                                                        "step": 0,
                                                    }
                                                ],
                                                "day_of_week": [
                                                    {
                                                        "end": 0,
                                                        "start": 0,
                                                        "step": 0,
                                                    }
                                                ],
                                                "hour": [
                                                    {
                                                        "end": 0,
                                                        "start": 0,
                                                        "step": 0,
                                                    }
                                                ],
                                                "minute": [
                                                    {
                                                        "end": 0,
                                                        "start": 0,
                                                        "step": 0,
                                                    }
                                                ],
                                                "month": [
                                                    {
                                                        "end": 0,
                                                        "start": 0,
                                                        "step": 0,
                                                    }
                                                ],
                                                "second": [
                                                    {
                                                        "end": 0,
                                                        "start": 0,
                                                        "step": 0,
                                                    }
                                                ],
                                            }
                                        ],
                                        "intervals": [
                                            {
                                                "every": "-160513s",
                                                "offset": "-160513s",
                                            }
                                        ],
                                        "timezone": "timezone",
                                    },
                                    "data": {},
                                    "initial_message": "initialMessage",
                                    "overlap_policy": "OVERLAP_POLICY_UNSPECIFIED",
                                    "user_data": {},
                                    "variation_id": "variationId",
                                },
                                "labels": {"foo": "string"},
                                "state": "STATE_UNSPECIFIED",
                            }
                        },
                        "state": "STATE_UNSPECIFIED",
                        "variations": {
                            "foo": {
                                "name": "name",
                                "spec": {
                                    "compaction_config": {
                                        "summarization": {"instructions": "instructions"},
                                        "tool_result_clearing": {"preserve_recent_results": 0},
                                        "trigger_threshold": 0,
                                    },
                                    "constraints": {
                                        "max_sub_objectives": 0,
                                        "max_tool_calls": 0,
                                    },
                                    "description": "description",
                                    "model_config": {
                                        "model_id": "modelId",
                                        "temperature": 0,
                                    },
                                    "progressive_discovery": {
                                        "hints": ["string"],
                                        "max_tools": 0,
                                        "rerank_threshold": 0,
                                    },
                                    "system_prompt_template": "systemPromptTemplate",
                                    "user_message_template": "userMessageTemplate",
                                    "weight": 0,
                                },
                                "assignments": [
                                    {
                                        "sub_agent_id": "subAgentId",
                                        "tool_id": "toolId",
                                        "tool_set_id": "toolSetId",
                                    }
                                ],
                                "labels": {"foo": "string"},
                                "memory_layers": [
                                    {
                                        "memory_layer_id": "memoryLayerId",
                                        "position": 0,
                                    }
                                ],
                            }
                        },
                    }
                },
                "automatically_publish_agents": True,
                "memory_layers": {
                    "foo": {
                        "name": "name",
                        "spec": {
                            "type": "MEMORY_LAYER_TYPE_UNSPECIFIED",
                            "description": "description",
                        },
                        "entries": {
                            "foo": {
                                "key": "key",
                                "content": "content",
                                "description": "description",
                                "upload_id": "uploadId",
                            }
                        },
                        "labels": {"foo": "string"},
                    }
                },
                "source_url": "sourceUrl",
                "tool_sets": {
                    "foo": {
                        "name": "name",
                        "spec": {
                            "adapter": {
                                "http": {
                                    "base_url": "baseUrl",
                                    "headers": {"foo": "string"},
                                },
                                "mcp": {
                                    "exclude_tools": {
                                        "operator": "OPERATOR_UNSPECIFIED",
                                        "filters": [
                                            {
                                                "attribute": "ATTRIBUTE_UNSPECIFIED",
                                                "matcher": {
                                                    "case_sensitive": True,
                                                    "contains": "contains",
                                                    "ends_with": "endsWith",
                                                    "exact": "exact",
                                                    "regex": "regex",
                                                    "starts_with": "startsWith",
                                                },
                                            }
                                        ],
                                    },
                                    "headers": {"foo": "string"},
                                    "include_tools": {
                                        "operator": "OPERATOR_UNSPECIFIED",
                                        "filters": [
                                            {
                                                "attribute": "ATTRIBUTE_UNSPECIFIED",
                                                "matcher": {
                                                    "case_sensitive": True,
                                                    "contains": "contains",
                                                    "ends_with": "endsWith",
                                                    "exact": "exact",
                                                    "regex": "regex",
                                                    "starts_with": "startsWith",
                                                },
                                            }
                                        ],
                                    },
                                    "tool_approvals": {
                                        "always": True,
                                        "only": {
                                            "operator": "OPERATOR_UNSPECIFIED",
                                            "filters": [
                                                {
                                                    "attribute": "ATTRIBUTE_UNSPECIFIED",
                                                    "matcher": {
                                                        "case_sensitive": True,
                                                        "contains": "contains",
                                                        "ends_with": "endsWith",
                                                        "exact": "exact",
                                                        "regex": "regex",
                                                        "starts_with": "startsWith",
                                                    },
                                                }
                                            ],
                                        },
                                    },
                                    "url": "url",
                                },
                                "openapi": {
                                    "base_url": "baseUrl",
                                    "exclude_tools": {
                                        "operator": "OPERATOR_UNSPECIFIED",
                                        "filters": [
                                            {
                                                "attribute": "ATTRIBUTE_UNSPECIFIED",
                                                "matcher": {
                                                    "case_sensitive": True,
                                                    "contains": "contains",
                                                    "ends_with": "endsWith",
                                                    "exact": "exact",
                                                    "regex": "regex",
                                                    "starts_with": "startsWith",
                                                },
                                            }
                                        ],
                                    },
                                    "headers": {"foo": "string"},
                                    "include_tools": {
                                        "operator": "OPERATOR_UNSPECIFIED",
                                        "filters": [
                                            {
                                                "attribute": "ATTRIBUTE_UNSPECIFIED",
                                                "matcher": {
                                                    "case_sensitive": True,
                                                    "contains": "contains",
                                                    "ends_with": "endsWith",
                                                    "exact": "exact",
                                                    "regex": "regex",
                                                    "starts_with": "startsWith",
                                                },
                                            }
                                        ],
                                    },
                                    "server_name": "serverName",
                                    "tool_approvals": {
                                        "always": True,
                                        "only": {
                                            "operator": "OPERATOR_UNSPECIFIED",
                                            "filters": [
                                                {
                                                    "attribute": "ATTRIBUTE_UNSPECIFIED",
                                                    "matcher": {
                                                        "case_sensitive": True,
                                                        "contains": "contains",
                                                        "ends_with": "endsWith",
                                                        "exact": "exact",
                                                        "regex": "regex",
                                                        "starts_with": "startsWith",
                                                    },
                                                }
                                            ],
                                        },
                                    },
                                    "upload_id": "uploadId",
                                    "url": "url",
                                },
                            },
                            "description": "description",
                        },
                        "labels": {"foo": "string"},
                        "tools": {
                            "foo": {
                                "name": "name",
                                "spec": {
                                    "config": {
                                        "http": {
                                            "request_method": "HTTP_METHOD_UNSPECIFIED",
                                            "headers": {"foo": "string"},
                                            "path": "path",
                                            "query": "query",
                                            "request_body_content_type": "requestBodyContentType",
                                            "request_body_template": "requestBodyTemplate",
                                            "tool_name": "toolName",
                                        },
                                        "mcp": {
                                            "tool_description": "toolDescription",
                                            "tool_name": "toolName",
                                            "tool_title": "toolTitle",
                                        },
                                        "openapi": {
                                            "method": "method",
                                            "operation_id": "operationId",
                                            "path": "path",
                                        },
                                    },
                                    "description": "description",
                                    "parameters": {"foo": "bar"},
                                    "requires_approval": True,
                                },
                                "labels": {"foo": "string"},
                                "state": "STATE_UNSPECIFIED",
                            }
                        },
                    }
                },
            },
        )
        assert_matches_type(BulkWorkspaceApply, bulk_workspace_resource, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_apply(self, async_client: AsyncCadenya) -> None:
        response = await async_client.bulk_workspace_resources.with_raw_response.apply(
            workspace_id="workspaceId",
            data={"bundle_key": "bundleKey"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk_workspace_resource = await response.parse()
        assert_matches_type(BulkWorkspaceApply, bulk_workspace_resource, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_apply(self, async_client: AsyncCadenya) -> None:
        async with async_client.bulk_workspace_resources.with_streaming_response.apply(
            workspace_id="workspaceId",
            data={"bundle_key": "bundleKey"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk_workspace_resource = await response.parse()
            assert_matches_type(BulkWorkspaceApply, bulk_workspace_resource, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_apply(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.bulk_workspace_resources.with_raw_response.apply(
                workspace_id="",
                data={"bundle_key": "bundleKey"},
            )
