# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cadenya import Cadenya, AsyncCadenya
from tests.utils import assert_matches_type
from cadenya.pagination import SyncCursorPagination, AsyncCursorPagination
from cadenya.types.agents import WebhookDelivery

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhookDeliveries:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Cadenya) -> None:
        webhook_delivery = client.agents.webhook_deliveries.list(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert_matches_type(SyncCursorPagination[WebhookDelivery], webhook_delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Cadenya) -> None:
        webhook_delivery = client.agents.webhook_deliveries.list(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            cursor="cursor",
            event_type="OBJECTIVE_EVENT_TYPE_UNSPECIFIED",
            labels="labels",
            limit=0,
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
        )
        assert_matches_type(SyncCursorPagination[WebhookDelivery], webhook_delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Cadenya) -> None:
        response = client.agents.webhook_deliveries.with_raw_response.list(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_delivery = response.parse()
        assert_matches_type(SyncCursorPagination[WebhookDelivery], webhook_delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Cadenya) -> None:
        with client.agents.webhook_deliveries.with_streaming_response.list(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_delivery = response.parse()
            assert_matches_type(SyncCursorPagination[WebhookDelivery], webhook_delivery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.agents.webhook_deliveries.with_raw_response.list(
                agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.webhook_deliveries.with_raw_response.list(
                agent_id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )


class TestAsyncWebhookDeliveries:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCadenya) -> None:
        webhook_delivery = await async_client.agents.webhook_deliveries.list(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert_matches_type(AsyncCursorPagination[WebhookDelivery], webhook_delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCadenya) -> None:
        webhook_delivery = await async_client.agents.webhook_deliveries.list(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            cursor="cursor",
            event_type="OBJECTIVE_EVENT_TYPE_UNSPECIFIED",
            labels="labels",
            limit=0,
            objective_id="obj_01HXKD2E5NQM3T9AYWCFQAZGFV",
        )
        assert_matches_type(AsyncCursorPagination[WebhookDelivery], webhook_delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCadenya) -> None:
        response = await async_client.agents.webhook_deliveries.with_raw_response.list(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_delivery = await response.parse()
        assert_matches_type(AsyncCursorPagination[WebhookDelivery], webhook_delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCadenya) -> None:
        async with async_client.agents.webhook_deliveries.with_streaming_response.list(
            agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_delivery = await response.parse()
            assert_matches_type(AsyncCursorPagination[WebhookDelivery], webhook_delivery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.agents.webhook_deliveries.with_raw_response.list(
                agent_id="agent_01HXKD2E5NQM3T9AYWCFMGWT9Y",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.webhook_deliveries.with_raw_response.list(
                agent_id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )
