# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import (
    is_given,
    is_mapping_t,
    get_async_library,
)
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import CadenyaError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import (
        agents,
        models,
        search,
        account,
        uploads,
        api_keys,
        profiles,
        tool_sets,
        objectives,
        workspaces,
        memory_layers,
        workspace_admin,
        ai_provider_keys,
        workspace_secrets,
    )
    from .resources.models import ModelsResource, AsyncModelsResource
    from .resources.search import SearchResource, AsyncSearchResource
    from .resources.account import AccountResource, AsyncAccountResource
    from .resources.uploads import UploadsResource, AsyncUploadsResource
    from .resources.profiles import ProfilesResource, AsyncProfilesResource
    from .resources.webhooks import WebhooksResource, AsyncWebhooksResource
    from .resources.workspaces import WorkspacesResource, AsyncWorkspacesResource
    from .resources.agents.agents import AgentsResource, AsyncAgentsResource
    from .resources.ai_provider_keys import AIProviderKeysResource, AsyncAIProviderKeysResource
    from .resources.api_keys.api_keys import APIKeysResource, AsyncAPIKeysResource
    from .resources.workspace_secrets import WorkspaceSecretsResource, AsyncWorkspaceSecretsResource
    from .resources.tool_sets.tool_sets import ToolSetsResource, AsyncToolSetsResource
    from .resources.objectives.objectives import ObjectivesResource, AsyncObjectivesResource
    from .resources.memory_layers.memory_layers import MemoryLayersResource, AsyncMemoryLayersResource
    from .resources.workspace_admin.workspace_admin import WorkspaceAdminResource, AsyncWorkspaceAdminResource

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Cadenya", "AsyncCadenya", "Client", "AsyncClient"]


