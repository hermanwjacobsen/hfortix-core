"""Type stubs for FIREWALL category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .auth import Auth
    from .count import Count
    from .deauth import Deauth


class Firewall:
    """Type stub for Firewall."""

    auth: Auth
    count: Count
    deauth: Deauth

    def __init__(self, client: IHTTPClient) -> None: ...
