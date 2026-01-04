"""FortiOS Monitor - Azure category"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient

from .application_list.refresh import Refresh

class ApplicationListEndpoints:
    """Endpoints under application_list."""

    def __init__(self, client):
        self.refresh = Refresh(client)


class Azure:
    """Azure endpoints wrapper for Monitor API."""

    def __init__(self, client: "IHTTPClient"):
        """Azure endpoints."""
        self.application_list = ApplicationListEndpoints(client)


__all__ = ["Azure"]
