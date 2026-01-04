"""Type stubs for TACACS_PLUS_ACCOUNTING category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import filter
    from . import setting


class TacacsPlusAccounting:
    """Type stub for TacacsPlusAccounting."""

    filter: filter.Filter
    setting: setting.Setting

    def __init__(self, client: IHTTPClient) -> None: ...
