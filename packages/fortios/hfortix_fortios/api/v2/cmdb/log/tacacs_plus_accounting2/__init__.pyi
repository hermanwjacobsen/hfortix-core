"""Type stubs for TACACS_PLUS_ACCOUNTING2 category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .filter import Filter
    from .setting import Setting


class TacacsPlusAccounting2:
    """Type stub for TacacsPlusAccounting2."""

    filter: Filter
    setting: Setting

    def __init__(self, client: IHTTPClient) -> None: ...
