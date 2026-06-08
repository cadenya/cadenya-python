from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `cadenya.resources` module.

    This is used so that we can lazily import `cadenya.resources` only when
    needed *and* so that users can just import `cadenya` and reference `cadenya.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("cadenya.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
