"""Type stubs for MANAGED_AP category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .led_blink import LedBlink
    from .restart import Restart
    from .set_status import SetStatus


class ManagedAp:
    """Type stub for ManagedAp."""

    led_blink: LedBlink
    restart: Restart
    set_status: SetStatus

    def __init__(self, client: IHTTPClient) -> None: ...
