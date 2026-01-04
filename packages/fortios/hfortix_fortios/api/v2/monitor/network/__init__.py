"""Auto-generated category __init__ file."""

from typing import TYPE_CHECKING

from .arp import Arp

if TYPE_CHECKING:
    from hfortix_core.client import FortinetClient


class Network:
    """Container for {category_name} endpoints."""

    def __init__(self, client: "FortinetClient"):
        self.arp = Arp(client)
