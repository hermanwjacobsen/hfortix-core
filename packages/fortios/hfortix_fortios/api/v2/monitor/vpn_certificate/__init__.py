"""FortiOS Monitor - VpnCertificate category"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient

from .ca.import_setting import ImportSetting
from .crl.import_setting import ImportSetting
from .csr.generate import Generate
from .local.create import Create
from .local.import_setting import ImportSetting
from .remote.import_setting import ImportSetting

class CaEndpoints:
    """Endpoints under ca."""

    def __init__(self, client):
        self.import_setting = ImportSetting(client)


class CrlEndpoints:
    """Endpoints under crl."""

    def __init__(self, client):
        self.import_setting = ImportSetting(client)


class CsrEndpoints:
    """Endpoints under csr."""

    def __init__(self, client):
        self.generate = Generate(client)


class LocalEndpoints:
    """Endpoints under local."""

    def __init__(self, client):
        self.create = Create(client)
        self.import_setting = ImportSetting(client)


class RemoteEndpoints:
    """Endpoints under remote."""

    def __init__(self, client):
        self.import_setting = ImportSetting(client)


class VpnCertificate:
    """VpnCertificate endpoints wrapper for Monitor API."""

    def __init__(self, client: "IHTTPClient"):
        """VpnCertificate endpoints."""
        self.ca = CaEndpoints(client)
        self.crl = CrlEndpoints(client)
        self.csr = CsrEndpoints(client)
        self.local = LocalEndpoints(client)
        self.remote = RemoteEndpoints(client)


__all__ = ["VpnCertificate"]
