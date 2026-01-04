"""Auto-generated category __init__ file."""

from typing import TYPE_CHECKING

from .ipsec import Ipsec
from .ipsec_base import Ipsec
from .ssl import Ssl
from .ssl_base import Ssl

if TYPE_CHECKING:
    from hfortix_core.client import FortinetClient


class Vpn:
    """Container for {category_name} endpoints."""

    def __init__(self, client: "FortinetClient"):
        self.ipsec = Ipsec(client)
        self.ipsec = Ipsec(client)
        self.ssl = Ssl(client)
        self.ssl = Ssl(client)
