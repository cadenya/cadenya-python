# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cadenya import Cadenya, AsyncCadenya
from tests.utils import assert_matches_type
from cadenya.types import (
    WidgetSession,
    WidgetSessionDeleteTenantResponse,
)
from cadenya._utils import parse_datetime
from cadenya.pagination import SyncCursorPagination, AsyncCursorPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWidgetSessions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Cadenya) -> None:
        widget_session = client.widget_sessions.create(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            spec={"widget_id": "wgt_01HXKD2E5NQM3T9AYWCFMZZZBD"},
        )
        assert_matches_type(WidgetSession, widget_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Cadenya) -> None:
        widget_session = client.widget_sessions.create(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            spec={
                "widget_id": "wgt_01HXKD2E5NQM3T9AYWCFMZZZBD",
                "expires_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "pinned_parameters": {"foo": "string"},
                "subject": {
                    "id": "customer-user-42",
                    "name": "Jane Doe",
                },
                "tenant": {
                    "id": "acme-corp",
                    "name": "Acme Corp",
                },
            },
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
        )
        assert_matches_type(WidgetSession, widget_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Cadenya) -> None:
        response = client.widget_sessions.with_raw_response.create(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            spec={"widget_id": "wgt_01HXKD2E5NQM3T9AYWCFMZZZBD"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        widget_session = response.parse()
        assert_matches_type(WidgetSession, widget_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Cadenya) -> None:
        with client.widget_sessions.with_streaming_response.create(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            spec={"widget_id": "wgt_01HXKD2E5NQM3T9AYWCFMZZZBD"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            widget_session = response.parse()
            assert_matches_type(WidgetSession, widget_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.widget_sessions.with_raw_response.create(
                workspace_id="",
                spec={"widget_id": "wgt_01HXKD2E5NQM3T9AYWCFMZZZBD"},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Cadenya) -> None:
        widget_session = client.widget_sessions.retrieve(
            id="id",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert_matches_type(WidgetSession, widget_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Cadenya) -> None:
        response = client.widget_sessions.with_raw_response.retrieve(
            id="id",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        widget_session = response.parse()
        assert_matches_type(WidgetSession, widget_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Cadenya) -> None:
        with client.widget_sessions.with_streaming_response.retrieve(
            id="id",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            widget_session = response.parse()
            assert_matches_type(WidgetSession, widget_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.widget_sessions.with_raw_response.retrieve(
                id="id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.widget_sessions.with_raw_response.retrieve(
                id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Cadenya) -> None:
        widget_session = client.widget_sessions.list(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert_matches_type(SyncCursorPagination[WidgetSession], widget_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Cadenya) -> None:
        widget_session = client.widget_sessions.list(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            cursor="cursor",
            include_info=True,
            labels="labels",
            limit=0,
            sort_order="sortOrder",
            state="STATE_UNSPECIFIED",
            subject_id="subjectId",
            tenant_id="tenantId",
            widget_id="widgetId",
        )
        assert_matches_type(SyncCursorPagination[WidgetSession], widget_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Cadenya) -> None:
        response = client.widget_sessions.with_raw_response.list(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        widget_session = response.parse()
        assert_matches_type(SyncCursorPagination[WidgetSession], widget_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Cadenya) -> None:
        with client.widget_sessions.with_streaming_response.list(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            widget_session = response.parse()
            assert_matches_type(SyncCursorPagination[WidgetSession], widget_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.widget_sessions.with_raw_response.list(
                workspace_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Cadenya) -> None:
        widget_session = client.widget_sessions.delete(
            id="id",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert widget_session is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Cadenya) -> None:
        response = client.widget_sessions.with_raw_response.delete(
            id="id",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        widget_session = response.parse()
        assert widget_session is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Cadenya) -> None:
        with client.widget_sessions.with_streaming_response.delete(
            id="id",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            widget_session = response.parse()
            assert widget_session is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.widget_sessions.with_raw_response.delete(
                id="id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.widget_sessions.with_raw_response.delete(
                id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_tenant(self, client: Cadenya) -> None:
        widget_session = client.widget_sessions.delete_tenant(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert_matches_type(WidgetSessionDeleteTenantResponse, widget_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_tenant_with_all_params(self, client: Cadenya) -> None:
        widget_session = client.widget_sessions.delete_tenant(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            tenant_id="tenantId",
        )
        assert_matches_type(WidgetSessionDeleteTenantResponse, widget_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_tenant(self, client: Cadenya) -> None:
        response = client.widget_sessions.with_raw_response.delete_tenant(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        widget_session = response.parse()
        assert_matches_type(WidgetSessionDeleteTenantResponse, widget_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_tenant(self, client: Cadenya) -> None:
        with client.widget_sessions.with_streaming_response.delete_tenant(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            widget_session = response.parse()
            assert_matches_type(WidgetSessionDeleteTenantResponse, widget_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete_tenant(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.widget_sessions.with_raw_response.delete_tenant(
                workspace_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_revoke(self, client: Cadenya) -> None:
        widget_session = client.widget_sessions.revoke(
            id="id",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert_matches_type(WidgetSession, widget_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_revoke(self, client: Cadenya) -> None:
        response = client.widget_sessions.with_raw_response.revoke(
            id="id",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        widget_session = response.parse()
        assert_matches_type(WidgetSession, widget_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_revoke(self, client: Cadenya) -> None:
        with client.widget_sessions.with_streaming_response.revoke(
            id="id",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            widget_session = response.parse()
            assert_matches_type(WidgetSession, widget_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_revoke(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.widget_sessions.with_raw_response.revoke(
                id="id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.widget_sessions.with_raw_response.revoke(
                id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )


class TestAsyncWidgetSessions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCadenya) -> None:
        widget_session = await async_client.widget_sessions.create(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            spec={"widget_id": "wgt_01HXKD2E5NQM3T9AYWCFMZZZBD"},
        )
        assert_matches_type(WidgetSession, widget_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCadenya) -> None:
        widget_session = await async_client.widget_sessions.create(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            spec={
                "widget_id": "wgt_01HXKD2E5NQM3T9AYWCFMZZZBD",
                "expires_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "pinned_parameters": {"foo": "string"},
                "subject": {
                    "id": "customer-user-42",
                    "name": "Jane Doe",
                },
                "tenant": {
                    "id": "acme-corp",
                    "name": "Acme Corp",
                },
            },
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
        )
        assert_matches_type(WidgetSession, widget_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCadenya) -> None:
        response = await async_client.widget_sessions.with_raw_response.create(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            spec={"widget_id": "wgt_01HXKD2E5NQM3T9AYWCFMZZZBD"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        widget_session = await response.parse()
        assert_matches_type(WidgetSession, widget_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCadenya) -> None:
        async with async_client.widget_sessions.with_streaming_response.create(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            spec={"widget_id": "wgt_01HXKD2E5NQM3T9AYWCFMZZZBD"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            widget_session = await response.parse()
            assert_matches_type(WidgetSession, widget_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.widget_sessions.with_raw_response.create(
                workspace_id="",
                spec={"widget_id": "wgt_01HXKD2E5NQM3T9AYWCFMZZZBD"},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCadenya) -> None:
        widget_session = await async_client.widget_sessions.retrieve(
            id="id",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert_matches_type(WidgetSession, widget_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCadenya) -> None:
        response = await async_client.widget_sessions.with_raw_response.retrieve(
            id="id",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        widget_session = await response.parse()
        assert_matches_type(WidgetSession, widget_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCadenya) -> None:
        async with async_client.widget_sessions.with_streaming_response.retrieve(
            id="id",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            widget_session = await response.parse()
            assert_matches_type(WidgetSession, widget_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.widget_sessions.with_raw_response.retrieve(
                id="id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.widget_sessions.with_raw_response.retrieve(
                id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCadenya) -> None:
        widget_session = await async_client.widget_sessions.list(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert_matches_type(AsyncCursorPagination[WidgetSession], widget_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCadenya) -> None:
        widget_session = await async_client.widget_sessions.list(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            cursor="cursor",
            include_info=True,
            labels="labels",
            limit=0,
            sort_order="sortOrder",
            state="STATE_UNSPECIFIED",
            subject_id="subjectId",
            tenant_id="tenantId",
            widget_id="widgetId",
        )
        assert_matches_type(AsyncCursorPagination[WidgetSession], widget_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCadenya) -> None:
        response = await async_client.widget_sessions.with_raw_response.list(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        widget_session = await response.parse()
        assert_matches_type(AsyncCursorPagination[WidgetSession], widget_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCadenya) -> None:
        async with async_client.widget_sessions.with_streaming_response.list(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            widget_session = await response.parse()
            assert_matches_type(AsyncCursorPagination[WidgetSession], widget_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.widget_sessions.with_raw_response.list(
                workspace_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCadenya) -> None:
        widget_session = await async_client.widget_sessions.delete(
            id="id",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert widget_session is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCadenya) -> None:
        response = await async_client.widget_sessions.with_raw_response.delete(
            id="id",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        widget_session = await response.parse()
        assert widget_session is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCadenya) -> None:
        async with async_client.widget_sessions.with_streaming_response.delete(
            id="id",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            widget_session = await response.parse()
            assert widget_session is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.widget_sessions.with_raw_response.delete(
                id="id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.widget_sessions.with_raw_response.delete(
                id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_tenant(self, async_client: AsyncCadenya) -> None:
        widget_session = await async_client.widget_sessions.delete_tenant(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert_matches_type(WidgetSessionDeleteTenantResponse, widget_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_tenant_with_all_params(self, async_client: AsyncCadenya) -> None:
        widget_session = await async_client.widget_sessions.delete_tenant(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            tenant_id="tenantId",
        )
        assert_matches_type(WidgetSessionDeleteTenantResponse, widget_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_tenant(self, async_client: AsyncCadenya) -> None:
        response = await async_client.widget_sessions.with_raw_response.delete_tenant(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        widget_session = await response.parse()
        assert_matches_type(WidgetSessionDeleteTenantResponse, widget_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_tenant(self, async_client: AsyncCadenya) -> None:
        async with async_client.widget_sessions.with_streaming_response.delete_tenant(
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            widget_session = await response.parse()
            assert_matches_type(WidgetSessionDeleteTenantResponse, widget_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete_tenant(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.widget_sessions.with_raw_response.delete_tenant(
                workspace_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_revoke(self, async_client: AsyncCadenya) -> None:
        widget_session = await async_client.widget_sessions.revoke(
            id="id",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )
        assert_matches_type(WidgetSession, widget_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_revoke(self, async_client: AsyncCadenya) -> None:
        response = await async_client.widget_sessions.with_raw_response.revoke(
            id="id",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        widget_session = await response.parse()
        assert_matches_type(WidgetSession, widget_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_revoke(self, async_client: AsyncCadenya) -> None:
        async with async_client.widget_sessions.with_streaming_response.revoke(
            id="id",
            workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            widget_session = await response.parse()
            assert_matches_type(WidgetSession, widget_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_revoke(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.widget_sessions.with_raw_response.revoke(
                id="id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.widget_sessions.with_raw_response.revoke(
                id="",
                workspace_id="workspace_01HXKD2E5NQM3T9AYWCF133E3Q",
            )