class Cadenya(SyncAPIClient):
    # client options
    api_key: str
    webhook_key: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        webhook_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Cadenya client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `CADENYA_API_KEY`
        - `webhook_key` from `CADENYA_WEBHOOK_KEY`
        """
        if api_key is None:
            api_key = os.environ.get("CADENYA_API_KEY")
        if api_key is None:
            raise CadenyaError(
                "The api_key client option must be set either by passing api_key to the client or by setting the CADENYA_API_KEY environment variable"
            )
        self.api_key = api_key

        if webhook_key is None:
            webhook_key = os.environ.get("CADENYA_WEBHOOK_KEY")
        self.webhook_key = webhook_key

        if base_url is None:
            base_url = os.environ.get("CADENYA_BASE_URL")
        if base_url is None:
            base_url = f"https://api.cadenya.com"

        custom_headers_env = os.environ.get("CADENYA_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self._default_stream_cls = Stream

    @cached_property
    def ai_provider_keys(self) -> AIProviderKeysResource:
        from .resources.ai_provider_keys import AIProviderKeysResource

        return AIProviderKeysResource(self)

    @cached_property
    def account(self) -> AccountResource:
        """Manage the authenticated account.

        Accounts are the top-level organizational
         unit and contain one or more workspaces.
        """
        from .resources.account import AccountResource

        return AccountResource(self)

    @cached_property
    def profiles(self) -> ProfilesResource:
        """
        Operations on profiles, the account-level principals (users, API keys,
         system) that authenticate against the API.
        """
        from .resources.profiles import ProfilesResource

        return ProfilesResource(self)

    @cached_property
    def agents(self) -> AgentsResource:
        """Manage AI agents within a workspace. Agents define AI behavior and tool access."""
        from .resources.agents import AgentsResource

        return AgentsResource(self)

    @cached_property
    def objectives(self) -> ObjectivesResource:
        from .resources.objectives import ObjectivesResource

        return ObjectivesResource(self)

    @cached_property
    def memory_layers(self) -> MemoryLayersResource:
        """Manage memory layers and their entries.

        Layers are named containers that can
         be composed into an objective's memory cascade; entries are the keyed values
         within a layer. System-managed layers (e.g., episodic layers created by the
         runtime) cannot be mutated through this API.
        """
        from .resources.memory_layers import MemoryLayersResource

        return MemoryLayersResource(self)

    @cached_property
    def uploads(self) -> UploadsResource:
        """Issue short-lived presigned URLs for direct client-to-object-storage
         uploads.

        Created uploads can be referenced by id when creating or updating
         resources that accept binary content (e.g., MemoryEntry).
        """
        from .resources.uploads import UploadsResource

        return UploadsResource(self)

    @cached_property
    def models(self) -> ModelsResource:
        """Manage LLM models available to a workspace.

        Models represent provider and
         family pairs (e.g., "anthropic/claude-sonnet-4.6"). Workspaces are seeded
         with the supported models and you can enable or disable each one.
        """
        from .resources.models import ModelsResource

        return ModelsResource(self)

    @cached_property
    def search(self) -> SearchResource:
        from .resources.search import SearchResource

        return SearchResource(self)

    @cached_property
    def tool_sets(self) -> ToolSetsResource:
        """Manage tool sets and the tools they contain.

        Tool sets group related tools,
         and tools define specific capabilities available to agents.

         When a tool set is managed, only API key actors can modify its tools; human
         (profile) actors cannot.
        """
        from .resources.tool_sets import ToolSetsResource

        return ToolSetsResource(self)

    @cached_property
    def api_keys(self) -> APIKeysResource:
        """
        Issue, rotate, and revoke API keys for the account, and grant or revoke
         each key's access to individual workspaces.
        """
        from .resources.api_keys import APIKeysResource

        return APIKeysResource(self)

    @cached_property
    def workspace_secrets(self) -> WorkspaceSecretsResource:
        from .resources.workspace_secrets import WorkspaceSecretsResource

        return WorkspaceSecretsResource(self)

    @cached_property
    def workspaces(self) -> WorkspacesResource:
        """Manage workspaces within an account.

        Workspaces provide organizational
         grouping and isolation for resources such as agents, tools, and API keys.

         This is the workspace-scoped, end-user surface. Administrative operations
         (create / archive workspaces, manage members) live in WorkspaceAdminService
         under /v1/account/workspaces and require the admin role.
        """
        from .resources.workspaces import WorkspacesResource

        return WorkspacesResource(self)

    @cached_property
    def workspace_admin(self) -> WorkspaceAdminResource:
        """
        Administer workspaces across the account: create and archive workspaces and
         manage their membership. These operations are account-scoped and require the
         admin role (a token whose profile holds the WorkOS admin role); they live
         under /v1/account/workspaces rather than the workspace-scoped /v1/workspaces
         tree so an admin can manage any workspace in the account, including ones they
         are not themselves a member of.
        """
        from .resources.workspace_admin import WorkspaceAdminResource

        return WorkspaceAdminResource(self)

    @cached_property
    def webhooks(self) -> WebhooksResource:
        from .resources.webhooks import WebhooksResource

        return WebhooksResource(self)

    @cached_property
    def with_raw_response(self) -> CadenyaWithRawResponse:
        return CadenyaWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CadenyaWithStreamedResponse:
        return CadenyaWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        webhook_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            webhook_key=webhook_key or self.webhook_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncCadenya(AsyncAPIClient):
    # client options
    api_key: str
    webhook_key: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        webhook_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncCadenya client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `CADENYA_API_KEY`
        - `webhook_key` from `CADENYA_WEBHOOK_KEY`
        """
        if api_key is None:
            api_key = os.environ.get("CADENYA_API_KEY")
        if api_key is None:
            raise CadenyaError(
                "The api_key client option must be set either by passing api_key to the client or by setting the CADENYA_API_KEY environment variable"
            )
        self.api_key = api_key

        if webhook_key is None:
            webhook_key = os.environ.get("CADENYA_WEBHOOK_KEY")
        self.webhook_key = webhook_key

        if base_url is None:
            base_url = os.environ.get("CADENYA_BASE_URL")
        if base_url is None:
            base_url = f"https://api.cadenya.com"

        custom_headers_env = os.environ.get("CADENYA_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self._default_stream_cls = AsyncStream

    @cached_property
    def ai_provider_keys(self) -> AsyncAIProviderKeysResource:
        from .resources.ai_provider_keys import AsyncAIProviderKeysResource

        return AsyncAIProviderKeysResource(self)

    @cached_property
    def account(self) -> AsyncAccountResource:
        """Manage the authenticated account.

        Accounts are the top-level organizational
         unit and contain one or more workspaces.
        """
        from .resources.account import AsyncAccountResource

        return AsyncAccountResource(self)

    @cached_property
    def profiles(self) -> AsyncProfilesResource:
        """
        Operations on profiles, the account-level principals (users, API keys,
         system) that authenticate against the API.
        """
        from .resources.profiles import AsyncProfilesResource

        return AsyncProfilesResource(self)

    @cached_property
    def agents(self) -> AsyncAgentsResource:
        """Manage AI agents within a workspace. Agents define AI behavior and tool access."""
        from .resources.agents import AsyncAgentsResource

        return AsyncAgentsResource(self)

    @cached_property
    def objectives(self) -> AsyncObjectivesResource:
        from .resources.objectives import AsyncObjectivesResource

        return AsyncObjectivesResource(self)

    @cached_property
    def memory_layers(self) -> AsyncMemoryLayersResource:
        """Manage memory layers and their entries.

        Layers are named containers that can
         be composed into an objective's memory cascade; entries are the keyed values
         within a layer. System-managed layers (e.g., episodic layers created by the
         runtime) cannot be mutated through this API.
        """
        from .resources.memory_layers import AsyncMemoryLayersResource

        return AsyncMemoryLayersResource(self)

    @cached_property
    def uploads(self) -> AsyncUploadsResource:
        """Issue short-lived presigned URLs for direct client-to-object-storage
         uploads.

        Created uploads can be referenced by id when creating or updating
         resources that accept binary content (e.g., MemoryEntry).
        """
        from .resources.uploads import AsyncUploadsResource

        return AsyncUploadsResource(self)

    @cached_property
    def models(self) -> AsyncModelsResource:
        """Manage LLM models available to a workspace.

        Models represent provider and
         family pairs (e.g., "anthropic/claude-sonnet-4.6"). Workspaces are seeded
         with the supported models and you can enable or disable each one.
        """
        from .resources.models import AsyncModelsResource

        return AsyncModelsResource(self)

    @cached_property
    def search(self) -> AsyncSearchResource:
        from .resources.search import AsyncSearchResource

        return AsyncSearchResource(self)

    @cached_property
    def tool_sets(self) -> AsyncToolSetsResource:
        """Manage tool sets and the tools they contain.

        Tool sets group related tools,
         and tools define specific capabilities available to agents.

         When a tool set is managed, only API key actors can modify its tools; human
         (profile) actors cannot.
        """
        from .resources.tool_sets import AsyncToolSetsResource

        return AsyncToolSetsResource(self)

    @cached_property
    def api_keys(self) -> AsyncAPIKeysResource:
        """
        Issue, rotate, and revoke API keys for the account, and grant or revoke
         each key's access to individual workspaces.
        """
        from .resources.api_keys import AsyncAPIKeysResource

        return AsyncAPIKeysResource(self)

    @cached_property
    def workspace_secrets(self) -> AsyncWorkspaceSecretsResource:
        from .resources.workspace_secrets import AsyncWorkspaceSecretsResource

        return AsyncWorkspaceSecretsResource(self)

    @cached_property
    def workspaces(self) -> AsyncWorkspacesResource:
        """Manage workspaces within an account.

        Workspaces provide organizational
         grouping and isolation for resources such as agents, tools, and API keys.

         This is the workspace-scoped, end-user surface. Administrative operations
         (create / archive workspaces, manage members) live in WorkspaceAdminService
         under /v1/account/workspaces and require the admin role.
        """
        from .resources.workspaces import AsyncWorkspacesResource

        return AsyncWorkspacesResource(self)

    @cached_property
    def workspace_admin(self) -> AsyncWorkspaceAdminResource:
        """
        Administer workspaces across the account: create and archive workspaces and
         manage their membership. These operations are account-scoped and require the
         admin role (a token whose profile holds the WorkOS admin role); they live
         under /v1/account/workspaces rather than the workspace-scoped /v1/workspaces
         tree so an admin can manage any workspace in the account, including ones they
         are not themselves a member of.
        """
        from .resources.workspace_admin import AsyncWorkspaceAdminResource

        return AsyncWorkspaceAdminResource(self)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResource:
        from .resources.webhooks import AsyncWebhooksResource

        return AsyncWebhooksResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncCadenyaWithRawResponse:
        return AsyncCadenyaWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCadenyaWithStreamedResponse:
        return AsyncCadenyaWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        webhook_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            webhook_key=webhook_key or self.webhook_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class CadenyaWithRawResponse:
    _client: Cadenya

    def __init__(self, client: Cadenya) -> None:
        self._client = client

    @cached_property
    def ai_provider_keys(self) -> ai_provider_keys.AIProviderKeysResourceWithRawResponse:
        from .resources.ai_provider_keys import AIProviderKeysResourceWithRawResponse

        return AIProviderKeysResourceWithRawResponse(self._client.ai_provider_keys)

    @cached_property
    def account(self) -> account.AccountResourceWithRawResponse:
        """Manage the authenticated account.

        Accounts are the top-level organizational
         unit and contain one or more workspaces.
        """
        from .resources.account import AccountResourceWithRawResponse

        return AccountResourceWithRawResponse(self._client.account)

    @cached_property
    def profiles(self) -> profiles.ProfilesResourceWithRawResponse:
        """
        Operations on profiles, the account-level principals (users, API keys,
         system) that authenticate against the API.
        """
        from .resources.profiles import ProfilesResourceWithRawResponse

        return ProfilesResourceWithRawResponse(self._client.profiles)

    @cached_property
    def agents(self) -> agents.AgentsResourceWithRawResponse:
        """Manage AI agents within a workspace. Agents define AI behavior and tool access."""
        from .resources.agents import AgentsResourceWithRawResponse

        return AgentsResourceWithRawResponse(self._client.agents)

    @cached_property
    def objectives(self) -> objectives.ObjectivesResourceWithRawResponse:
        from .resources.objectives import ObjectivesResourceWithRawResponse

        return ObjectivesResourceWithRawResponse(self._client.objectives)

    @cached_property
    def memory_layers(self) -> memory_layers.MemoryLayersResourceWithRawResponse:
        """Manage memory layers and their entries.

        Layers are named containers that can
         be composed into an objective's memory cascade; entries are the keyed values
         within a layer. System-managed layers (e.g., episodic layers created by the
         runtime) cannot be mutated through this API.
        """
        from .resources.memory_layers import MemoryLayersResourceWithRawResponse

        return MemoryLayersResourceWithRawResponse(self._client.memory_layers)

    @cached_property
    def uploads(self) -> uploads.UploadsResourceWithRawResponse:
        """Issue short-lived presigned URLs for direct client-to-object-storage
         uploads.

        Created uploads can be referenced by id when creating or updating
         resources that accept binary content (e.g., MemoryEntry).
        """
        from .resources.uploads import UploadsResourceWithRawResponse

        return UploadsResourceWithRawResponse(self._client.uploads)

    @cached_property
    def models(self) -> models.ModelsResourceWithRawResponse:
        """Manage LLM models available to a workspace.

        Models represent provider and
         family pairs (e.g., "anthropic/claude-sonnet-4.6"). Workspaces are seeded
         with the supported models and you can enable or disable each one.
        """
        from .resources.models import ModelsResourceWithRawResponse

        return ModelsResourceWithRawResponse(self._client.models)

    @cached_property
    def search(self) -> search.SearchResourceWithRawResponse:
        from .resources.search import SearchResourceWithRawResponse

        return SearchResourceWithRawResponse(self._client.search)

    @cached_property
    def tool_sets(self) -> tool_sets.ToolSetsResourceWithRawResponse:
        """Manage tool sets and the tools they contain.

        Tool sets group related tools,
         and tools define specific capabilities available to agents.

         When a tool set is managed, only API key actors can modify its tools; human
         (profile) actors cannot.
        """
        from .resources.tool_sets import ToolSetsResourceWithRawResponse

        return ToolSetsResourceWithRawResponse(self._client.tool_sets)

    @cached_property
    def api_keys(self) -> api_keys.APIKeysResourceWithRawResponse:
        """
        Issue, rotate, and revoke API keys for the account, and grant or revoke
         each key's access to individual workspaces.
        """
        from .resources.api_keys import APIKeysResourceWithRawResponse

        return APIKeysResourceWithRawResponse(self._client.api_keys)

    @cached_property
    def workspace_secrets(self) -> workspace_secrets.WorkspaceSecretsResourceWithRawResponse:
        from .resources.workspace_secrets import WorkspaceSecretsResourceWithRawResponse

        return WorkspaceSecretsResourceWithRawResponse(self._client.workspace_secrets)

    @cached_property
    def workspaces(self) -> workspaces.WorkspacesResourceWithRawResponse:
        """Manage workspaces within an account.

        Workspaces provide organizational
         grouping and isolation for resources such as agents, tools, and API keys.

         This is the workspace-scoped, end-user surface. Administrative operations
         (create / archive workspaces, manage members) live in WorkspaceAdminService
         under /v1/account/workspaces and require the admin role.
        """
        from .resources.workspaces import WorkspacesResourceWithRawResponse

        return WorkspacesResourceWithRawResponse(self._client.workspaces)

    @cached_property
    def workspace_admin(self) -> workspace_admin.WorkspaceAdminResourceWithRawResponse:
        """
        Administer workspaces across the account: create and archive workspaces and
         manage their membership. These operations are account-scoped and require the
         admin role (a token whose profile holds the WorkOS admin role); they live
         under /v1/account/workspaces rather than the workspace-scoped /v1/workspaces
         tree so an admin can manage any workspace in the account, including ones they
         are not themselves a member of.
        """
        from .resources.workspace_admin import WorkspaceAdminResourceWithRawResponse

        return WorkspaceAdminResourceWithRawResponse(self._client.workspace_admin)


class AsyncCadenyaWithRawResponse:
    _client: AsyncCadenya

    def __init__(self, client: AsyncCadenya) -> None:
        self._client = client

    @cached_property
    def ai_provider_keys(self) -> ai_provider_keys.AsyncAIProviderKeysResourceWithRawResponse:
        from .resources.ai_provider_keys import AsyncAIProviderKeysResourceWithRawResponse

        return AsyncAIProviderKeysResourceWithRawResponse(self._client.ai_provider_keys)

    @cached_property
    def account(self) -> account.AsyncAccountResourceWithRawResponse:
        """Manage the authenticated account.

        Accounts are the top-level organizational
         unit and contain one or more workspaces.
        """
        from .resources.account import AsyncAccountResourceWithRawResponse

        return AsyncAccountResourceWithRawResponse(self._client.account)

    @cached_property
    def profiles(self) -> profiles.AsyncProfilesResourceWithRawResponse:
        """
        Operations on profiles, the account-level principals (users, API keys,
         system) that authenticate against the API.
        """
        from .resources.profiles import AsyncProfilesResourceWithRawResponse

        return AsyncProfilesResourceWithRawResponse(self._client.profiles)

    @cached_property
    def agents(self) -> agents.AsyncAgentsResourceWithRawResponse:
        """Manage AI agents within a workspace. Agents define AI behavior and tool access."""
        from .resources.agents import AsyncAgentsResourceWithRawResponse

        return AsyncAgentsResourceWithRawResponse(self._client.agents)

    @cached_property
    def objectives(self) -> objectives.AsyncObjectivesResourceWithRawResponse:
        from .resources.objectives import AsyncObjectivesResourceWithRawResponse

        return AsyncObjectivesResourceWithRawResponse(self._client.objectives)

    @cached_property
    def memory_layers(self) -> memory_layers.AsyncMemoryLayersResourceWithRawResponse:
        """Manage memory layers and their entries.

        Layers are named containers that can
         be composed into an objective's memory cascade; entries are the keyed values
         within a layer. System-managed layers (e.g., episodic layers created by the
         runtime) cannot be mutated through this API.
        """
        from .resources.memory_layers import AsyncMemoryLayersResourceWithRawResponse

        return AsyncMemoryLayersResourceWithRawResponse(self._client.memory_layers)

    @cached_property
    def uploads(self) -> uploads.AsyncUploadsResourceWithRawResponse:
        """Issue short-lived presigned URLs for direct client-to-object-storage
         uploads.

        Created uploads can be referenced by id when creating or updating
         resources that accept binary content (e.g., MemoryEntry).
        """
        from .resources.uploads import AsyncUploadsResourceWithRawResponse

        return AsyncUploadsResourceWithRawResponse(self._client.uploads)

    @cached_property
    def models(self) -> models.AsyncModelsResourceWithRawResponse:
        """Manage LLM models available to a workspace.

        Models represent provider and
         family pairs (e.g., "anthropic/claude-sonnet-4.6"). Workspaces are seeded
         with the supported models and you can enable or disable each one.
        """
        from .resources.models import AsyncModelsResourceWithRawResponse

        return AsyncModelsResourceWithRawResponse(self._client.models)

    @cached_property
    def search(self) -> search.AsyncSearchResourceWithRawResponse:
        from .resources.search import AsyncSearchResourceWithRawResponse

        return AsyncSearchResourceWithRawResponse(self._client.search)

    @cached_property
    def tool_sets(self) -> tool_sets.AsyncToolSetsResourceWithRawResponse:
        """Manage tool sets and the tools they contain.

        Tool sets group related tools,
         and tools define specific capabilities available to agents.

         When a tool set is managed, only API key actors can modify its tools; human
         (profile) actors cannot.
        """
        from .resources.tool_sets import AsyncToolSetsResourceWithRawResponse

        return AsyncToolSetsResourceWithRawResponse(self._client.tool_sets)

    @cached_property
    def api_keys(self) -> api_keys.AsyncAPIKeysResourceWithRawResponse:
        """
        Issue, rotate, and revoke API keys for the account, and grant or revoke
         each key's access to individual workspaces.
        """
        from .resources.api_keys import AsyncAPIKeysResourceWithRawResponse

        return AsyncAPIKeysResourceWithRawResponse(self._client.api_keys)

    @cached_property
    def workspace_secrets(self) -> workspace_secrets.AsyncWorkspaceSecretsResourceWithRawResponse:
        from .resources.workspace_secrets import AsyncWorkspaceSecretsResourceWithRawResponse

        return AsyncWorkspaceSecretsResourceWithRawResponse(self._client.workspace_secrets)

    @cached_property
    def workspaces(self) -> workspaces.AsyncWorkspacesResourceWithRawResponse:
        """Manage workspaces within an account.

        Workspaces provide organizational
         grouping and isolation for resources such as agents, tools, and API keys.

         This is the workspace-scoped, end-user surface. Administrative operations
         (create / archive workspaces, manage members) live in WorkspaceAdminService
         under /v1/account/workspaces and require the admin role.
        """
        from .resources.workspaces import AsyncWorkspacesResourceWithRawResponse

        return AsyncWorkspacesResourceWithRawResponse(self._client.workspaces)

    @cached_property
    def workspace_admin(self) -> workspace_admin.AsyncWorkspaceAdminResourceWithRawResponse:
        """
        Administer workspaces across the account: create and archive workspaces and
         manage their membership. These operations are account-scoped and require the
         admin role (a token whose profile holds the WorkOS admin role); they live
         under /v1/account/workspaces rather than the workspace-scoped /v1/workspaces
         tree so an admin can manage any workspace in the account, including ones they
         are not themselves a member of.
        """
        from .resources.workspace_admin import AsyncWorkspaceAdminResourceWithRawResponse

        return AsyncWorkspaceAdminResourceWithRawResponse(self._client.workspace_admin)


class CadenyaWithStreamedResponse:
    _client: Cadenya

    def __init__(self, client: Cadenya) -> None:
        self._client = client

    @cached_property
    def ai_provider_keys(self) -> ai_provider_keys.AIProviderKeysResourceWithStreamingResponse:
        from .resources.ai_provider_keys import AIProviderKeysResourceWithStreamingResponse

        return AIProviderKeysResourceWithStreamingResponse(self._client.ai_provider_keys)

    @cached_property
    def account(self) -> account.AccountResourceWithStreamingResponse:
        """Manage the authenticated account.

        Accounts are the top-level organizational
         unit and contain one or more workspaces.
        """
        from .resources.account import AccountResourceWithStreamingResponse

        return AccountResourceWithStreamingResponse(self._client.account)

    @cached_property
    def profiles(self) -> profiles.ProfilesResourceWithStreamingResponse:
        """
        Operations on profiles, the account-level principals (users, API keys,
         system) that authenticate against the API.
        """
        from .resources.profiles import ProfilesResourceWithStreamingResponse

        return ProfilesResourceWithStreamingResponse(self._client.profiles)

    @cached_property
    def agents(self) -> agents.AgentsResourceWithStreamingResponse:
        """Manage AI agents within a workspace. Agents define AI behavior and tool access."""
        from .resources.agents import AgentsResourceWithStreamingResponse

        return AgentsResourceWithStreamingResponse(self._client.agents)

    @cached_property
    def objectives(self) -> objectives.ObjectivesResourceWithStreamingResponse:
        from .resources.objectives import ObjectivesResourceWithStreamingResponse

        return ObjectivesResourceWithStreamingResponse(self._client.objectives)

    @cached_property
    def memory_layers(self) -> memory_layers.MemoryLayersResourceWithStreamingResponse:
        """Manage memory layers and their entries.

        Layers are named containers that can
         be composed into an objective's memory cascade; entries are the keyed values
         within a layer. System-managed layers (e.g., episodic layers created by the
         runtime) cannot be mutated through this API.
        """
        from .resources.memory_layers import MemoryLayersResourceWithStreamingResponse

        return MemoryLayersResourceWithStreamingResponse(self._client.memory_layers)

    @cached_property
    def uploads(self) -> uploads.UploadsResourceWithStreamingResponse:
        """Issue short-lived presigned URLs for direct client-to-object-storage
         uploads.

        Created uploads can be referenced by id when creating or updating
         resources that accept binary content (e.g., MemoryEntry).
        """
        from .resources.uploads import UploadsResourceWithStreamingResponse

        return UploadsResourceWithStreamingResponse(self._client.uploads)

    @cached_property
    def models(self) -> models.ModelsResourceWithStreamingResponse:
        """Manage LLM models available to a workspace.

        Models represent provider and
         family pairs (e.g., "anthropic/claude-sonnet-4.6"). Workspaces are seeded
         with the supported models and you can enable or disable each one.
        """
        from .resources.models import ModelsResourceWithStreamingResponse

        return ModelsResourceWithStreamingResponse(self._client.models)

    @cached_property
    def search(self) -> search.SearchResourceWithStreamingResponse:
        from .resources.search import SearchResourceWithStreamingResponse

        return SearchResourceWithStreamingResponse(self._client.search)

    @cached_property
    def tool_sets(self) -> tool_sets.ToolSetsResourceWithStreamingResponse:
        """Manage tool sets and the tools they contain.

        Tool sets group related tools,
         and tools define specific capabilities available to agents.

         When a tool set is managed, only API key actors can modify its tools; human
         (profile) actors cannot.
        """
        from .resources.tool_sets import ToolSetsResourceWithStreamingResponse

        return ToolSetsResourceWithStreamingResponse(self._client.tool_sets)

    @cached_property
    def api_keys(self) -> api_keys.APIKeysResourceWithStreamingResponse:
        """
        Issue, rotate, and revoke API keys for the account, and grant or revoke
         each key's access to individual workspaces.
        """
        from .resources.api_keys import APIKeysResourceWithStreamingResponse

        return APIKeysResourceWithStreamingResponse(self._client.api_keys)

    @cached_property
    def workspace_secrets(self) -> workspace_secrets.WorkspaceSecretsResourceWithStreamingResponse:
        from .resources.workspace_secrets import WorkspaceSecretsResourceWithStreamingResponse

        return WorkspaceSecretsResourceWithStreamingResponse(self._client.workspace_secrets)

    @cached_property
    def workspaces(self) -> workspaces.WorkspacesResourceWithStreamingResponse:
        """Manage workspaces within an account.

        Workspaces provide organizational
         grouping and isolation for resources such as agents, tools, and API keys.

         This is the workspace-scoped, end-user surface. Administrative operations
         (create / archive workspaces, manage members) live in WorkspaceAdminService
         under /v1/account/workspaces and require the admin role.
        """
        from .resources.workspaces import WorkspacesResourceWithStreamingResponse

        return WorkspacesResourceWithStreamingResponse(self._client.workspaces)

    @cached_property
    def workspace_admin(self) -> workspace_admin.WorkspaceAdminResourceWithStreamingResponse:
        """
        Administer workspaces across the account: create and archive workspaces and
         manage their membership. These operations are account-scoped and require the
         admin role (a token whose profile holds the WorkOS admin role); they live
         under /v1/account/workspaces rather than the workspace-scoped /v1/workspaces
         tree so an admin can manage any workspace in the account, including ones they
         are not themselves a member of.
        """
        from .resources.workspace_admin import WorkspaceAdminResourceWithStreamingResponse

        return WorkspaceAdminResourceWithStreamingResponse(self._client.workspace_admin)


class AsyncCadenyaWithStreamedResponse:
    _client: AsyncCadenya

    def __init__(self, client: AsyncCadenya) -> None:
        self._client = client

    @cached_property
    def ai_provider_keys(self) -> ai_provider_keys.AsyncAIProviderKeysResourceWithStreamingResponse:
        from .resources.ai_provider_keys import AsyncAIProviderKeysResourceWithStreamingResponse

        return AsyncAIProviderKeysResourceWithStreamingResponse(self._client.ai_provider_keys)

    @cached_property
    def account(self) -> account.AsyncAccountResourceWithStreamingResponse:
        """Manage the authenticated account.

        Accounts are the top-level organizational
         unit and contain one or more workspaces.
        """
        from .resources.account import AsyncAccountResourceWithStreamingResponse

        return AsyncAccountResourceWithStreamingResponse(self._client.account)

    @cached_property
    def profiles(self) -> profiles.AsyncProfilesResourceWithStreamingResponse:
        """
        Operations on profiles, the account-level principals (users, API keys,
         system) that authenticate against the API.
        """
        from .resources.profiles import AsyncProfilesResourceWithStreamingResponse

        return AsyncProfilesResourceWithStreamingResponse(self._client.profiles)

    @cached_property
    def agents(self) -> agents.AsyncAgentsResourceWithStreamingResponse:
        """Manage AI agents within a workspace. Agents define AI behavior and tool access."""
        from .resources.agents import AsyncAgentsResourceWithStreamingResponse

        return AsyncAgentsResourceWithStreamingResponse(self._client.agents)

    @cached_property
    def objectives(self) -> objectives.AsyncObjectivesResourceWithStreamingResponse:
        from .resources.objectives import AsyncObjectivesResourceWithStreamingResponse

        return AsyncObjectivesResourceWithStreamingResponse(self._client.objectives)

    @cached_property
    def memory_layers(self) -> memory_layers.AsyncMemoryLayersResourceWithStreamingResponse:
        """Manage memory layers and their entries.

        Layers are named containers that can
         be composed into an objective's memory cascade; entries are the keyed values
         within a layer. System-managed layers (e.g., episodic layers created by the
         runtime) cannot be mutated through this API.
        """
        from .resources.memory_layers import AsyncMemoryLayersResourceWithStreamingResponse

        return AsyncMemoryLayersResourceWithStreamingResponse(self._client.memory_layers)

    @cached_property
    def uploads(self) -> uploads.AsyncUploadsResourceWithStreamingResponse:
        """Issue short-lived presigned URLs for direct client-to-object-storage
         uploads.

        Created uploads can be referenced by id when creating or updating
         resources that accept binary content (e.g., MemoryEntry).
        """
        from .resources.uploads import AsyncUploadsResourceWithStreamingResponse

        return AsyncUploadsResourceWithStreamingResponse(self._client.uploads)

    @cached_property
    def models(self) -> models.AsyncModelsResourceWithStreamingResponse:
        """Manage LLM models available to a workspace.

        Models represent provider and
         family pairs (e.g., "anthropic/claude-sonnet-4.6"). Workspaces are seeded
         with the supported models and you can enable or disable each one.
        """
        from .resources.models import AsyncModelsResourceWithStreamingResponse

        return AsyncModelsResourceWithStreamingResponse(self._client.models)

    @cached_property
    def search(self) -> search.AsyncSearchResourceWithStreamingResponse:
        from .resources.search import AsyncSearchResourceWithStreamingResponse

        return AsyncSearchResourceWithStreamingResponse(self._client.search)

    @cached_property
    def tool_sets(self) -> tool_sets.AsyncToolSetsResourceWithStreamingResponse:
        """Manage tool sets and the tools they contain.

        Tool sets group related tools,
         and tools define specific capabilities available to agents.

         When a tool set is managed, only API key actors can modify its tools; human
         (profile) actors cannot.
        """
        from .resources.tool_sets import AsyncToolSetsResourceWithStreamingResponse

        return AsyncToolSetsResourceWithStreamingResponse(self._client.tool_sets)

    @cached_property
    def api_keys(self) -> api_keys.AsyncAPIKeysResourceWithStreamingResponse:
        """
        Issue, rotate, and revoke API keys for the account, and grant or revoke
         each key's access to individual workspaces.
        """
        from .resources.api_keys import AsyncAPIKeysResourceWithStreamingResponse

        return AsyncAPIKeysResourceWithStreamingResponse(self._client.api_keys)

    @cached_property
    def workspace_secrets(self) -> workspace_secrets.AsyncWorkspaceSecretsResourceWithStreamingResponse:
        from .resources.workspace_secrets import AsyncWorkspaceSecretsResourceWithStreamingResponse

        return AsyncWorkspaceSecretsResourceWithStreamingResponse(self._client.workspace_secrets)

    @cached_property
    def workspaces(self) -> workspaces.AsyncWorkspacesResourceWithStreamingResponse:
        """Manage workspaces within an account.

        Workspaces provide organizational
         grouping and isolation for resources such as agents, tools, and API keys.

         This is the workspace-scoped, end-user surface. Administrative operations
         (create / archive workspaces, manage members) live in WorkspaceAdminService
         under /v1/account/workspaces and require the admin role.
        """
        from .resources.workspaces import AsyncWorkspacesResourceWithStreamingResponse

        return AsyncWorkspacesResourceWithStreamingResponse(self._client.workspaces)

    @cached_property
    def workspace_admin(self) -> workspace_admin.AsyncWorkspaceAdminResourceWithStreamingResponse:
        """
        Administer workspaces across the account: create and archive workspaces and
         manage their membership. These operations are account-scoped and require the
         admin role (a token whose profile holds the WorkOS admin role); they live
         under /v1/account/workspaces rather than the workspace-scoped /v1/workspaces
         tree so an admin can manage any workspace in the account, including ones they
         are not themselves a member of.
        """
        from .resources.workspace_admin import AsyncWorkspaceAdminResourceWithStreamingResponse

        return AsyncWorkspaceAdminResourceWithStreamingResponse(self._client.workspace_admin)


Client = Cadenya

AsyncClient = AsyncCadenya
