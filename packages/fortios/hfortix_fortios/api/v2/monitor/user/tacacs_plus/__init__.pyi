"""Type stubs for TACACS_PLUS category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .test import Test, TestDictMode, TestObjectMode

__all__ = [
    "Test",
    "TacacsplusDictMode",
    "TacacsplusObjectMode",
]

class TacacsplusDictMode:
    """TACACS_PLUS API category for dict response mode.
    
    This class is returned when the client is instantiated with response_mode="dict" (default).
    All endpoints return dict/TypedDict responses by default.
    """
    
    test: TestDictMode

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize tacacs_plus category with HTTP client."""
        ...


class TacacsplusObjectMode:
    """TACACS_PLUS API category for object response mode.
    
    This class is returned when the client is instantiated with response_mode="object".
    All endpoints return FortiObject responses by default.
    """
    
    test: TestObjectMode

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize tacacs_plus category with HTTP client."""
        ...


# Base class for backwards compatibility
class Tacacsplus:
    """TACACS_PLUS API category."""
    
    test: Test

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize tacacs_plus category with HTTP client."""
        ...
