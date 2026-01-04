"""Type stubs for ALERTEMAIL category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import setting


class Alertemail:
    """Type stub for Alertemail."""

    setting: setting.Setting

    def __init__(self, client: IHTTPClient) -> None: ...
