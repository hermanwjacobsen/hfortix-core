"""Type stubs for REPORT category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import layout
    from . import setting


class Report:
    """Type stub for Report."""

    layout: layout.Layout
    setting: setting.Setting

    def __init__(self, client: IHTTPClient) -> None: ...
