"""FortiOS Monitor - WebUi category"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient

from .custom_language.create import Create
from .custom_language.update import Update

class CustomLanguageEndpoints:
    """Endpoints under custom_language."""

    def __init__(self, client):
        self.create = Create(client)
        self.update = Update(client)


class WebUi:
    """WebUi endpoints wrapper for Monitor API."""

    def __init__(self, client: "IHTTPClient"):
        """WebUi endpoints."""
        self.custom_language = CustomLanguageEndpoints(client)


__all__ = ["WebUi"]
