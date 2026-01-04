"""Type stubs for LTE_MODEM category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import status
    from . import upgrade
    from . import upload


class LteModem:
    """Type stub for LteModem."""

    status: status.Status
    upgrade: upgrade.Upgrade
    upload: upload.Upload

    def __init__(self, client: IHTTPClient) -> None: ...
