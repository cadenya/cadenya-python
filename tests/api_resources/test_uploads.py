# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cadenya import Cadenya, AsyncCadenya
from tests.utils import assert_matches_type
from cadenya.types import Upload

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUploads:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Cadenya) -> None:
        upload = client.uploads.create(
            workspace_id="workspaceId",
            metadata={"name": "name"},
            spec={
                "content_type": "contentType",
                "filename": "filename",
                "size_bytes": "sizeBytes",
            },
        )
        assert_matches_type(Upload, upload, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Cadenya) -> None:
        upload = client.uploads.create(
            workspace_id="workspaceId",
            metadata={
                "name": "name",
                "bundle_key": "bundleKey",
                "external_id": "externalId",
                "labels": {"foo": "string"},
            },
            spec={
                "content_type": "contentType",
                "filename": "filename",
                "size_bytes": "sizeBytes",
            },
        )
        assert_matches_type(Upload, upload, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Cadenya) -> None:
        response = client.uploads.with_raw_response.create(
            workspace_id="workspaceId",
            metadata={"name": "name"},
            spec={
                "content_type": "contentType",
                "filename": "filename",
                "size_bytes": "sizeBytes",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = response.parse()
        assert_matches_type(Upload, upload, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Cadenya) -> None:
        with client.uploads.with_streaming_response.create(
            workspace_id="workspaceId",
            metadata={"name": "name"},
            spec={
                "content_type": "contentType",
                "filename": "filename",
                "size_bytes": "sizeBytes",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = response.parse()
            assert_matches_type(Upload, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.uploads.with_raw_response.create(
                workspace_id="",
                metadata={"name": "name"},
                spec={
                    "content_type": "contentType",
                    "filename": "filename",
                    "size_bytes": "sizeBytes",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Cadenya) -> None:
        upload = client.uploads.retrieve(
            id="id",
            workspace_id="workspaceId",
        )
        assert_matches_type(Upload, upload, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Cadenya) -> None:
        response = client.uploads.with_raw_response.retrieve(
            id="id",
            workspace_id="workspaceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = response.parse()
        assert_matches_type(Upload, upload, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Cadenya) -> None:
        with client.uploads.with_streaming_response.retrieve(
            id="id",
            workspace_id="workspaceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = response.parse()
            assert_matches_type(Upload, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Cadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.uploads.with_raw_response.retrieve(
                id="id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.uploads.with_raw_response.retrieve(
                id="",
                workspace_id="workspaceId",
            )


class TestAsyncUploads:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCadenya) -> None:
        upload = await async_client.uploads.create(
            workspace_id="workspaceId",
            metadata={"name": "name"},
            spec={
                "content_type": "contentType",
                "filename": "filename",
                "size_bytes": "sizeBytes",
            },
        )
        assert_matches_type(Upload, upload, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCadenya) -> None:
        upload = await async_client.uploads.create(
            workspace_id="workspaceId",
            metadata={
                "name": "name",
                "bundle_key": "bundleKey",
                "external_id": "externalId",
                "labels": {"foo": "string"},
            },
            spec={
                "content_type": "contentType",
                "filename": "filename",
                "size_bytes": "sizeBytes",
            },
        )
        assert_matches_type(Upload, upload, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCadenya) -> None:
        response = await async_client.uploads.with_raw_response.create(
            workspace_id="workspaceId",
            metadata={"name": "name"},
            spec={
                "content_type": "contentType",
                "filename": "filename",
                "size_bytes": "sizeBytes",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = await response.parse()
        assert_matches_type(Upload, upload, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCadenya) -> None:
        async with async_client.uploads.with_streaming_response.create(
            workspace_id="workspaceId",
            metadata={"name": "name"},
            spec={
                "content_type": "contentType",
                "filename": "filename",
                "size_bytes": "sizeBytes",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = await response.parse()
            assert_matches_type(Upload, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.uploads.with_raw_response.create(
                workspace_id="",
                metadata={"name": "name"},
                spec={
                    "content_type": "contentType",
                    "filename": "filename",
                    "size_bytes": "sizeBytes",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCadenya) -> None:
        upload = await async_client.uploads.retrieve(
            id="id",
            workspace_id="workspaceId",
        )
        assert_matches_type(Upload, upload, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCadenya) -> None:
        response = await async_client.uploads.with_raw_response.retrieve(
            id="id",
            workspace_id="workspaceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = await response.parse()
        assert_matches_type(Upload, upload, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCadenya) -> None:
        async with async_client.uploads.with_streaming_response.retrieve(
            id="id",
            workspace_id="workspaceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = await response.parse()
            assert_matches_type(Upload, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCadenya) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.uploads.with_raw_response.retrieve(
                id="id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.uploads.with_raw_response.retrieve(
                id="",
                workspace_id="workspaceId",
            )
