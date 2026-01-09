"""Type stubs for SCTP_FILTER category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .profile import Profile, ProfileDictMode, ProfileObjectMode

__all__ = [
    "Profile",
    "SctpfilterDictMode",
    "SctpfilterObjectMode",
]

class SctpfilterDictMode:
    """SCTP_FILTER API category for dict response mode.
    
    This class is returned when the client is instantiated with response_mode="dict" (default).
    All endpoints return dict/TypedDict responses by default.
    """
    
    profile: ProfileDictMode

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize sctp_filter category with HTTP client."""
        ...


class SctpfilterObjectMode:
    """SCTP_FILTER API category for object response mode.
    
    This class is returned when the client is instantiated with response_mode="object".
    All endpoints return FortiObject responses by default.
    """
    
    profile: ProfileObjectMode

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize sctp_filter category with HTTP client."""
        ...


# Base class for backwards compatibility
class Sctpfilter:
    """SCTP_FILTER API category."""
    
    profile: Profile

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize sctp_filter category with HTTP client."""
        ...
