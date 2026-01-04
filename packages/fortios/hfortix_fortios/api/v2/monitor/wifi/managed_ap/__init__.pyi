"""Type stubs for MANAGED_AP category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import led_blink
    from . import restart
    from . import set_status


class ManagedAp:
    """Type stub for ManagedAp."""

    led_blink: led_blink.LedBlink
    restart: restart.Restart
    set_status: set_status.SetStatus

    def __init__(self, client: IHTTPClient) -> None: ...
