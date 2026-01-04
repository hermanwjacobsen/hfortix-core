"""Type stubs for CLIENT category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import disassociate


class Client:
    """Type stub for Client."""

    disassociate: disassociate.Disassociate

    def __init__(self, client: IHTTPClient) -> None: ...
