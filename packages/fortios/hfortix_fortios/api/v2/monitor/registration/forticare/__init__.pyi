"""Type stubs for FORTICARE category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import add_license
    from . import check_connectivity
    from . import create
    from . import deregister_device
    from . import login
    from . import transfer


class Forticare:
    """Type stub for Forticare."""

    add_license: add_license.AddLicense
    check_connectivity: check_connectivity.CheckConnectivity
    create: create.Create
    deregister_device: deregister_device.DeregisterDevice
    login: login.Login
    transfer: transfer.Transfer

    def __init__(self, client: IHTTPClient) -> None: ...
