"""Type stubs for endpoint."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient


class EndpointClass:
    """Type stub for endpoint class."""

    def __init__(self, client: IHTTPClient) -> None: ...

    def get(self, **params: Any) -> dict[str, Any] | list[dict[str, Any]]: ...

    def post(self, **data: Any) -> dict[str, Any]: ...
