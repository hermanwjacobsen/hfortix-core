"""FortiOS Monitor - Service category"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient

from .ldap.query import Query

class LdapEndpoints:
    """Endpoints under ldap."""

    def __init__(self, client):
        self.query = Query(client)


class Service:
    """Service endpoints wrapper for Monitor API."""

    def __init__(self, client: "IHTTPClient"):
        """Service endpoints."""
        self.ldap = LdapEndpoints(client)


__all__ = ["Service"]
