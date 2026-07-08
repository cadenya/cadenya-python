# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cadenya import Cadenya, AsyncCadenya
from tests.utils import assert_matches_type
from cadenya.pagination import SyncCursorPagination, AsyncCursorPagination
from cadenya.types.agents import (
    AgentVariation,
    VariationAssignment,
    VariationMemoryLayerAssignment,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVariations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Cadenya) -> None:
        variation = client.agents.variations.create(
            agent_id="agentId",
            workspace_id="workspaceId",
            metadata={"name": "name"},
            spec={},
        )
        assert_matches_type(AgentVariation, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Cadenya) -> None:
        variation = client.agents.variations.create(
            agent_id="agentId",
            workspace_id="workspaceId",
            metadata={
                "name": "name",
                "external_id": "externalId",
                "labels": {"foo": "string"},
            },
            spec={
                "compaction_config": {
                    "summarization": {"instructions": "instructions"},
                    "tool_result_clearing": {"preserve_recent_results": 0},
                    "trigger_threshold": 0,
                },
                "constraints": {
                    "inactivity_timeout": "-160513s",
                    "max_sub_objectives": 0,
                    "max_tool_calls": 0,
                },
                "description": "description",
                "first_user_message_template": "firstUserMessageTemplate",
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
                "weight": 0,
            },
        )
        assert_matches_type(AgentVariation, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Cadenya) -> None:
        response = client.agents.variations.with_raw_response.create(
            agent_id="agentId",
            workspace_id="workspaceId",
            metadata={"name": "name"},
            spec={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variation = response.parse()
        assert_matches_type(AgentVariation, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Cadenya) -> None:
        with client.agents.variations.with_streaming_response.create(
            agent_id="agentId",
            workspace_id="workspaceId",
            metadata={"name": "name"},
            spec={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            variation = response.parse()
            assert_matches_type(AgentVariation, variation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.agents.variations.with_raw_response.create(
                agent_id="agentId",
                workspace_id="",
                metadata={"name": "name"},
                spec={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.variations.with_raw_response.create(
                agent_id="",
                workspace_id="workspaceId",
                metadata={"name": "name"},
                spec={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Cadenya) -> None:
        variation = client.agents.variations.retrieve(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
        )
        assert_matches_type(AgentVariation, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Cadenya) -> None:
        response = client.agents.variations.with_raw_response.retrieve(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variation = response.parse()
        assert_matches_type(AgentVariation, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Cadenya) -> None:
        with client.agents.variations.with_streaming_response.retrieve(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            variation = response.parse()
            assert_matches_type(AgentVariation, variation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.agents.variations.with_raw_response.retrieve(
                id="id",
                workspace_id="",
                agent_id="agentId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.variations.with_raw_response.retrieve(
                id="id",
                workspace_id="workspaceId",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.agents.variations.with_raw_response.retrieve(
                id="",
                workspace_id="workspaceId",
                agent_id="agentId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Cadenya) -> None:
        variation = client.agents.variations.update(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
        )
        assert_matches_type(AgentVariation, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Cadenya) -> None:
        variation = client.agents.variations.update(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
            metadata={
                "name": "name",
                "external_id": "externalId",
                "labels": {"foo": "string"},
            },
            spec={
                "compaction_config": {
                    "summarization": {"instructions": "instructions"},
                    "tool_result_clearing": {"preserve_recent_results": 0},
                    "trigger_threshold": 0,
                },
                "constraints": {
                    "inactivity_timeout": "-160513s",
                    "max_sub_objectives": 0,
                    "max_tool_calls": 0,
                },
                "description": "description",
                "first_user_message_template": "firstUserMessageTemplate",
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
                "weight": 0,
            },
            update_mask="updateMask",
        )
        assert_matches_type(AgentVariation, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Cadenya) -> None:
        response = client.agents.variations.with_raw_response.update(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variation = response.parse()
        assert_matches_type(AgentVariation, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Cadenya) -> None:
        with client.agents.variations.with_streaming_response.update(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            variation = response.parse()
            assert_matches_type(AgentVariation, variation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.agents.variations.with_raw_response.update(
                id="id",
                workspace_id="",
                agent_id="agentId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.variations.with_raw_response.update(
                id="id",
                workspace_id="workspaceId",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.agents.variations.with_raw_response.update(
                id="",
                workspace_id="workspaceId",
                agent_id="agentId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Cadenya) -> None:
        variation = client.agents.variations.list(
            agent_id="agentId",
            workspace_id="workspaceId",
        )
        assert_matches_type(SyncCursorPagination[AgentVariation], variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Cadenya) -> None:
        variation = client.agents.variations.list(
            agent_id="agentId",
            workspace_id="workspaceId",
            cursor="cursor",
            include_info=True,
            labels="labels",
            limit=0,
            sort_order="sortOrder",
        )
        assert_matches_type(SyncCursorPagination[AgentVariation], variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Cadenya) -> None:
        response = client.agents.variations.with_raw_response.list(
            agent_id="agentId",
            workspace_id="workspaceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variation = response.parse()
        assert_matches_type(SyncCursorPagination[AgentVariation], variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Cadenya) -> None:
        with client.agents.variations.with_streaming_response.list(
            agent_id="agentId",
            workspace_id="workspaceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            variation = response.parse()
            assert_matches_type(SyncCursorPagination[AgentVariation], variation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.agents.variations.with_raw_response.list(
                agent_id="agentId",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.variations.with_raw_response.list(
                agent_id="",
                workspace_id="workspaceId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Cadenya) -> None:
        variation = client.agents.variations.delete(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
        )
        assert variation is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Cadenya) -> None:
        response = client.agents.variations.with_raw_response.delete(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variation = response.parse()
        assert variation is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Cadenya) -> None:
        with client.agents.variations.with_streaming_response.delete(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            variation = response.parse()
            assert variation is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.agents.variations.with_raw_response.delete(
                id="id",
                workspace_id="",
                agent_id="agentId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.variations.with_raw_response.delete(
                id="id",
                workspace_id="workspaceId",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.agents.variations.with_raw_response.delete(
                id="",
                workspace_id="workspaceId",
                agent_id="agentId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add_assignment(self, client: Cadenya) -> None:
        variation = client.agents.variations.add_assignment(
            variation_id="variationId",
            workspace_id="workspaceId",
            agent_id="agentId",
        )
        assert_matches_type(VariationAssignment, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add_assignment_with_all_params(self, client: Cadenya) -> None:
        variation = client.agents.variations.add_assignment(
            variation_id="variationId",
            workspace_id="workspaceId",
            agent_id="agentId",
            sub_agent_id="subAgentId",
            tool_id="toolId",
            tool_set_id="toolSetId",
        )
        assert_matches_type(VariationAssignment, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_add_assignment(self, client: Cadenya) -> None:
        response = client.agents.variations.with_raw_response.add_assignment(
            variation_id="variationId",
            workspace_id="workspaceId",
            agent_id="agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variation = response.parse()
        assert_matches_type(VariationAssignment, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_add_assignment(self, client: Cadenya) -> None:
        with client.agents.variations.with_streaming_response.add_assignment(
            variation_id="variationId",
            workspace_id="workspaceId",
            agent_id="agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            variation = response.parse()
            assert_matches_type(VariationAssignment, variation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_add_assignment(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.agents.variations.with_raw_response.add_assignment(
                variation_id="variationId",
                workspace_id="",
                agent_id="agentId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.variations.with_raw_response.add_assignment(
                variation_id="variationId",
                workspace_id="workspaceId",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `variation_id` but received ''"):
            client.agents.variations.with_raw_response.add_assignment(
                variation_id="",
                workspace_id="workspaceId",
                agent_id="agentId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add_memory_layer(self, client: Cadenya) -> None:
        variation = client.agents.variations.add_memory_layer(
            variation_id="variationId",
            workspace_id="workspaceId",
            agent_id="agentId",
        )
        assert_matches_type(VariationMemoryLayerAssignment, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add_memory_layer_with_all_params(self, client: Cadenya) -> None:
        variation = client.agents.variations.add_memory_layer(
            variation_id="variationId",
            workspace_id="workspaceId",
            agent_id="agentId",
            memory_layer_id="memoryLayerId",
            position=0,
        )
        assert_matches_type(VariationMemoryLayerAssignment, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_add_memory_layer(self, client: Cadenya) -> None:
        response = client.agents.variations.with_raw_response.add_memory_layer(
            variation_id="variationId",
            workspace_id="workspaceId",
            agent_id="agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variation = response.parse()
        assert_matches_type(VariationMemoryLayerAssignment, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_add_memory_layer(self, client: Cadenya) -> None:
        with client.agents.variations.with_streaming_response.add_memory_layer(
            variation_id="variationId",
            workspace_id="workspaceId",
            agent_id="agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            variation = response.parse()
            assert_matches_type(VariationMemoryLayerAssignment, variation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_add_memory_layer(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.agents.variations.with_raw_response.add_memory_layer(
                variation_id="variationId",
                workspace_id="",
                agent_id="agentId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.variations.with_raw_response.add_memory_layer(
                variation_id="variationId",
                workspace_id="workspaceId",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `variation_id` but received ''"):
            client.agents.variations.with_raw_response.add_memory_layer(
                variation_id="",
                workspace_id="workspaceId",
                agent_id="agentId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_remove_assignment(self, client: Cadenya) -> None:
        variation = client.agents.variations.remove_assignment(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
            variation_id="variationId",
        )
        assert variation is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_remove_assignment(self, client: Cadenya) -> None:
        response = client.agents.variations.with_raw_response.remove_assignment(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
            variation_id="variationId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variation = response.parse()
        assert variation is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_remove_assignment(self, client: Cadenya) -> None:
        with client.agents.variations.with_streaming_response.remove_assignment(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
            variation_id="variationId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            variation = response.parse()
            assert variation is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_remove_assignment(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.agents.variations.with_raw_response.remove_assignment(
                id="id",
                workspace_id="",
                agent_id="agentId",
                variation_id="variationId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.variations.with_raw_response.remove_assignment(
                id="id",
                workspace_id="workspaceId",
                agent_id="",
                variation_id="variationId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `variation_id` but received ''"):
            client.agents.variations.with_raw_response.remove_assignment(
                id="id",
                workspace_id="workspaceId",
                agent_id="agentId",
                variation_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.agents.variations.with_raw_response.remove_assignment(
                id="",
                workspace_id="workspaceId",
                agent_id="agentId",
                variation_id="variationId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_remove_memory_layer(self, client: Cadenya) -> None:
        variation = client.agents.variations.remove_memory_layer(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
            variation_id="variationId",
        )
        assert variation is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_remove_memory_layer(self, client: Cadenya) -> None:
        response = client.agents.variations.with_raw_response.remove_memory_layer(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
            variation_id="variationId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variation = response.parse()
        assert variation is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_remove_memory_layer(self, client: Cadenya) -> None:
        with client.agents.variations.with_streaming_response.remove_memory_layer(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
            variation_id="variationId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            variation = response.parse()
            assert variation is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_remove_memory_layer(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.agents.variations.with_raw_response.remove_memory_layer(
                id="id",
                workspace_id="",
                agent_id="agentId",
                variation_id="variationId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.variations.with_raw_response.remove_memory_layer(
                id="id",
                workspace_id="workspaceId",
                agent_id="",
                variation_id="variationId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `variation_id` but received ''"):
            client.agents.variations.with_raw_response.remove_memory_layer(
                id="id",
                workspace_id="workspaceId",
                agent_id="agentId",
                variation_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.agents.variations.with_raw_response.remove_memory_layer(
                id="",
                workspace_id="workspaceId",
                agent_id="agentId",
                variation_id="variationId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_memory_layer(self, client: Cadenya) -> None:
        variation = client.agents.variations.update_memory_layer(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
            variation_id="variationId",
        )
        assert_matches_type(VariationMemoryLayerAssignment, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_memory_layer_with_all_params(self, client: Cadenya) -> None:
        variation = client.agents.variations.update_memory_layer(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
            variation_id="variationId",
            position=0,
        )
        assert_matches_type(VariationMemoryLayerAssignment, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_memory_layer(self, client: Cadenya) -> None:
        response = client.agents.variations.with_raw_response.update_memory_layer(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
            variation_id="variationId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variation = response.parse()
        assert_matches_type(VariationMemoryLayerAssignment, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_memory_layer(self, client: Cadenya) -> None:
        with client.agents.variations.with_streaming_response.update_memory_layer(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
            variation_id="variationId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            variation = response.parse()
            assert_matches_type(VariationMemoryLayerAssignment, variation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_memory_layer(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.agents.variations.with_raw_response.update_memory_layer(
                id="id",
                workspace_id="",
                agent_id="agentId",
                variation_id="variationId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.variations.with_raw_response.update_memory_layer(
                id="id",
                workspace_id="workspaceId",
                agent_id="",
                variation_id="variationId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `variation_id` but received ''"):
            client.agents.variations.with_raw_response.update_memory_layer(
                id="id",
                workspace_id="workspaceId",
                agent_id="agentId",
                variation_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.agents.variations.with_raw_response.update_memory_layer(
                id="",
                workspace_id="workspaceId",
                agent_id="agentId",
                variation_id="variationId",
            )


class TestAsyncVariations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCadenya) -> None:
        variation = await async_client.agents.variations.create(
            agent_id="agentId",
            workspace_id="workspaceId",
            metadata={"name": "name"},
            spec={},
        )
        assert_matches_type(AgentVariation, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCadenya) -> None:
        variation = await async_client.agents.variations.create(
            agent_id="agentId",
            workspace_id="workspaceId",
            metadata={
                "name": "name",
                "external_id": "externalId",
                "labels": {"foo": "string"},
            },
            spec={
                "compaction_config": {
                    "summarization": {"instructions": "instructions"},
                    "tool_result_clearing": {"preserve_recent_results": 0},
                    "trigger_threshold": 0,
                },
                "constraints": {
                    "inactivity_timeout": "-160513s",
                    "max_sub_objectives": 0,
                    "max_tool_calls": 0,
                },
                "description": "description",
                "first_user_message_template": "firstUserMessageTemplate",
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
                "weight": 0,
            },
        )
        assert_matches_type(AgentVariation, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCadenya) -> None:
        response = await async_client.agents.variations.with_raw_response.create(
            agent_id="agentId",
            workspace_id="workspaceId",
            metadata={"name": "name"},
            spec={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variation = await response.parse()
        assert_matches_type(AgentVariation, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCadenya) -> None:
        async with async_client.agents.variations.with_streaming_response.create(
            agent_id="agentId",
            workspace_id="workspaceId",
            metadata={"name": "name"},
            spec={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            variation = await response.parse()
            assert_matches_type(AgentVariation, variation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.agents.variations.with_raw_response.create(
                agent_id="agentId",
                workspace_id="",
                metadata={"name": "name"},
                spec={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.variations.with_raw_response.create(
                agent_id="",
                workspace_id="workspaceId",
                metadata={"name": "name"},
                spec={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCadenya) -> None:
        variation = await async_client.agents.variations.retrieve(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
        )
        assert_matches_type(AgentVariation, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCadenya) -> None:
        response = await async_client.agents.variations.with_raw_response.retrieve(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variation = await response.parse()
        assert_matches_type(AgentVariation, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCadenya) -> None:
        async with async_client.agents.variations.with_streaming_response.retrieve(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            variation = await response.parse()
            assert_matches_type(AgentVariation, variation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.agents.variations.with_raw_response.retrieve(
                id="id",
                workspace_id="",
                agent_id="agentId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.variations.with_raw_response.retrieve(
                id="id",
                workspace_id="workspaceId",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.agents.variations.with_raw_response.retrieve(
                id="",
                workspace_id="workspaceId",
                agent_id="agentId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncCadenya) -> None:
        variation = await async_client.agents.variations.update(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
        )
        assert_matches_type(AgentVariation, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCadenya) -> None:
        variation = await async_client.agents.variations.update(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
            metadata={
                "name": "name",
                "external_id": "externalId",
                "labels": {"foo": "string"},
            },
            spec={
                "compaction_config": {
                    "summarization": {"instructions": "instructions"},
                    "tool_result_clearing": {"preserve_recent_results": 0},
                    "trigger_threshold": 0,
                },
                "constraints": {
                    "inactivity_timeout": "-160513s",
                    "max_sub_objectives": 0,
                    "max_tool_calls": 0,
                },
                "description": "description",
                "first_user_message_template": "firstUserMessageTemplate",
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
                "weight": 0,
            },
            update_mask="updateMask",
        )
        assert_matches_type(AgentVariation, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCadenya) -> None:
        response = await async_client.agents.variations.with_raw_response.update(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variation = await response.parse()
        assert_matches_type(AgentVariation, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCadenya) -> None:
        async with async_client.agents.variations.with_streaming_response.update(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            variation = await response.parse()
            assert_matches_type(AgentVariation, variation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.agents.variations.with_raw_response.update(
                id="id",
                workspace_id="",
                agent_id="agentId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.variations.with_raw_response.update(
                id="id",
                workspace_id="workspaceId",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.agents.variations.with_raw_response.update(
                id="",
                workspace_id="workspaceId",
                agent_id="agentId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCadenya) -> None:
        variation = await async_client.agents.variations.list(
            agent_id="agentId",
            workspace_id="workspaceId",
        )
        assert_matches_type(AsyncCursorPagination[AgentVariation], variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCadenya) -> None:
        variation = await async_client.agents.variations.list(
            agent_id="agentId",
            workspace_id="workspaceId",
            cursor="cursor",
            include_info=True,
            labels="labels",
            limit=0,
            sort_order="sortOrder",
        )
        assert_matches_type(AsyncCursorPagination[AgentVariation], variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCadenya) -> None:
        response = await async_client.agents.variations.with_raw_response.list(
            agent_id="agentId",
            workspace_id="workspaceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variation = await response.parse()
        assert_matches_type(AsyncCursorPagination[AgentVariation], variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCadenya) -> None:
        async with async_client.agents.variations.with_streaming_response.list(
            agent_id="agentId",
            workspace_id="workspaceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            variation = await response.parse()
            assert_matches_type(AsyncCursorPagination[AgentVariation], variation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.agents.variations.with_raw_response.list(
                agent_id="agentId",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.variations.with_raw_response.list(
                agent_id="",
                workspace_id="workspaceId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCadenya) -> None:
        variation = await async_client.agents.variations.delete(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
        )
        assert variation is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCadenya) -> None:
        response = await async_client.agents.variations.with_raw_response.delete(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variation = await response.parse()
        assert variation is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCadenya) -> None:
        async with async_client.agents.variations.with_streaming_response.delete(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            variation = await response.parse()
            assert variation is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.agents.variations.with_raw_response.delete(
                id="id",
                workspace_id="",
                agent_id="agentId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.variations.with_raw_response.delete(
                id="id",
                workspace_id="workspaceId",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.agents.variations.with_raw_response.delete(
                id="",
                workspace_id="workspaceId",
                agent_id="agentId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add_assignment(self, async_client: AsyncCadenya) -> None:
        variation = await async_client.agents.variations.add_assignment(
            variation_id="variationId",
            workspace_id="workspaceId",
            agent_id="agentId",
        )
        assert_matches_type(VariationAssignment, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add_assignment_with_all_params(self, async_client: AsyncCadenya) -> None:
        variation = await async_client.agents.variations.add_assignment(
            variation_id="variationId",
            workspace_id="workspaceId",
            agent_id="agentId",
            sub_agent_id="subAgentId",
            tool_id="toolId",
            tool_set_id="toolSetId",
        )
        assert_matches_type(VariationAssignment, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_add_assignment(self, async_client: AsyncCadenya) -> None:
        response = await async_client.agents.variations.with_raw_response.add_assignment(
            variation_id="variationId",
            workspace_id="workspaceId",
            agent_id="agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variation = await response.parse()
        assert_matches_type(VariationAssignment, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_add_assignment(self, async_client: AsyncCadenya) -> None:
        async with async_client.agents.variations.with_streaming_response.add_assignment(
            variation_id="variationId",
            workspace_id="workspaceId",
            agent_id="agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            variation = await response.parse()
            assert_matches_type(VariationAssignment, variation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_add_assignment(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.agents.variations.with_raw_response.add_assignment(
                variation_id="variationId",
                workspace_id="",
                agent_id="agentId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.variations.with_raw_response.add_assignment(
                variation_id="variationId",
                workspace_id="workspaceId",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `variation_id` but received ''"):
            await async_client.agents.variations.with_raw_response.add_assignment(
                variation_id="",
                workspace_id="workspaceId",
                agent_id="agentId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add_memory_layer(self, async_client: AsyncCadenya) -> None:
        variation = await async_client.agents.variations.add_memory_layer(
            variation_id="variationId",
            workspace_id="workspaceId",
            agent_id="agentId",
        )
        assert_matches_type(VariationMemoryLayerAssignment, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add_memory_layer_with_all_params(self, async_client: AsyncCadenya) -> None:
        variation = await async_client.agents.variations.add_memory_layer(
            variation_id="variationId",
            workspace_id="workspaceId",
            agent_id="agentId",
            memory_layer_id="memoryLayerId",
            position=0,
        )
        assert_matches_type(VariationMemoryLayerAssignment, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_add_memory_layer(self, async_client: AsyncCadenya) -> None:
        response = await async_client.agents.variations.with_raw_response.add_memory_layer(
            variation_id="variationId",
            workspace_id="workspaceId",
            agent_id="agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variation = await response.parse()
        assert_matches_type(VariationMemoryLayerAssignment, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_add_memory_layer(self, async_client: AsyncCadenya) -> None:
        async with async_client.agents.variations.with_streaming_response.add_memory_layer(
            variation_id="variationId",
            workspace_id="workspaceId",
            agent_id="agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            variation = await response.parse()
            assert_matches_type(VariationMemoryLayerAssignment, variation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_add_memory_layer(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.agents.variations.with_raw_response.add_memory_layer(
                variation_id="variationId",
                workspace_id="",
                agent_id="agentId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.variations.with_raw_response.add_memory_layer(
                variation_id="variationId",
                workspace_id="workspaceId",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `variation_id` but received ''"):
            await async_client.agents.variations.with_raw_response.add_memory_layer(
                variation_id="",
                workspace_id="workspaceId",
                agent_id="agentId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_remove_assignment(self, async_client: AsyncCadenya) -> None:
        variation = await async_client.agents.variations.remove_assignment(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
            variation_id="variationId",
        )
        assert variation is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_remove_assignment(self, async_client: AsyncCadenya) -> None:
        response = await async_client.agents.variations.with_raw_response.remove_assignment(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
            variation_id="variationId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variation = await response.parse()
        assert variation is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_remove_assignment(self, async_client: AsyncCadenya) -> None:
        async with async_client.agents.variations.with_streaming_response.remove_assignment(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
            variation_id="variationId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            variation = await response.parse()
            assert variation is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_remove_assignment(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.agents.variations.with_raw_response.remove_assignment(
                id="id",
                workspace_id="",
                agent_id="agentId",
                variation_id="variationId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.variations.with_raw_response.remove_assignment(
                id="id",
                workspace_id="workspaceId",
                agent_id="",
                variation_id="variationId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `variation_id` but received ''"):
            await async_client.agents.variations.with_raw_response.remove_assignment(
                id="id",
                workspace_id="workspaceId",
                agent_id="agentId",
                variation_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.agents.variations.with_raw_response.remove_assignment(
                id="",
                workspace_id="workspaceId",
                agent_id="agentId",
                variation_id="variationId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_remove_memory_layer(self, async_client: AsyncCadenya) -> None:
        variation = await async_client.agents.variations.remove_memory_layer(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
            variation_id="variationId",
        )
        assert variation is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_remove_memory_layer(self, async_client: AsyncCadenya) -> None:
        response = await async_client.agents.variations.with_raw_response.remove_memory_layer(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
            variation_id="variationId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variation = await response.parse()
        assert variation is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_remove_memory_layer(self, async_client: AsyncCadenya) -> None:
        async with async_client.agents.variations.with_streaming_response.remove_memory_layer(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
            variation_id="variationId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            variation = await response.parse()
            assert variation is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_remove_memory_layer(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.agents.variations.with_raw_response.remove_memory_layer(
                id="id",
                workspace_id="",
                agent_id="agentId",
                variation_id="variationId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.variations.with_raw_response.remove_memory_layer(
                id="id",
                workspace_id="workspaceId",
                agent_id="",
                variation_id="variationId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `variation_id` but received ''"):
            await async_client.agents.variations.with_raw_response.remove_memory_layer(
                id="id",
                workspace_id="workspaceId",
                agent_id="agentId",
                variation_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.agents.variations.with_raw_response.remove_memory_layer(
                id="",
                workspace_id="workspaceId",
                agent_id="agentId",
                variation_id="variationId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_memory_layer(self, async_client: AsyncCadenya) -> None:
        variation = await async_client.agents.variations.update_memory_layer(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
            variation_id="variationId",
        )
        assert_matches_type(VariationMemoryLayerAssignment, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_memory_layer_with_all_params(self, async_client: AsyncCadenya) -> None:
        variation = await async_client.agents.variations.update_memory_layer(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
            variation_id="variationId",
            position=0,
        )
        assert_matches_type(VariationMemoryLayerAssignment, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_memory_layer(self, async_client: AsyncCadenya) -> None:
        response = await async_client.agents.variations.with_raw_response.update_memory_layer(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
            variation_id="variationId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variation = await response.parse()
        assert_matches_type(VariationMemoryLayerAssignment, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_memory_layer(self, async_client: AsyncCadenya) -> None:
        async with async_client.agents.variations.with_streaming_response.update_memory_layer(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
            variation_id="variationId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            variation = await response.parse()
            assert_matches_type(VariationMemoryLayerAssignment, variation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_memory_layer(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.agents.variations.with_raw_response.update_memory_layer(
                id="id",
                workspace_id="",
                agent_id="agentId",
                variation_id="variationId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.variations.with_raw_response.update_memory_layer(
                id="id",
                workspace_id="workspaceId",
                agent_id="",
                variation_id="variationId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `variation_id` but received ''"):
            await async_client.agents.variations.with_raw_response.update_memory_layer(
                id="id",
                workspace_id="workspaceId",
                agent_id="agentId",
                variation_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.agents.variations.with_raw_response.update_memory_layer(
                id="",
                workspace_id="workspaceId",
                agent_id="agentId",
                variation_id="variationId",
            )
