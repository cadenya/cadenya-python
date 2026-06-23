# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cadenya import Cadenya, AsyncCadenya
from tests.utils import assert_matches_type
from cadenya.pagination import SyncCursorPagination, AsyncCursorPagination
from cadenya.types.agents import (
    AgentSchedule,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSchedules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Cadenya) -> None:
        schedule = client.agents.schedules.create(
            agent_id="agentId",
            workspace_id="workspaceId",
            metadata={"name": "name"},
            spec={"schedule": {}},
        )
        assert_matches_type(AgentSchedule, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Cadenya) -> None:
        schedule = client.agents.schedules.create(
            agent_id="agentId",
            workspace_id="workspaceId",
            metadata={
                "name": "name",
                "external_id": "externalId",
                "labels": {"foo": "string"},
            },
            spec={
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
        )
        assert_matches_type(AgentSchedule, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Cadenya) -> None:
        response = client.agents.schedules.with_raw_response.create(
            agent_id="agentId",
            workspace_id="workspaceId",
            metadata={"name": "name"},
            spec={"schedule": {}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert_matches_type(AgentSchedule, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Cadenya) -> None:
        with client.agents.schedules.with_streaming_response.create(
            agent_id="agentId",
            workspace_id="workspaceId",
            metadata={"name": "name"},
            spec={"schedule": {}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = response.parse()
            assert_matches_type(AgentSchedule, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.agents.schedules.with_raw_response.create(
                agent_id="agentId",
                workspace_id="",
                metadata={"name": "name"},
                spec={"schedule": {}},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.schedules.with_raw_response.create(
                agent_id="",
                workspace_id="workspaceId",
                metadata={"name": "name"},
                spec={"schedule": {}},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Cadenya) -> None:
        schedule = client.agents.schedules.retrieve(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
        )
        assert_matches_type(AgentSchedule, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Cadenya) -> None:
        response = client.agents.schedules.with_raw_response.retrieve(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert_matches_type(AgentSchedule, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Cadenya) -> None:
        with client.agents.schedules.with_streaming_response.retrieve(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = response.parse()
            assert_matches_type(AgentSchedule, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.agents.schedules.with_raw_response.retrieve(
                id="id",
                workspace_id="",
                agent_id="agentId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.schedules.with_raw_response.retrieve(
                id="id",
                workspace_id="workspaceId",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.agents.schedules.with_raw_response.retrieve(
                id="",
                workspace_id="workspaceId",
                agent_id="agentId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Cadenya) -> None:
        schedule = client.agents.schedules.update(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
        )
        assert_matches_type(AgentSchedule, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Cadenya) -> None:
        schedule = client.agents.schedules.update(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
            metadata={
                "name": "name",
                "external_id": "externalId",
                "labels": {"foo": "string"},
            },
            spec={
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
            update_mask="updateMask",
        )
        assert_matches_type(AgentSchedule, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Cadenya) -> None:
        response = client.agents.schedules.with_raw_response.update(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert_matches_type(AgentSchedule, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Cadenya) -> None:
        with client.agents.schedules.with_streaming_response.update(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = response.parse()
            assert_matches_type(AgentSchedule, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.agents.schedules.with_raw_response.update(
                id="id",
                workspace_id="",
                agent_id="agentId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.schedules.with_raw_response.update(
                id="id",
                workspace_id="workspaceId",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.agents.schedules.with_raw_response.update(
                id="",
                workspace_id="workspaceId",
                agent_id="agentId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Cadenya) -> None:
        schedule = client.agents.schedules.list(
            agent_id="agentId",
            workspace_id="workspaceId",
        )
        assert_matches_type(SyncCursorPagination[AgentSchedule], schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Cadenya) -> None:
        schedule = client.agents.schedules.list(
            agent_id="agentId",
            workspace_id="workspaceId",
            cursor="cursor",
            include_info=True,
            limit=0,
            prefix="prefix",
            query="query",
            sort_order="sortOrder",
        )
        assert_matches_type(SyncCursorPagination[AgentSchedule], schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Cadenya) -> None:
        response = client.agents.schedules.with_raw_response.list(
            agent_id="agentId",
            workspace_id="workspaceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert_matches_type(SyncCursorPagination[AgentSchedule], schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Cadenya) -> None:
        with client.agents.schedules.with_streaming_response.list(
            agent_id="agentId",
            workspace_id="workspaceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = response.parse()
            assert_matches_type(SyncCursorPagination[AgentSchedule], schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.agents.schedules.with_raw_response.list(
                agent_id="agentId",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.schedules.with_raw_response.list(
                agent_id="",
                workspace_id="workspaceId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Cadenya) -> None:
        schedule = client.agents.schedules.delete(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
        )
        assert schedule is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Cadenya) -> None:
        response = client.agents.schedules.with_raw_response.delete(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert schedule is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Cadenya) -> None:
        with client.agents.schedules.with_streaming_response.delete(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = response.parse()
            assert schedule is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.agents.schedules.with_raw_response.delete(
                id="id",
                workspace_id="",
                agent_id="agentId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.schedules.with_raw_response.delete(
                id="id",
                workspace_id="workspaceId",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.agents.schedules.with_raw_response.delete(
                id="",
                workspace_id="workspaceId",
                agent_id="agentId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_archive(self, client: Cadenya) -> None:
        schedule = client.agents.schedules.archive(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
        )
        assert_matches_type(AgentSchedule, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_archive(self, client: Cadenya) -> None:
        response = client.agents.schedules.with_raw_response.archive(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert_matches_type(AgentSchedule, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_archive(self, client: Cadenya) -> None:
        with client.agents.schedules.with_streaming_response.archive(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = response.parse()
            assert_matches_type(AgentSchedule, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_archive(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.agents.schedules.with_raw_response.archive(
                id="id",
                workspace_id="",
                agent_id="agentId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.schedules.with_raw_response.archive(
                id="id",
                workspace_id="workspaceId",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.agents.schedules.with_raw_response.archive(
                id="",
                workspace_id="workspaceId",
                agent_id="agentId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_pause(self, client: Cadenya) -> None:
        schedule = client.agents.schedules.pause(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
        )
        assert_matches_type(AgentSchedule, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_pause(self, client: Cadenya) -> None:
        response = client.agents.schedules.with_raw_response.pause(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert_matches_type(AgentSchedule, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_pause(self, client: Cadenya) -> None:
        with client.agents.schedules.with_streaming_response.pause(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = response.parse()
            assert_matches_type(AgentSchedule, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_pause(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.agents.schedules.with_raw_response.pause(
                id="id",
                workspace_id="",
                agent_id="agentId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.schedules.with_raw_response.pause(
                id="id",
                workspace_id="workspaceId",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.agents.schedules.with_raw_response.pause(
                id="",
                workspace_id="workspaceId",
                agent_id="agentId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_resume(self, client: Cadenya) -> None:
        schedule = client.agents.schedules.resume(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
        )
        assert_matches_type(AgentSchedule, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_resume(self, client: Cadenya) -> None:
        response = client.agents.schedules.with_raw_response.resume(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert_matches_type(AgentSchedule, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_resume(self, client: Cadenya) -> None:
        with client.agents.schedules.with_streaming_response.resume(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = response.parse()
            assert_matches_type(AgentSchedule, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_resume(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.agents.schedules.with_raw_response.resume(
                id="id",
                workspace_id="",
                agent_id="agentId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.schedules.with_raw_response.resume(
                id="id",
                workspace_id="workspaceId",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.agents.schedules.with_raw_response.resume(
                id="",
                workspace_id="workspaceId",
                agent_id="agentId",
            )


class TestAsyncSchedules:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCadenya) -> None:
        schedule = await async_client.agents.schedules.create(
            agent_id="agentId",
            workspace_id="workspaceId",
            metadata={"name": "name"},
            spec={"schedule": {}},
        )
        assert_matches_type(AgentSchedule, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCadenya) -> None:
        schedule = await async_client.agents.schedules.create(
            agent_id="agentId",
            workspace_id="workspaceId",
            metadata={
                "name": "name",
                "external_id": "externalId",
                "labels": {"foo": "string"},
            },
            spec={
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
        )
        assert_matches_type(AgentSchedule, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCadenya) -> None:
        response = await async_client.agents.schedules.with_raw_response.create(
            agent_id="agentId",
            workspace_id="workspaceId",
            metadata={"name": "name"},
            spec={"schedule": {}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert_matches_type(AgentSchedule, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCadenya) -> None:
        async with async_client.agents.schedules.with_streaming_response.create(
            agent_id="agentId",
            workspace_id="workspaceId",
            metadata={"name": "name"},
            spec={"schedule": {}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = await response.parse()
            assert_matches_type(AgentSchedule, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.agents.schedules.with_raw_response.create(
                agent_id="agentId",
                workspace_id="",
                metadata={"name": "name"},
                spec={"schedule": {}},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.schedules.with_raw_response.create(
                agent_id="",
                workspace_id="workspaceId",
                metadata={"name": "name"},
                spec={"schedule": {}},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCadenya) -> None:
        schedule = await async_client.agents.schedules.retrieve(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
        )
        assert_matches_type(AgentSchedule, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCadenya) -> None:
        response = await async_client.agents.schedules.with_raw_response.retrieve(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert_matches_type(AgentSchedule, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCadenya) -> None:
        async with async_client.agents.schedules.with_streaming_response.retrieve(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = await response.parse()
            assert_matches_type(AgentSchedule, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.agents.schedules.with_raw_response.retrieve(
                id="id",
                workspace_id="",
                agent_id="agentId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.schedules.with_raw_response.retrieve(
                id="id",
                workspace_id="workspaceId",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.agents.schedules.with_raw_response.retrieve(
                id="",
                workspace_id="workspaceId",
                agent_id="agentId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncCadenya) -> None:
        schedule = await async_client.agents.schedules.update(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
        )
        assert_matches_type(AgentSchedule, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCadenya) -> None:
        schedule = await async_client.agents.schedules.update(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
            metadata={
                "name": "name",
                "external_id": "externalId",
                "labels": {"foo": "string"},
            },
            spec={
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
            update_mask="updateMask",
        )
        assert_matches_type(AgentSchedule, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCadenya) -> None:
        response = await async_client.agents.schedules.with_raw_response.update(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert_matches_type(AgentSchedule, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCadenya) -> None:
        async with async_client.agents.schedules.with_streaming_response.update(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = await response.parse()
            assert_matches_type(AgentSchedule, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.agents.schedules.with_raw_response.update(
                id="id",
                workspace_id="",
                agent_id="agentId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.schedules.with_raw_response.update(
                id="id",
                workspace_id="workspaceId",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.agents.schedules.with_raw_response.update(
                id="",
                workspace_id="workspaceId",
                agent_id="agentId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCadenya) -> None:
        schedule = await async_client.agents.schedules.list(
            agent_id="agentId",
            workspace_id="workspaceId",
        )
        assert_matches_type(AsyncCursorPagination[AgentSchedule], schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCadenya) -> None:
        schedule = await async_client.agents.schedules.list(
            agent_id="agentId",
            workspace_id="workspaceId",
            cursor="cursor",
            include_info=True,
            limit=0,
            prefix="prefix",
            query="query",
            sort_order="sortOrder",
        )
        assert_matches_type(AsyncCursorPagination[AgentSchedule], schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCadenya) -> None:
        response = await async_client.agents.schedules.with_raw_response.list(
            agent_id="agentId",
            workspace_id="workspaceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert_matches_type(AsyncCursorPagination[AgentSchedule], schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCadenya) -> None:
        async with async_client.agents.schedules.with_streaming_response.list(
            agent_id="agentId",
            workspace_id="workspaceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = await response.parse()
            assert_matches_type(AsyncCursorPagination[AgentSchedule], schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.agents.schedules.with_raw_response.list(
                agent_id="agentId",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.schedules.with_raw_response.list(
                agent_id="",
                workspace_id="workspaceId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCadenya) -> None:
        schedule = await async_client.agents.schedules.delete(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
        )
        assert schedule is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCadenya) -> None:
        response = await async_client.agents.schedules.with_raw_response.delete(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert schedule is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCadenya) -> None:
        async with async_client.agents.schedules.with_streaming_response.delete(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = await response.parse()
            assert schedule is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.agents.schedules.with_raw_response.delete(
                id="id",
                workspace_id="",
                agent_id="agentId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.schedules.with_raw_response.delete(
                id="id",
                workspace_id="workspaceId",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.agents.schedules.with_raw_response.delete(
                id="",
                workspace_id="workspaceId",
                agent_id="agentId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_archive(self, async_client: AsyncCadenya) -> None:
        schedule = await async_client.agents.schedules.archive(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
        )
        assert_matches_type(AgentSchedule, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncCadenya) -> None:
        response = await async_client.agents.schedules.with_raw_response.archive(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert_matches_type(AgentSchedule, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncCadenya) -> None:
        async with async_client.agents.schedules.with_streaming_response.archive(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = await response.parse()
            assert_matches_type(AgentSchedule, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_archive(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.agents.schedules.with_raw_response.archive(
                id="id",
                workspace_id="",
                agent_id="agentId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.schedules.with_raw_response.archive(
                id="id",
                workspace_id="workspaceId",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.agents.schedules.with_raw_response.archive(
                id="",
                workspace_id="workspaceId",
                agent_id="agentId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_pause(self, async_client: AsyncCadenya) -> None:
        schedule = await async_client.agents.schedules.pause(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
        )
        assert_matches_type(AgentSchedule, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_pause(self, async_client: AsyncCadenya) -> None:
        response = await async_client.agents.schedules.with_raw_response.pause(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert_matches_type(AgentSchedule, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_pause(self, async_client: AsyncCadenya) -> None:
        async with async_client.agents.schedules.with_streaming_response.pause(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = await response.parse()
            assert_matches_type(AgentSchedule, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_pause(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.agents.schedules.with_raw_response.pause(
                id="id",
                workspace_id="",
                agent_id="agentId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.schedules.with_raw_response.pause(
                id="id",
                workspace_id="workspaceId",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.agents.schedules.with_raw_response.pause(
                id="",
                workspace_id="workspaceId",
                agent_id="agentId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_resume(self, async_client: AsyncCadenya) -> None:
        schedule = await async_client.agents.schedules.resume(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
        )
        assert_matches_type(AgentSchedule, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_resume(self, async_client: AsyncCadenya) -> None:
        response = await async_client.agents.schedules.with_raw_response.resume(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert_matches_type(AgentSchedule, schedule, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_resume(self, async_client: AsyncCadenya) -> None:
        async with async_client.agents.schedules.with_streaming_response.resume(
            id="id",
            workspace_id="workspaceId",
            agent_id="agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = await response.parse()
            assert_matches_type(AgentSchedule, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_resume(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.agents.schedules.with_raw_response.resume(
                id="id",
                workspace_id="",
                agent_id="agentId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.schedules.with_raw_response.resume(
                id="id",
                workspace_id="workspaceId",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.agents.schedules.with_raw_response.resume(
                id="",
                workspace_id="workspaceId",
                agent_id="agentId",
            )
