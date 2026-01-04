"""Type stubs for SERVICE category."""

from __future__ import annotations

from typing import TYPE_CHECKING

from .sniffer import Sniffer as Sniffer
from .system import System as System

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient


class Service:
    """Type stub for Service."""

    sniffer: Sniffer
    system: System

    def __init__(self, client: IHTTPClient) -> None: ...
