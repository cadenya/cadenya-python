# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.api_key import APIKey

__all__ = ["GlobalAPIKeyResource", "AsyncGlobalAPIKeyResource"]


class GlobalAPIKeyResource(SyncAPIResource):
    """Manage the account's system-provisioned global API key.

    The global key is
     the only key that spans every workspace; it is created by the system and
     cannot be deleted, so the surface is retrieve, rotate, and the
     disable/enable kill switch.
    """

    @cached_property
    def with_raw_response(self) -> GlobalAPIKeyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cadenya/cadenya-python#accessing-raw-response-data-eg-headers
        """
        return GlobalAPIKeyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GlobalAPIKeyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cadenya/cadenya-python#with_streaming_response
        """
        return GlobalAPIKeyResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKey:
        """Retrieves the account's global API key.

        The token is included only when the
        caller's scopes dominate the key's.
        """
        return self._get(
            "/v1/account/global_api_key",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKey,
        )

    def disable(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKey:
        """Disables the global API key.

        While disabled, presenting its token fails
        authentication on every endpoint; the key is retained. Idempotent.
        """
        return self._post(
            "/v1/account/global_api_key:disable",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKey,
        )

    def enable(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKey:
        """
        Re-enables the disabled global API key so its token authenticates again.
        Idempotent.
        """
        return self._post(
            "/v1/account/global_api_key:enable",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKey,
        )

    def rotate(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKey:
        """Rotates the global API key and returns a new token.

        All previous tokens are
        invalidated.
        """
        return self._post(
            "/v1/account/global_api_key:rotate",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKey,
        )


class AsyncGlobalAPIKeyResource(AsyncAPIResource):
    """Manage the account's system-provisioned global API key.

    The global key is
     the only key that spans every workspace; it is created by the system and
     cannot be deleted, so the surface is retrieve, rotate, and the
     disable/enable kill switch.
    """

    @cached_property
    def with_raw_response(self) -> AsyncGlobalAPIKeyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cadenya/cadenya-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGlobalAPIKeyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGlobalAPIKeyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cadenya/cadenya-python#with_streaming_response
        """
        return AsyncGlobalAPIKeyResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKey:
        """Retrieves the account's global API key.

        The token is included only when the
        caller's scopes dominate the key's.
        """
        return await self._get(
            "/v1/account/global_api_key",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKey,
        )

    async def disable(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKey:
        """Disables the global API key.

        While disabled, presenting its token fails
        authentication on every endpoint; the key is retained. Idempotent.
        """
        return await self._post(
            "/v1/account/global_api_key:disable",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKey,
        )

    async def enable(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKey:
        """
        Re-enables the disabled global API key so its token authenticates again.
        Idempotent.
        """
        return await self._post(
            "/v1/account/global_api_key:enable",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKey,
        )

    async def rotate(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKey:
        """Rotates the global API key and returns a new token.

        All previous tokens are
        invalidated.
        """
        return await self._post(
            "/v1/account/global_api_key:rotate",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKey,
        )


class GlobalAPIKeyResourceWithRawResponse:
    def __init__(self, global_api_key: GlobalAPIKeyResource) -> None:
        self._global_api_key = global_api_key

        self.retrieve = to_raw_response_wrapper(
            global_api_key.retrieve,
        )
        self.disable = to_raw_response_wrapper(
            global_api_key.disable,
        )
        self.enable = to_raw_response_wrapper(
            global_api_key.enable,
        )
        self.rotate = to_raw_response_wrapper(
            global_api_key.rotate,
        )


class AsyncGlobalAPIKeyResourceWithRawResponse:
    def __init__(self, global_api_key: AsyncGlobalAPIKeyResource) -> None:
        self._global_api_key = global_api_key

        self.retrieve = async_to_raw_response_wrapper(
            global_api_key.retrieve,
        )
        self.disable = async_to_raw_response_wrapper(
            global_api_key.disable,
        )
        self.enable = async_to_raw_response_wrapper(
            global_api_key.enable,
        )
        self.rotate = async_to_raw_response_wrapper(
            global_api_key.rotate,
        )


class GlobalAPIKeyResourceWithStreamingResponse:
    def __init__(self, global_api_key: GlobalAPIKeyResource) -> None:
        self._global_api_key = global_api_key

        self.retrieve = to_streamed_response_wrapper(
            global_api_key.retrieve,
        )
        self.disable = to_streamed_response_wrapper(
            global_api_key.disable,
        )
        self.enable = to_streamed_response_wrapper(
            global_api_key.enable,
        )
        self.rotate = to_streamed_response_wrapper(
            global_api_key.rotate,
        )


class AsyncGlobalAPIKeyResourceWithStreamingResponse:
    def __init__(self, global_api_key: AsyncGlobalAPIKeyResource) -> None:
        self._global_api_key = global_api_key

        self.retrieve = async_to_streamed_response_wrapper(
            global_api_key.retrieve,
        )
        self.disable = async_to_streamed_response_wrapper(
            global_api_key.disable,
        )
        self.enable = async_to_streamed_response_wrapper(
            global_api_key.enable,
        )
        self.rotate = async_to_streamed_response_wrapper(
            global_api_key.rotate,
        )
