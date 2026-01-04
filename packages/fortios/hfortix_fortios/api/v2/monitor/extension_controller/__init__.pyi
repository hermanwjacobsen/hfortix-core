"""Type stubs for EXTENSION_CONTROLLER category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import fortigate
    from . import lan_extension_vdom_status


class ExtensionController:
    """Type stub for ExtensionController."""

    fortigate: fortigate.Fortigate
    lan_extension_vdom_status: lan_extension_vdom_status.LanExtensionVdomStatus

    def __init__(self, client: IHTTPClient) -> None: ...
