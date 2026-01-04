"""FortiOS Monitor - Geoip category"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient

from .geoip_query.select import Select

class GeoipQueryEndpoints:
    """Endpoints under geoip_query."""

    def __init__(self, client):
        self.select = Select(client)


class Geoip:
    """Geoip endpoints wrapper for Monitor API."""

    def __init__(self, client: "IHTTPClient"):
        """Geoip endpoints."""
        self.geoip_query = GeoipQueryEndpoints(client)


__all__ = ["Geoip"]
