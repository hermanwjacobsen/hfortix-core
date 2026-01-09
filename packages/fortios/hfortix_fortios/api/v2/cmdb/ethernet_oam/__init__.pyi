"""Type stubs for ETHERNET_OAM category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .cfm import Cfm, CfmDictMode, CfmObjectMode

__all__ = [
    "Cfm",
    "EthernetoamDictMode",
    "EthernetoamObjectMode",
]

class EthernetoamDictMode:
    """ETHERNET_OAM API category for dict response mode.
    
    This class is returned when the client is instantiated with response_mode="dict" (default).
    All endpoints return dict/TypedDict responses by default.
    """
    
    cfm: CfmDictMode

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize ethernet_oam category with HTTP client."""
        ...


class EthernetoamObjectMode:
    """ETHERNET_OAM API category for object response mode.
    
    This class is returned when the client is instantiated with response_mode="object".
    All endpoints return FortiObject responses by default.
    """
    
    cfm: CfmObjectMode

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize ethernet_oam category with HTTP client."""
        ...


# Base class for backwards compatibility
class Ethernetoam:
    """ETHERNET_OAM API category."""
    
    cfm: Cfm

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize ethernet_oam category with HTTP client."""
        ...
