"""Type stubs for IPPOOL category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .mapping import Mapping


class Ippool:
    """Type stub for Ippool."""

    mapping: Mapping

    def __init__(self, client: IHTTPClient) -> None: ...
