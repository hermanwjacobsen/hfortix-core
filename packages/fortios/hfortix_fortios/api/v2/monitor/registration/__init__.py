"""FortiOS Monitor - Registration category"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient

from .forticare.add_license import AddLicense
from .forticare.create import Create
from .forticare.deregister_device import DeregisterDevice
from .forticare.login import Login
from .forticare.transfer import Transfer
from .forticloud.domains import Domains
from .forticloud.login import Login
from .forticloud.logout import Logout
from .forticloud.migrate import Migrate
from .forticloud.register_device import RegisterDevice
from .vdom.add_license import AddLicense

class ForticareEndpoints:
    """Endpoints under forticare."""

    def __init__(self, client):
        self.add_license = AddLicense(client)
        self.create = Create(client)
        self.deregister_device = DeregisterDevice(client)
        self.login = Login(client)
        self.transfer = Transfer(client)


class ForticloudEndpoints:
    """Endpoints under forticloud."""

    def __init__(self, client):
        self.domains = Domains(client)
        self.login = Login(client)
        self.logout = Logout(client)
        self.migrate = Migrate(client)
        self.register_device = RegisterDevice(client)


class VdomEndpoints:
    """Endpoints under vdom."""

    def __init__(self, client):
        self.add_license = AddLicense(client)


class Registration:
    """Registration endpoints wrapper for Monitor API."""

    def __init__(self, client: "IHTTPClient"):
        """Registration endpoints."""
        self.forticare = ForticareEndpoints(client)
        self.forticloud = ForticloudEndpoints(client)
        self.vdom = VdomEndpoints(client)


__all__ = ["Registration"]
