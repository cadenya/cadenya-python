# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from datetime import datetime, timezone

import pytest
import standardwebhooks

from cadenya import Cadenya

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhooks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.parametrize(
        "client_opt,method_opt",
        [
            ("whsec_c2VjcmV0Cg==", None),
            ("wrong", b"secret\n"),
            ("wrong", "whsec_c2VjcmV0Cg=="),
            (None, b"secret\n"),
            (None, "whsec_c2VjcmV0Cg=="),
        ],
    )
    def test_method_unwrap(self, client: Cadenya, client_opt: str | None, method_opt: str | bytes | None) -> None:
        hook = standardwebhooks.Webhook(b"secret\n")

        client = client.with_options(webhook_key=client_opt)

        data = """{"data":{"agent":{"id":"id","accountId":"account_01HXKD2E5NQM3T9AYWCFTJHJVF","createdAt":"2019-12-27T18:11:19.117Z","name":"name","profileId":"profile_01HXKD2E5NQM3T9AYWCFS0AP08","workspaceId":"workspace_01HXKD2E5NQM3T9AYWCF133E3Q","externalId":"externalId","labels":{"foo":"string"},"updatedAt":"2019-12-27T18:11:19.117Z"},"agentVariation":{"id":"id","accountId":"account_01HXKD2E5NQM3T9AYWCFTJHJVF","createdAt":"2019-12-27T18:11:19.117Z","name":"name","profileId":"profile_01HXKD2E5NQM3T9AYWCFS0AP08","workspaceId":"workspace_01HXKD2E5NQM3T9AYWCF133E3Q","externalId":"externalId","labels":{"foo":"string"},"updatedAt":"2019-12-27T18:11:19.117Z"},"objective":{"id":"id","accountId":"account_01HXKD2E5NQM3T9AYWCFTJHJVF","createdAt":"2019-12-27T18:11:19.117Z","profileId":"profile_01HXKD2E5NQM3T9AYWCFS0AP08","workspaceId":"workspace_01HXKD2E5NQM3T9AYWCF133E3Q","externalId":"externalId","labels":{"foo":"string"}},"objectiveEvent":{"data":{"type":"userMessage","userMessage":{"content":"content"}},"metadata":{"id":"id","accountId":"account_01HXKD2E5NQM3T9AYWCFTJHJVF","createdAt":"2019-12-27T18:11:19.117Z","profileId":"profile_01HXKD2E5NQM3T9AYWCFS0AP08","workspaceId":"workspace_01HXKD2E5NQM3T9AYWCF133E3Q","externalId":"externalId","labels":{"foo":"string"}},"contextWindowId":"objwin_01HXKD2E5NQM3T9AYWCFN7BSTR","duration":"-160513s","info":{"createdBy":{"metadata":{"id":"id","accountId":"account_01HXKD2E5NQM3T9AYWCFTJHJVF","name":"name","profileId":"profile_01HXKD2E5NQM3T9AYWCFS0AP08","createdAt":"2019-12-27T18:11:19.117Z","externalId":"externalId","labels":{"foo":"string"}},"spec":{"type":"PROFILE_TYPE_UNSPECIFIED","email":"email","name":"name"}},"objective":{"id":"id","accountId":"account_01HXKD2E5NQM3T9AYWCFTJHJVF","createdAt":"2019-12-27T18:11:19.117Z","profileId":"profile_01HXKD2E5NQM3T9AYWCFS0AP08","workspaceId":"workspace_01HXKD2E5NQM3T9AYWCF133E3Q","externalId":"externalId","labels":{"foo":"string"}}}}},"timestamp":"2019-12-27T18:11:19.117Z","type":"type"}"""
        msg_id = "1"
        timestamp = datetime.now(tz=timezone.utc)
        sig = hook.sign(msg_id=msg_id, timestamp=timestamp, data=data)
        headers = {
            "webhook-id": msg_id,
            "webhook-timestamp": str(int(timestamp.timestamp())),
            "webhook-signature": sig,
        }

        try:
            _ = client.webhooks.unwrap(data, headers=headers, key=method_opt)
        except standardwebhooks.WebhookVerificationError as e:
            raise AssertionError("Failed to unwrap valid webhook") from e

        bad_headers = [
            {**headers, "webhook-signature": hook.sign(msg_id=msg_id, timestamp=timestamp, data="xxx")},
            {**headers, "webhook-id": "bad"},
            {**headers, "webhook-timestamp": "0"},
        ]
        for bad_header in bad_headers:
            with pytest.raises(standardwebhooks.WebhookVerificationError):
                _ = client.webhooks.unwrap(data, headers=bad_header, key=method_opt)


class TestAsyncWebhooks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.parametrize(
        "client_opt,method_opt",
        [
            ("whsec_c2VjcmV0Cg==", None),
            ("wrong", b"secret\n"),
            ("wrong", "whsec_c2VjcmV0Cg=="),
            (None, b"secret\n"),
            (None, "whsec_c2VjcmV0Cg=="),
        ],
    )
    def test_method_unwrap(self, async_client: Cadenya, client_opt: str | None, method_opt: str | bytes | None) -> None:
        hook = standardwebhooks.Webhook(b"secret\n")

        async_client = async_client.with_options(webhook_key=client_opt)

        data = """{"data":{"agent":{"id":"id","accountId":"account_01HXKD2E5NQM3T9AYWCFTJHJVF","createdAt":"2019-12-27T18:11:19.117Z","name":"name","profileId":"profile_01HXKD2E5NQM3T9AYWCFS0AP08","workspaceId":"workspace_01HXKD2E5NQM3T9AYWCF133E3Q","externalId":"externalId","labels":{"foo":"string"},"updatedAt":"2019-12-27T18:11:19.117Z"},"agentVariation":{"id":"id","accountId":"account_01HXKD2E5NQM3T9AYWCFTJHJVF","createdAt":"2019-12-27T18:11:19.117Z","name":"name","profileId":"profile_01HXKD2E5NQM3T9AYWCFS0AP08","workspaceId":"workspace_01HXKD2E5NQM3T9AYWCF133E3Q","externalId":"externalId","labels":{"foo":"string"},"updatedAt":"2019-12-27T18:11:19.117Z"},"objective":{"id":"id","accountId":"account_01HXKD2E5NQM3T9AYWCFTJHJVF","createdAt":"2019-12-27T18:11:19.117Z","profileId":"profile_01HXKD2E5NQM3T9AYWCFS0AP08","workspaceId":"workspace_01HXKD2E5NQM3T9AYWCF133E3Q","externalId":"externalId","labels":{"foo":"string"}},"objectiveEvent":{"data":{"type":"userMessage","userMessage":{"content":"content"}},"metadata":{"id":"id","accountId":"account_01HXKD2E5NQM3T9AYWCFTJHJVF","createdAt":"2019-12-27T18:11:19.117Z","profileId":"profile_01HXKD2E5NQM3T9AYWCFS0AP08","workspaceId":"workspace_01HXKD2E5NQM3T9AYWCF133E3Q","externalId":"externalId","labels":{"foo":"string"}},"contextWindowId":"objwin_01HXKD2E5NQM3T9AYWCFN7BSTR","duration":"-160513s","info":{"createdBy":{"metadata":{"id":"id","accountId":"account_01HXKD2E5NQM3T9AYWCFTJHJVF","name":"name","profileId":"profile_01HXKD2E5NQM3T9AYWCFS0AP08","createdAt":"2019-12-27T18:11:19.117Z","externalId":"externalId","labels":{"foo":"string"}},"spec":{"type":"PROFILE_TYPE_UNSPECIFIED","email":"email","name":"name"}},"objective":{"id":"id","accountId":"account_01HXKD2E5NQM3T9AYWCFTJHJVF","createdAt":"2019-12-27T18:11:19.117Z","profileId":"profile_01HXKD2E5NQM3T9AYWCFS0AP08","workspaceId":"workspace_01HXKD2E5NQM3T9AYWCF133E3Q","externalId":"externalId","labels":{"foo":"string"}}}}},"timestamp":"2019-12-27T18:11:19.117Z","type":"type"}"""
        msg_id = "1"
        timestamp = datetime.now(tz=timezone.utc)
        sig = hook.sign(msg_id=msg_id, timestamp=timestamp, data=data)
        headers = {
            "webhook-id": msg_id,
            "webhook-timestamp": str(int(timestamp.timestamp())),
            "webhook-signature": sig,
        }

        try:
            _ = async_client.webhooks.unwrap(data, headers=headers, key=method_opt)
        except standardwebhooks.WebhookVerificationError as e:
            raise AssertionError("Failed to unwrap valid webhook") from e

        bad_headers = [
            {**headers, "webhook-signature": hook.sign(msg_id=msg_id, timestamp=timestamp, data="xxx")},
            {**headers, "webhook-id": "bad"},
            {**headers, "webhook-timestamp": "0"},
        ]
        for bad_header in bad_headers:
            with pytest.raises(standardwebhooks.WebhookVerificationError):
                _ = async_client.webhooks.unwrap(data, headers=bad_header, key=method_opt)
