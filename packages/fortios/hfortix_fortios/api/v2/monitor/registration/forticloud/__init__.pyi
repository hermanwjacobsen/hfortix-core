"""Type stubs for FORTICLOUD category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import device_status
    from . import disclaimer
    from . import login
    from . import logout
    from . import migrate
    from . import register_device


class Forticloud:
    """Type stub for Forticloud."""

    device_status: device_status.DeviceStatus
    disclaimer: disclaimer.Disclaimer
    login: login.Login
    logout: logout.Logout
    migrate: migrate.Migrate
    register_device: register_device.RegisterDevice

    def __init__(self, client: IHTTPClient) -> None: ...
