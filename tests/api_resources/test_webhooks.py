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

        data = """{"data":{"agent":{"id":"id","accountId":"accountId","createdAt":"2019-12-27T18:11:19.117Z","name":"name","profileId":"profileId","workspaceId":"workspaceId","externalId":"externalId","labels":{"foo":"string"},"updatedAt":"2019-12-27T18:11:19.117Z"},"agentVariation":{"id":"id","accountId":"accountId","createdAt":"2019-12-27T18:11:19.117Z","name":"name","profileId":"profileId","workspaceId":"workspaceId","externalId":"externalId","labels":{"foo":"string"},"updatedAt":"2019-12-27T18:11:19.117Z"},"objective":{"id":"id","accountId":"accountId","createdAt":"2019-12-27T18:11:19.117Z","profileId":"profileId","workspaceId":"workspaceId","externalId":"externalId","labels":{"foo":"string"}},"objectiveEvent":{"data":{"assistantMessage":{"content":"content","toolCalls":[{"arguments":"arguments","functionName":"functionName","tool":{"agent":{"id":"id","accountId":"accountId","createdAt":"2019-12-27T18:11:19.117Z","name":"name","profileId":"profileId","workspaceId":"workspaceId","externalId":"externalId","labels":{"foo":"string"},"updatedAt":"2019-12-27T18:11:19.117Z"},"cadenyaProvidedTool":{"id":"id","accountId":"accountId","createdAt":"2019-12-27T18:11:19.117Z","name":"name","profileId":"profileId","workspaceId":"workspaceId","externalId":"externalId","labels":{"foo":"string"},"updatedAt":"2019-12-27T18:11:19.117Z"},"tool":{"id":"id","accountId":"accountId","createdAt":"2019-12-27T18:11:19.117Z","name":"name","profileId":"profileId","workspaceId":"workspaceId","externalId":"externalId","labels":{"foo":"string"},"updatedAt":"2019-12-27T18:11:19.117Z"}}}]},"cancelled":{"message":"message"},"contextWindowCompacted":{"messagesCompacted":0,"newContextWindow":{"completionTokens":0,"objectiveId":"objectiveId","previousWindowContinueInstructions":"previousWindowContinueInstructions","promptTokens":0,"sequence":0},"strategies":["string"],"summary":"summary"},"error":{"message":"message","type":"type"},"finalized":{"output":{}},"memoryRead":{"memoryEntryId":"memoryEntryId","memoryLayerId":"memoryLayerId","message":"message"},"notice":{"key":"key","level":"LEVEL_UNSPECIFIED","message":"message"},"subAgentSpawned":{"agent":{"id":"id","accountId":"accountId","createdAt":"2019-12-27T18:11:19.117Z","name":"name","profileId":"profileId","workspaceId":"workspaceId","externalId":"externalId","labels":{"foo":"string"},"updatedAt":"2019-12-27T18:11:19.117Z"},"objective":{"id":"id","accountId":"accountId","createdAt":"2019-12-27T18:11:19.117Z","profileId":"profileId","workspaceId":"workspaceId","externalId":"externalId","labels":{"foo":"string"}},"task":"task"},"subAgentUpdated":{"agent":{"id":"id","name":"name"},"message":"message","objective":{"id":"id","name":"name"},"status":"STATUS_UNSPECIFIED"},"timedOut":{"message":"message"},"toolApprovalRequested":{"toolCallId":"toolCallId"},"toolApproved":{"toolCallId":"toolCallId"},"toolCalled":{"arguments":{"foo":"bar"},"config":{"bare":{},"http":{"requestMethod":"HTTP_METHOD_UNSPECIFIED","headers":{"foo":"string"},"path":"path","query":"query","requestBodyContentType":"requestBodyContentType","requestBodyTemplate":"requestBodyTemplate"},"mcp":{"annotations":{"destructiveHint":true,"idempotentHint":true,"openWorldHint":true,"readOnlyHint":true,"title":"title"}},"openapi":{"method":"method","path":"path"}},"tool":{"agent":{"id":"id","accountId":"accountId","createdAt":"2019-12-27T18:11:19.117Z","name":"name","profileId":"profileId","workspaceId":"workspaceId","externalId":"externalId","labels":{"foo":"string"},"updatedAt":"2019-12-27T18:11:19.117Z"},"cadenyaProvidedTool":{"id":"id","accountId":"accountId","createdAt":"2019-12-27T18:11:19.117Z","name":"name","profileId":"profileId","workspaceId":"workspaceId","externalId":"externalId","labels":{"foo":"string"},"updatedAt":"2019-12-27T18:11:19.117Z"},"tool":{"id":"id","accountId":"accountId","createdAt":"2019-12-27T18:11:19.117Z","name":"name","profileId":"profileId","workspaceId":"workspaceId","externalId":"externalId","labels":{"foo":"string"},"updatedAt":"2019-12-27T18:11:19.117Z"}},"toolCallId":"toolCallId"},"toolDenied":{"memo":"memo","toolCallId":"toolCallId"},"toolError":{"message":"message","toolCallId":"toolCallId"},"toolResult":{"result":{"content":[{"audio":{"expiresAt":"2019-12-27T18:11:19.117Z","mimeType":"mimeType","sizeBytes":"sizeBytes","url":"url"},"image":{"expiresAt":"2019-12-27T18:11:19.117Z","mimeType":"mimeType","sizeBytes":"sizeBytes","url":"url"},"text":{"text":"text"}}]},"toolCallId":"toolCallId"},"type":"type","userMessage":{"content":"content"}},"metadata":{"id":"id","accountId":"accountId","createdAt":"2019-12-27T18:11:19.117Z","profileId":"profileId","workspaceId":"workspaceId","externalId":"externalId","labels":{"foo":"string"}},"contextWindowId":"contextWindowId","info":{"createdBy":{"metadata":{"id":"id","accountId":"accountId","name":"name","profileId":"profileId","createdAt":"2019-12-27T18:11:19.117Z","externalId":"externalId","labels":{"foo":"string"}},"spec":{"type":"PROFILE_TYPE_UNSPECIFIED","email":"email","name":"name"}},"objective":{"id":"id","accountId":"accountId","createdAt":"2019-12-27T18:11:19.117Z","profileId":"profileId","workspaceId":"workspaceId","externalId":"externalId","labels":{"foo":"string"}}}}},"timestamp":"2019-12-27T18:11:19.117Z","type":"type"}"""
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

        data = """{"data":{"agent":{"id":"id","accountId":"accountId","createdAt":"2019-12-27T18:11:19.117Z","name":"name","profileId":"profileId","workspaceId":"workspaceId","externalId":"externalId","labels":{"foo":"string"},"updatedAt":"2019-12-27T18:11:19.117Z"},"agentVariation":{"id":"id","accountId":"accountId","createdAt":"2019-12-27T18:11:19.117Z","name":"name","profileId":"profileId","workspaceId":"workspaceId","externalId":"externalId","labels":{"foo":"string"},"updatedAt":"2019-12-27T18:11:19.117Z"},"objective":{"id":"id","accountId":"accountId","createdAt":"2019-12-27T18:11:19.117Z","profileId":"profileId","workspaceId":"workspaceId","externalId":"externalId","labels":{"foo":"string"}},"objectiveEvent":{"data":{"assistantMessage":{"content":"content","toolCalls":[{"arguments":"arguments","functionName":"functionName","tool":{"agent":{"id":"id","accountId":"accountId","createdAt":"2019-12-27T18:11:19.117Z","name":"name","profileId":"profileId","workspaceId":"workspaceId","externalId":"externalId","labels":{"foo":"string"},"updatedAt":"2019-12-27T18:11:19.117Z"},"cadenyaProvidedTool":{"id":"id","accountId":"accountId","createdAt":"2019-12-27T18:11:19.117Z","name":"name","profileId":"profileId","workspaceId":"workspaceId","externalId":"externalId","labels":{"foo":"string"},"updatedAt":"2019-12-27T18:11:19.117Z"},"tool":{"id":"id","accountId":"accountId","createdAt":"2019-12-27T18:11:19.117Z","name":"name","profileId":"profileId","workspaceId":"workspaceId","externalId":"externalId","labels":{"foo":"string"},"updatedAt":"2019-12-27T18:11:19.117Z"}}}]},"cancelled":{"message":"message"},"contextWindowCompacted":{"messagesCompacted":0,"newContextWindow":{"completionTokens":0,"objectiveId":"objectiveId","previousWindowContinueInstructions":"previousWindowContinueInstructions","promptTokens":0,"sequence":0},"strategies":["string"],"summary":"summary"},"error":{"message":"message","type":"type"},"finalized":{"output":{}},"memoryRead":{"memoryEntryId":"memoryEntryId","memoryLayerId":"memoryLayerId","message":"message"},"notice":{"key":"key","level":"LEVEL_UNSPECIFIED","message":"message"},"subAgentSpawned":{"agent":{"id":"id","accountId":"accountId","createdAt":"2019-12-27T18:11:19.117Z","name":"name","profileId":"profileId","workspaceId":"workspaceId","externalId":"externalId","labels":{"foo":"string"},"updatedAt":"2019-12-27T18:11:19.117Z"},"objective":{"id":"id","accountId":"accountId","createdAt":"2019-12-27T18:11:19.117Z","profileId":"profileId","workspaceId":"workspaceId","externalId":"externalId","labels":{"foo":"string"}},"task":"task"},"subAgentUpdated":{"agent":{"id":"id","name":"name"},"message":"message","objective":{"id":"id","name":"name"},"status":"STATUS_UNSPECIFIED"},"timedOut":{"message":"message"},"toolApprovalRequested":{"toolCallId":"toolCallId"},"toolApproved":{"toolCallId":"toolCallId"},"toolCalled":{"arguments":{"foo":"bar"},"config":{"bare":{},"http":{"requestMethod":"HTTP_METHOD_UNSPECIFIED","headers":{"foo":"string"},"path":"path","query":"query","requestBodyContentType":"requestBodyContentType","requestBodyTemplate":"requestBodyTemplate"},"mcp":{"annotations":{"destructiveHint":true,"idempotentHint":true,"openWorldHint":true,"readOnlyHint":true,"title":"title"}},"openapi":{"method":"method","path":"path"}},"tool":{"agent":{"id":"id","accountId":"accountId","createdAt":"2019-12-27T18:11:19.117Z","name":"name","profileId":"profileId","workspaceId":"workspaceId","externalId":"externalId","labels":{"foo":"string"},"updatedAt":"2019-12-27T18:11:19.117Z"},"cadenyaProvidedTool":{"id":"id","accountId":"accountId","createdAt":"2019-12-27T18:11:19.117Z","name":"name","profileId":"profileId","workspaceId":"workspaceId","externalId":"externalId","labels":{"foo":"string"},"updatedAt":"2019-12-27T18:11:19.117Z"},"tool":{"id":"id","accountId":"accountId","createdAt":"2019-12-27T18:11:19.117Z","name":"name","profileId":"profileId","workspaceId":"workspaceId","externalId":"externalId","labels":{"foo":"string"},"updatedAt":"2019-12-27T18:11:19.117Z"}},"toolCallId":"toolCallId"},"toolDenied":{"memo":"memo","toolCallId":"toolCallId"},"toolError":{"message":"message","toolCallId":"toolCallId"},"toolResult":{"result":{"content":[{"audio":{"expiresAt":"2019-12-27T18:11:19.117Z","mimeType":"mimeType","sizeBytes":"sizeBytes","url":"url"},"image":{"expiresAt":"2019-12-27T18:11:19.117Z","mimeType":"mimeType","sizeBytes":"sizeBytes","url":"url"},"text":{"text":"text"}}]},"toolCallId":"toolCallId"},"type":"type","userMessage":{"content":"content"}},"metadata":{"id":"id","accountId":"accountId","createdAt":"2019-12-27T18:11:19.117Z","profileId":"profileId","workspaceId":"workspaceId","externalId":"externalId","labels":{"foo":"string"}},"contextWindowId":"contextWindowId","info":{"createdBy":{"metadata":{"id":"id","accountId":"accountId","name":"name","profileId":"profileId","createdAt":"2019-12-27T18:11:19.117Z","externalId":"externalId","labels":{"foo":"string"}},"spec":{"type":"PROFILE_TYPE_UNSPECIFIED","email":"email","name":"name"}},"objective":{"id":"id","accountId":"accountId","createdAt":"2019-12-27T18:11:19.117Z","profileId":"profileId","workspaceId":"workspaceId","externalId":"externalId","labels":{"foo":"string"}}}}},"timestamp":"2019-12-27T18:11:19.117Z","type":"type"}"""
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
