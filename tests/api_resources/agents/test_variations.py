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
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            metadata={"name": "name"},
            spec={},
        )
        assert_matches_type(AgentVariation, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Cadenya) -> None:
        variation = client.agents.variations.create(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
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
                    "model_id": "claude/opus-4.6",
                    "temperature": 0,
                },
                "progressive_discovery": {
                    "hints": ["string"],
                    "max_tools": 0,
                },
                "system_prompt_template": "systemPromptTemplate",
            },
        )
        assert_matches_type(AgentVariation, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Cadenya) -> None:
        response = client.agents.variations.with_raw_response.create(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
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
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
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
                agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
                workspace_id="",
                metadata={"name": "name"},
                spec={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.variations.with_raw_response.create(
                agent_id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
                metadata={"name": "name"},
                spec={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Cadenya) -> None:
        variation = client.agents.variations.retrieve(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert_matches_type(AgentVariation, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Cadenya) -> None:
        response = client.agents.variations.with_raw_response.retrieve(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variation = response.parse()
        assert_matches_type(AgentVariation, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Cadenya) -> None:
        with client.agents.variations.with_streaming_response.retrieve(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
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
                agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
                id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.variations.with_raw_response.retrieve(
                agent_id="",
                id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.agents.variations.with_raw_response.retrieve(
                agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
                id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Cadenya) -> None:
        variation = client.agents.variations.update(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert_matches_type(AgentVariation, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Cadenya) -> None:
        variation = client.agents.variations.update(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
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
                    "model_id": "claude/opus-4.6",
                    "temperature": 0,
                },
                "progressive_discovery": {
                    "hints": ["string"],
                    "max_tools": 0,
                },
                "system_prompt_template": "systemPromptTemplate",
            },
            update_mask="updateMask",
        )
        assert_matches_type(AgentVariation, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Cadenya) -> None:
        response = client.agents.variations.with_raw_response.update(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variation = response.parse()
        assert_matches_type(AgentVariation, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Cadenya) -> None:
        with client.agents.variations.with_streaming_response.update(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
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
                agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
                id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.variations.with_raw_response.update(
                agent_id="",
                id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.agents.variations.with_raw_response.update(
                agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
                id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Cadenya) -> None:
        variation = client.agents.variations.list(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert_matches_type(SyncCursorPagination[AgentVariation], variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Cadenya) -> None:
        variation = client.agents.variations.list(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
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
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variation = response.parse()
        assert_matches_type(SyncCursorPagination[AgentVariation], variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Cadenya) -> None:
        with client.agents.variations.with_streaming_response.list(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
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
                agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.variations.with_raw_response.list(
                agent_id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Cadenya) -> None:
        variation = client.agents.variations.delete(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert variation is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Cadenya) -> None:
        response = client.agents.variations.with_raw_response.delete(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variation = response.parse()
        assert variation is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Cadenya) -> None:
        with client.agents.variations.with_streaming_response.delete(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
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
                agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
                id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.variations.with_raw_response.delete(
                agent_id="",
                id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.agents.variations.with_raw_response.delete(
                agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
                id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add_assignment_overload_1(self, client: Cadenya) -> None:
        variation = client.agents.variations.add_assignment(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            tool_id="tool_01HXKD2E5NQM3T9AYWCFWVYY9K",
            type="toolId",
        )
        assert_matches_type(VariationAssignment, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_add_assignment_overload_1(self, client: Cadenya) -> None:
        response = client.agents.variations.with_raw_response.add_assignment(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            tool_id="tool_01HXKD2E5NQM3T9AYWCFWVYY9K",
            type="toolId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variation = response.parse()
        assert_matches_type(VariationAssignment, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_add_assignment_overload_1(self, client: Cadenya) -> None:
        with client.agents.variations.with_streaming_response.add_assignment(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            tool_id="tool_01HXKD2E5NQM3T9AYWCFWVYY9K",
            type="toolId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            variation = response.parse()
            assert_matches_type(VariationAssignment, variation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_add_assignment_overload_1(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.agents.variations.with_raw_response.add_assignment(
                agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
                variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
                workspace_id="",
                tool_id="tool_01HXKD2E5NQM3T9AYWCFWVYY9K",
                type="toolId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.variations.with_raw_response.add_assignment(
                agent_id="",
                variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
                tool_id="tool_01HXKD2E5NQM3T9AYWCFWVYY9K",
                type="toolId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `variation_id` but received ''"):
            client.agents.variations.with_raw_response.add_assignment(
                agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
                variation_id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
                tool_id="tool_01HXKD2E5NQM3T9AYWCFWVYY9K",
                type="toolId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add_assignment_overload_2(self, client: Cadenya) -> None:
        variation = client.agents.variations.add_assignment(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            tool_set_id="toolset_01HXKD2E5NQM3T9AYWCFNRMN74",
            type="toolSetId",
        )
        assert_matches_type(VariationAssignment, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_add_assignment_overload_2(self, client: Cadenya) -> None:
        response = client.agents.variations.with_raw_response.add_assignment(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            tool_set_id="toolset_01HXKD2E5NQM3T9AYWCFNRMN74",
            type="toolSetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variation = response.parse()
        assert_matches_type(VariationAssignment, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_add_assignment_overload_2(self, client: Cadenya) -> None:
        with client.agents.variations.with_streaming_response.add_assignment(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            tool_set_id="toolset_01HXKD2E5NQM3T9AYWCFNRMN74",
            type="toolSetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            variation = response.parse()
            assert_matches_type(VariationAssignment, variation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_add_assignment_overload_2(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.agents.variations.with_raw_response.add_assignment(
                agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
                variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
                workspace_id="",
                tool_set_id="toolset_01HXKD2E5NQM3T9AYWCFNRMN74",
                type="toolSetId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.variations.with_raw_response.add_assignment(
                agent_id="",
                variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
                tool_set_id="toolset_01HXKD2E5NQM3T9AYWCFNRMN74",
                type="toolSetId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `variation_id` but received ''"):
            client.agents.variations.with_raw_response.add_assignment(
                agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
                variation_id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
                tool_set_id="toolset_01HXKD2E5NQM3T9AYWCFNRMN74",
                type="toolSetId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add_assignment_overload_3(self, client: Cadenya) -> None:
        variation = client.agents.variations.add_assignment(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            sub_agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            type="subAgentId",
        )
        assert_matches_type(VariationAssignment, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_add_assignment_overload_3(self, client: Cadenya) -> None:
        response = client.agents.variations.with_raw_response.add_assignment(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            sub_agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            type="subAgentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variation = response.parse()
        assert_matches_type(VariationAssignment, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_add_assignment_overload_3(self, client: Cadenya) -> None:
        with client.agents.variations.with_streaming_response.add_assignment(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            sub_agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            type="subAgentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            variation = response.parse()
            assert_matches_type(VariationAssignment, variation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_add_assignment_overload_3(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.agents.variations.with_raw_response.add_assignment(
                agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
                variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
                workspace_id="",
                sub_agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
                type="subAgentId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.variations.with_raw_response.add_assignment(
                agent_id="",
                variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
                sub_agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
                type="subAgentId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `variation_id` but received ''"):
            client.agents.variations.with_raw_response.add_assignment(
                agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
                variation_id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
                sub_agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
                type="subAgentId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add_memory_layer(self, client: Cadenya) -> None:
        variation = client.agents.variations.add_memory_layer(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            memory_layer_id="memlyr_01HXKD2E5NQM3T9AYWCFFFBMJH",
        )
        assert_matches_type(VariationMemoryLayerAssignment, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add_memory_layer_with_all_params(self, client: Cadenya) -> None:
        variation = client.agents.variations.add_memory_layer(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            memory_layer_id="memlyr_01HXKD2E5NQM3T9AYWCFFFBMJH",
            position=0,
        )
        assert_matches_type(VariationMemoryLayerAssignment, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_add_memory_layer(self, client: Cadenya) -> None:
        response = client.agents.variations.with_raw_response.add_memory_layer(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            memory_layer_id="memlyr_01HXKD2E5NQM3T9AYWCFFFBMJH",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variation = response.parse()
        assert_matches_type(VariationMemoryLayerAssignment, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_add_memory_layer(self, client: Cadenya) -> None:
        with client.agents.variations.with_streaming_response.add_memory_layer(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            memory_layer_id="memlyr_01HXKD2E5NQM3T9AYWCFFFBMJH",
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
                agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
                variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
                workspace_id="",
                memory_layer_id="memlyr_01HXKD2E5NQM3T9AYWCFFFBMJH",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.variations.with_raw_response.add_memory_layer(
                agent_id="",
                variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
                memory_layer_id="memlyr_01HXKD2E5NQM3T9AYWCFFFBMJH",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `variation_id` but received ''"):
            client.agents.variations.with_raw_response.add_memory_layer(
                agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
                variation_id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
                memory_layer_id="memlyr_01HXKD2E5NQM3T9AYWCFFFBMJH",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_remove_assignment(self, client: Cadenya) -> None:
        variation = client.agents.variations.remove_assignment(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            id="avt_01HXKD2E5NQM3T9AYWCFJE6K89",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert variation is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_remove_assignment(self, client: Cadenya) -> None:
        response = client.agents.variations.with_raw_response.remove_assignment(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            id="avt_01HXKD2E5NQM3T9AYWCFJE6K89",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variation = response.parse()
        assert variation is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_remove_assignment(self, client: Cadenya) -> None:
        with client.agents.variations.with_streaming_response.remove_assignment(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            id="avt_01HXKD2E5NQM3T9AYWCFJE6K89",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
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
                agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
                variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
                id="avt_01HXKD2E5NQM3T9AYWCFJE6K89",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.variations.with_raw_response.remove_assignment(
                agent_id="",
                variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
                id="avt_01HXKD2E5NQM3T9AYWCFJE6K89",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `variation_id` but received ''"):
            client.agents.variations.with_raw_response.remove_assignment(
                agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
                variation_id="",
                id="avt_01HXKD2E5NQM3T9AYWCFJE6K89",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.agents.variations.with_raw_response.remove_assignment(
                agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
                variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
                id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_remove_memory_layer(self, client: Cadenya) -> None:
        variation = client.agents.variations.remove_memory_layer(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            id="avml_01HXKD2E5NQM3T9AYWCFX8AF59",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert variation is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_remove_memory_layer(self, client: Cadenya) -> None:
        response = client.agents.variations.with_raw_response.remove_memory_layer(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            id="avml_01HXKD2E5NQM3T9AYWCFX8AF59",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variation = response.parse()
        assert variation is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_remove_memory_layer(self, client: Cadenya) -> None:
        with client.agents.variations.with_streaming_response.remove_memory_layer(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            id="avml_01HXKD2E5NQM3T9AYWCFX8AF59",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
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
                agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
                variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
                id="avml_01HXKD2E5NQM3T9AYWCFX8AF59",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.variations.with_raw_response.remove_memory_layer(
                agent_id="",
                variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
                id="avml_01HXKD2E5NQM3T9AYWCFX8AF59",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `variation_id` but received ''"):
            client.agents.variations.with_raw_response.remove_memory_layer(
                agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
                variation_id="",
                id="avml_01HXKD2E5NQM3T9AYWCFX8AF59",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.agents.variations.with_raw_response.remove_memory_layer(
                agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
                variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
                id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_memory_layer(self, client: Cadenya) -> None:
        variation = client.agents.variations.update_memory_layer(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            id="avml_01HXKD2E5NQM3T9AYWCFX8AF59",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert_matches_type(VariationMemoryLayerAssignment, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_memory_layer_with_all_params(self, client: Cadenya) -> None:
        variation = client.agents.variations.update_memory_layer(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            id="avml_01HXKD2E5NQM3T9AYWCFX8AF59",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            position=0,
        )
        assert_matches_type(VariationMemoryLayerAssignment, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_memory_layer(self, client: Cadenya) -> None:
        response = client.agents.variations.with_raw_response.update_memory_layer(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            id="avml_01HXKD2E5NQM3T9AYWCFX8AF59",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variation = response.parse()
        assert_matches_type(VariationMemoryLayerAssignment, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_memory_layer(self, client: Cadenya) -> None:
        with client.agents.variations.with_streaming_response.update_memory_layer(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            id="avml_01HXKD2E5NQM3T9AYWCFX8AF59",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
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
                agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
                variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
                id="avml_01HXKD2E5NQM3T9AYWCFX8AF59",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.variations.with_raw_response.update_memory_layer(
                agent_id="",
                variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
                id="avml_01HXKD2E5NQM3T9AYWCFX8AF59",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `variation_id` but received ''"):
            client.agents.variations.with_raw_response.update_memory_layer(
                agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
                variation_id="",
                id="avml_01HXKD2E5NQM3T9AYWCFX8AF59",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.agents.variations.with_raw_response.update_memory_layer(
                agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
                variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
                id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )


class TestAsyncVariations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCadenya) -> None:
        variation = await async_client.agents.variations.create(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            metadata={"name": "name"},
            spec={},
        )
        assert_matches_type(AgentVariation, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCadenya) -> None:
        variation = await async_client.agents.variations.create(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
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
                    "model_id": "claude/opus-4.6",
                    "temperature": 0,
                },
                "progressive_discovery": {
                    "hints": ["string"],
                    "max_tools": 0,
                },
                "system_prompt_template": "systemPromptTemplate",
            },
        )
        assert_matches_type(AgentVariation, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCadenya) -> None:
        response = await async_client.agents.variations.with_raw_response.create(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
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
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
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
                agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
                workspace_id="",
                metadata={"name": "name"},
                spec={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.variations.with_raw_response.create(
                agent_id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
                metadata={"name": "name"},
                spec={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCadenya) -> None:
        variation = await async_client.agents.variations.retrieve(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert_matches_type(AgentVariation, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCadenya) -> None:
        response = await async_client.agents.variations.with_raw_response.retrieve(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variation = await response.parse()
        assert_matches_type(AgentVariation, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCadenya) -> None:
        async with async_client.agents.variations.with_streaming_response.retrieve(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
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
                agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
                id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.variations.with_raw_response.retrieve(
                agent_id="",
                id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.agents.variations.with_raw_response.retrieve(
                agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
                id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncCadenya) -> None:
        variation = await async_client.agents.variations.update(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert_matches_type(AgentVariation, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCadenya) -> None:
        variation = await async_client.agents.variations.update(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
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
                    "model_id": "claude/opus-4.6",
                    "temperature": 0,
                },
                "progressive_discovery": {
                    "hints": ["string"],
                    "max_tools": 0,
                },
                "system_prompt_template": "systemPromptTemplate",
            },
            update_mask="updateMask",
        )
        assert_matches_type(AgentVariation, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCadenya) -> None:
        response = await async_client.agents.variations.with_raw_response.update(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variation = await response.parse()
        assert_matches_type(AgentVariation, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCadenya) -> None:
        async with async_client.agents.variations.with_streaming_response.update(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
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
                agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
                id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.variations.with_raw_response.update(
                agent_id="",
                id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.agents.variations.with_raw_response.update(
                agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
                id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCadenya) -> None:
        variation = await async_client.agents.variations.list(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert_matches_type(AsyncCursorPagination[AgentVariation], variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCadenya) -> None:
        variation = await async_client.agents.variations.list(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
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
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variation = await response.parse()
        assert_matches_type(AsyncCursorPagination[AgentVariation], variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCadenya) -> None:
        async with async_client.agents.variations.with_streaming_response.list(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
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
                agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.variations.with_raw_response.list(
                agent_id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCadenya) -> None:
        variation = await async_client.agents.variations.delete(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert variation is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCadenya) -> None:
        response = await async_client.agents.variations.with_raw_response.delete(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variation = await response.parse()
        assert variation is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCadenya) -> None:
        async with async_client.agents.variations.with_streaming_response.delete(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
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
                agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
                id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.variations.with_raw_response.delete(
                agent_id="",
                id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.agents.variations.with_raw_response.delete(
                agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
                id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add_assignment_overload_1(self, async_client: AsyncCadenya) -> None:
        variation = await async_client.agents.variations.add_assignment(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            tool_id="tool_01HXKD2E5NQM3T9AYWCFWVYY9K",
            type="toolId",
        )
        assert_matches_type(VariationAssignment, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_add_assignment_overload_1(self, async_client: AsyncCadenya) -> None:
        response = await async_client.agents.variations.with_raw_response.add_assignment(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            tool_id="tool_01HXKD2E5NQM3T9AYWCFWVYY9K",
            type="toolId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variation = await response.parse()
        assert_matches_type(VariationAssignment, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_add_assignment_overload_1(self, async_client: AsyncCadenya) -> None:
        async with async_client.agents.variations.with_streaming_response.add_assignment(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            tool_id="tool_01HXKD2E5NQM3T9AYWCFWVYY9K",
            type="toolId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            variation = await response.parse()
            assert_matches_type(VariationAssignment, variation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_add_assignment_overload_1(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.agents.variations.with_raw_response.add_assignment(
                agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
                variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
                workspace_id="",
                tool_id="tool_01HXKD2E5NQM3T9AYWCFWVYY9K",
                type="toolId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.variations.with_raw_response.add_assignment(
                agent_id="",
                variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
                tool_id="tool_01HXKD2E5NQM3T9AYWCFWVYY9K",
                type="toolId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `variation_id` but received ''"):
            await async_client.agents.variations.with_raw_response.add_assignment(
                agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
                variation_id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
                tool_id="tool_01HXKD2E5NQM3T9AYWCFWVYY9K",
                type="toolId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add_assignment_overload_2(self, async_client: AsyncCadenya) -> None:
        variation = await async_client.agents.variations.add_assignment(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            tool_set_id="toolset_01HXKD2E5NQM3T9AYWCFNRMN74",
            type="toolSetId",
        )
        assert_matches_type(VariationAssignment, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_add_assignment_overload_2(self, async_client: AsyncCadenya) -> None:
        response = await async_client.agents.variations.with_raw_response.add_assignment(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            tool_set_id="toolset_01HXKD2E5NQM3T9AYWCFNRMN74",
            type="toolSetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variation = await response.parse()
        assert_matches_type(VariationAssignment, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_add_assignment_overload_2(self, async_client: AsyncCadenya) -> None:
        async with async_client.agents.variations.with_streaming_response.add_assignment(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            tool_set_id="toolset_01HXKD2E5NQM3T9AYWCFNRMN74",
            type="toolSetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            variation = await response.parse()
            assert_matches_type(VariationAssignment, variation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_add_assignment_overload_2(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.agents.variations.with_raw_response.add_assignment(
                agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
                variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
                workspace_id="",
                tool_set_id="toolset_01HXKD2E5NQM3T9AYWCFNRMN74",
                type="toolSetId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.variations.with_raw_response.add_assignment(
                agent_id="",
                variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
                tool_set_id="toolset_01HXKD2E5NQM3T9AYWCFNRMN74",
                type="toolSetId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `variation_id` but received ''"):
            await async_client.agents.variations.with_raw_response.add_assignment(
                agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
                variation_id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
                tool_set_id="toolset_01HXKD2E5NQM3T9AYWCFNRMN74",
                type="toolSetId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add_assignment_overload_3(self, async_client: AsyncCadenya) -> None:
        variation = await async_client.agents.variations.add_assignment(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            sub_agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            type="subAgentId",
        )
        assert_matches_type(VariationAssignment, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_add_assignment_overload_3(self, async_client: AsyncCadenya) -> None:
        response = await async_client.agents.variations.with_raw_response.add_assignment(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            sub_agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            type="subAgentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variation = await response.parse()
        assert_matches_type(VariationAssignment, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_add_assignment_overload_3(self, async_client: AsyncCadenya) -> None:
        async with async_client.agents.variations.with_streaming_response.add_assignment(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            sub_agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            type="subAgentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            variation = await response.parse()
            assert_matches_type(VariationAssignment, variation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_add_assignment_overload_3(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.agents.variations.with_raw_response.add_assignment(
                agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
                variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
                workspace_id="",
                sub_agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
                type="subAgentId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.variations.with_raw_response.add_assignment(
                agent_id="",
                variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
                sub_agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
                type="subAgentId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `variation_id` but received ''"):
            await async_client.agents.variations.with_raw_response.add_assignment(
                agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
                variation_id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
                sub_agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
                type="subAgentId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add_memory_layer(self, async_client: AsyncCadenya) -> None:
        variation = await async_client.agents.variations.add_memory_layer(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            memory_layer_id="memlyr_01HXKD2E5NQM3T9AYWCFFFBMJH",
        )
        assert_matches_type(VariationMemoryLayerAssignment, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add_memory_layer_with_all_params(self, async_client: AsyncCadenya) -> None:
        variation = await async_client.agents.variations.add_memory_layer(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            memory_layer_id="memlyr_01HXKD2E5NQM3T9AYWCFFFBMJH",
            position=0,
        )
        assert_matches_type(VariationMemoryLayerAssignment, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_add_memory_layer(self, async_client: AsyncCadenya) -> None:
        response = await async_client.agents.variations.with_raw_response.add_memory_layer(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            memory_layer_id="memlyr_01HXKD2E5NQM3T9AYWCFFFBMJH",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variation = await response.parse()
        assert_matches_type(VariationMemoryLayerAssignment, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_add_memory_layer(self, async_client: AsyncCadenya) -> None:
        async with async_client.agents.variations.with_streaming_response.add_memory_layer(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            memory_layer_id="memlyr_01HXKD2E5NQM3T9AYWCFFFBMJH",
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
                agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
                variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
                workspace_id="",
                memory_layer_id="memlyr_01HXKD2E5NQM3T9AYWCFFFBMJH",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.variations.with_raw_response.add_memory_layer(
                agent_id="",
                variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
                memory_layer_id="memlyr_01HXKD2E5NQM3T9AYWCFFFBMJH",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `variation_id` but received ''"):
            await async_client.agents.variations.with_raw_response.add_memory_layer(
                agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
                variation_id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
                memory_layer_id="memlyr_01HXKD2E5NQM3T9AYWCFFFBMJH",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_remove_assignment(self, async_client: AsyncCadenya) -> None:
        variation = await async_client.agents.variations.remove_assignment(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            id="avt_01HXKD2E5NQM3T9AYWCFJE6K89",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert variation is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_remove_assignment(self, async_client: AsyncCadenya) -> None:
        response = await async_client.agents.variations.with_raw_response.remove_assignment(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            id="avt_01HXKD2E5NQM3T9AYWCFJE6K89",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variation = await response.parse()
        assert variation is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_remove_assignment(self, async_client: AsyncCadenya) -> None:
        async with async_client.agents.variations.with_streaming_response.remove_assignment(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            id="avt_01HXKD2E5NQM3T9AYWCFJE6K89",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
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
                agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
                variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
                id="avt_01HXKD2E5NQM3T9AYWCFJE6K89",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.variations.with_raw_response.remove_assignment(
                agent_id="",
                variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
                id="avt_01HXKD2E5NQM3T9AYWCFJE6K89",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `variation_id` but received ''"):
            await async_client.agents.variations.with_raw_response.remove_assignment(
                agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
                variation_id="",
                id="avt_01HXKD2E5NQM3T9AYWCFJE6K89",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.agents.variations.with_raw_response.remove_assignment(
                agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
                variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
                id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_remove_memory_layer(self, async_client: AsyncCadenya) -> None:
        variation = await async_client.agents.variations.remove_memory_layer(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            id="avml_01HXKD2E5NQM3T9AYWCFX8AF59",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert variation is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_remove_memory_layer(self, async_client: AsyncCadenya) -> None:
        response = await async_client.agents.variations.with_raw_response.remove_memory_layer(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            id="avml_01HXKD2E5NQM3T9AYWCFX8AF59",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variation = await response.parse()
        assert variation is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_remove_memory_layer(self, async_client: AsyncCadenya) -> None:
        async with async_client.agents.variations.with_streaming_response.remove_memory_layer(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            id="avml_01HXKD2E5NQM3T9AYWCFX8AF59",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
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
                agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
                variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
                id="avml_01HXKD2E5NQM3T9AYWCFX8AF59",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.variations.with_raw_response.remove_memory_layer(
                agent_id="",
                variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
                id="avml_01HXKD2E5NQM3T9AYWCFX8AF59",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `variation_id` but received ''"):
            await async_client.agents.variations.with_raw_response.remove_memory_layer(
                agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
                variation_id="",
                id="avml_01HXKD2E5NQM3T9AYWCFX8AF59",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.agents.variations.with_raw_response.remove_memory_layer(
                agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
                variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
                id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_memory_layer(self, async_client: AsyncCadenya) -> None:
        variation = await async_client.agents.variations.update_memory_layer(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            id="avml_01HXKD2E5NQM3T9AYWCFX8AF59",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert_matches_type(VariationMemoryLayerAssignment, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_memory_layer_with_all_params(self, async_client: AsyncCadenya) -> None:
        variation = await async_client.agents.variations.update_memory_layer(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            id="avml_01HXKD2E5NQM3T9AYWCFX8AF59",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            position=0,
        )
        assert_matches_type(VariationMemoryLayerAssignment, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_memory_layer(self, async_client: AsyncCadenya) -> None:
        response = await async_client.agents.variations.with_raw_response.update_memory_layer(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            id="avml_01HXKD2E5NQM3T9AYWCFX8AF59",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        variation = await response.parse()
        assert_matches_type(VariationMemoryLayerAssignment, variation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_memory_layer(self, async_client: AsyncCadenya) -> None:
        async with async_client.agents.variations.with_streaming_response.update_memory_layer(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
            id="avml_01HXKD2E5NQM3T9AYWCFX8AF59",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
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
                agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
                variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
                id="avml_01HXKD2E5NQM3T9AYWCFX8AF59",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.variations.with_raw_response.update_memory_layer(
                agent_id="",
                variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
                id="avml_01HXKD2E5NQM3T9AYWCFX8AF59",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `variation_id` but received ''"):
            await async_client.agents.variations.with_raw_response.update_memory_layer(
                agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
                variation_id="",
                id="avml_01HXKD2E5NQM3T9AYWCFX8AF59",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.agents.variations.with_raw_response.update_memory_layer(
                agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
                variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
                id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )
