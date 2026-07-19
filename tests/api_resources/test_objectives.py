# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cadenya import Cadenya, AsyncCadenya
from tests.utils import assert_matches_type
from cadenya.types import (
    Objective,
    ObjectiveEvent,
    ObjectiveContextWindow,
    ObjectiveCompactResponse,
    ObjectiveRetrieveDiagnosticsResponse,
)
from cadenya.pagination import SyncCursorPagination, AsyncCursorPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestObjectives:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Cadenya) -> None:
        objective = client.objectives.create(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            system_prompt_data={"foo": "bar"},
        )
        assert_matches_type(Objective, objective, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Cadenya) -> None:
        objective = client.objectives.create(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            system_prompt_data={"foo": "bar"},
            episodic_memory={"key": "key"},
            first_user_message="firstUserMessage",
            first_user_message_data={"foo": "bar"},
            memory_cascade=[
                {
                    "memory_layer_id": "memlyr_01HXKD2E5NQM3T9AYWCFFFBMJH",
                    "memory_entry_id": "mementry_01HXKD2E5NQM3T9AYWCF5E52Z0",
                }
            ],
            metadata={
                "external_id": "externalId",
                "labels": {"foo": "string"},
            },
            secrets=[
                {
                    "name": "name",
                    "value": "value",
                }
            ],
            variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
        )
        assert_matches_type(Objective, objective, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Cadenya) -> None:
        response = client.objectives.with_raw_response.create(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            system_prompt_data={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        objective = response.parse()
        assert_matches_type(Objective, objective, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Cadenya) -> None:
        with client.objectives.with_streaming_response.create(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            system_prompt_data={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            objective = response.parse()
            assert_matches_type(Objective, objective, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.objectives.with_raw_response.create(
                workspace_id="",
                agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
                system_prompt_data={"foo": "bar"},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Cadenya) -> None:
        objective = client.objectives.retrieve(
            id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert_matches_type(Objective, objective, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Cadenya) -> None:
        response = client.objectives.with_raw_response.retrieve(
            id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        objective = response.parse()
        assert_matches_type(Objective, objective, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Cadenya) -> None:
        with client.objectives.with_streaming_response.retrieve(
            id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            objective = response.parse()
            assert_matches_type(Objective, objective, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.objectives.with_raw_response.retrieve(
                id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.objectives.with_raw_response.retrieve(
                id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Cadenya) -> None:
        objective = client.objectives.list(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert_matches_type(SyncCursorPagination[Objective], objective, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Cadenya) -> None:
        objective = client.objectives.list(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            agent_schedule_id="agentScheduleId",
            cursor="cursor",
            include_info=True,
            labels="labels",
            limit=0,
            parent_objective_id="parentObjectiveId",
            profile_id="profile_01HXKD2E5NQM3T9AYWCFS0AP08",
            sort_order="sortOrder",
            state="STATE_UNSPECIFIED",
        )
        assert_matches_type(SyncCursorPagination[Objective], objective, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Cadenya) -> None:
        response = client.objectives.with_raw_response.list(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        objective = response.parse()
        assert_matches_type(SyncCursorPagination[Objective], objective, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Cadenya) -> None:
        with client.objectives.with_streaming_response.list(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            objective = response.parse()
            assert_matches_type(SyncCursorPagination[Objective], objective, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.objectives.with_raw_response.list(
                workspace_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_cancel(self, client: Cadenya) -> None:
        objective = client.objectives.cancel(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert_matches_type(Objective, objective, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_cancel_with_all_params(self, client: Cadenya) -> None:
        objective = client.objectives.cancel(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            reason="reason",
        )
        assert_matches_type(Objective, objective, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_cancel(self, client: Cadenya) -> None:
        response = client.objectives.with_raw_response.cancel(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        objective = response.parse()
        assert_matches_type(Objective, objective, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_cancel(self, client: Cadenya) -> None:
        with client.objectives.with_streaming_response.cancel(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            objective = response.parse()
            assert_matches_type(Objective, objective, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_cancel(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.objectives.with_raw_response.cancel(
                objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `objective_id` but received ''"):
            client.objectives.with_raw_response.cancel(
                objective_id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_compact(self, client: Cadenya) -> None:
        objective = client.objectives.compact(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert_matches_type(ObjectiveCompactResponse, objective, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_compact_with_all_params(self, client: Cadenya) -> None:
        objective = client.objectives.compact(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            compaction_config={
                "summarization": {"instructions": "instructions"},
                "tool_result_clearing": {"preserve_recent_results": 0},
                "trigger_threshold": 0,
            },
        )
        assert_matches_type(ObjectiveCompactResponse, objective, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_compact(self, client: Cadenya) -> None:
        response = client.objectives.with_raw_response.compact(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        objective = response.parse()
        assert_matches_type(ObjectiveCompactResponse, objective, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_compact(self, client: Cadenya) -> None:
        with client.objectives.with_streaming_response.compact(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            objective = response.parse()
            assert_matches_type(ObjectiveCompactResponse, objective, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_compact(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.objectives.with_raw_response.compact(
                objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `objective_id` but received ''"):
            client.objectives.with_raw_response.compact(
                objective_id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_continue(self, client: Cadenya) -> None:
        objective = client.objectives.continue_(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            message="message",
        )
        assert_matches_type(ObjectiveEvent, objective, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_continue_with_all_params(self, client: Cadenya) -> None:
        objective = client.objectives.continue_(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            message="message",
            enqueue=True,
        )
        assert_matches_type(ObjectiveEvent, objective, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_continue(self, client: Cadenya) -> None:
        response = client.objectives.with_raw_response.continue_(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            message="message",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        objective = response.parse()
        assert_matches_type(ObjectiveEvent, objective, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_continue(self, client: Cadenya) -> None:
        with client.objectives.with_streaming_response.continue_(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            message="message",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            objective = response.parse()
            assert_matches_type(ObjectiveEvent, objective, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_continue(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.objectives.with_raw_response.continue_(
                objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
                workspace_id="",
                message="message",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `objective_id` but received ''"):
            client.objectives.with_raw_response.continue_(
                objective_id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
                message="message",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_context_windows(self, client: Cadenya) -> None:
        objective = client.objectives.list_context_windows(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert_matches_type(SyncCursorPagination[ObjectiveContextWindow], objective, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_context_windows_with_all_params(self, client: Cadenya) -> None:
        objective = client.objectives.list_context_windows(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            cursor="cursor",
            include_info=True,
            labels="labels",
            limit=0,
        )
        assert_matches_type(SyncCursorPagination[ObjectiveContextWindow], objective, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_context_windows(self, client: Cadenya) -> None:
        response = client.objectives.with_raw_response.list_context_windows(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        objective = response.parse()
        assert_matches_type(SyncCursorPagination[ObjectiveContextWindow], objective, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_context_windows(self, client: Cadenya) -> None:
        with client.objectives.with_streaming_response.list_context_windows(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            objective = response.parse()
            assert_matches_type(SyncCursorPagination[ObjectiveContextWindow], objective, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_context_windows(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.objectives.with_raw_response.list_context_windows(
                objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `objective_id` but received ''"):
            client.objectives.with_raw_response.list_context_windows(
                objective_id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_events(self, client: Cadenya) -> None:
        objective = client.objectives.list_events(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert_matches_type(SyncCursorPagination[ObjectiveEvent], objective, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_events_with_all_params(self, client: Cadenya) -> None:
        objective = client.objectives.list_events(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            cursor="cursor",
            include_info=True,
            labels="labels",
            limit=0,
            since_event_id="sinceEventId",
            sort_order="sortOrder",
            window_id="windowId",
        )
        assert_matches_type(SyncCursorPagination[ObjectiveEvent], objective, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_events(self, client: Cadenya) -> None:
        response = client.objectives.with_raw_response.list_events(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        objective = response.parse()
        assert_matches_type(SyncCursorPagination[ObjectiveEvent], objective, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_events(self, client: Cadenya) -> None:
        with client.objectives.with_streaming_response.list_events(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            objective = response.parse()
            assert_matches_type(SyncCursorPagination[ObjectiveEvent], objective, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_events(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.objectives.with_raw_response.list_events(
                objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `objective_id` but received ''"):
            client.objectives.with_raw_response.list_events(
                objective_id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_diagnostics(self, client: Cadenya) -> None:
        objective = client.objectives.retrieve_diagnostics(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert_matches_type(ObjectiveRetrieveDiagnosticsResponse, objective, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_diagnostics(self, client: Cadenya) -> None:
        response = client.objectives.with_raw_response.retrieve_diagnostics(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        objective = response.parse()
        assert_matches_type(ObjectiveRetrieveDiagnosticsResponse, objective, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_diagnostics(self, client: Cadenya) -> None:
        with client.objectives.with_streaming_response.retrieve_diagnostics(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            objective = response.parse()
            assert_matches_type(ObjectiveRetrieveDiagnosticsResponse, objective, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_diagnostics(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.objectives.with_raw_response.retrieve_diagnostics(
                objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `objective_id` but received ''"):
            client.objectives.with_raw_response.retrieve_diagnostics(
                objective_id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stream_events(self, client: Cadenya) -> None:
        objective_stream = client.objectives.stream_events(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        objective_stream.response.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_stream_events(self, client: Cadenya) -> None:
        response = client.objectives.with_raw_response.stream_events(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_stream_events(self, client: Cadenya) -> None:
        with client.objectives.with_streaming_response.stream_events(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_stream_events(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.objectives.with_raw_response.stream_events(
                objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `objective_id` but received ''"):
            client.objectives.with_raw_response.stream_events(
                objective_id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )


class TestAsyncObjectives:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCadenya) -> None:
        objective = await async_client.objectives.create(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            system_prompt_data={"foo": "bar"},
        )
        assert_matches_type(Objective, objective, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCadenya) -> None:
        objective = await async_client.objectives.create(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            system_prompt_data={"foo": "bar"},
            episodic_memory={"key": "key"},
            first_user_message="firstUserMessage",
            first_user_message_data={"foo": "bar"},
            memory_cascade=[
                {
                    "memory_layer_id": "memlyr_01HXKD2E5NQM3T9AYWCFFFBMJH",
                    "memory_entry_id": "mementry_01HXKD2E5NQM3T9AYWCF5E52Z0",
                }
            ],
            metadata={
                "external_id": "externalId",
                "labels": {"foo": "string"},
            },
            secrets=[
                {
                    "name": "name",
                    "value": "value",
                }
            ],
            variation_id="agentvar_01HXKD2E5NQM3T9AYWCF32BSPP",
        )
        assert_matches_type(Objective, objective, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCadenya) -> None:
        response = await async_client.objectives.with_raw_response.create(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            system_prompt_data={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        objective = await response.parse()
        assert_matches_type(Objective, objective, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCadenya) -> None:
        async with async_client.objectives.with_streaming_response.create(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            system_prompt_data={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            objective = await response.parse()
            assert_matches_type(Objective, objective, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.objectives.with_raw_response.create(
                workspace_id="",
                agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
                system_prompt_data={"foo": "bar"},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCadenya) -> None:
        objective = await async_client.objectives.retrieve(
            id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert_matches_type(Objective, objective, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCadenya) -> None:
        response = await async_client.objectives.with_raw_response.retrieve(
            id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        objective = await response.parse()
        assert_matches_type(Objective, objective, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCadenya) -> None:
        async with async_client.objectives.with_streaming_response.retrieve(
            id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            objective = await response.parse()
            assert_matches_type(Objective, objective, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.objectives.with_raw_response.retrieve(
                id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.objectives.with_raw_response.retrieve(
                id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCadenya) -> None:
        objective = await async_client.objectives.list(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert_matches_type(AsyncCursorPagination[Objective], objective, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCadenya) -> None:
        objective = await async_client.objectives.list(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            agent_schedule_id="agentScheduleId",
            cursor="cursor",
            include_info=True,
            labels="labels",
            limit=0,
            parent_objective_id="parentObjectiveId",
            profile_id="profile_01HXKD2E5NQM3T9AYWCFS0AP08",
            sort_order="sortOrder",
            state="STATE_UNSPECIFIED",
        )
        assert_matches_type(AsyncCursorPagination[Objective], objective, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCadenya) -> None:
        response = await async_client.objectives.with_raw_response.list(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        objective = await response.parse()
        assert_matches_type(AsyncCursorPagination[Objective], objective, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCadenya) -> None:
        async with async_client.objectives.with_streaming_response.list(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            objective = await response.parse()
            assert_matches_type(AsyncCursorPagination[Objective], objective, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.objectives.with_raw_response.list(
                workspace_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_cancel(self, async_client: AsyncCadenya) -> None:
        objective = await async_client.objectives.cancel(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert_matches_type(Objective, objective, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_cancel_with_all_params(self, async_client: AsyncCadenya) -> None:
        objective = await async_client.objectives.cancel(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            reason="reason",
        )
        assert_matches_type(Objective, objective, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncCadenya) -> None:
        response = await async_client.objectives.with_raw_response.cancel(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        objective = await response.parse()
        assert_matches_type(Objective, objective, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncCadenya) -> None:
        async with async_client.objectives.with_streaming_response.cancel(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            objective = await response.parse()
            assert_matches_type(Objective, objective, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.objectives.with_raw_response.cancel(
                objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `objective_id` but received ''"):
            await async_client.objectives.with_raw_response.cancel(
                objective_id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_compact(self, async_client: AsyncCadenya) -> None:
        objective = await async_client.objectives.compact(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert_matches_type(ObjectiveCompactResponse, objective, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_compact_with_all_params(self, async_client: AsyncCadenya) -> None:
        objective = await async_client.objectives.compact(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            compaction_config={
                "summarization": {"instructions": "instructions"},
                "tool_result_clearing": {"preserve_recent_results": 0},
                "trigger_threshold": 0,
            },
        )
        assert_matches_type(ObjectiveCompactResponse, objective, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_compact(self, async_client: AsyncCadenya) -> None:
        response = await async_client.objectives.with_raw_response.compact(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        objective = await response.parse()
        assert_matches_type(ObjectiveCompactResponse, objective, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_compact(self, async_client: AsyncCadenya) -> None:
        async with async_client.objectives.with_streaming_response.compact(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            objective = await response.parse()
            assert_matches_type(ObjectiveCompactResponse, objective, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_compact(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.objectives.with_raw_response.compact(
                objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `objective_id` but received ''"):
            await async_client.objectives.with_raw_response.compact(
                objective_id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_continue(self, async_client: AsyncCadenya) -> None:
        objective = await async_client.objectives.continue_(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            message="message",
        )
        assert_matches_type(ObjectiveEvent, objective, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_continue_with_all_params(self, async_client: AsyncCadenya) -> None:
        objective = await async_client.objectives.continue_(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            message="message",
            enqueue=True,
        )
        assert_matches_type(ObjectiveEvent, objective, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_continue(self, async_client: AsyncCadenya) -> None:
        response = await async_client.objectives.with_raw_response.continue_(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            message="message",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        objective = await response.parse()
        assert_matches_type(ObjectiveEvent, objective, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_continue(self, async_client: AsyncCadenya) -> None:
        async with async_client.objectives.with_streaming_response.continue_(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            message="message",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            objective = await response.parse()
            assert_matches_type(ObjectiveEvent, objective, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_continue(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.objectives.with_raw_response.continue_(
                objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
                workspace_id="",
                message="message",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `objective_id` but received ''"):
            await async_client.objectives.with_raw_response.continue_(
                objective_id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
                message="message",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_context_windows(self, async_client: AsyncCadenya) -> None:
        objective = await async_client.objectives.list_context_windows(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert_matches_type(AsyncCursorPagination[ObjectiveContextWindow], objective, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_context_windows_with_all_params(self, async_client: AsyncCadenya) -> None:
        objective = await async_client.objectives.list_context_windows(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            cursor="cursor",
            include_info=True,
            labels="labels",
            limit=0,
        )
        assert_matches_type(AsyncCursorPagination[ObjectiveContextWindow], objective, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_context_windows(self, async_client: AsyncCadenya) -> None:
        response = await async_client.objectives.with_raw_response.list_context_windows(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        objective = await response.parse()
        assert_matches_type(AsyncCursorPagination[ObjectiveContextWindow], objective, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_context_windows(self, async_client: AsyncCadenya) -> None:
        async with async_client.objectives.with_streaming_response.list_context_windows(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            objective = await response.parse()
            assert_matches_type(AsyncCursorPagination[ObjectiveContextWindow], objective, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_context_windows(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.objectives.with_raw_response.list_context_windows(
                objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `objective_id` but received ''"):
            await async_client.objectives.with_raw_response.list_context_windows(
                objective_id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_events(self, async_client: AsyncCadenya) -> None:
        objective = await async_client.objectives.list_events(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert_matches_type(AsyncCursorPagination[ObjectiveEvent], objective, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_events_with_all_params(self, async_client: AsyncCadenya) -> None:
        objective = await async_client.objectives.list_events(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            cursor="cursor",
            include_info=True,
            labels="labels",
            limit=0,
            since_event_id="sinceEventId",
            sort_order="sortOrder",
            window_id="windowId",
        )
        assert_matches_type(AsyncCursorPagination[ObjectiveEvent], objective, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_events(self, async_client: AsyncCadenya) -> None:
        response = await async_client.objectives.with_raw_response.list_events(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        objective = await response.parse()
        assert_matches_type(AsyncCursorPagination[ObjectiveEvent], objective, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_events(self, async_client: AsyncCadenya) -> None:
        async with async_client.objectives.with_streaming_response.list_events(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            objective = await response.parse()
            assert_matches_type(AsyncCursorPagination[ObjectiveEvent], objective, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_events(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.objectives.with_raw_response.list_events(
                objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `objective_id` but received ''"):
            await async_client.objectives.with_raw_response.list_events(
                objective_id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_diagnostics(self, async_client: AsyncCadenya) -> None:
        objective = await async_client.objectives.retrieve_diagnostics(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert_matches_type(ObjectiveRetrieveDiagnosticsResponse, objective, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_diagnostics(self, async_client: AsyncCadenya) -> None:
        response = await async_client.objectives.with_raw_response.retrieve_diagnostics(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        objective = await response.parse()
        assert_matches_type(ObjectiveRetrieveDiagnosticsResponse, objective, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_diagnostics(self, async_client: AsyncCadenya) -> None:
        async with async_client.objectives.with_streaming_response.retrieve_diagnostics(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            objective = await response.parse()
            assert_matches_type(ObjectiveRetrieveDiagnosticsResponse, objective, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_diagnostics(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.objectives.with_raw_response.retrieve_diagnostics(
                objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `objective_id` but received ''"):
            await async_client.objectives.with_raw_response.retrieve_diagnostics(
                objective_id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stream_events(self, async_client: AsyncCadenya) -> None:
        objective_stream = await async_client.objectives.stream_events(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        await objective_stream.response.aclose()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_stream_events(self, async_client: AsyncCadenya) -> None:
        response = await async_client.objectives.with_raw_response.stream_events(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_stream_events(self, async_client: AsyncCadenya) -> None:
        async with async_client.objectives.with_streaming_response.stream_events(
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_stream_events(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.objectives.with_raw_response.stream_events(
                objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `objective_id` but received ''"):
            await async_client.objectives.with_raw_response.stream_events(
                objective_id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )
