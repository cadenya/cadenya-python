# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cadenya import Cadenya, AsyncCadenya
from tests.utils import assert_matches_type
from cadenya.types import (
    ToolSet,
    ToolSetEvent,
    ToolSetGetOpenAPISpecResponse,
)
from cadenya.pagination import SyncCursorPagination, AsyncCursorPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestToolSets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Cadenya) -> None:
        tool_set = client.tool_sets.create(
            workspace_id="workspaceId",
            metadata={"name": "name"},
            spec={},
        )
        assert_matches_type(ToolSet, tool_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Cadenya) -> None:
        tool_set = client.tool_sets.create(
            workspace_id="workspaceId",
            metadata={
                "name": "name",
                "bundle_key": "bundleKey",
                "external_id": "externalId",
                "labels": {"foo": "string"},
            },
            spec={
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
        )
        assert_matches_type(ToolSet, tool_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Cadenya) -> None:
        response = client.tool_sets.with_raw_response.create(
            workspace_id="workspaceId",
            metadata={"name": "name"},
            spec={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool_set = response.parse()
        assert_matches_type(ToolSet, tool_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Cadenya) -> None:
        with client.tool_sets.with_streaming_response.create(
            workspace_id="workspaceId",
            metadata={"name": "name"},
            spec={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool_set = response.parse()
            assert_matches_type(ToolSet, tool_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.tool_sets.with_raw_response.create(
                workspace_id="",
                metadata={"name": "name"},
                spec={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Cadenya) -> None:
        tool_set = client.tool_sets.retrieve(
            id="id",
            workspace_id="workspaceId",
        )
        assert_matches_type(ToolSet, tool_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Cadenya) -> None:
        response = client.tool_sets.with_raw_response.retrieve(
            id="id",
            workspace_id="workspaceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool_set = response.parse()
        assert_matches_type(ToolSet, tool_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Cadenya) -> None:
        with client.tool_sets.with_streaming_response.retrieve(
            id="id",
            workspace_id="workspaceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool_set = response.parse()
            assert_matches_type(ToolSet, tool_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.tool_sets.with_raw_response.retrieve(
                id="id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tool_sets.with_raw_response.retrieve(
                id="",
                workspace_id="workspaceId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Cadenya) -> None:
        tool_set = client.tool_sets.update(
            id="id",
            workspace_id="workspaceId",
        )
        assert_matches_type(ToolSet, tool_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Cadenya) -> None:
        tool_set = client.tool_sets.update(
            id="id",
            workspace_id="workspaceId",
            metadata={
                "name": "name",
                "bundle_key": "bundleKey",
                "external_id": "externalId",
                "labels": {"foo": "string"},
            },
            spec={
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
            update_mask="updateMask",
        )
        assert_matches_type(ToolSet, tool_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Cadenya) -> None:
        response = client.tool_sets.with_raw_response.update(
            id="id",
            workspace_id="workspaceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool_set = response.parse()
        assert_matches_type(ToolSet, tool_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Cadenya) -> None:
        with client.tool_sets.with_streaming_response.update(
            id="id",
            workspace_id="workspaceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool_set = response.parse()
            assert_matches_type(ToolSet, tool_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.tool_sets.with_raw_response.update(
                id="id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tool_sets.with_raw_response.update(
                id="",
                workspace_id="workspaceId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Cadenya) -> None:
        tool_set = client.tool_sets.list(
            workspace_id="workspaceId",
        )
        assert_matches_type(SyncCursorPagination[ToolSet], tool_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Cadenya) -> None:
        tool_set = client.tool_sets.list(
            workspace_id="workspaceId",
            bundle_key="bundleKey",
            cursor="cursor",
            include_info=True,
            limit=0,
            prefix="prefix",
            query="query",
            sort_order="sortOrder",
            state="STATE_UNSPECIFIED",
        )
        assert_matches_type(SyncCursorPagination[ToolSet], tool_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Cadenya) -> None:
        response = client.tool_sets.with_raw_response.list(
            workspace_id="workspaceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool_set = response.parse()
        assert_matches_type(SyncCursorPagination[ToolSet], tool_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Cadenya) -> None:
        with client.tool_sets.with_streaming_response.list(
            workspace_id="workspaceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool_set = response.parse()
            assert_matches_type(SyncCursorPagination[ToolSet], tool_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.tool_sets.with_raw_response.list(
                workspace_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Cadenya) -> None:
        tool_set = client.tool_sets.delete(
            id="id",
            workspace_id="workspaceId",
        )
        assert tool_set is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Cadenya) -> None:
        response = client.tool_sets.with_raw_response.delete(
            id="id",
            workspace_id="workspaceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool_set = response.parse()
        assert tool_set is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Cadenya) -> None:
        with client.tool_sets.with_streaming_response.delete(
            id="id",
            workspace_id="workspaceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool_set = response.parse()
            assert tool_set is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.tool_sets.with_raw_response.delete(
                id="id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tool_sets.with_raw_response.delete(
                id="",
                workspace_id="workspaceId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_archive(self, client: Cadenya) -> None:
        tool_set = client.tool_sets.archive(
            id="id",
            workspace_id="workspaceId",
        )
        assert_matches_type(ToolSet, tool_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_archive(self, client: Cadenya) -> None:
        response = client.tool_sets.with_raw_response.archive(
            id="id",
            workspace_id="workspaceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool_set = response.parse()
        assert_matches_type(ToolSet, tool_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_archive(self, client: Cadenya) -> None:
        with client.tool_sets.with_streaming_response.archive(
            id="id",
            workspace_id="workspaceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool_set = response.parse()
            assert_matches_type(ToolSet, tool_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_archive(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.tool_sets.with_raw_response.archive(
                id="id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tool_sets.with_raw_response.archive(
                id="",
                workspace_id="workspaceId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_openapi_spec(self, client: Cadenya) -> None:
        tool_set = client.tool_sets.get_openapi_spec(
            tool_set_id="toolSetId",
            workspace_id="workspaceId",
        )
        assert_matches_type(ToolSetGetOpenAPISpecResponse, tool_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_openapi_spec(self, client: Cadenya) -> None:
        response = client.tool_sets.with_raw_response.get_openapi_spec(
            tool_set_id="toolSetId",
            workspace_id="workspaceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool_set = response.parse()
        assert_matches_type(ToolSetGetOpenAPISpecResponse, tool_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_openapi_spec(self, client: Cadenya) -> None:
        with client.tool_sets.with_streaming_response.get_openapi_spec(
            tool_set_id="toolSetId",
            workspace_id="workspaceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool_set = response.parse()
            assert_matches_type(ToolSetGetOpenAPISpecResponse, tool_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_openapi_spec(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.tool_sets.with_raw_response.get_openapi_spec(
                tool_set_id="toolSetId",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_set_id` but received ''"):
            client.tool_sets.with_raw_response.get_openapi_spec(
                tool_set_id="",
                workspace_id="workspaceId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_events(self, client: Cadenya) -> None:
        tool_set = client.tool_sets.list_events(
            tool_set_id="toolSetId",
            workspace_id="workspaceId",
        )
        assert_matches_type(SyncCursorPagination[ToolSetEvent], tool_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_events_with_all_params(self, client: Cadenya) -> None:
        tool_set = client.tool_sets.list_events(
            tool_set_id="toolSetId",
            workspace_id="workspaceId",
            cursor="cursor",
            include_info=True,
            limit=0,
            sort_order="sortOrder",
        )
        assert_matches_type(SyncCursorPagination[ToolSetEvent], tool_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_events(self, client: Cadenya) -> None:
        response = client.tool_sets.with_raw_response.list_events(
            tool_set_id="toolSetId",
            workspace_id="workspaceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool_set = response.parse()
        assert_matches_type(SyncCursorPagination[ToolSetEvent], tool_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_events(self, client: Cadenya) -> None:
        with client.tool_sets.with_streaming_response.list_events(
            tool_set_id="toolSetId",
            workspace_id="workspaceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool_set = response.parse()
            assert_matches_type(SyncCursorPagination[ToolSetEvent], tool_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_events(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.tool_sets.with_raw_response.list_events(
                tool_set_id="toolSetId",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_set_id` but received ''"):
            client.tool_sets.with_raw_response.list_events(
                tool_set_id="",
                workspace_id="workspaceId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_unarchive(self, client: Cadenya) -> None:
        tool_set = client.tool_sets.unarchive(
            id="id",
            workspace_id="workspaceId",
        )
        assert_matches_type(ToolSet, tool_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_unarchive(self, client: Cadenya) -> None:
        response = client.tool_sets.with_raw_response.unarchive(
            id="id",
            workspace_id="workspaceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool_set = response.parse()
        assert_matches_type(ToolSet, tool_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_unarchive(self, client: Cadenya) -> None:
        with client.tool_sets.with_streaming_response.unarchive(
            id="id",
            workspace_id="workspaceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool_set = response.parse()
            assert_matches_type(ToolSet, tool_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_unarchive(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.tool_sets.with_raw_response.unarchive(
                id="id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tool_sets.with_raw_response.unarchive(
                id="",
                workspace_id="workspaceId",
            )


class TestAsyncToolSets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCadenya) -> None:
        tool_set = await async_client.tool_sets.create(
            workspace_id="workspaceId",
            metadata={"name": "name"},
            spec={},
        )
        assert_matches_type(ToolSet, tool_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCadenya) -> None:
        tool_set = await async_client.tool_sets.create(
            workspace_id="workspaceId",
            metadata={
                "name": "name",
                "bundle_key": "bundleKey",
                "external_id": "externalId",
                "labels": {"foo": "string"},
            },
            spec={
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
        )
        assert_matches_type(ToolSet, tool_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCadenya) -> None:
        response = await async_client.tool_sets.with_raw_response.create(
            workspace_id="workspaceId",
            metadata={"name": "name"},
            spec={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool_set = await response.parse()
        assert_matches_type(ToolSet, tool_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCadenya) -> None:
        async with async_client.tool_sets.with_streaming_response.create(
            workspace_id="workspaceId",
            metadata={"name": "name"},
            spec={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool_set = await response.parse()
            assert_matches_type(ToolSet, tool_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.tool_sets.with_raw_response.create(
                workspace_id="",
                metadata={"name": "name"},
                spec={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCadenya) -> None:
        tool_set = await async_client.tool_sets.retrieve(
            id="id",
            workspace_id="workspaceId",
        )
        assert_matches_type(ToolSet, tool_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCadenya) -> None:
        response = await async_client.tool_sets.with_raw_response.retrieve(
            id="id",
            workspace_id="workspaceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool_set = await response.parse()
        assert_matches_type(ToolSet, tool_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCadenya) -> None:
        async with async_client.tool_sets.with_streaming_response.retrieve(
            id="id",
            workspace_id="workspaceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool_set = await response.parse()
            assert_matches_type(ToolSet, tool_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.tool_sets.with_raw_response.retrieve(
                id="id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tool_sets.with_raw_response.retrieve(
                id="",
                workspace_id="workspaceId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncCadenya) -> None:
        tool_set = await async_client.tool_sets.update(
            id="id",
            workspace_id="workspaceId",
        )
        assert_matches_type(ToolSet, tool_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCadenya) -> None:
        tool_set = await async_client.tool_sets.update(
            id="id",
            workspace_id="workspaceId",
            metadata={
                "name": "name",
                "bundle_key": "bundleKey",
                "external_id": "externalId",
                "labels": {"foo": "string"},
            },
            spec={
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
            update_mask="updateMask",
        )
        assert_matches_type(ToolSet, tool_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCadenya) -> None:
        response = await async_client.tool_sets.with_raw_response.update(
            id="id",
            workspace_id="workspaceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool_set = await response.parse()
        assert_matches_type(ToolSet, tool_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCadenya) -> None:
        async with async_client.tool_sets.with_streaming_response.update(
            id="id",
            workspace_id="workspaceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool_set = await response.parse()
            assert_matches_type(ToolSet, tool_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.tool_sets.with_raw_response.update(
                id="id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tool_sets.with_raw_response.update(
                id="",
                workspace_id="workspaceId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCadenya) -> None:
        tool_set = await async_client.tool_sets.list(
            workspace_id="workspaceId",
        )
        assert_matches_type(AsyncCursorPagination[ToolSet], tool_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCadenya) -> None:
        tool_set = await async_client.tool_sets.list(
            workspace_id="workspaceId",
            bundle_key="bundleKey",
            cursor="cursor",
            include_info=True,
            limit=0,
            prefix="prefix",
            query="query",
            sort_order="sortOrder",
            state="STATE_UNSPECIFIED",
        )
        assert_matches_type(AsyncCursorPagination[ToolSet], tool_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCadenya) -> None:
        response = await async_client.tool_sets.with_raw_response.list(
            workspace_id="workspaceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool_set = await response.parse()
        assert_matches_type(AsyncCursorPagination[ToolSet], tool_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCadenya) -> None:
        async with async_client.tool_sets.with_streaming_response.list(
            workspace_id="workspaceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool_set = await response.parse()
            assert_matches_type(AsyncCursorPagination[ToolSet], tool_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.tool_sets.with_raw_response.list(
                workspace_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCadenya) -> None:
        tool_set = await async_client.tool_sets.delete(
            id="id",
            workspace_id="workspaceId",
        )
        assert tool_set is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCadenya) -> None:
        response = await async_client.tool_sets.with_raw_response.delete(
            id="id",
            workspace_id="workspaceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool_set = await response.parse()
        assert tool_set is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCadenya) -> None:
        async with async_client.tool_sets.with_streaming_response.delete(
            id="id",
            workspace_id="workspaceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool_set = await response.parse()
            assert tool_set is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.tool_sets.with_raw_response.delete(
                id="id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tool_sets.with_raw_response.delete(
                id="",
                workspace_id="workspaceId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_archive(self, async_client: AsyncCadenya) -> None:
        tool_set = await async_client.tool_sets.archive(
            id="id",
            workspace_id="workspaceId",
        )
        assert_matches_type(ToolSet, tool_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncCadenya) -> None:
        response = await async_client.tool_sets.with_raw_response.archive(
            id="id",
            workspace_id="workspaceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool_set = await response.parse()
        assert_matches_type(ToolSet, tool_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncCadenya) -> None:
        async with async_client.tool_sets.with_streaming_response.archive(
            id="id",
            workspace_id="workspaceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool_set = await response.parse()
            assert_matches_type(ToolSet, tool_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_archive(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.tool_sets.with_raw_response.archive(
                id="id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tool_sets.with_raw_response.archive(
                id="",
                workspace_id="workspaceId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_openapi_spec(self, async_client: AsyncCadenya) -> None:
        tool_set = await async_client.tool_sets.get_openapi_spec(
            tool_set_id="toolSetId",
            workspace_id="workspaceId",
        )
        assert_matches_type(ToolSetGetOpenAPISpecResponse, tool_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_openapi_spec(self, async_client: AsyncCadenya) -> None:
        response = await async_client.tool_sets.with_raw_response.get_openapi_spec(
            tool_set_id="toolSetId",
            workspace_id="workspaceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool_set = await response.parse()
        assert_matches_type(ToolSetGetOpenAPISpecResponse, tool_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_openapi_spec(self, async_client: AsyncCadenya) -> None:
        async with async_client.tool_sets.with_streaming_response.get_openapi_spec(
            tool_set_id="toolSetId",
            workspace_id="workspaceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool_set = await response.parse()
            assert_matches_type(ToolSetGetOpenAPISpecResponse, tool_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_openapi_spec(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.tool_sets.with_raw_response.get_openapi_spec(
                tool_set_id="toolSetId",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_set_id` but received ''"):
            await async_client.tool_sets.with_raw_response.get_openapi_spec(
                tool_set_id="",
                workspace_id="workspaceId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_events(self, async_client: AsyncCadenya) -> None:
        tool_set = await async_client.tool_sets.list_events(
            tool_set_id="toolSetId",
            workspace_id="workspaceId",
        )
        assert_matches_type(AsyncCursorPagination[ToolSetEvent], tool_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_events_with_all_params(self, async_client: AsyncCadenya) -> None:
        tool_set = await async_client.tool_sets.list_events(
            tool_set_id="toolSetId",
            workspace_id="workspaceId",
            cursor="cursor",
            include_info=True,
            limit=0,
            sort_order="sortOrder",
        )
        assert_matches_type(AsyncCursorPagination[ToolSetEvent], tool_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_events(self, async_client: AsyncCadenya) -> None:
        response = await async_client.tool_sets.with_raw_response.list_events(
            tool_set_id="toolSetId",
            workspace_id="workspaceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool_set = await response.parse()
        assert_matches_type(AsyncCursorPagination[ToolSetEvent], tool_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_events(self, async_client: AsyncCadenya) -> None:
        async with async_client.tool_sets.with_streaming_response.list_events(
            tool_set_id="toolSetId",
            workspace_id="workspaceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool_set = await response.parse()
            assert_matches_type(AsyncCursorPagination[ToolSetEvent], tool_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_events(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.tool_sets.with_raw_response.list_events(
                tool_set_id="toolSetId",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_set_id` but received ''"):
            await async_client.tool_sets.with_raw_response.list_events(
                tool_set_id="",
                workspace_id="workspaceId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_unarchive(self, async_client: AsyncCadenya) -> None:
        tool_set = await async_client.tool_sets.unarchive(
            id="id",
            workspace_id="workspaceId",
        )
        assert_matches_type(ToolSet, tool_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_unarchive(self, async_client: AsyncCadenya) -> None:
        response = await async_client.tool_sets.with_raw_response.unarchive(
            id="id",
            workspace_id="workspaceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool_set = await response.parse()
        assert_matches_type(ToolSet, tool_set, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_unarchive(self, async_client: AsyncCadenya) -> None:
        async with async_client.tool_sets.with_streaming_response.unarchive(
            id="id",
            workspace_id="workspaceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool_set = await response.parse()
            assert_matches_type(ToolSet, tool_set, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_unarchive(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.tool_sets.with_raw_response.unarchive(
                id="id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tool_sets.with_raw_response.unarchive(
                id="",
                workspace_id="workspaceId",
            )
