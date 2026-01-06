"""Type stubs for CLIENT category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .disassociate import Disassociate


class Client:
    """Type stub for Client."""

    disassociate: Disassociate

    def __init__(self, client: IHTTPClient) -> None: ...
