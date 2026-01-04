"""FortiOS Monitor - Casb category"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient

from .saas_application.details import Details

class SaasApplicationEndpoints:
    """Endpoints under saas_application."""

    def __init__(self, client):
        self.details = Details(client)


class Casb:
    """Casb endpoints wrapper for Monitor API."""

    def __init__(self, client: "IHTTPClient"):
        """Casb endpoints."""
        self.saas_application = SaasApplicationEndpoints(client)


__all__ = ["Casb"]
