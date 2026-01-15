"""Type stubs for SERVICE category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import security_rating
    from . import service
    from . import sniffer
    from . import system

__all__ = [
    "Service",
    "ServiceDictMode",
    "ServiceObjectMode",
]

class ServiceDictMode:
    """SERVICE API category for dict response mode.
    
    This class is returned when the client is instantiated with response_mode="dict" (default).
    All endpoints return dict/TypedDict responses by default.
    """
    
    security_rating: security_rating.SecurityRatingDictMode
    service: service.ServiceDictMode
    sniffer: sniffer.SnifferDictMode
    system: system.SystemDictMode

    def __init__(self, client: IHTTPClient) -> None:
        """Initialize SERVICE category with HTTP client."""
        ...


class ServiceObjectMode:
    """SERVICE API category for object response mode.
    
    This class is returned when the client is instantiated with response_mode="object".
    All endpoints return FortiObject responses by default.
    """
    
    security_rating: security_rating.SecurityRatingObjectMode
    service: service.ServiceObjectMode
    sniffer: sniffer.SnifferObjectMode
    system: system.SystemObjectMode

    def __init__(self, client: IHTTPClient) -> None:
        """Initialize SERVICE category with HTTP client."""
        ...


# Base class for backwards compatibility
class Service:
    """SERVICE API category."""
    
    security_rating: security_rating.SecurityRating
    service: service.Service
    sniffer: sniffer.Sniffer
    system: system.System

    def __init__(self, client: IHTTPClient) -> None:
        """Initialize SERVICE category with HTTP client."""
        ...