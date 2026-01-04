"""
FortiOS API v2 - service endpoints.

Auto-generated from FortiOS 7.6 schemas.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient

from .sniffer import Sniffer
from .system import System


class Service:
    """Service category endpoints."""
    
    def __init__(self, client: "IHTTPClient"):
        """Initialize Service endpoints."""
        self.sniffer = Sniffer(client)
        self.system = System(client)


__all__ = ["Service"]
