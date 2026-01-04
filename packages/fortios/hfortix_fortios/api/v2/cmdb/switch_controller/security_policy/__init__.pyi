"""Type stubs for SECURITY_POLICY category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import local_access
    from . import x802_1X


class SecurityPolicy:
    """Type stub for SecurityPolicy."""

    local_access: local_access.LocalAccess
    x802_1X: x802_1X.X8021x

    def __init__(self, client: IHTTPClient) -> None: ...
