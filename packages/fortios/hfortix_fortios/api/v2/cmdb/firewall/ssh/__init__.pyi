"""Type stubs for SSH category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import host_key
    from . import local_ca
    from . import local_key
    from . import setting


class Ssh:
    """Type stub for Ssh."""

    host_key: host_key.HostKey
    local_ca: local_ca.LocalCa
    local_key: local_key.LocalKey
    setting: setting.Setting

    def __init__(self, client: IHTTPClient) -> None: ...
