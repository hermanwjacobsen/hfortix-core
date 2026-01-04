"""Type stubs for FIREWALL category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import auth
    from . import deauth


class Firewall:
    """Type stub for Firewall."""

    auth: auth.Auth
    deauth: deauth.Deauth

    def __init__(self, client: IHTTPClient) -> None: ...
