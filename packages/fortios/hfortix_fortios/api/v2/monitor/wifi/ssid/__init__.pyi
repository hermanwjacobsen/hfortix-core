"""Type stubs for SSID category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import generate_keys


class Ssid:
    """Type stub for Ssid."""

    generate_keys: generate_keys.GenerateKeys

    def __init__(self, client: IHTTPClient) -> None: ...
