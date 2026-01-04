"""Type stubs for SHAPER category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import per_ip_shaper
    from . import traffic_shaper


class Shaper:
    """Type stub for Shaper."""

    per_ip_shaper: per_ip_shaper.PerIpShaper
    traffic_shaper: traffic_shaper.TrafficShaper

    def __init__(self, client: IHTTPClient) -> None: ...
