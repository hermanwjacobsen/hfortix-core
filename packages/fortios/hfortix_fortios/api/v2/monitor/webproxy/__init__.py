"""FortiOS Monitor - Webproxy category"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient

from .pacfile.upload import Upload

class PacfileEndpoints:
    """Endpoints under pacfile."""

    def __init__(self, client):
        self.upload = Upload(client)


class Webproxy:
    """Webproxy endpoints wrapper for Monitor API."""

    def __init__(self, client: "IHTTPClient"):
        """Webproxy endpoints."""
        self.pacfile = PacfileEndpoints(client)


__all__ = ["Webproxy"]
